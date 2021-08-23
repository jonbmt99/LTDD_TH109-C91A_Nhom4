import 'package:flutter/material.dart';

import 'components/body.dart';

class CompleteProfilePage extends Page {
  CompleteProfilePage() : super(key: ValueKey('CompleteProfilePage'));

  @override
  Route createRoute(BuildContext context) {
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return CompleteProfileScreen();
        });
  }
}

class CompleteProfileScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Sign Up'),
      ),
      body: Body(),
    );
  }
}
