import 'package:flutter/material.dart';
import 'package:shop_app/providers/cart.provider.dart';
import 'package:shop_app/providers/navigate.provider.dart';
import 'package:provider/provider.dart';
import 'package:shop_app/providers/order.provider.dart';
import '../../../size_config.dart';
import 'icon_btn_with_counter.dart';
import 'search_field.dart';

class HomeHeader extends StatefulWidget {
  const HomeHeader({
    Key key,
  }) : super(key: key);

  @override
  _HomeHeaderState createState() => _HomeHeaderState();
}

class _HomeHeaderState extends State<HomeHeader> {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding:
          EdgeInsets.symmetric(horizontal: getProportionateScreenWidth(20)),
      child: Consumer<CartProvider>(builder: (context, cart, child) =>
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              SearchField(),
              IconBtnWithCounter(
                svgSrc: "assets/icons/Cart Icon.svg",
                numOfitem: context.read<CartProvider>().totalItem,
                press: () => context.read<NavigateProvider>().navigate('/cart'),
              ),
              IconBtnWithCounter(
                svgSrc: "assets/icons/Bill Icon.svg",
                press: () => context.read<NavigateProvider>().navigate('/order'),
              ),
            ],
          ),
      ),
    );
  }
}
