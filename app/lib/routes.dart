import 'package:flutter/widgets.dart';
import 'package:shop_app/screens/complete_profile/complete_profile_screen.dart';
import 'package:shop_app/screens/forgot_password/forgot_password_screen.dart';
import 'package:shop_app/screens/otp/otp_screen.dart';
import 'package:shop_app/screens/profile/profile_screen.dart';
import 'package:shop_app/screens/splash/splash_screen.dart';


// We use name route
// All our routes will be available here
final Map<String, WidgetBuilder> routes = {
  SplashScreen.routeName: (context) => SplashScreen(),
  ForgotPasswordScreen.routeName: (context) => ForgotPasswordScreen(),
  OtpScreen.routeName: (context) => OtpScreen(),
  ProfileScreen.routeName: (context) => ProfileScreen(),
};
