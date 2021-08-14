import 'package:flutter/material.dart';
import 'package:shop_app/components/coustom_bottom_nav_bar.dart';
import 'package:shop_app/enums.dart';
import 'package:shop_app/services/category.service.dart';

import 'components/body.dart';

class HomePage extends Page {
  HomePage() : super(key: ValueKey('HomePage'));

  @override
  Route createRoute(BuildContext context) {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      CategoryService.getCategories(context: context);
    });
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return HomeScreen();
        });
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Body(),
      bottomNavigationBar: CustomBottomNavBar(selectedMenu: MenuState.home),
    );
  }
}
