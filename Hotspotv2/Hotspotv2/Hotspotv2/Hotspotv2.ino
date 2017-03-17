#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server(80);
WiFiServer server1(8080);

const char *espssid = "ESP8266";
const char *esppassword = "password";

String Wifi_username = "";
String Wifi_pass     = "";
String msg           = "";

int access_point = 0;
int wifi_connected =0;

//Pin Declaration
#define D0  16
#define D1  5
#define D2  4
#define D3  0


//If handler is not found then redirect
void handleNotFound(){
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

void handleRoot(){
                    //  Serial.println("Enter handleRoot");
                    String header;
                      if (!is_authentified()){
                        String header = "HTTP/1.1 301 OK\r\nLocation: /login\r\nCache-Control: no-cache\r\n\r\n";
                        server.sendContent(header);
                        return;
                      }
                      else{
                        String content = "<html><head><center><title>Home Automation - SQS INDIA</title></center></head><body><center><h1>IOT-HOME AUTOMATION<br>BY SQS INDIA<h1><p>Thank You</a><br></center></body></html><br><br>";
                        server.send(200, "text/html", content); 
                        return;
                      }
                      
                   }

//Check if header is present and correct
bool is_authentified(){
                      //  Serial.println("Enter is_authentified");
                      if (server.hasHeader("Cookie")){   
                          //    Serial.print("Found cookie: ");
                          String cookie = server.header("Cookie");
                          //    Serial.println(cookie);
                          if (cookie.indexOf("ESPSESSIONID=1") != -1) {
                      //      Serial.println("Authentification Successful");
                            return true;
                          }
                       }
                        //  Serial.println("Authentification Failed");
                        return false;  
                      }

//Login Page
void handleLogin(){
                    if (server.hasHeader("Cookie")){   
                  //    Serial.print("Found cookie: ");
                      String cookie = server.header("Cookie");
                  //    Serial.println(cookie);
                    }
                    if (server.hasArg("DISCONNECT")){
                  //    Serial.println("Disconnection");
                      String header = "HTTP/1.1 301 OK\r\nSet-Cookie: ESPSESSIONID=0\r\nLocation: /login\r\nCache-Control: no-cache\r\n\r\n";
                      server.sendContent(header);
                      return;
                    }
                    if (server.hasArg("USERNAME") && server.hasArg("PASSWORD")){
                         Wifi_username  = server.arg("USERNAME");
                         Wifi_pass      = server.arg("PASSWORD");
                         WifiSetup(Wifi_username, Wifi_pass);
                         if((WiFi.status() == WL_CONNECTED)){
                                String header = "HTTP/1.1 301 OK\r\nSet-Cookie: ESPSESSIONID=1\r\nLocation: /\r\nCache-Control: no-cache\r\n\r\n";
                                server.sendContent(header);
                                return;
                          }
                         else{
                           msg = "Cannot connect to Given Username/Password";
                           String header = "HTTP/1.1 301 OK\r\nSet-Cookie: ESPSESSIONID=0\r\nLocation: /login\r\nCache-Control: no-cache\r\n\r\n";
                           server.sendContent(header);
                         }
                      }
                    
                    //Here the whole HTML page is saved in form of string
                    String content = "<html><body><center><p>IOT-HOME AUTOMATION LOGIN <br>MADE BY SQS-INDIA</p></center><form action='/login' method='POST'><br>";
                    content += "<br><center>Please Enter Login In details</center><br><center>Username(SSID):<input type='text' name='USERNAME' placeholder='user name'></center><br>";
                    content += "<center>Password:<input type='password' name='PASSWORD' placeholder='password'></center><br>";
                    content += "<center><input type='submit' name='SUBMIT' value='Submit'></form><br><br>" + msg + "<br></center></body></html>";
                    server.send(200, "text/html", content);
                  }


void createAccessPoint() {
                          delay(1000);
                          Serial.begin(115200);
                          Serial.println();
                          Serial.println("Configuring access point...");
                          WiFi.softAP(espssid, esppassword);
                          IPAddress myIP = WiFi.softAPIP();
                          Serial.println("AP IP address: ");
                          Serial.println(myIP);
                          server.on("/", handleRoot);
                          server.on("/login", handleLogin);
                          server.onNotFound(handleNotFound);
                          //here the list of headers to be recorded
                          const char * headerkeys[] = {"User-Agent","Cookie"} ;     //Headers are like cookies will use to validate sessions
                          size_t headerkeyssize = sizeof(headerkeys)/sizeof(char*);
                          //ask server to track these headers
                          server.collectHeaders(headerkeys, headerkeyssize );
                          server.begin();
                          Serial.println("HTTP server started");
                          }


void WifiSetup(String wifi, String wifi_pass){ 
                                             //WiFi.hostname("Home");
                                             const char *wifissid  = wifi.c_str();
                                             const char *wifipass  = wifi_pass.c_str();

                                             Serial.println(wifissid);
                                             Serial.println(wifipass);       
                                                                                    
                                             Serial.print("Connecting to ");
                                             Serial.println(Wifi_username);
                                           
                                             WiFi.begin(wifissid,wifipass);
                                             delay(500);

                                             while (WiFi.status() != WL_CONNECTED) { 
                                                        delay(500);
                                                        Serial.print(".");
                                             }
                                             
                                             String content = "<html><head><center><title>Home Automation - SQS INDIA</title></center></head><body><center><h1>Connected to Wifi<h1><p>Thank You</a><br></center></body></html><br><br>";
                                             server.send(200, "text/html", content); 
                                             
                                             Serial.println("WiFi connected");
                                             
                                             WiFi.softAPdisconnect(true);
                                             delay(100);    
                                             
                                             server1.begin();
                                             Serial.println("Server1 started");
                                             wifi_connected = 1;
                                             all_off();
                                             // Print the IP address
                                             Serial.print("Use this URL to connect: ");
                                             Serial.print("http://");
                                             Serial.print(WiFi.localIP());                                        
                                             Serial.print("/");
                                            }
void pin_declaration(){
                        pinMode(D0, OUTPUT);
                        pinMode(D1, OUTPUT);
                        pinMode(D2, OUTPUT);
                        pinMode(D3, OUTPUT);
                      
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

void Home_Auto(){
  while(true){ 
       WiFiClient client = server1.available();
       if(!client)
          return;
       while(!client.available())
                   delay(1);
                   
       Serial.println("new client");            
       String request = client.readStringUntil('\r');
       client.print("ACK");
       Serial.println(request);
       client.flush();
                     
       if (request.indexOf("/LED=ON") != -1)
                      all_on();
                      
       else if (request.indexOf("/LED1=ON") != -1)
                      digitalWrite(D0, LOW);
                      
       else if (request.indexOf("/LED2=ON") != -1)
                      digitalWrite(D1, LOW);
                      
       else if (request.indexOf("/LED3=ON") != -1)
                      digitalWrite(D2, LOW);
                      
       else if (request.indexOf("/LED4=ON") != -1)
                      digitalWrite(D3, LOW);
                                          
       else if (request.indexOf("/LED=OFF") != -1)
                      all_off();
 
       else if (request.indexOf("/LED1=OFF") != -1)
                      digitalWrite(D0, HIGH);
                      
       else if (request.indexOf("/LED2=OFF") != -1)
                      digitalWrite(D1, HIGH);
                      
       else if (request.indexOf("/LED3=OFF") != -1)
                      digitalWrite(D2, HIGH);
                      
       else if (request.indexOf("/LED4=OFF") != -1)
                      digitalWrite(D3, HIGH);  
                                     
  }
}

void setup(){
            createAccessPoint();
            pin_declaration();           
}                            

void loop(){
    if(wifi_connected == 0)
        server.handleClient();
    else
      Home_Auto();
}
