import 'package:flutter/material.dart';

import 'components/body.dart';

class SignUpPage extends Page {
  SignUpPage() : super(key: ValueKey('SignUpPage'));

  @override
  Route createRoute(BuildContext context) {
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return SignUpScreen();
        });
  }
}

class SignUpScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Đăng kí"),
      ),
      body: Body(),
    );
  }
}
