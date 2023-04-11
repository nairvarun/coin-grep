//import 'dart:convert';
import 'package:flutter/material.dart';
//import 'package:http/http.dart' as http;
import 'package:google_fonts/google_fonts.dart';
//import 'package:coin_grep/input_page.dart';

class OutputPage extends StatefulWidget {
  const OutputPage({
    Key? key,
    required this.title,
    required this.output,
    required this.input,
  }) : super(key: key);

  //final String output;

  final String output;
  final String? input;
  final String title;


  @override
  _OutputPageState createState() => _OutputPageState();
}

Shader linearGradient_ =  const LinearGradient(
  colors: <Color>[

    Color(0xFF8AD4EC),
    Color(0xFFEF96FF),
    Color(0xFFFF56A9),
    Color(0xffFFAA6C)
  ],
  stops: [0.39,0.6, 0.8, 1],
).createShader(Rect.fromLTWH(0, 0, 280.0, 40.0));

class _OutputPageState extends State<OutputPage> {
  String get output => widget.output;
  String? get input => widget.input;
  
  @override
  Widget build(BuildContext context) {
    //var height = MediaQuery.of(context).size.height;
    //var width = MediaQuery.of(context).size.width;
    return Scaffold(

        body: Center(
          child: Container(
            height: 1000.0,
            width: 500.0,
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment(1, 1),
                colors: <Color>[
                  //#cc2b5e → #753a88
                  Color(0xf9cc2b5e),
                  Color(0xff753a88),
                  //Color(0xf4b70581)//,
                  Color(0xff510B2E),
                ],
                // Gradient from https://learnui.design/tools/gradient-generator.html
                tileMode: TileMode.mirror,
              ),
            ),

            child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[

            Padding(
            padding: const EdgeInsets.only(top: 50.0),

              child: Text("Output: $output\n\nAddress: $input ",
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  textStyle:  TextStyle(
                    fontStyle: FontStyle.italic,
                    fontSize: 30.0,
                    color: Colors.white,
                    fontWeight: FontWeight.w600,
                    //foreground: Paint()..shader = linearGradient_,
                  ),),
              ),

            ),
            ]
          ),
        ),
        )
    );
  }
}