import 'package:shop_app/services/http.service.dart';

final HttpService http = HttpService();

class CategoryApi {

  static Future<dynamic> getCategories() async {
    try {
      return await http.post('/get-categories', {});
    } catch (e) {
      print('ERROR in getCategories Api. $e');
      return [];
    }
  }

}

