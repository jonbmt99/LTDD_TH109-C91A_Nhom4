import 'package:shop_app/services/http.service.dart';

final HttpService http = HttpService();

class CustomerApi {

  static Future<dynamic> createCustomer(CreateCustomerRequest request) async {
    try {
      return await http.post('/admin/customer-management/create-customer', request.toJson());
    } catch (e) {
      print('ERROR in create customer. $e');
      return e;
    }
  }

}

class CreateCustomerRequest {
  String accountId;
  String lastName;
  String firstName;
  String email;
  String phone;
  String address;

  CreateCustomerRequest({
    this.accountId,
    this.lastName,
    this.firstName,
    this.email,
    this.phone,
    this.address
  });

  Map<String, dynamic> toJson() => {
    "account_id": accountId,
    "last_name": lastName,
    "first_name": firstName,
    "email": email,
    "phone": phone,
    "address": address
  };

}
