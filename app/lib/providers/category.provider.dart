import 'package:flutter/foundation.dart' hide Category;
import 'package:shop_app/models/category/Category.dart';
import 'package:shop_app/utils/array-handler.dart';


class CategoryProvider with ChangeNotifier, DiagnosticableTreeMixin {

  bool _loadingCategories = false;
  List<Category> _categories = [];

  bool get loadingCategories => _loadingCategories;
  List<Category> get categories => _categories;

  setLoading(bool loading) {
    _loadingCategories = loading;
    notifyListeners();
  }

  setCategories(List<Category> categories) {
    categories.forEach((category) {
      _categories = ArrayHandler<Category>().upsert(_categories, category);
    });
    notifyListeners();
  }


  @override
  void debugFillProperties(DiagnosticPropertiesBuilder properties) {
    super.debugFillProperties(properties);
  }
}
