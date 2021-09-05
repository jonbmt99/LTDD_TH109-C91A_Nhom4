import 'package:flutter/material.dart';

import 'package:provider/provider.dart';
import 'package:shop_app/api/order_api.dart';
import 'package:shop_app/models/Order.dart';
import 'package:shop_app/providers/authenticate.provider.dart';


class OrderService {
  static getOrders(BuildContext context) async {
    try {
      final customerId = context.read<AuthenticateProvider>().customerId;
      final request = SearchOrderRequest(customerId: int.parse(customerId), page: 1, perPage: 20);
      final res = await OrderApi.searchOrder(request);
      final List<dynamic> _rawOrders = res["orders"];
      // final List<Order> orders = _rawOrders.map((order) => {
      //   Order(
      //     orderId: order["order_id"] as int,
      //     orderDate:  order["order_date"] as DateTime,
      //     orderDetail: [OrderDetail(productId: order["order_details"][0]["book"]["book_id"] as int,
      //         quantity: order["order_details"][0]["quantity"] as int)]
      //   )
      // }).cast<Order>();
    } catch (e) {
      print("Error in search Order");
    }
  }
}
