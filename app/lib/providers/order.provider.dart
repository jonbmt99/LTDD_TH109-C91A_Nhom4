import 'package:flutter/foundation.dart' hide Category;
import 'package:shop_app/models/Order.dart';


class OrderProvider with ChangeNotifier, DiagnosticableTreeMixin {
  List<Order> _orders = [];

  get orders => _orders;

  setOrder(List<Order> orders) {
    _orders = orders;
    notifyListeners();
  }

  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
  }
}
