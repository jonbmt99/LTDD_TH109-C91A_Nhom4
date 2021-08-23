import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:barcode_scan/barcode_scan.dart';
import 'package:permission_handler/permission_handler.dart';

class QrCodeScanPage extends Page {
  QrCodeScanPage() : super(key: ValueKey('QrCodeScanPage'));

  @override
  Route createRoute(BuildContext context) {
    return MaterialPageRoute(
        settings: this,
        builder: (BuildContext context) {
          return QrCodeScanScreen();
        });
  }
}

class QrCodeScanScreen extends StatefulWidget {
  @override
  _QrCodeScanScreenState createState() => _QrCodeScanScreenState();
}

class _QrCodeScanScreenState extends State<QrCodeScanScreen> {
  String result = "Please scan the QR code or Barcode";

  @override
  void initState() {
    () async {
      PermissionStatus permission = await _getCameraPermission();
      if (permission == PermissionStatus.granted) {
        showRequestPermission('Quyền truy cập camera',
            'Shop app muốn truy cập camera để quét QR code');
      }
    }();

    super.initState();
  }

  Future _scanQR() async {
    try {
      String qrResult = await BarcodeScanner.scan();
      setState(() {
        result = qrResult;
      });
    } on PlatformException catch (ex) {
      if (ex.code == BarcodeScanner.CameraAccessDenied) {
        setState(() {
          result = "Camera permission was denied";
        });
      } else {
        setState(() {
          result = "Unknown Error $ex";
        });
      }
    } on FormatException {
      setState(() {
        result = "You pressed the back button before scanning anything";
      });
    } catch (ex) {
      setState(() {
        result = "Unknown Error $ex";
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Thông tin sản phẩm"),
      ),
      body: Text(
        result,
        style: new TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
      ),
      floatingActionButton: FloatingActionButton.extended(
        icon: Icon(Icons.camera_alt),
        label: Text("Scan"),
        onPressed: _scanQR,
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
    );
  }

  showRequestPermission(String title, String content) {
    return showDialog(
        context: context,
        builder: (BuildContext context) => CupertinoAlertDialog(
              title: Text(title),
              content: Text(content),
              actions: <Widget>[
                CupertinoDialogAction(
                  child: Text('Đóng'),
                  onPressed: () => Navigator.of(context).pop(),
                ),
                CupertinoDialogAction(
                  child: Text('Thiết lập'),
                  onPressed: () => openSettingsApp(context),
                ),
              ],
            ));
  }

  openSettingsApp(BuildContext context) {
    Navigator.of(context).pop();
    openAppSettings();
  }

  Future<PermissionStatus> _getCameraPermission() async {
    PermissionStatus permission = await Permission.camera.status;
    if (permission != PermissionStatus.granted &&
        permission != PermissionStatus.permanentlyDenied) {
      PermissionStatus permissionStatus = await Permission.camera.request();
      return permissionStatus;
    } else {
      return permission;
    }
  }
}
