import 'package:flutter/foundation.dart' hide Category;
import 'package:shop_app/models/Product.dart';
import 'package:shop_app/utils/array-handler.dart';


class ProductProvider with ChangeNotifier, DiagnosticableTreeMixin {

  bool _loadingCategories = false;
  List<Product> _products = demoProducts;
  Product _productActive;

  bool get loadingCategories => _loadingCategories;
  Product get productActive => _productActive;
  List<Product> get products => _products;

  setLoading(bool loading) {
    _loadingCategories = loading;
    notifyListeners();
  }

  setProducts(List<Product> products) {
    products.forEach((product) {
      _products = ArrayHandler<Product>().upsert(_products, product);
    });
    notifyListeners();
  }

  setProductActive(Product product) {
    _productActive = product;
  }


  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
  }
}
