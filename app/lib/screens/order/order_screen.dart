import 'package:flutter/material.dart';
import 'package:shop_app/providers/cart.provider.dart';
import 'package:provider/provider.dart';
import 'package:shop_app/services/order.service.dart';

import 'components/body.dart';

class OrderPage extends Page {
  OrderPage() : super(key: ValueKey('OrderPage'));

  @override
  Route createRoute(BuildContext context) {
    OrderService.getOrders(context);
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return OrderScreen();
        });
  }
}

class OrderScreen extends StatefulWidget {
  @override
  _OrderScreenState createState() => _OrderScreenState();
}

class _OrderScreenState extends State<OrderScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: buildAppBar(context),
      body: Body(),
    );
  }

  AppBar buildAppBar(BuildContext context) {
    return AppBar(
      title: Text(
        "Đơn hàng",
        style: TextStyle(color: Colors.black),
      ),
    );
  }
}
