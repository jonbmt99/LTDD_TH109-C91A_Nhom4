import 'package:flutter/material.dart';
import 'package:shop_app/components/default_button.dart';
import 'package:shop_app/components/rounded_icon_btn.dart';
import 'package:shop_app/models/Cart.dart';
import 'package:shop_app/models/Product.dart';
import 'package:shop_app/screens/details/components/top_rounded_container.dart';
import 'package:shop_app/services/cart.service.dart';
import 'package:shop_app/utils/toast.dart';

import '../../../constants.dart';
import '../../../size_config.dart';

class ColorDots extends StatefulWidget {
  const ColorDots({
    Key key,
    @required this.product,
  }) : super(key: key);

  final Product product;

  @override
  _ColorDotsState createState() => _ColorDotsState();
}

class _ColorDotsState extends State<ColorDots> {
  int numOfItem = 1;
  @override
  Widget build(BuildContext context) {
    // Now this is fixed and only for demo
    int selectedColor = 3;
    return Padding(
      padding:
          EdgeInsets.symmetric(horizontal: getProportionateScreenWidth(20)),
      child: Column(
        children: [
          Row(
            children: [
              ...List.generate(
                widget.product.colors.length,
                (index) => ColorDot(
                  color: widget.product.colors[index],
                  isSelected: index == selectedColor,
                ),
              ),
              Spacer(),
              RoundedIconBtn(
                icon: Icons.remove,
                press: () {
                  setState(() {
                    numOfItem--;
                  });
                },
              ),
              SizedBox(
                width: getProportionateScreenWidth(40),
                child: Center(
                  child: Text(numOfItem.toString()),
                ),
              ),
              RoundedIconBtn(
                icon: Icons.add,
                showShadow: true,
                press: () {
                  setState(() {
                    numOfItem++;
                  });
                },
              ),
            ],
          ),
          TopRoundedContainer(
            color: Colors.white,
            child: Padding(
              padding: EdgeInsets.only(
                left: SizeConfig.screenWidth * 0.15,
                right: SizeConfig.screenWidth * 0.15,
                bottom: getProportionateScreenWidth(40),
                top: getProportionateScreenWidth(15),
              ),
              child: DefaultButton(
                text: "Thêm vào giỏ hàng",
                press: () {
                  CartService().updateCart(context: context,item: Cart(product: widget.product,numOfItem: numOfItem));
                  EToast.success(context, 'Thêm $numOfItem ${widget.product.title} vào giỏ hàng thành công');
                },
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class ColorDot extends StatelessWidget {
  const ColorDot({
    Key key,
    @required this.color,
    this.isSelected = false,
  }) : super(key: key);

  final Color color;
  final bool isSelected;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.only(right: 2),
      padding: EdgeInsets.all(getProportionateScreenWidth(8)),
      height: getProportionateScreenWidth(40),
      width: getProportionateScreenWidth(40),
      decoration: BoxDecoration(
        color: Colors.transparent,
        border:
            Border.all(color: isSelected ? kPrimaryColor : Colors.transparent),
        shape: BoxShape.circle,
      ),
      child: DecoratedBox(
        decoration: BoxDecoration(
          color: color,
          shape: BoxShape.circle,
        ),
      ),
    );
  }
}
