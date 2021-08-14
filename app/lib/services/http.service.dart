import 'dart:convert';
import 'dart:io';
import 'package:shop_app/providers/authenticate.provider.dart';
import 'package:flutter/widgets.dart';
import 'package:http/http.dart';
import 'package:http/io_client.dart';
import 'package:provider/provider.dart';

const DEFAULT_HOST = 'http://localhost:5000';

BuildContext _context;

class JsonHttpResponse {
  int statusCode = 0;
  Map<String, dynamic> body = {};
}

class HttpService {
  static String hostUrl = DEFAULT_HOST;

  static setHost(String url) {
    hostUrl = url;
  }

  static injectContext(BuildContext context) {
    _context = context;
  }

  createHeader(String token) {
    String jwt;
    // if (token != null && token.length > 0) {
    //   jwt = token;
    // } else {
    //   jwt = _context.read<AuthenticateProvider>().currentToken;
    // }

    return {"authorization": "Bearer $jwt", "content-type": "application/json"};
  }

  dynamic handleError(Map<String, dynamic> body) {
    throw {
      "code": body["code"],
      "msg": body["msg"]
    };
  }

  dynamic extractData(Response res) {
    print("EXTRACT DATA $res");
    String _bodyBytes = utf8.decode(res.bodyBytes);

    JsonHttpResponse response = JsonHttpResponse();

    response.statusCode = res.statusCode;
    print("HTTP statusCode ${response.statusCode}");
    response.body = json.decode(_bodyBytes);

    if ((response.statusCode >= 200 && response.statusCode < 300)) {
      return response.body;
    }
    throw response.body;
  }

  dynamic post(String url, dynamic body, [String token]) {
    HttpClient _client = HttpClient();
    _client.badCertificateCallback = ((X509Certificate cert, String host, int port) => true);

    final http = IOClient(_client);
    final uri = Uri.parse(hostUrl + url);

    print("HTTP POST :: ${jsonEncode(body)}");
    return http
        .post(uri, headers: createHeader(token), body: jsonEncode(body))
        .then((res) => extractData(res))
        .catchError((error) {print("ERROR ${error.toString()}"); handleError(error);});
  }
}
