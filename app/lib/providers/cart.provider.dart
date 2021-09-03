import 'package:flutter/foundation.dart' hide Category;
import 'package:shop_app/models/Cart.dart';
import 'package:shop_app/models/Product.dart';
import 'package:shop_app/utils/array-handler.dart';


class CartProvider with ChangeNotifier, DiagnosticableTreeMixin {
  List<Cart> _cart = [];

  List<Cart> get cart => _cart;

  updateCart(Cart item) {
    _cart.add(item);
    notifyListeners();
  }

  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
  }
}
