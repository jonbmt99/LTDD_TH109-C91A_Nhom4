import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:provider/provider.dart';
import 'package:shop_app/providers/authenticate.provider.dart';
import 'package:shop_app/providers/navigate.provider.dart';
import 'package:shop_app/screens/cart/cart_screen.dart';
import 'package:shop_app/screens/complete_profile/complete_profile_screen.dart';
import 'package:shop_app/screens/details/details_screen.dart';
import 'package:shop_app/screens/home/home_screen.dart';
import 'package:shop_app/screens/profile/profile_screen.dart';
import 'package:shop_app/screens/qr_code_scan/qr_code_scan_screen.dart';
import 'package:shop_app/screens/sign_in/sign_in_screen.dart';
import 'package:shop_app/screens/sign_up/sign_up_screen.dart';

import 'route-path.dart';


class AppRouterDelegate extends RouterDelegate<RoutePath>
    with ChangeNotifier, PopNavigatorRouterDelegateMixin<RoutePath> {

  final GlobalKey<NavigatorState> navigatorKey = GlobalKey<NavigatorState>();

  @override
  Widget build(BuildContext context) {

    String _watchingToken = context.watch<AuthenticateProvider>().currentToken ?? '';
    bool _watchingAuthenticated =_watchingToken.isNotEmpty;

    List<String> _routeSegments =
        context.watch<NavigateProvider>().route.split("/");


    return Navigator(
      key: navigatorKey,
      pages: [
        if (!_watchingAuthenticated) SignInPage(),
        if (!_watchingAuthenticated && _routeSegments[1] == 'register') SignUpPage(),
        if (!_watchingAuthenticated && _routeSegments[1] == 'register-info') CompleteProfilePage(),
        if (_watchingAuthenticated) HomePage(),
        if (_watchingAuthenticated &&_routeSegments[1] == 'profile') ProfilePage(),
        if (_watchingAuthenticated &&_routeSegments[1] == 'detail') DetailPage(),
        if(_watchingAuthenticated && _routeSegments[1] == 'cart') CartPage(),
        if(_watchingAuthenticated && _routeSegments[1] == 'qr-code-scan') QrCodeScanPage(),
      ],
      onPopPage: (route, result) {
        if (!route.didPop(result)) {
          return false;
        }
        return true;
      },
    );
  }

  @override
  Future<void> setNewRoutePath(RoutePath path) async {
    print("setNewRoutePath $path");
  }
}
