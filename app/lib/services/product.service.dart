import 'package:provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:shop_app/api/category_api.dart';
import 'package:shop_app/models/category/Category.dart';
import 'package:shop_app/providers/category.provider.dart';

class ProductService {
  static Future<void> getCategories({BuildContext context, bool doLoading = true}) async {
    if (doLoading) {
      context.read<CategoryProvider>().setLoading(true);
    }
    try {

      final res = await CategoryApi.getCategories();
      final List<dynamic> _rawCategories = res["categories"];
      final List<Category> categories = _rawCategories.map((_category) => Category.fromJson(_category)).toList();
      context.read<CategoryProvider>().setCategories(categories);
    } catch (e) {
      print("ERROR in getCategories Service $e");
    }
    if (doLoading) {
      context.read<CategoryProvider>().setLoading(false);
    }
  }
}
