import 'package:flutter/material.dart';
import 'package:shop_app/providers/product.provider.dart';
import '../../models/Product.dart';
import 'components/body.dart';
import 'components/custom_app_bar.dart';
import 'package:provider/provider.dart';


class DetailPage extends Page {
  DetailPage() : super(key: ValueKey('DetailPage'));

  @override
  Route createRoute(BuildContext context) {
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return DetailsScreen();
        });
  }
}

class DetailsScreen extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    final Product productDetails = context.watch<ProductProvider>().productActive;
    return Scaffold(
      backgroundColor: Color(0xFFF5F6F9),
      appBar: CustomAppBar(rating: productDetails.rating),
      body: Body(product: productDetails),
    );
  }
}

class ProductDetailsArguments {
  final Product product;

  ProductDetailsArguments({@required this.product});
}
