import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:google_fonts/google_fonts.dart';
import 'package:coin_grep/output_page.dart';
import 'package:coin_grep/QR_screen.dart';
import 'package:coin_grep/qr3.dart';

class InputPage extends StatefulWidget {
  const InputPage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  _InputPageState createState() => _InputPageState();
}

Shader linearGradient_ =  const LinearGradient(
  colors: <Color>[

    Color(0xFF8AD4EC),
    Color(0xFFEF96FF),
    Color(0xFFFF56A9),
    Color(0xffFFAA6C)
  ],
  stops: [0.39,0.6, 0.8, 1],
).createShader(const Rect.fromLTWH(0, 0, 280.0, 40.0));


class _InputPageState extends State<InputPage> {
  final TextEditingController _inputController = TextEditingController();
  String output = "";
  String input="";

  /*Future<void> _getOutput() async {
    print("Sending API request");
    // Replace the URL below with your own FastAPI endpoint
    final url = Uri.parse("http://10.0.2.2:8000/check_fullnode");

    // Encode the input as JSON
    final input =  _inputController.text;
    final body = json.encode(input);

    // Make the API call
    final response = await http.post(url, headers: {"Content-Type": "application/json"}, body: body);

    //final response = await http.post(Uri.parse('http://localhost:8000'), headers: <String, String>{'Content-Type': 'application/json; charset=UTF-8',},
    //body: jsonEncode(<String, dynamic>{'input': input}),
    //);
    final output = json.decode(response.body)["output"];
    // Decode the response JSON

    print("recieve API request");
    print(output);
    // Update the UI with the output
    setState(() {
      _output = output;
    });*/
    //
    Future<String> getOutput(String? _input) async
    {
      if (_input == null) {
        print('Input cannot be null');
      }
      var url ="http://10.0.2.2:8000/check_fullnode?addr=$_input";
      //var url = 'https://your-api-url.com/'; // Replace this with the actual API endpoint
      var response = await http.post(Uri.parse(url), body: {'_input': _input});

      if (response.statusCode == 200) {
        return response.body;
      } else {
        throw Exception('Failed to retrieve output');
      }
    }
    void _updateInput(String value) {
      setState(() {
        input = value;
      });
    }


    //
   /* Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => OutputPage(output: _output,input: input, title: 'tarun',),
      ),
    );
  }*/

  @override
  Widget build(BuildContext context) {
    final Color myColor = const Color(0xFF44A1CE);
    return Scaffold(
        resizeToAvoidBottomInset : false,
      // appBar: AppBar(
       backgroundColor: Colors.black,
      //   title: Text(widget.title),
      // ),

      body: SingleChildScrollView(
            child: Container(
                height: 900.0,
                width: 500.0,
              //backgroundColor: Colors.pinkAccent,

                /*decoration: const BoxDecoration(
                gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment(1, 1),
                colors: <Color>[
                //#cc2b5e → #753a88
                Color(0xf9cc2b5e),
                Color(0xff753a88),
                //Color(0xf4b70581)//,
                Color(0xff510B2E),
                ], // Gradient from https://learnui.design/tools/gradient-generator.html
                tileMode: TileMode.mirror,
                ),
            ),*/

              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Padding(
                  padding: const EdgeInsets.only(left: 15.0,right: 15.0),
                  child:TextField(
                    onChanged: (value) => _updateInput(value),
                        textAlign: TextAlign.center,
                        enableInteractiveSelection: true ,
                        cursorColor: Colors.white,
                        cursorHeight: 30.0,
                        maxLines: 2,
                        cursorWidth: 2,
                        controller: _inputController,
                        decoration: const InputDecoration(
                          filled:true,
                            hintText: "Enter the crypto address",
                            fillColor: Color(0xDD42CBCB),
                          hintStyle: TextStyle(color: Colors.black,
                          fontWeight: FontWeight.w700),
                            contentPadding: EdgeInsets.symmetric(vertical: 10.0),
                            enabledBorder: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.white,width: 2.0)),
                            focusedBorder: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.white,width: 2.0)),
                        ),
                        style: const TextStyle(color: Colors.black87,
                        fontWeight: FontWeight.w500,
                        fontSize: 19),

                      ),
                  ),

                  Padding(
                    padding: const EdgeInsets.only(top: 50.0),
                    child: SizedBox(
                      width: 370.0,
                      height: 60,

                      child:MaterialButton(
                        elevation: 15.0,
                        highlightColor: const Color(0xFFB3E5FC),
                        color: Colors.white,
                        onPressed:() async {
                          // Call the _getOutput function to get the output
                          output = await getOutput(input);
                          if(output == "---"){
                            output = "Invalid Address";
                          }
                          print(output);
                          print("\n");
                          print(input);

                          // Navigate to the ResultScreen and pass the input and output as arguments
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                              builder: (context) => OutputPage(
                                  output: output,input: input,title: 'tarun',),
                            ),
                          );
                        },
                        /*async {
                          output = await getOutput(input);
                          Navigator.of(context).push(
                            MaterialPageRoute(
                              builder: (context) => OutputPage(output: output,input: input, title: 'tarun',),
                            ),
                          );

                        },*/
                        shape: (
                            RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(35.0),
                                side: const BorderSide(color: Colors.white)
                            )
                        ),
                        child: Text("Check this Address",
                          textAlign: TextAlign.center,
                          style: GoogleFonts.poppins(
                            textStyle:  TextStyle(
                              fontStyle: FontStyle.italic,
                              fontSize: 30.0,
                              color: Colors.cyan,
                              fontWeight: FontWeight.w600,
                              //foreground: Paint()..shader = linearGradient_,
                            ),),
                        ),
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 30.0),
                    child: SizedBox(
                      width: 370.0,
                      height: 60,

                      child: Text("OR",
                        textAlign: TextAlign.center,
                        style: GoogleFonts.poppins(
                          textStyle:  const TextStyle(
                            //fontStyle: FontStyle.italic,
                            fontSize: 30.0,
                            color: Colors.white,
                            fontWeight: FontWeight.w600,
                          ),),
                      ),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(left: 0.0, right: 0),
                    child: Stack(
                      //alignment: Alignment.center,
                      children: <Widget>[
                      Image.asset(
                      "Assets/QR.png",
                        fit: BoxFit.fill,
                        width: 150.0,
                        height: 145.0,
                        color: Colors.cyan.withOpacity(1),
                        //colorBlendMode: BlendMode.modulate,
                      ),
                      ],
                     ),
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 20.0),
                    child: SizedBox(
                      width: 370.0,
                      height: 60,

                      child:MaterialButton(
                        elevation: 15.0,
                        highlightColor: const Color(0xFFB3E5FC),
                        color: Colors.white,
                        onPressed:(){
                          Navigator.push(
                              context,
                              MaterialPageRoute(builder: (context) => const QRViewExample()
                              )
                          );
                        },
                        shape: (
                            RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(35.0),
                                side: const BorderSide(color: Colors.white)
                            )
                        ),

                        child: Text("Scan",
                          textAlign: TextAlign.center,
                          style: GoogleFonts.poppins(
                            textStyle:  TextStyle(
                              fontStyle: FontStyle.italic,
                              fontSize: 30.0,
                              color: Colors.cyan,
                              fontWeight: FontWeight.w600,
                              //foreground: Paint()..shader = linearGradient_,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),

                  ],
                  //SizedBox(height: 30,),
                  //Text("Output: $_output"),
                //),
              ),
      ),
      )
    );
  }
}