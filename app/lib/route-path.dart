class RoutePath {
  final String path;

  RoutePath.login() : path = "/";
  RoutePath.home() : path = "/home";
  RoutePath.register() : path = "/register";
  RoutePath.profile() : path = "/profile";

  bool get isLoginPage => path == "/";
  bool get isHomePage => path == "/home";
  bool get isRegisterPage => path == "/register";
  bool get isProfilePage => path == "/profile";
}
