import 'package:shop_app/services/http.service.dart';

final HttpService http = HttpService();

class AccountApi {

  static Future<dynamic> createAccount(CreateAccountRequest request) async {
    try {
      return await http.post('/admin/account-management/create-account', request.toJson());
    } catch (e) {
      print('ERROR in create account. $e');
      return e;
    }
  }

  static Future<dynamic> login(LoginRequest request) async {
    try {
      return await http.post('/admin/account-management/login', request.toJson());
    } catch (e) {
      print('ERROR in login. $e');
      return e;
    }
  }

  static Future<dynamic> sendEmailResetPassword(String email) async {
    try {
      return await http.post('/send-reset-password-email-customer', {"email": email});
    } catch (e) {
      print('ERROR in send email reset password. $e');
      return e;
    }
  }

  static Future<dynamic> getCustomer(int customerId) async {
    try {
      return await http.post('/admin/customer-management/search-customers', {"customer_id": customerId});
    } catch (e) {
      print('Error in get customer. $e');
      return e;
    }
  }
}

class LoginRequest {
  String userName;
  String password;
  
  LoginRequest({this.userName, this.password});
  
  Map<String, dynamic> toJson() => {
    "user_name": userName,
    "password": password
  };
}

class CreateAccountRequest {
  String roleId;
  String accountName;
  String accountPassword;

  CreateAccountRequest({
    this.roleId,
    this.accountName,
    this.accountPassword
});

  Map<String, dynamic> toJson() => {
    "role_id": roleId,
    "account_name": accountName,
    "account_password": accountPassword,
    "confirm_account_password": accountPassword
  };

}
