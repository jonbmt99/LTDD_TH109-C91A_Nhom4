import 'package:shop_app/services/http.service.dart';

final HttpService http = HttpService();

class OrderApi {

  static Future<dynamic> createOrder(CreateOrderRequest request) async {
    try {
      return await http.post('/admin/order-management/create-order', request.toJson());
    } catch (e) {
      print('ERROR in create customer. $e');
      return e;
    }
  }

  static Future<dynamic> searchOrder(SearchOrderRequest request) async {
    try {
      return await http.post('/admin/order-management/search-orders', request.toJson());
    } catch (e) {
      print('ERROR in search customer. $e');
      return [];
    }
  }

}

class CreateOrderRequest {
  String customerId;
  List<OrderDetail> orderDetailList;


  CreateOrderRequest({
    this.customerId,
    this.orderDetailList,
  });

  Map<String, dynamic> toJson() => {
    "customer_id": customerId,
    "order_detail_list": orderDetailList,
  };

}

class SearchOrderRequest {
  int customerId;
  int page;
  int perPage;

  SearchOrderRequest({this.customerId, this.page, this.perPage});

  Map<String, dynamic> toJson() => {
    "customer_id": customerId,
    "page": page,
    "per_page": perPage,
  };
}

class OrderDetail {
  int productId;
  int quantity;

  OrderDetail({this.productId, this.quantity});

  Map<String, dynamic> toJson() => {
    "book_id": productId,
    "quantity": quantity,
  };
}
