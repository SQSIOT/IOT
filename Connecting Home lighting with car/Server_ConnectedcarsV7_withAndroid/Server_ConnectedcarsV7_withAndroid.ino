#include <ESP8266WiFi.h>
#include <ESP8266WiFi.h>
#include <ESP8266mDNS.h>
#include <ArduinoOTA.h>
#include <ESP8266WebServer.h>

//Username and password
const char* ssid = "SQS";
const char* password = "d0n773llN0On3";
int value = HIGH;


//SQS Information
IPAddress ip(192, 168, 163, 150);   
IPAddress gateway(192, 168, 160, 1); 
IPAddress subnet(255,255,255,0); 
IPAddress dns1(192, 168, 192,4); 
IPAddress dns2(192, 168, 70,58);

//Pins to trigger relays
#define D1  16
#define D2  5
#define D3  4
#define D4  0

ESP8266WebServer server(80);
WiFiServer server2(10000);
WiFiServer server3(10001);

//Check if header is present and correct
bool is_authentified(){
  Serial.println("Enter is_authentified");
  if (server.hasHeader("Cookie")){   
    Serial.print("Found cookie: ");
    String cookie = server.header("Cookie");
    Serial.println(cookie);
    if (cookie.indexOf("ESPSESSIONID=1") != -1) {
      Serial.println("Authentification Successful");
      return true;
    }
  }
  Serial.println("Authentification Failed");
  return false;  
}

//Login Page
void handleLogin(){
  String msg;
  if (server.hasHeader("Cookie")){   
    Serial.print("Found cookie: ");
    String cookie = server.header("Cookie");
    Serial.println(cookie);
  }
  if (server.hasArg("DISCONNECT")){
    Serial.println("Disconnection");
    String header = "HTTP/1.1 301 OK\r\nSet-Cookie: ESPSESSIONID=0\r\nLocation: /login\r\nCache-Control: no-cache\r\n\r\n";
    server.sendContent(header);
    return;
  }
  if (server.hasArg("USERNAME") && server.hasArg("PASSWORD")){
    if (server.arg("USERNAME") == "admin" &&  server.arg("PASSWORD") == "admin" ){
      String header = "HTTP/1.1 301 OK\r\nSet-Cookie: ESPSESSIONID=1\r\nLocation: /\r\nCache-Control: no-cache\r\n\r\n";
      server.sendContent(header);
      Serial.println("Log in Successful");
      return;
    }
  msg = "Wrong username/password! try again.";
  Serial.println("Log in Failed");
  }
  //Here the whole HTML page is saved in form of string
  String content = "<html><body><center><p>IOT-HOME AUTOMATION LOGIN <br>MADE BY SQS-INDIA</p></center><form action='/login' method='POST'><br>";
  content += "<center>Username:<input type='text' name='USERNAME' placeholder='user name'></center><br>";
  content += "<center>Password:<input type='password' name='PASSWORD' placeholder='password'></center><br>";
  content += "<center><input type='submit' name='SUBMIT' value='Submit'></form>" + msg + "<br></center></body></html>";
  server.send(200, "text/html", content);
}


//If username and password is correct then display page to turn lights on and off
void handleRoot()
{
  Serial.println("Enter handleRoot");
  String header;
  if (!is_authentified()){
    String header = "HTTP/1.1 301 OK\r\nLocation: /login\r\nCache-Control: no-cache\r\n\r\n";
    server.sendContent(header);
    return;
  }
  String content = "<html><head><center><title>Home Automation - SQS INDIA</title></center></head><body><center><h1>IOT-HOME AUTOMATION<br>BY SQS INDIA<h1><p>Light <a href=\"/Light=OFF\">OFF</a> <br><p>Light <a href=\"/Light=ON\">ON</a><br></center></body></html><br><br>";
  if (server.hasHeader("User-Agent")){
    //content += "the user agent used is : " + server.header("User-Agent") + "<br><br>";
  }
  content += "<center><a href=\"/login?DISCONNECT=YES\">LOGOUT</a></center></body></html>";
  server.send(200, "text/html", content);
}

//If handler is not found then redirect
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

  pinMode(D1, OUTPUT);                                       //pins to trigger relay to be set as output
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);

  digitalWrite(D1, HIGH);                                    //Inverted logic on NodeMCU side so making pins high means they are set low initially
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  delay(1);

  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.config(ip,gateway,subnet,dns1,dns2);                 //Configure wifi by given default parameters
  WiFi.begin(ssid, password);                               //give username and password to connect to network

  while (WiFi.status() != WL_CONNECTED)                     //wait for wifi to get connected
  {
    Serial.print(".");
    WiFi.begin(ssid, password);
    delay(15000);
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.println(WiFi.localIP());                           //Will print IP to which webpage is being created open that page in Browser
  server.begin();                                           //Start your server here
  server2.begin();
  server3.begin();
  server.on("/", handleRoot);
  server.on("/login", handleLogin);                         //Handlers to redirect Pages
  server.on("/Light=OFF", LightOff);                        //Handlers to redirect Pages to turn Lights off
  server.on("/Light=ON", LightOn);                          //Handlers to redirect Pages to turn Lights ON

  server.onNotFound(handleNotFound);
  //here the list of headers to be recorded
  const char * headerkeys[] = {"User-Agent","Cookie"} ;     //Headers are like cookies will use to validate sessions
  size_t headerkeyssize = sizeof(headerkeys)/sizeof(char*);
  //ask server to track these headers
  server.collectHeaders(headerkeys, headerkeyssize );
}

void TurnOn(){
      digitalWrite(D1, LOW);
      digitalWrite(D2, LOW);
      digitalWrite(D3, LOW);
      digitalWrite(D4, LOW);
      Serial.println("Light On");
  }
void TurnOFF(){
      digitalWrite(D1, HIGH);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
      Serial.println("Light Off");
  }

void pi(){
  
  WiFiClient client1 = server2.available();
  if (!client1){
     //Serial.println("Not present");
     return;
  }

  //Serial.println("I was here");
  String req = client1.readStringUntil('\r');
  Serial.println(req);
  client1.flush();
  
  if(req == "Hello I'm Pi") {
      Serial.println(req);
      TurnOn();
      delay(1000);
  }
}

int android(){
  WiFiClient client2 = server3.available();
  if (!client2){
     //Serial.println("Not present");
     return 1;
  }
  while(!client2.available()){
    delay(10);  
  }
  String req1 = client2.readStringUntil('\r');
  Serial.println(req1);
  if(req1 == "Client"){
   //client2.println("Hello Shikha\n");
   while(1){
    client2.flush();
    String req1 = client2.readStringUntil('\r');
    Serial.println(req1);
    
      if(req1 == "l1on"){
        Serial.println(req1);
        digitalWrite(D1, LOW);
      }

       if(req1 == "l2on"){
        Serial.println(req1);
        digitalWrite(D2, LOW);
      }
       if(req1 == "l3on"){
        Serial.println(req1);
        digitalWrite(D3, LOW);
      }  
       if(req1 == "l4on"){
        Serial.println(req1);
        TurnOn();
      }
  
        if(req1 == "l1off"){
        Serial.println(req1);
        digitalWrite(D1, HIGH);
      }
  
       if(req1 == "l2off"){
        Serial.println(req1);
        digitalWrite(D2, HIGH);
      }
       if(req1 == "l3off"){
        Serial.println(req1);;
        digitalWrite(D3, HIGH);
      }  
       if(req1 == "l4off"){
        Serial.println(req1);
        TurnOFF();
      }
      if(req1 == "ClientClose"){
        Serial.println(req1);
        TurnOFF();
        client2.flush();
        client2.stop();
        delay(10);
        return 1;
      }
    }
  }
  else{return 1;} 
}                           
void loop(){
  server.handleClient();
  pi();
  android();
  
}


//This function will turn the lights on and redirect to pervious IP, we are just basically making pins low to turn the lights on due to inverted logic
void LightOn()
{ 
   String message = "<html><head><meta http-equiv=\"refresh\" content=\"1;url=http://192.168.163.150\"><center><p>LIGHTS OFF...!!!</p></center></head></html>";
   digitalWrite(D1, LOW);
   digitalWrite(D2, LOW);
   digitalWrite(D3, LOW);
   digitalWrite(D4, LOW);
   value = LOW;
   Serial.println("ON");
   delay(10);
   server.send ( 200, "text/html", message);
}

//This function will turn the lights off and redirect to pervious IP, we are just basically making pins high to turn the lights on due to inverted logic
void LightOff()
{
  String message = "<html><head><meta http-equiv=\"refresh\" content=\"1;url=http://192.168.163.150\"><center><p>LIGHTS OFF...!!!</p></center></head></html>";
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  value = HIGH;   
  Serial.println("OFF");
  delay(10);
  server.send ( 200, "text/html", message);
}

