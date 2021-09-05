import 'package:flutter/material.dart';
import 'package:flutter_money_formatter/flutter_money_formatter.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:shop_app/api/order_api.dart';
import 'package:shop_app/components/default_button.dart';
import 'package:shop_app/providers/authenticate.provider.dart';
import 'package:shop_app/providers/cart.provider.dart';
import 'package:shop_app/services/cart.service.dart';
import 'package:provider/provider.dart';
import 'package:shop_app/utils/toast.dart';

import '../../../constants.dart';
import '../../../size_config.dart';

class CheckoutCard extends StatefulWidget {

  const CheckoutCard({
    Key key,
  }) : super(key: key);

  @override
  _CheckoutCardState createState() => _CheckoutCardState();
}

class _CheckoutCardState extends State<CheckoutCard> {
  createOrder(BuildContext context) {
    final currentCart = context.read<CartProvider>().cart;
    if(currentCart.isEmpty) {
      EToast.error(context, "Giỏ hàng chưa có sản phẩm");
      return;
    }
    else {
      try {
        List<OrderDetail> listOrderDetail = [];
        currentCart.forEach((item) {
          listOrderDetail.add(OrderDetail(productId: item.product.id, quantity: item.numOfItem));
        });
        final request = CreateOrderRequest(customerId: context.read<AuthenticateProvider>().customerId, orderDetailList: listOrderDetail);
        OrderApi.createOrder(request);
        EToast.success(context, "Tạo đơn hàng thành công");
        context.read<CartProvider>().clearCart();
      } catch (e) {
        print("Error in create order $e");
        EToast.error(context, "Tạo đơn hàng thất bại");
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(
        vertical: getProportionateScreenWidth(15),
        horizontal: getProportionateScreenWidth(30),
      ),
      // height: 174,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.only(
          topLeft: Radius.circular(30),
          topRight: Radius.circular(30),
        ),
        boxShadow: [
          BoxShadow(
            offset: Offset(0, -15),
            blurRadius: 20,
            color: Color(0xFFDADADA).withOpacity(0.15),
          )
        ],
      ),
      child: SafeArea(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Container(
                  padding: EdgeInsets.all(10),
                  height: getProportionateScreenWidth(40),
                  width: getProportionateScreenWidth(40),
                  decoration: BoxDecoration(
                    color: Color(0xFFF5F6F9),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: SvgPicture.asset("assets/icons/receipt.svg"),
                ),
                Spacer(),
                Text("Thêm mã khuyến mãi"),
                const SizedBox(width: 10),
                Icon(
                  Icons.arrow_forward_ios,
                  size: 12,
                  color: kTextColor,
                )
              ],
            ),
            SizedBox(height: getProportionateScreenHeight(20)),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text.rich(
                  TextSpan(
                    text: "Tổng cộng:\n",
                    children: [
                      TextSpan(
                        text: '${FlutterMoneyFormatter(amount: CartService()
                            .totalPayment(context: context)).output.withoutFractionDigits}đ',
                        style: TextStyle(fontSize: 16, color: Colors.black),
                      ),
                    ],
                  ),
                ),
                SizedBox(
                  width: getProportionateScreenWidth(190),
                  child: DefaultButton(
                    text: "Thanh toán",
                    press: () {
                      setState(() {
                        createOrder(context);
                      });
                      }
                    ,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
