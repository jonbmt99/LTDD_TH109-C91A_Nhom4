import json
import random
import string
from datetime import datetime, timedelta

import jwt
import requests
from flask import url_for, session, request, jsonify, render_template
from oauthlib.oauth2 import WebApplicationClient
from requests_oauthlib import OAuth2Session


from library import app, db, socketio
from library.DAL import models, EmployeeRep, CustomerRep
from library.DAL.AccountRep import CreateAccount
from library.common.Req.AccountReq import CreateAccountReq, LoginRsp


from config import GOOGLE_DISCOVERY_URL, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
client = WebApplicationClient(GOOGLE_CLIENT_ID)
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
def get_google_auth(state=None, token=None):
    if token:
        return OAuth2Session(Auth.CLIENT_ID, token=token)
    if state:
        return OAuth2Session(Auth.CLIENT_ID, state=state, redirect_uri=Auth.REDIRECT_URI)
    oauth = OAuth2Session(Auth.CLIENT_ID, redirect_uri=Auth.REDIRECT_URI, scope=Auth.SCOPE)
    return oauth

class Auth:
    CLIENT_ID = ('258914989074-2rkptjvoc5mv1biv91pg4hhqd1igc9fs.apps.googleusercontent.com')
    CLIENT_SECRET = '1DtIDHTRYgVUQtdiGB_FNdXh'
    REDIRECT_URI = 'http://127.0.0.1:5000/gLogin/gCallback'
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'


@app.route("/gLogin", methods=['POST', 'GET'])
def gLogin():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/gCallback",
        scope=["openid", "email", "profile"],
    )
    return jsonify({
        "url": request_uri
    })

@app.route("/gLogin/gCallback", methods=['POST', 'GET'])
def gCallback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    print("userinfo_response: ", userinfo_response.json())
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        last_name = userinfo_response.json()["family_name"]
        first_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400


    customer = getCustomerByEmail(users_email)
    if customer != None:
        account = getAccountByID(customer.account_id)
    else:
        account = CreateAccount(CreateAccountReq(
            {
                "role_id": 3,
                "account_name": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
                "account_password": ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            }
        ))
        create_customer = models.Customers(last_name=last_name,
                                           first_name=first_name,
                                           email=users_email,
                                           account_id=account['account_id'],
                        )
        db.session.add(create_customer)
        db.session.commit()

    if (account['role']['role_id'] == 3):  # customer
        user = (models.Customers.query.filter(models.Customers.account_id == account['account_id'],
                                              models.Customers.account_id != None).first().serialize())
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
        'user_info':user,
    }
    res = LoginRsp(result).serialize()
    print(res)
    socketio.emit('login-google', {"data": res, "success": True}, room=0)
    return render_template("hello.html")

def getAccountByID(account_id):
    account = models.Accounts.query.filter(models.Accounts.account_id == account_id).first()
    return account.serialize() if account != None else None

def getCustomerByEmail(email):
    return models.Customers.query.filter(models.Customers.email == email).first()


