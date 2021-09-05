import 'package:flutter/foundation.dart' hide Category;
import 'package:shop_app/models/Cart.dart';
import 'package:shop_app/utils/array-handler.dart';


class CartProvider with ChangeNotifier, DiagnosticableTreeMixin {
  List<Cart> _cart = [];

  List<Cart> get cart => _cart;

  updateCart(Cart item) {
    final indexItemInCart = _cart.indexWhere((cart) => cart.product.id == item.product.id);
    if(indexItemInCart >= 0) {
      _cart[indexItemInCart].numOfItem += item.numOfItem;
    } else {
      _cart.add(item);
    }
    notifyListeners();
  }

  get totalItem {
    int total = 0;
    _cart.forEach((item) {
      total += item.numOfItem;
    });
    return total;
  }

  clearCart() {
    _cart = [];
    notifyListeners();
  }

  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
  }
}
