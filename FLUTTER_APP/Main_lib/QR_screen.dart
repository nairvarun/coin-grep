import 'package:flutter/material.dart';
import 'package:qr_code_scanner/qr_code_scanner.dart';

class QRScannerPage extends StatefulWidget {
  @override
  _QRScannerPageState createState() => _QRScannerPageState();
}

class _QRScannerPageState extends State<QRScannerPage> {
  final GlobalKey qrKey = GlobalKey(debugLabel: 'QR');
  final qrText = TextEditingController();
  late QRViewController controller;

  void _onQRViewCreated(QRViewController controller) {
    this.controller = controller;
    controller.scannedDataStream.listen((scanData) {
      // Do something with the scan data
      print(scanData.code);
    });
  }

/*  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('QR Scanner'),
      ),
      body: QRView(
        key: qrKey,
        onQRViewCreated: _onQRViewCreated,
      ),
    );
  }*/
  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Expanded(
            child: QRView(
              key: qrKey,
              onQRViewCreated: _onQRViewCreated,
            ),
          ),
          TextField(
            controller: qrText,
            decoration: const InputDecoration(
              hintText: 'Scanned QR Code',
              border: OutlineInputBorder(),
            ),
          ),
        ],
      ),
    );
  }

  void onQRViewCreated(QRViewController controller) {
    this.controller = controller;
    controller.scannedDataStream.listen((scanData) {
      if (scanData.code != null) {
        setState(() {
          qrText.text = scanData.code!;
        });
        // Send the scanned string for further processing
        _sendString(scanData.code!);
      }
    });
  }

  void _sendString(String? scannedString) {
    // Send the scanned string for further processing
    print('Scanned String: $scannedString');
  }


  @override
  void toggleFlash() async {
    if (controller != null) {
      await controller.toggleFlash();
    }
  }
}

