import 'package:flutter/material.dart';
import 'package:shop_app/providers/cart.provider.dart';
import 'package:provider/provider.dart';

import 'components/body.dart';
import 'components/check_out_card.dart';

class CartPage extends Page {
  CartPage() : super(key: ValueKey('CartPage'));

  @override
  Route createRoute(BuildContext context) {
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return CartScreen();
        });
  }
}

class CartScreen extends StatefulWidget {
  @override
  _CartScreenState createState() => _CartScreenState();
}

class _CartScreenState extends State<CartScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: buildAppBar(context),
      body: Body(),
      bottomNavigationBar: CheckoutCard(),
    );
  }

  AppBar buildAppBar(BuildContext context) {
    return AppBar(
      title: Column(
        children: [
          Text(
            "Giỏ hàng",
            style: TextStyle(color: Colors.black),
          ),
          Text(
            "${context.read<CartProvider>().cart.length} sản phẩm",
            style: Theme.of(context).textTheme.caption,
          ),
        ],
      ),
    );
  }
}
