import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:shop_app/providers/authenticate.provider.dart';
import 'package:shop_app/providers/category.provider.dart';
import 'package:shop_app/providers/navigate.provider.dart';
import 'package:shop_app/providers/product.provider.dart';
import 'package:shop_app/route-information-parser.dart';
import 'package:shop_app/router-delegate.dart';
import 'package:shop_app/theme.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    AppRouterDelegate _routerDelegate = AppRouterDelegate();
    AppRouteInformationParser _routeInformationParser = AppRouteInformationParser();
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthenticateProvider()),
        ChangeNotifierProvider(create: (_) => NavigateProvider()),
        ChangeNotifierProvider(create: (_) => CategoryProvider()),
        ChangeNotifierProvider(create: (_) => ProductProvider()),
      ],
      child: MaterialApp.router(
        debugShowCheckedModeBanner: false,
        title: 'Flutter Ecommerce App',
        routerDelegate: _routerDelegate,
        routeInformationParser: _routeInformationParser,
        theme: theme(),
      ),
    );
  }
}
