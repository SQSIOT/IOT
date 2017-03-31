#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#define SERIAL_DEBUG  Serial

WiFiServer server1(8080);
char Off = '1';

//Pin Declaration
#define D0  16
#define D1  5
#define D2  4
#define D3  0


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


void setup()
{ 
    Serial.begin(115200);
    pin_declaration();  
    ESP.eraseConfig();
    const char *wifissid  = "IoTLab";
    const char *wifipass  = "Discover&Share";
                                            
    SERIAL_DEBUG.println("\r\n========== SDK Saved parameters Start"); 
    WiFi.printDiag(SERIAL_DEBUG);
    SERIAL_DEBUG.println("========== SDK Saved parameters End"); 
                                            
    SERIAL_DEBUG.println("Connecting...");
    SERIAL_DEBUG.flush();
    WiFi.begin(wifissid, wifipass);
                                  
    uint8_t timeout = 20; // 20 * 500 ms = 5 sec time out
    while ( ((WiFi.status()) != WL_CONNECTED) && timeout ){
                                  SERIAL_DEBUG.print(".");
                                  SERIAL_DEBUG.flush();
                                  delay(500);
                                  --timeout;
   }
 
   if ((WiFi.status()) == WL_CONNECTED) {
                                    SERIAL_DEBUG.println("connected!");
                                                                     
                                    SERIAL_DEBUG.print("IP address   : "); 
                                    SERIAL_DEBUG.println(WiFi.localIP());
                                    SERIAL_DEBUG.print("MAC address  : "); 
                                    SERIAL_DEBUG.println(WiFi.macAddress());
                                    
                                    delay(100);    
                                    server1.begin();
                                    Serial.println("Server1 started");
                                    all_on();
   }
   else {
        SERIAL_DEBUG.println("Configuring access point...");
        SERIAL_DEBUG.flush();
   }
}                            

void loop()
{
        if(WiFi.status() == WL_CONNECTED)
        {
            WiFiClient client = server1.available();
            if(!client)
                return;
            while(!client.available())
                delay(1);
                       
            Serial.println("new client");            
            String request = client.readStringUntil('\r');
            client.print("ACK");
            Serial.println(request);
            Serial.println(request[request.indexOf("/")+1]);
            Serial.println(request[request.indexOf("/")+2]);
            Serial.println(request[request.indexOf("/")+3]);
            Serial.println(request[request.indexOf("/")+4]);
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
        }
        else{
              all_off();
              return;
        }
}

