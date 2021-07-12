from functools import wraps

import jwt
from flask import request, jsonify

from library.DAL.models import Roles, Employees, Customers
from library.BLL import AccountSvc


def user_required(function):
    @wraps(function)
    def _verify():
        auth_headers = request.headers.get('Authorization', '').split()

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

        if len(auth_headers) != 2:
            return jsonify(not_authenticated_msg), 401
        try:
            token = auth_headers[1]
            account = AccountSvc.extractToken(token)
            if account["role"]["role_id"] == 3:
                user_info = Customers.query.filter(Customers.delete_at == None,
                                              Customers.account_id == account["account_id"])
                session = {
                    "account": account,
                    "user_info": user_info
                }
                return function(session)


        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401 # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError) as e:
            return jsonify(invalid_msg), 401
        return jsonify(not_authenticated_msg), 403
    return _verify


def owner_required(function):
    @wraps(function)
    def _verify():
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_role = {
            'message': 'Yêu cầu quyền hạn của chủ shop',
            'authenticated': False
        }
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

        if len(auth_headers) != 2:
            return jsonify(not_authenticated_msg), 401
        try:

            token = auth_headers[1]
            account = AccountSvc.extractToken(token)
            if (account["role"]["role_id"] == 1 or account["role_id"] == 2):
                user_info = Employees.query.filter(Employees.delete_at == None,
                                                   Employees.account_id == account["account_id"])
                session = {
                    "account": account,
                    "user_info": user_info
                }
                return function(session)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError) as e:
            return jsonify(invalid_msg), 401

        return jsonify(invalid_role), 403
    return _verify


def manager_required(f):
    @wraps(f)
    def _verify(auth_info):
        invalid_role = {
            'message': 'Yêu cầu quyền hạn của quản lí',
            'authenticated': False
        }
        if(auth_info['account']['role']['role_id'] == 1):
            return f(auth_info)

        return jsonify(invalid_role), 403
    return _verify
