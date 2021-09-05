class RoutePath {
  final String path;

  RoutePath.login() : path = "/";
  RoutePath.home() : path = "/home";
  RoutePath.register() : path = "/register";
  RoutePath.registerInfo() : path ="/register-info";
  RoutePath.profile() : path = "/profile";
  RoutePath.detail() : path = "/detail";
  RoutePath.cart() : path = "/cart";
  RoutePath.order() : path = "/order";
  RoutePath.qrCodeScan() : path = '/qr-code-scan';

  bool get isLoginPage => path == "/";
  bool get isHomePage => path == "/home";
  bool get isRegisterPage => path == "/register";
  bool get isProfilePage => path == "/profile";
  bool get isDetailPage => path == "/detail";
  bool get isCartPage => path == "/cart";
  bool get isOrderPage => path == "/order";
  bool get isQrCodeScanPage => path == "/qr-code-scan";
  bool get registerInfo => path == "/register-info";
}
