import 'package:flutter/material.dart';

import '../../size_config.dart';
import 'components/body.dart';

class SignInPage extends Page {
  SignInPage() : super(key: ValueKey('SignInPage'));

  @override
  Route createRoute(BuildContext context) {
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return SignInScreen();
        });
  }
}

class SignInScreen extends StatelessWidget {
  static String routeName = "/sign_in";
  @override
  Widget build(BuildContext context) {
    SizeConfig().init(context);
    return Scaffold(
      appBar: AppBar(
        title: Text("Đăng nhập"),
      ),
      body: Body(),
    );
  }
}
