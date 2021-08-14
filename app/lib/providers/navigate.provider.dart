import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';


class NavigateProvider with ChangeNotifier, DiagnosticableTreeMixin {
  NavigateProvider();

  String _route = "/call-center";
  int _bottomMenuIndex = 0;

  String get route => _route;
  int get bottomMenuIndex => _bottomMenuIndex;

  navigate(String destination, [int menuIndex]) {
    _route = destination;

    if (menuIndex != null) {
      _bottomMenuIndex = menuIndex;
    }

    notifyListeners();
  }

  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
    properties.add(StringProperty('route', route));
    properties.add(IntProperty('bottomMenuIndex', bottomMenuIndex));
  }
}
