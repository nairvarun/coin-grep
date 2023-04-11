import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:coin_grep/Homepage.dart';
import 'package:responsive_framework/responsive_framework.dart';

void main() => runApp(HomepageApp());

class   HomepageApp extends StatelessWidget {
  const HomepageApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return  MaterialApp(
      title: 'Starting page',
      home: StartingPage(),
      builder: (context, child) => ResponsiveWrapper.builder(
          child,
          minWidth: 480,
          //maxWidth: 1200,
          minWidthLandscape : 200,
          defaultScale: true,
          breakpoints: [
            ResponsiveBreakpoint.resize(480, name: MOBILE),
            ResponsiveBreakpoint.autoScale(800, name: TABLET),
            ResponsiveBreakpoint.resize(1000, name: DESKTOP),
          ],
          background: Container(color: Color(0xFFF5F5F5))),
      initialRoute: "/",
    );
  }
}
class InputPage_App extends StatelessWidget {
  const InputPage_App({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'API Demo',

      home: InputPage_App(),
      builder: (context, child) => ResponsiveWrapper.builder(
          child,
          maxWidth: 1200,
          minWidth: 480,
          defaultScale: true,
          breakpoints: [
            ResponsiveBreakpoint.resize(480, name: MOBILE),
            ResponsiveBreakpoint.autoScale(800, name: TABLET),
            ResponsiveBreakpoint.resize(1000, name: DESKTOP),
          ],
          background: Container(color: Color(0xFFF5F5F5))),
      initialRoute: "/",
    );
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'API Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'API Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController _inputController = TextEditingController();
  String _output = "";

  Future<void> _getOutput() async {
    // Replace the URL below with your own FastAPI endpoint
    final url = Uri.parse("https://your-fastapi-endpoint.com/your-endpoint");

    // Encode the input as JSON
    final input = {"input": _inputController.text};
    final body = json.encode(input);

    // Make the API call
    final response = await http.post(url, headers: {"Content-Type": "application/json"}, body: body);

    // Decode the response JSON
    final output = json.decode(response.body)["output"];

    // Update the UI with the output
    setState(() {
      _output = output;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            TextField(
              controller: _inputController,
              decoration: InputDecoration(hintText: "Enter input"),
            ),
            ElevatedButton(
              onPressed: _getOutput,
              child: Text("Get output"),
            ),
            SizedBox(height: 20),
            Text("Output: $_output"),
          ],
        ),
      ),
    );
  }
}