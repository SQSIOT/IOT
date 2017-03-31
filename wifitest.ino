#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <EEPROM.h>

ESP8266WebServer server(80);
WiFiServer server1(8080);

const char* ssid = "ESP8266";
const char* passphrase = "password";

String st;
String content;

char Off = '1';
int reconnect   = 0;
int wificonnect = 0;
int statusCode;
int val = 1;
int delay1 = 0;

//Pin Declaration
#define D0        16
#define D1        5
#define D2        4
#define D3        0
#define reset     2


void pin_declaration(){
                      pinMode(D0, OUTPUT);
                      pinMode(D1, OUTPUT);
                      pinMode(D2, OUTPUT);
                      pinMode(D3, OUTPUT);
                      pinMode(reset, INPUT);
                                        
                      digitalWrite(D0, HIGH);
                      digitalWrite(D1, HIGH);
                      digitalWrite(D2, HIGH);
                      digitalWrite(D3, HIGH);
}

void all_on(){
              digitalWrite(D0, LOW);
              digitalWrite(D1, LOW);
              digitalWrite(D2, LOW);
              digitalWrite(D3, LOW); 
}

void all_off(){
              digitalWrite(D0, HIGH);
              digitalWrite(D1, HIGH);
              digitalWrite(D2, HIGH);
              digitalWrite(D3, HIGH); 
}
              
bool testWifi(void) {
  int c = 0;
  Serial.println("Waiting for Wifi to connect");  

  while ( c < 20 ) {
      if (WiFi.status() == WL_CONNECTED) { 
                  all_on();
                  server1.begin();
                  Serial.println("Server1 started");
                  wificonnect = 1;
                  return true;
    }
    delay(500);
    Serial.print(WiFi.status());    
    c++;
  }
  Serial.println("");
  Serial.println("Connect timed out, opening AP");
  return false;
} 



void launchWeb(int webtype) {
  Serial.println("");
  Serial.println("Access point created");
//  Serial.print("Local IP: ");
//  Serial.println(WiFi.localIP());
//  Serial.print("SoftAP IP: ");
//  Serial.println(WiFi.softAPIP());
//  Serial.println("In launchweb");
  createWebServer(webtype);
//  Serial.println("Exit launcweb");
  // Start the server
  server.begin();
  Serial.println("Server started"); 
}

void setupAP(void) {
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
  
//  Serial.println("In setupAP");
  int n = WiFi.scanNetworks();
  Serial.println("scan done");
  if (n == 0)
    Serial.println("no networks found");
  else
  {
    Serial.print(n);
    Serial.println(" networks found");
    for (int i = 0; i < n; i++)
     {
      // Print SSID and RSSI for each network found
      Serial.print(i + 1);
      Serial.print(": ");
      Serial.print(WiFi.SSID(i));
      Serial.print(" (");
      Serial.print(WiFi.RSSI(i));
      Serial.print(")");
      Serial.println((WiFi.encryptionType(i) == ENC_TYPE_NONE)?" ":"*");
      delay(10);
     }
  }
  Serial.println(""); 
  st = "<ol>";
  for (int i = 0; i < n; i++)
    {
      // Print SSID and RSSI for each network found
      st += "<li>";
      st += WiFi.SSID(i);
      st += " (";
      st += WiFi.RSSI(i);
      st += ")";
      st += (WiFi.encryptionType(i) == ENC_TYPE_NONE)?" ":"*";
      st += "</li>";
    }
  st += "</ol>";
  delay(100);
  WiFi.softAP(ssid, passphrase);
  Serial.println("Connect to ESP8266 to configure wifi");
  launchWeb(1);
//  Serial.println("Exit setupAB");
//  Serial.println("over");
}

void createWebServer(int webtype)
{
  if ( webtype == 1 ) {
//    Serial.println("In createwebserver/1");
    server.on("/", []() {
        IPAddress ip = WiFi.softAPIP();
        String ipStr = String(ip[0]) + '.' + String(ip[1]) + '.' + String(ip[2]) + '.' + String(ip[3]);
        content = "<!DOCTYPE HTML>\r\n<html>Hello from ESP8266 at ";
        content += ipStr;
        content += "<p>";
        content += st;
        content += "</p><form method='get' action='setting'><label>SSID: </label><input name='ssid' length=32><input name='pass' length=64><input type='submit'></form>";
        content += "</html>";
        server.send(200, "text/html", content);  
    });
    server.on("/setting", []() {
        String qsid = server.arg("ssid");
        String qpass = server.arg("pass");
        if (qsid.length() > 0 && qpass.length() > 0) {
          Serial.println("clearing eeprom");
          for (int i = 0; i < 96; i++) { EEPROM.write(i, 0); }
//          Serial.println(qsid);
//          Serial.println("");
//          Serial.println(qpass);
//          Serial.println("");
            
          Serial.println("writing eeprom ssid:");
          for (int i = 0; i < qsid.length(); i++)
            {
              EEPROM.write(i, qsid[i]);
//              Serial.print("Wrote: ");
//              Serial.println(qsid[i]); 
            }
          Serial.println("writing eeprom pass:"); 
          for (int i = 0; i < qpass.length(); i++)
            {
              EEPROM.write(40+i, qpass[i]);
//              Serial.print("Wrote: ");
//              Serial.println(qpass[i]); 
            }    
          EEPROM.commit();
          content = "{\"Success\":\"saved to eeprom... reset to boot into new wifi\"}";
          statusCode = 200;
        } else {
          content = "{\"Error\":\"404 not found\"}";
          statusCode = 404;
          Serial.println("Sending 404");
        }
        server.send(statusCode, "application/json", content);
    });
  } else if (webtype == 0) {
//    Serial.println("In createwebserver/0");
    server.on("/", []() {
      IPAddress ip = WiFi.localIP();
      String ipStr = String(ip[0]) + '.' + String(ip[1]) + '.' + String(ip[2]) + '.' + String(ip[3]);
      server.send(200, "application/json", "{\"IP\":\"" + ipStr + "\"}");
    });
    server.on("/cleareeprom", []() {
      content = "<!DOCTYPE HTML>\r\n<html>";
      content += "<p>Clearing the EEPROM</p></html>";
      server.send(200, "text/html", content);
      Serial.println("clearing eeprom");
      for (int i = 0; i < 96; i++) { EEPROM.write(i, 0); }
      EEPROM.commit();
    });
  }
}



void setup() {

  Serial.begin(115200);
  EEPROM.begin(512);
  pin_declaration();
  
  delay(10);
  Serial.println();
  Serial.println();
  //Serial.println("Startup");
  // read eeprom for ssid and pass
  
  String esid;

 
  Serial.println("Press external reset button to enter configuration mode");
  while (delay1 < 100){
      val = digitalRead(reset);
      if(!val)
        break;
      Serial.print(".");
      delay(100);
      ++ delay1;
  }
  if(!val){
        //Serial.println("");
        ;
  }
  else{
    Serial.println("Reading EEPROM ssid");   
    for (int i = 0; i < 40; i++)
    {
        esid += char(EEPROM.read(i));
    }
  
    Serial.print("SSID: ");
    Serial.println(esid);
    Serial.println("Reading EEPROM pass");
    String epass = "";
    for (int i = 40; i < 96; i++)
    {
        epass += char(EEPROM.read(i));
    }
    Serial.print("PASS: ");
    Serial.println(epass);  
  
    if ( esid.length() > 1 ) {
        WiFi.begin(esid.c_str(), epass.c_str());
        if (testWifi()) {
          launchWeb(0);
          return;
        } 
    }
    setupAP();
  }
  setupAP();
}

void Home_Auto()
{   //Serial.println(WiFi.localIP()); 
    while(true)
    { 
        if(WiFi.status() == WL_CONNECTED){
            WiFiClient client = server1.available();
            if(!client)
                return;
            while(!client.available())
                delay(1);
                       
            Serial.println("new client");            
            String request = client.readStringUntil('\r');
            client.print("ACK");
            Serial.println(request);
            //Serial.println(request[request.indexOf("/")+1]);
            //Serial.println(request[request.indexOf("/")+2]);
            //Serial.println(request[request.indexOf("/")+3]);
            //Serial.println(request[request.indexOf("/")+4]);
            client.flush();      
           
            if (request[request.indexOf("/") + 1] == Off)
                digitalWrite(D0, LOW);
            else 
                digitalWrite(D0, HIGH);
    
            if (request[request.indexOf("/") + 2] == Off)
                digitalWrite(D1, LOW);
            else 
                digitalWrite(D1, HIGH);
    
            if (request[request.indexOf("/") + 3] == Off)
                digitalWrite(D2, LOW);
            else 
                digitalWrite(D2, HIGH);
    
            if (request[request.indexOf("/") + 4] == Off)
                digitalWrite(D3, LOW);
            else 
                digitalWrite(D3, HIGH);
        }else{
          all_off();
          reconnect = 1;
          return;
         }
    }
}

void loop(){   
  if(wificonnect == 0)
        server.handleClient();
  else
        Home_Auto();
        if(reconnect == 1){
          ESP.eraseConfig(); return;}
        delay(1000);
}
