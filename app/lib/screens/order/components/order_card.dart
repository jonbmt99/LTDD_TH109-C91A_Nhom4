import 'package:flutter/material.dart';
import 'package:flutter_money_formatter/flutter_money_formatter.dart';
import 'package:shop_app/components/rounded_icon_btn.dart';
import 'package:shop_app/models/Cart.dart';

import '../../../constants.dart';
import '../../../size_config.dart';

class OrderCard extends StatelessWidget {
  const OrderCard({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 120,
      padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
      color: Color(0xFFF5F6F9),
      child: Row(
        children: [
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                "Mã đơn hàng: 31",
                style: TextStyle(color: Colors.black, fontSize: 16),
                maxLines: 2,
              ),
              Text(
                "Số lượng sản phẩm: 2",
                style: TextStyle(color: Colors.black, fontSize: 16),
                maxLines: 2,
              ),
              Text(
                "Tổng cộng: ${FlutterMoneyFormatter(amount: 1250000).output.withoutFractionDigits}đ",
                style: TextStyle(color: Colors.black, fontSize: 16),
                maxLines: 2,
              ),
              Text(
                "Xem chi tiết",
                style: TextStyle(color: kPrimaryColor, fontSize: 16),
                maxLines: 2,
              ),
            ],
          )
        ],
      ),
    );
  }
}
