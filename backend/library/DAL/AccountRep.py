from flask import jsonify, url_for
from flask_bcrypt import check_password_hash
from sqlalchemy import or_
import hashlib
from library import db
from library.common.Req.AccountReq import CreateAccountReq, DeleteAccountReq, LoginReq, SendResetPasswordEmailReq, \
    ChangePasswordReq, CreateCustomerAccountReq, CreateEmployeeAccountReq
from library.common.Rsp.SingleRsp import ErrorRsp
from library.common.util import ConvertModelListToDictList
from library.DAL import models
from datetime import datetime
from library import bcrypt


def CreateAccount(req: CreateAccountReq):
    hashed_password = hashlib.md5(req.account_password.encode('utf-8')).hexdigest()
    create_account = models.Accounts(account_name=req.account_name,
                                     account_password=hashed_password,
                                     note=req.note, delete_at=req.deleted_at, role_id=req.role_id)
    db.session.add(create_account)
    db.session.commit()
    return create_account.serialize()


def ValidateAccountName(acc_name: str):
    acc = models.Accounts.query.filter(
        models.Accounts.account_name == acc_name and models.Accounts.delete_at is None).first()
    return True if acc else False


def GetAccountsByPage(req):
    account_pagination = models.Accounts.query.filter(models.Accounts.delete_at == None).paginate(page=req.page,
                                                                                                  per_page=req.per_page)
    has_next = account_pagination.has_next
    has_prev = account_pagination.has_prev
    accounts = ConvertModelListToDictList(account_pagination.items)
    return has_next, has_prev, accounts


def SearchAccounts(acc_info):
    model_accounts = models.Accounts.query.filter(or_(models.Accounts.account_id == acc_info.account_id,
                                                      models.Accounts.account_name == acc_info.account_name,
                                                      )).all()
    accounts = ConvertModelListToDictList(model_accounts)
    return accounts


def DeleteAccount(acc_info: DeleteAccountReq):
    deleted_account = models.Accounts.query.filter((models.Accounts.account_name == acc_info.account_name) | (
            models.Accounts.account_id == acc_info.account_id)).first()
    deleted_account.delete_at = datetime.now()
    db.session.add(deleted_account)
    db.session.commit()
    return acc_info


def Authenticate(acc_info: LoginReq):
    account = models.Accounts.query.filter_by(account_name=acc_info.user_name).first()
    if not account:
        raise ErrorRsp(code=400, message='Tài khoản không tồn tại', msg='Tài khoản không tồn tại')

    if str(hashlib.md5(acc_info.password.encode('utf-8')).hexdigest()) != account.account_password:
        raise ErrorRsp(code=400, message='Mật khẩu không chính xác', msg='Mật khẩu không chính xác')
    return account.serialize()


def GetAccountByCustomerEmail(req):
    customer_email = req.email
    account = models.Customers.query.filter(models.Customers.email == customer_email).first().account.serialize()
    return account


def GetAccountByEmployeeEmail(req: SendResetPasswordEmailReq):
    employee_email = req.email
    account = models.Employees.query.filter(models.Employees.email == employee_email).first().account.serialize()
    return account


def ResetPassword(acc_id, password):
    account = models.Accounts.query.get(int(acc_id))
    account.account_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    db.session.commit()
    return account.serialize()


def ChangePassword(req: ChangePasswordReq):
    account = models.Accounts.query.get(int(req.account_id))
    hashed_new_password = str(hashlib.md5(req.new_password.strip().encode("utf-8")).hexdigest())
    hashed_current_password = str(hashlib.md5(req.current_password.strip().encode("utf-8")).hexdigest())

    if account.account_password == hashed_current_password:
        account.account_password = hashed_new_password
        db.session.commit()
    else:
        raise ErrorRsp(code=400, message='Mật khẩu không chính xác', msg="Mật khẩu không chính xác")

    return account.serialize()


def CreateCustomerAccount(req: CreateCustomerAccountReq):
    is_exist_account_name_customer = models.Accounts.query.filter(
        models.Accounts.account_name == req.account_name).first()
    is_exist_email_phone_customer = models.Customers.query.filter(or_(models.Customers.email == req.email,
                                                                      models.Customers.phone == req.phone)).first()
    if is_exist_account_name_customer:
        raise ErrorRsp(code=400, message='Tài khoản tồn tại', msg='Tài khoản tồn tại')

    hashed_password = hashlib.md5(req.account_password.encode('utf-8')).hexdigest()
    create_account = models.Accounts(account_name=req.account_name,
                                     account_password=hashed_password, role_id=req.role_id)

    db.session.begin_nested()
    db.session.add(create_account)
    db.session.commit()

    if is_exist_email_phone_customer:
        db.session.rollback()
        raise ErrorRsp(code=400, message='số điện thoại, chứng minh nhân dân hoặc email đẫ tồn tại',
                       msg='số điện thoại, chứng minh nhân dânhoặc email đẫ tồn tại')
    create_customer = models.Customers(
                                       account_id=create_account.account_id,
                                       last_name=req.last_name,
                                       first_name=req.first_name,
                                       phone=req.phone,
                                       birth_date=req.birth_date,
                                       address=req.address,
                                       gender=req.gender,
                                       province_id=req.province_id,
                                       district_id=req.district_id,
                                       ward_id=req.ward_id,
                                       email=req.email,
                                       image=req.image,
                                       )

    db.session.add(create_customer)
    db.session.commit()

    return create_account.serialize(), create_customer.serialize()


def CreateEmployeeAccount(req: CreateEmployeeAccountReq):
    is_exist_account_name_employee = models.Accounts.query.filter(models.Accounts.account_name == req.account_name).first()
    is_exist_email_phone_employee = models.Employees.query.filter(or_(models.Employees.email == req.email,
                                                                      models.Employees.phone == req.phone,
                                                                      )).first()
    if is_exist_account_name_employee:
        raise ErrorRsp(code=400, message='Tài khoản tồn tại', msg='Tài khoản tồn tại')

    hashed_password = hashlib.md5(req.account_password.encode('utf-8')).hexdigest()
    create_account = models.Accounts(account_name=req.account_name,
                                     account_password=hashed_password,
                                     note=req.note, role_id=req.role_id)
    db.session.begin_nested()
    db.session.add(create_account)
    db.session.commit()
    if is_exist_email_phone_employee:
        db.session.rollback()
        raise ErrorRsp(code=400, message='số điện thoại, chứng minh nhân dân hoặc email đẫ tồn tại',
                       msg='số điện thoại, chứng minh nhân dân hoặc email đẫ tồn tại')
    create_employee = models.Employees(
                                       account_id=create_account.account_id,
                                       last_name=req.last_name,
                                       first_name=req.first_name,
                                       phone=req.phone,
                                       email=req.email,
                                       birth_date=req.birth_date,
                                       hire_date=req.hire_date,
                                       address=req.address,
                                       gender=req.gender,
                                       image=req.image,
                                       basic_rate=req.basic_rate,
                                       province_id=req.province_id,
                                       district_id=req.district_id,
                                       ward_id=req.ward_id,
                                       note=req.note)

    db.session.add(create_employee)
    db.session.commit()

    return create_account.serialize(), create_employee.serialize()

def getAccountById(id):
    accountModel = models.Accounts.query.filter(models.Accounts.account_id == id).first()
    return accountModel.serialize()
