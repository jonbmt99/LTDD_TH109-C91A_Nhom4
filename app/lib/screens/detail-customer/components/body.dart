import 'package:flutter/material.dart';
import 'package:shop_app/api/account_api.dart';
import 'package:shop_app/providers/authenticate.provider.dart';
import 'package:shop_app/providers/navigate.provider.dart';
import 'package:provider/provider.dart';

class Body extends StatefulWidget {
  @override
  _BodyState createState() => _BodyState();
}

class _BodyState extends State<Body> {
  String fullName = "";
  String email = "";
  String phone;
  String address = "";

  getDetailCustomer(BuildContext context) async {
    try {
      final customerId = context.read<AuthenticateProvider>().customerId;
      final res = await AccountApi.getCustomer(int.parse(customerId));
      final customer = res["customer"][0];
      setState(() {
        this.fullName = customer["first_name"] as String;
        this.fullName += " " + customer["last_name"];
        this.email = customer["email"] as String;
        this.phone = customer["phone"] as String;
        this.address = customer["address"] as String;
        print("fullname123: ${this.fullName}");
      });
    } catch (e) {
      print("Error in get detail Customer in detail-customer screen");
    }
  }


  @override
  void initState() {
    super.initState();
    getDetailCustomer(context);
  }

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      padding: EdgeInsets.symmetric(vertical: 20),
      child: Column(
        children: [
          rowInfo("Tên: ", fullName),
          rowInfo("Email: ", email),
          rowInfo("Số điện thoại: ", phone),
          rowInfo("Địa chỉ: ", address),
        ],
      ),
    );
  }
}

Widget rowInfo(String title, String info) {
  return Padding(
    padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
    child: FlatButton(
      padding: EdgeInsets.all(20),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
      color: Color(0xFFF5F6F9),
      onPressed: () async {},
      child: Row(
        children: [
          Text(title),
          SizedBox(width: 5),
          Text(info),
        ],
      ),
    ),
  );
}
