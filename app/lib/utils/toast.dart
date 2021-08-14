import 'dart:async';

import 'package:flutter/material.dart';

class EToastBody extends StatefulWidget {
  final String message;
  final Color toastColor;

  EToastBody({
    @required this.message,
    @required this.toastColor
  });

  @override
  State<StatefulWidget> createState() => _EToastBodyState();
}

class _EToastBodyState extends State<EToastBody> {
  bool _forceDismiss = false;

  forceDismiss() {
    setState(() {
      _forceDismiss = true;
    });
  }

  @override
  Widget build(BuildContext context) {
    Timer(Duration(milliseconds: 1500), () {
      if (!_forceDismiss) {
        Navigator.of(context).pop();
      }
    });

    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Expanded(child: TextButton(
          onPressed: () {
            forceDismiss();
            Navigator.of(context).pop();
          },
          child: Row(
            children: [
              Expanded(child: Container(
                decoration: BoxDecoration(
                  color: widget.toastColor,
                ),
                padding: EdgeInsets.symmetric(vertical: 25, horizontal: 15),
                child: Text(
                    widget.message,
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 13,
                        decoration: TextDecoration.none
                    )
                ),
              ))
            ],
          )
        ))
      ],
    );
  }

}

class EToast {
  static show(BuildContext context, String message, Color toastColor) {
    showDialog(
      barrierColor: Colors.transparent,
      barrierDismissible: false,
      context: context,
      builder: (context) {
        return EToastBody(message: message, toastColor: toastColor);
      }
    );
  }

  static success(BuildContext context, String message) {
    show(context, message, Colors.green);
  }

  static error(BuildContext context, String message) {
    show(context, message, Colors.red);
  }
}
