#include <ESP8266WiFi.h>
const char* ssid = "*";
const char* password = "*";


//SQS
IPAddress ip(*, *, *, *);   
IPAddress gateway(*, *, *, *); 
IPAddress subnet(*,*,*,*); 
IPAddress dns1(*, *, *,*); 
IPAddress dns2(*, *, *,*);

#define D1  16
#define D2  5
#define D3  4
#define D4  0

WiFiServer server(8080);
String WEB = "";

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

  //WEB += "<h1>ESP8266 WEB</h1>";
  
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

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.println(WiFi.localIP());
}


void loop() {

  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client){
     //Serial.print("Client not available");
     return;
  }
  
  String req = client.readStringUntil('\r');
  client.flush();
  if(req == "Hello I'm Pi") {
      Serial.println(req);
      digitalWrite(D1, LOW);
      digitalWrite(D2, LOW);
      digitalWrite(D3, LOW);
      digitalWrite(D4, LOW);
      client.print("Hello Pi");
      delay(10000);
  }
}


