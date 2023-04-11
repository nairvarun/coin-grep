import 'package:flutter/material.dart';
import 'package:coin_grep/input_page.dart';
import 'package:google_fonts/google_fonts.dart';

class StartingPage extends StatefulWidget {
  const StartingPage({Key? key}) : super(key: key);

  @override
  State<StartingPage> createState() => _StartingPageState();
}

Shader linearGradient_ =  LinearGradient(
  colors: <Color>[

    Color(0xFF8AD4EC),
    Color(0xFFEF96FF),
    Color(0xFFFF56A9),
    Color(0xffFFAA6C)
  ],
  stops: [0.39,0.6, 0.8, 1],
).createShader(Rect.fromLTWH(0, 0, 280.0, 40.0));

class _StartingPageState extends State<StartingPage> {

  @override
  Widget build(BuildContext context) {
    //var height = MediaQuery.of(context).size.height;
    //var width = MediaQuery.of(context).size.width;
    return Scaffold(
      //backgroundColor: const Color(0xFFE5413F),
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
                /*Color(0xffac255e),
                Color(0xffca485c),
                Color(0xffe16b5c),
                Color(0xfff39060),
                Color(0xffffb56b),*/
                ], // Gradient from https://learnui.design/tools/gradient-generator.html
                tileMode: TileMode.mirror,
              ),
            ),

            /*child: Stack(
              alignment: Alignment.center,
              children: <Widget>[
                Image.asset(
                  "Assets/Main logo.png",
                  fit: BoxFit.none,
                  height: 1000.0,
                  width: 1000.0,
                  color: Colors.white.withOpacity(1),
                  colorBlendMode: BlendMode.modulate,
            ),*/
            child: Padding(
              padding: const EdgeInsets.only(top: 75.0, left:70),
              child: Stack(
                //alignment: Alignment.center,
                children: <Widget>[
                  Image.asset(
                    "Assets/Main logo.png",
                    fit: BoxFit.fill,
                    width: 350.0,
                    height: 330.0,
                    color: Colors.white.withOpacity(1),
                    colorBlendMode: BlendMode.modulate,
                  ),
                  Padding(
                    padding: const EdgeInsets.only(top: 350, left: 80.0),
                    child: Stack(
                      alignment: Alignment.center,
                      children: <Widget>[

                        Text(
                          'COIN GREP\n\n',
                          textAlign: TextAlign.center,
                          style: GoogleFonts.poppins(
                            textStyle:  TextStyle(
                              fontSize: 22.0,
                              //color: Colors.white,
                              fontWeight: FontWeight.w700,
                              foreground: Paint()..shader = linearGradient_,
                            ),
                          ),
                        ),
                        Text(
                          'By SLOUGH KMK',
                          textAlign: TextAlign.center,
                          style: GoogleFonts.poppins(
                            textStyle:  TextStyle(
                              fontStyle: FontStyle.italic,
                              fontSize: 22.0,
                              //color: Colors.white,
                              fontWeight: FontWeight.w600,
                              foreground: Paint()..shader = linearGradient_,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                      Padding(
                      padding: const EdgeInsets.only(top: 530.0,left: 80),
                          child: SizedBox(
                            width: 200.0,
                            height: 60,

                            child:MaterialButton(
                              elevation: 15.0,
                              highlightColor: const Color(0xFFB3E5FC),
                              color: Colors.white,
                              onPressed:(){
                                Navigator.push(
                                    context,
                                    MaterialPageRoute(builder: (context) => InputPage(title: 'COIN GREP',)
                                    )
                                );
                              },
                              shape: (
                                RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(35.0),
                                side: const BorderSide(color: Colors.white)
                                )
                              ),
                              child: Text("Start",
                                textAlign: TextAlign.center,
                                style: GoogleFonts.poppins(
                                  textStyle:  TextStyle(
                                    fontStyle: FontStyle.italic,
                                    fontSize: 30.0,
                                    //color: Colors.white,
                                    fontWeight: FontWeight.w600,
                                    foreground: Paint()..shader = linearGradient_,
                                  ),),
                                ),
                              ),
                    ),
                  ),
      ],
      ),
            ),

          ),
      )
    );
  }
}


