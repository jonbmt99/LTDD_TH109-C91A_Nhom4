import 'package:flutter/widgets.dart';

import 'route-path.dart';

class AppRouteInformationParser
    extends RouteInformationParser<RoutePath> {
  @override
  Future<RoutePath> parseRouteInformation(
      RouteInformation routeInformation) async {
    final uri = Uri.parse(routeInformation.location);

    // Handle "/"

    if (uri.pathSegments.length == 0) {
      return RoutePath.login();
    }

    if (uri.pathSegments.length == 1) {
      switch (uri.pathSegments[0]) {
        case "home":
          return RoutePath.home();
        case "register":
          return RoutePath.register();
        case "profile":
          return RoutePath.profile();
        default:
          return RoutePath.login();
      }
    }

    return RoutePath.login();
  }

  @override
  RouteInformation restoreRouteInformation(RoutePath path) {
    if (path.isLoginPage) {
      return RouteInformation(location: "/");
    }
    if (path.isHomePage) {
      return RouteInformation(location: "/home");
    }
    if (path.isRegisterPage) {
      return RouteInformation(location: "/register");
    }
    return null;
  }
}
