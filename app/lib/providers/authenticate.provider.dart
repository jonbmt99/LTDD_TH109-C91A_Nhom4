import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'package:shared_preferences/shared_preferences.dart';


class AuthenticateProvider with ChangeNotifier, DiagnosticableTreeMixin {
  AuthenticateProvider() {
    checkToken();
  }

  String _token = "";
  String _accountId;

  String get currentToken => _token;
  String get accountId => _accountId;

  void setAccountId(String accountId) {
    _accountId = accountId;
  }

  Future<void> updateToken(String token) async {
    _token = token;
    notifyListeners();

    final prefs = await SharedPreferences.getInstance();
    prefs.setString('token', token);

    if (token.isEmpty) {
      prefs.clear();
    }
  }

  Future<SharedPreferences> checkToken() async {
    final prefs = await SharedPreferences.getInstance();
    try {
      updateToken(prefs.getString('token') ?? "");
    } catch (e) {
      print("ERROR in checkToken $e");
      updateToken("");
    }
    return prefs;
  }
}
