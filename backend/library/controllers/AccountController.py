import json
from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request, jsonify

from library import app, smtp, db
from library.BLL import AccountSvc
from library.common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, LoginRsp, SearchAccountsReq, \
    SendResetPasswordEmailReq, ResetPasswordReq, ChangePasswordReq, CreateCustomerAccountReq, CreateEmployeeAccountReq
from library.common.Req.CustomerReq import SearchCustomersReq
from library.common.Req.EmployeeReq import SearchEmployeesReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq, SearchItemsReq
from library.common.Rsp.AccountRsp import SearchAccountsRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from library.common.Rsp.SingleRsp import ErrorRsp
from library.DAL import EmployeeRep, CustomerRep, AccountRep, models, LocationRep
import smtplib
from email.message import EmailMessage

from library.common.util import ConvertModelListToDictList, ConvertModelListToJson


@app.route('/admin/account-management/create-account', methods=['POST'])
def CreateAccount() -> CreateAccountReq:
    req = CreateAccountReq(request.json)
    result = AccountSvc.CreateAccount(req)
    return result


@app.route('/admin/account-management/get-accounts', methods=['POST'])
def GetAccounts():
    req = GetItemsByPageReq(request.json)
    result = AccountSvc.GetAccountsByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['accounts']).serialize()
    return jsonify(res)


@app.route('/admin/account-management/delete-account', methods=['POST'])
def DeleteAccount():
    req = DeleteAccountReq(request.json)
    res = AccountSvc.DeleteAccount(req)
    return jsonify(res.serialize())


@app.route('/admin/account-management/get-account', methods=['POST'])
def getAccount():
    req = SearchAccountsReq(request.json)
    info_accounts = AccountSvc.SearchAccounts(req)
    res = SearchAccountsRsp(info_accounts).serialize()
    return jsonify(res)


@app.route('/admin/account-management/search-accounts', methods=['POST'])
def SearchAccounts():
    req = SearchItemsReq(request.json)
    if (req.account_id):
        accounts = models.Accounts.query.filter(models.Accounts.account_id == req.account_id).all()
        info_accounts = []
        for account in ConvertModelListToDictList(accounts):
            user_info = {}
            if (account['role']['role_id'] == 3):  # customer
                all_customers = models.Customers.query.all()
                all_customers = [customer for customer in all_customers if (customer.account_id == account['account_id'] and customer.delete_at == None)]
                user_info = ConvertModelListToDictList(all_customers)

            if (account['role']['role_id'] == 1 or account['role']['role_id'] == 2):  # admin, manager
                search_employee_req = SearchEmployeesReq({'account_id': account['account_id']})
                user_info = EmployeeRep.SearchEmployees(search_employee_req)

            account_info = user_info[0] if user_info else {'account': account}
            account_info['account_id'] = account['account_id']
            account_info['account_name'] = account['account_name']
            account_info['role'] = account['role']
            account_info['note'] = account['note']
            account_info['delete_at'] = account['delete_at']
            info_accounts.append(account_info)
        return jsonify((info_accounts))
    all_accounts = models.Accounts.query
    if req.account_name != None:
        all_accounts = all_accounts.filter(models.Accounts.account_name.contains(req.account_name))
    if req.role_id != None:
        all_accounts = all_accounts.filter(models.Accounts.role_id == (req.role_id))
    all_accounts = all_accounts.filter(models.Accounts.delete_at == None)
    accounts = ConvertModelListToDictList(all_accounts.all())
    info_accounts = []
    for account in accounts:
        user_info = {}
        if (account['role']['role_id'] == 3):  # customer
            search_customer_req = SearchCustomersReq({'account_id': account['account_id']})
            user_info = CustomerRep.SearchCustomers(search_customer_req)

        if (account['role']['role_id'] == 1 or account['role']['role_id'] == 2):  # admin, manager
            search_employee_req = SearchEmployeesReq({'account_id': account['account_id']})
            user_info = EmployeeRep.SearchEmployees(search_employee_req)

        account_info = user_info[0] if user_info else {'account': account}
        account_info['account_id'] = account['account_id']
        account_info['account_name'] = account['account_name']
        account_info['role'] = account['role']
        account_info['note'] = account['note']
        account_info['delete_at'] = account['delete_at']
        info_accounts.append(account_info)
    return jsonify(info_accounts)

@app.route('/admin/account-management/login', methods=['POST'])
def LoginAccount():
    try:
        req = LoginReq(request.json)
        result = AccountSvc.AuthenticateUser(req)
        res = LoginRsp(result).serialize()
        return jsonify(res)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401

class UpdateSessionReq():
    def __init__(self,req):
        self.access_token = req['access_token'] if 'access_token' in req else None

@app.route('/update-session-info', methods=['POST'])
def updateSession():
    not_authenticated_msg = {
        'message': 'Bạn không có quyền truy cập.',
        'authenticated': False
    }

    invalid_msg = {
        'message': 'Token không hợp lệ.',
        'authenticated': False
    }
    expired_msg = {
        'message': 'Token hết hạn sử dụng.',
        'authenticated': False
    }
    try:
        req = UpdateSessionReq(request.json)
        account = AccountSvc.extractToken(req.access_token)
        if (account['role']['role_id'] == 3):  # customer
            user = (models.Customers.query.filter(models.Customers.account_id == account['account_id'],
                                                  models.Customers.account_id != None).first().serialize())

        if (account['role']['role_id'] == 1 or account['role']['role_id'] == 2):  # admin, manager
            user = (models.Employees.query.filter(models.Employees.account_id == account['account_id'],
                                                  models.Employees.account_id != None).first().serialize())

        result = {
            'access_token': req.access_token,
            'account': account,
             'user_info': user,
        }
        return jsonify(result)
    except jwt.ExpiredSignatureError:
        return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
    except (jwt.InvalidTokenError) as e:
        return jsonify(invalid_msg), 401
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401


@app.route('/send-reset-password-email-customer', methods=['POST'])
def SendResetPasswordEmailCustomer():
    req = SendResetPasswordEmailReq(request.json)
    result = AccountSvc.SendResetPasswordEmailCustomer(req)
    return jsonify(result)


@app.route('/send-reset-password-email-employee', methods=['POST'])
def SendResetPasswordEmailEmployee():
    req = SendResetPasswordEmailReq(request.json)
    result = AccountSvc.SendResetPasswordEmailEmployee(req)
    return result


@app.route('/reset-password', methods=['POST'])
def ResetPassword():
    req = ResetPasswordReq(request.json)
    result = AccountSvc.ResetPassword(req)
    return jsonify(result)


@app.route('/change-password', methods=['POST'])
def ChangePassword():
    try:
        req = ChangePasswordReq(request.json)
        result = AccountSvc.ChangePassword(req)
        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf8'), 401


@app.route('/create-customer-account', methods=['POST'])
def CreateCustomerAccount():
    try:
        req = CreateCustomerAccountReq(request.json)
        result = AccountSvc.CreateCustomerAccount(req)
        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401


@app.route('/create-employee-account', methods=['POST'])
def CreateEmployeeAccount():
    try:
        req = CreateEmployeeAccountReq(request.json)
        result = AccountSvc.CreateEmployeeAccount(req)
        return jsonify(result)
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401

@app.route('/create-role', methods=['POST'])
def CreateRole():
    try:
        req = CreateEmployeeAccountReq(request.json)
        role = models.Roles(role_id=1,role_name= "admin", note="note", delete_at=None)
        role1 = models.Roles(role_id=2,role_name= "admin-manager", note="note", delete_at=None)
        role2 = models.Roles(role_id=3,role_name= "user", note="note", delete_at=None)
        db.session.add(role)
        db.session.add(role1)
        db.session.add(role2)
        db.session.commit()
        return jsonify({})
    except ErrorRsp as e:
        return json.dumps(e.__dict__, ensure_ascii=False).encode('utf-8'), 401



@app.route('/get-provinces', methods=['POST'])
def getProvinces():
    return jsonify(LocationRep.getProvinces())


@app.route('/get-districts', methods=['POST'])
def getDistricts():
    return jsonify(LocationRep.getDistricts())


@app.route('/get-wards', methods=['POST'])
def getWards():
    return jsonify(LocationRep.getWards())


@app.route('/admin/role-management/get-roles', methods=['POST'])
def getRoles():
    rolesModel = models.Roles.query.filter(models.Roles.delete_at == None).all()
    return jsonify(ConvertModelListToDictList(rolesModel))

@app.route('/admin/role-management/create-role', methods=['POST'])
def createRole():
    role = models.Roles(role_name=request.json["role_name"], note=request.json["note"])
    db.session.add(role)
    db.session.commit()
    return jsonify(role.serialize())