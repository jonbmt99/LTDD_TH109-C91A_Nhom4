import 'package:flutter/material.dart';
import 'package:shop_app/components/coustom_bottom_nav_bar.dart';
import 'package:shop_app/enums.dart';

import 'components/body.dart';

class DetailCustomerPage extends Page {
  DetailCustomerPage() : super(key: ValueKey('DetailCustomerPage'));

  @override
  Route createRoute(BuildContext context) {
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return DetailCustomerScreen();
        });
  }
}

class DetailCustomerScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Thông tin tài khoản"),
      ),
      body: Body(),
    );
  }
}
