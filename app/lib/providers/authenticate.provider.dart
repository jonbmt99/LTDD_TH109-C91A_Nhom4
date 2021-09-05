import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:flutter/widgets.dart';
import 'package:shared_preferences/shared_preferences.dart';


class AuthenticateProvider with ChangeNotifier, DiagnosticableTreeMixin {
  AuthenticateProvider() {
    checkToken();
  }

  String _token = "";
  String _accountId = "";
  String _customerId;
  String _fullName = "";

  String get currentToken => _token;
  String get accountId => _accountId;
  String get customerId => _customerId;
  String get fullName => _fullName;

  void setAccountId(String accountId) {
    _accountId = accountId;
    notifyListeners();
  }

  void setFullName(String fullName) {
    _fullName = fullName;
    notifyListeners();
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

  Future<void> updateCustomerId(String customerId) async {
    _customerId = customerId;
    notifyListeners();

    final prefs = await SharedPreferences.getInstance();
    prefs.setString('customerId', customerId);
    if (customerId.isEmpty) {
      prefs.setString("customerId", "");
    }
  }

  Future<SharedPreferences> checkToken() async {
    final prefs = await SharedPreferences.getInstance();
    try {
      updateToken(prefs.getString('token') ?? "");
      updateCustomerId(prefs.getString('customerId') ?? "");
    } catch (e) {
      print("ERROR in checkToken $e");
      updateToken("");
    }
    return prefs;
  }
}
