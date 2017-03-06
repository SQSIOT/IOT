#include <ESP8266WiFi.h>

/*
const char* ssid = "Airtel-E5573-3965";
const char* password = "1g4bbhy9";
*/

/*
const char* ssid = "SQS";
const char* password = "d0n773llN0On3";

IPAddress ip(192, 168, 163, 150);   
IPAddress gateway(192, 168, 160, 1); 
IPAddress subnet(255,255,224,0); 
IPAddress dns1(192, 168, 192,4); 
IPAddress dns2(192, 168, 70,58);
*/

/*
const char* ssid = "Tata-Photon-Max-Wi-Fi-338E";
const char* password = "12345678";
*/


const char* ssid = "Highfive";
const char* password = "Highfive";
 
IPAddress ip(192, 168, 1, 150);   
IPAddress gateway(192, 168, 1, 1); 
IPAddress subnet(255,255,225,0); 
IPAddress dns1(192, 168, 1, 1); 
IPAddress dns2(192, 168, 1, 1); 
//String dbserver = "192.168.1.102";

#define D0  16
#define D1  5
#define D2  4
#define D3  0
#define D4  2
#define D5  14
#define D6  12
#define D7  13
#define D8  15

String data, data1, data2, data3, data4, data5;


WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  delay(10);

  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  pinMode(D5, OUTPUT);
  pinMode(D6, OUTPUT);
  pinMode(D7, OUTPUT);
  pinMode(D8, OUTPUT);

  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
  digitalWrite(D7, HIGH);
  digitalWrite(D8, HIGH);
 
 // Connect to WiFi network
 Serial.println();
 Serial.print("Connecting to ");
 Serial.println(ssid);

 
  WiFi.config(ip,gateway,subnet,dns1,dns2);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
   delay(500);
   Serial.print(".");
   }
   Serial.println("");
   Serial.println("WiFi connected"); 
   //----------------------------------------------------
   //HIT the Webpage 1.
        // data1="";
        digitalWrite(D0, LOW);
        digitalWrite(D1, LOW);
        digitalWrite(D2, LOW);
        digitalWrite(D3, LOW);
          /*
          data = "Main=ON";
          WiFiClient client1;
          if (client1.connect("192.168.1.102",8080)) { // REPLACE WITH YOUR SERVER ADDRESS
            Serial.println ("MainON Successful Connection");
            client1.println("POST /iot/MAINON.php HTTP/1.0"); 
            client1.println("Host: 192.168.1.102:8080"); // SERVER ADDRESS HERE TOO
            client1.println("Content-Type: application/x-www-form-urlencoded"); 
            client1.print("Content-Length: "); 
            client1.println(data.length()); 
            client1.println(); 
            client1.print(data); 
          }*/
  
   //---------------------------------------------------------  
   
   // Start the server
   server.begin();
   Serial.println("Server started");
  
   // Print the IP address
   Serial.print("Use this URL to connect: ");
   Serial.print("http://");
   Serial.print(WiFi.localIP());
   Serial.println("/");
   data = "";
}



void loop() {
 // Check if a client has connected
 WiFiClient client = server.available();
    if (!client) {
      return;
     }

// Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
  delay(1);
  }
  //client.print(String("POST")+"http/1.0\r\n"+host+"\r\n");
  //client.println("Host: http://192.168.163.171:8080/iot/MainON.PHP");

  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.print("ack arduino");
  client.flush();
 
      int value = LOW;
      if (request.indexOf("/LED=OFF") != -1) {
        digitalWrite(D0, HIGH);
        digitalWrite(D1, HIGH);
        digitalWrite(D2, HIGH);
        digitalWrite(D3, HIGH);
        value = HIGH;
       
//----------------------------------------------------
        //HIT the Webpage 2.
        //data2="";
        data2 = "Main=OFF";
        WiFiClient client2;
        if (client2.connect("192.168.1.102",8080)) { // REPLACE WITH YOUR SERVER ADDRESS
          Serial.println ("MainOFF Successful Connection");
          client2.println("POST /iot/MAINOFF.php HTTP/1.0"); 
          client2.println("Host:192.168.1.102:8080"); // SERVER ADDRESS HERE TOO
          client2.println("Content-Type: application/x-www-form-urlencoded"); 
          client2.print("Content-Length: "); 
          client2.println(data2.length()); 
          client2.println(); 
          client2.print(data2); 
        }
//---------------------------------------------------------  
     }
     else if (request.indexOf("/LED1=ON") != -1){
          digitalWrite(D1, LOW);
         
//----------------------------------------------------
        //HIT the Webpage 3.
        //data3="";   
        data3 = "L1=ON";
        WiFiClient client3;
        if (client3.connect("192.168.1.102",8080)) { // REPLACE WITH YOUR SERVER ADDRESS
          Serial.println ("L1ON Successful Connection");
          client3.println("POST /iot/LED1ON.php HTTP/1.0"); 
          client3.println("Host:192.168.1.102:8080"); // SERVER ADDRESS HERE TOO
          client3.println("Content-Type: application/x-www-form-urlencoded"); 
          client3.print("Content-Length: "); 
          client3.println(data3.length()); 
          client3.println(); 
          client3.print(data3); 
        }
//---------------------------------------------------------  
  }
           
     else if (request.indexOf("/LED=ON") != -1) {
        digitalWrite(D0, LOW);
        digitalWrite(D2, LOW);
        digitalWrite(D3, LOW);
//----------------------------------------------------
        //HIT the Webpage 4.
        //data4="";   
        data4 = "L2L3L4=ON";
        WiFiClient client4;
        if (client4.connect("192.168.1.102",8080)) { // REPLACE WITH YOUR SERVER ADDRESS
          Serial.println ("L2L3L4ON Successful Connection");
          client4.println("POST /iot/L2L3L4ON.php HTTP/1.0"); 
          client4.println("Host:192.168.1.102:8080"); // SERVER ADDRESS HERE TOO
          client4.println("Content-Type: application/x-www-form-urlencoded"); 
          client4.print("Content-Length: "); 
          client4.println(data4.length()); 
          client4.println(); 
          client4.print(data4); 
        }
//---------------------------------------------------------  
          delay(30000);
          digitalWrite(D1, HIGH);
          data = "/LED=ON";
          value = LOW;
//----------------------------------------------------
    //HIT the Webpage 5.
       // data5="";   
        data5 = "L1=OFF";
        WiFiClient client5;
        if (client5.connect("192.168.1.102",8080)) { // REPLACE WITH YOUR SERVER ADDRESS
          Serial.println ("L1OFF Successful Connection");
          client5.println("POST /iot/LED1OFF.php HTTP/1.0"); 
          client5.println("Host:192.168.1.102:8080"); // SERVER ADDRESS HERE TOO
          client5.println("Content-Type: application/x-www-form-urlencoded"); 
          client5.print("Content-Length: "); 
          client5.println(data5.length()); 
          client5.println(); 
          client5.print(data5); 
        }
 //---------------------------------------------------------       
     }
   Serial.print("Initial Status");
      if(value == HIGH)
        Serial.println("Off");
      else
        client.print("On");
}
