#include <ESP8266WiFi.h>
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <ArduinoOTA.h>
#include <ESP8266WebServer.h>

const char* ssid = "SQS";
const char* password = "d0n773llN0On3";
int value = HIGH;
//String readString = String(1);

//SQS
IPAddress ip(192, 168, 163, 150);   
IPAddress gateway(192, 168, 160, 1); 
IPAddress subnet(255,255,255,0); 
IPAddress dns1(192, 168, 192,4); 
IPAddress dns2(192, 168, 70,58);


const char* www_username = "admin";
const char* www_password = "esp8266";


#define D1  16
#define D2  5
#define D3  4
#define D4  0

ESP8266WebServer server(80);

void handleRoot()
{
  char temp[400];
  snprintf ( temp, 400, 
      "<html>\
         <head>\
          <title>Home Automation Login Page</title>\
         </head>\
         <body>\
           <h1>Turn Lights on and of by clicking here<h1>\
           <p>Click <a href=\"/Light=OFF\">here</a> Turn Light OFF<br>\
           <p>Click <a href=\"/Light=ON\">here</a> Turn Light ON<br>\
          </body>\
       </html>"
   );
   server.send(200, "text/html", temp); 
}

void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += ( server.method() == HTTP_GET ) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";

  for ( uint8_t i = 0; i < server.args(); i++ ) {
    message += " " + server.argName ( i ) + ": " + server.arg ( i ) + "\n";
  }
  server.send ( 404, "text/plain", message );
}

void setup() {
  Serial.begin(115200);
  Serial.println();
  Serial.print("Configuring access point...");
  delay(10);

  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);

  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  delay(1);

  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.config(ip,gateway,subnet,dns1,dns2);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) 
  {
    Serial.print(".");
    WiFi.begin(ssid, password);
    delay(15000);
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.println(WiFi.localIP());
  server.begin();
   ArduinoOTA.begin();
              server.on("/", [](){
                if(!server.authenticate(www_username, www_password))
                  return server.requestAuthentication();
                   if ( MDNS.begin ( "esp8266" ) ) {
                         Serial.println ( "MDNS responder started" );
                    }
                      server.on ( "/", handleRoot );
                      server.on ( "/Light=ON", LightOn );
                      server.on ( "/Light=OFF", LightOff );
                      server.on ( "/inline", []() {
                        server.send ( 200, "text/plain", "this works as well" );
                      } );
                      
                      server.onNotFound ( handleNotFound );
                         //   server.send(200, "text/plain", "Login OK");
              });
}
                  
    /*
     Serial.println(req);
              
              //client.flush();
               if(req == "Hello I'm Pi") {
                Serial.println(req);
                digitalWrite(D1, LOW);
                digitalWrite(D2, LOW);
                digitalWrite(D3, LOW);
                digitalWrite(D4, LOW);
                client.print("Hello Pi");
                delay(10000);
               }*/
        
void loop(){
  // listen for incoming clients
  ArduinoOTA.handle();
  server.handleClient();
}

void LightOn()
{ 
   String message = "Lights on";
   digitalWrite(D1, LOW);
   digitalWrite(D2, LOW);
   digitalWrite(D3, LOW);
   digitalWrite(D4, LOW);
   value = LOW;
   Serial.println("ON");
   delay(10);
   server.send ( 404, "text/plain", message);
}


void LightOff()
{
  String message = "Lights off";
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  value = HIGH;   
  Serial.println("OFF");
  delay(10);
  server.send ( 404, "text/plain", message);
}

