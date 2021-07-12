from email.message import EmailMessage

import jwt
from datetime import datetime, timedelta

from flask import jsonify

from library import app, smtp

from library.common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, SendResetPasswordEmailReq, \
    ResetPasswordReq, ChangePasswordReq

from library.common.Req.CustomerReq import SearchCustomersReq

from library.common.Req.EmployeeReq import SearchEmployeesReq

from library.common.Rsp.SingleRsp import ErrorRsp

from library.DAL import AccountRep, CustomerRep, EmployeeRep, MessageRep, models
from library.common.util import ConvertModelListToDictList


def CreateAccount(req):
    is_account_existed = AccountRep.ValidateAccountName(req.account_name)
    if (is_account_existed):
        return jsonify({'msg': "Taif khoan da ton tai "}), 401
    else:
        res = AccountRep.CreateAccount(req)
        return res


def GetAccountsByPage(req):
    has_next, has_prev, accounts = AccountRep.GetAccountsByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "accounts": accounts
    }
    return result


def DeleteAccount(req: DeleteAccountReq):
    res = AccountRep.DeleteAccount(req)
    return res


def SearchAccounts(acc_info):
    accounts = AccountRep.SearchAccounts(acc_info)
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
        info_accounts.append(account_info)

    return info_accounts


def AuthenticateUser(acc: LoginReq):
    try:
        account = AccountRep.Authenticate(acc)
        if (account['role']['role_id'] == 3):  # customer
            user = (models.Customers.query.filter(models.Customers.account_id == account['account_id'],
                                                  models.Customers.account_id != None).first().serialize())
        if (account['role']['role_id'] == 1 or account['role']['role_id'] == 2):  # admin, manager
            user = (models.Employees.query.filter(models.Employees.account_id == account['account_id'],
                                                  models.Employees.account_id != None).first().serialize())
        secect_key = app.config['SECRET_KEY']
        payload = {
            'account_id': account['account_id'],
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=300000)
        }
        access_token = jwt.encode(payload, secect_key)
        result = {
            'access_token': access_token,
            'account': account,
            'user_info': user,
        }
        return result
    except ErrorRsp as e:
        raise e


def SendResetPasswordEmailCustomer(req: SendResetPasswordEmailReq):
    smtp.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    account = AccountRep.GetAccountByCustomerEmail(req)
    secect_key = app.config['SECRET_KEY']
    payload = {
        'account_id': account['account_id'],
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=300000)
    }
    reset_email_token = jwt.encode(payload, secect_key).decode('utf-8')

    msg = EmailMessage()
    msg['Subject'] = 'Khôi phục mật khẩu Thư quán Đại học Mở TPHCM'
    msg['From'] = app.config['MAIL_USERNAME']
    msg['To'] = req.email
    msg.set_content(
        f'''    Gửi {app.config['MAIL_USERNAME']},
    Bạn (hoặc một ai đó) đang muốn khôi phục mật khẩu của tài khoản shinichi24567@gmail.com-01-test.
    Nếu là bạn, hãy bấm vào liên kết bên dưới để khôi phục mật khẩu: (có hiệu lực trong 24 giờ)

    http://localhost:4200/reset-password?token={reset_email_token}
    Nếu không phải bạn, hãy bỏ qua email này.

    Đội ngũ quản lý thư quán Đại học Mở TPHCM!
''')
    smtp.send_message(msg)
    return " Vui lòng kiểm tra email để reset mật khẩu"


def SendResetPasswordEmailEmployee(req: SendResetPasswordEmailReq):
    smtp.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    account = AccountRep.GetAccountByEmployeeEmail(req)
    secect_key = app.config['SECRET_KEY']
    payload = {
        'account_id': account['account_id'],
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=300000)
    }
    reset_email_token = jwt.encode(payload, secect_key).decode('utf-8')

    msg = EmailMessage()
    msg['Subject'] = 'Khôi phục mật khẩu Thư quán Đại học Mở TPHCM'
    msg['From'] = app.config['MAIL_USERNAME']
    msg['To'] = req.email
    msg.set_content(
        f'''    Gửi {app.config['MAIL_USERNAME']},
    Bạn (hoặc một ai đó) đang muốn khôi phục mật khẩu của tài khoản shinichi24567@gmail.com-01-test.
    Nếu là bạn, hãy bấm vào liên kết bên dưới để khôi phục mật khẩu: (có hiệu lực trong 24 giờ)

    http://localhost:4200/reset-password?token={reset_email_token}
    Nếu không phải bạn, hãy bỏ qua email này.

    Đội ngũ quản lý thư quán Đại học Mở TPHCM!
''')
    smtp.send_message(msg)
    return {msg: 'Vui lòng kiểm tra email để reset mật khẩu'}


def ResetPassword(req: ResetPasswordReq):
    payload = jwt.decode(req.token, app.config['SECRET_KEY'])
    account_id = payload['account_id']
    result = AccountRep.ResetPassword(account_id, req.password)
    return result


def ChangePassword(req: ChangePasswordReq):
    try:
        result = AccountRep.ChangePassword(req)
        return result
    except ErrorRsp as e:
        raise e


def CreateCustomerAccount(req):
    create_customer_account = AccountRep.CreateCustomerAccount(req)
    create_conversation_request = {
        'customer_account_id': create_customer_account[0]['account_id']
    }
    _ = MessageRep.CreateConversation(create_conversation_request)
    return create_customer_account


def CreateEmployeeAccount(req):
    create_employee_account = AccountRep.CreateEmployeeAccount(req)
    return create_employee_account


def extractToken(token):
    payload = jwt.decode(token, app.config['SECRET_KEY'])
    accountId = payload["account_id"]

    account = AccountRep.getAccountById(accountId)
    return account


def sessionInfo(token):
    invalid_msg = {
        'message': 'Token không hợp lệ.',
        'authenticated': False
    }
    expired_msg = {
        'message': 'Token hết hạn sử dụng.',
        'authenticated': False
    }
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        accountId = payload["accountId"]
        account = AccountRep.getAccountById(accountId)
        result = {
            'accessToken': token,
            'account': account,
        }
        return result

    except jwt.ExpiredSignatureError:
        return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
    except (jwt.InvalidTokenError) as e:
        return jsonify(invalid_msg), 401
