import 'package:flutter/material.dart';
import 'package:shop_app/api/order_api.dart';

class Order {
  int orderId;
  List<OrderDetail> orderDetail;
  DateTime orderDate;

  Order({this.orderId,this.orderDetail, this.orderDate});
}


