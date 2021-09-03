import 'package:flutter/material.dart';
import 'package:shop_app/models/Cart.dart';
import 'package:shop_app/providers/cart.provider.dart';
import 'package:provider/provider.dart';


class CartService {
  updateCart({BuildContext context, Cart item}) {
    context.read<CartProvider>().updateCart(item);
  }

  double totalPayment({BuildContext context}) {
    final cart = context.read<CartProvider>().cart;
    double total = 0;
    cart.forEach((item) {
      total += item.numOfItem * item.product.price;
    });
    return total;
  }
}
