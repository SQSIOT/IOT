#include <ESP8266WiFi.h>

const char* ssid = "	";
const char* password = "	";

IPAddress ip(192, 168, 163, 150);   
IPAddress gateway(192, 168, 160, 1); 
IPAddress subnet(255,255,224,0); 
IPAddress dns1(192, 168, 192,4); 
IPAddress dns2(192, 168, 70,58); 



#define D1  16
#define D2  5
#define D3  4
#define D4  0

WiFiServer server(80);

void setup() {
 Serial.begin(115200);
 delay(10);

  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);

  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);

// Connect to WiFi network
 Serial.println();
 Serial.println();
 Serial.print("Connecting to ");
 Serial.println(ssid);

WiFi.begin(ssid, password);

while (WiFi.status() != WL_CONNECTED) {
 delay(500);
 Serial.print(".");
 }
 Serial.println("");
 Serial.println("WiFi connected");

// Start the server
 server.begin();
 Serial.println("Server started");

// Print the IP address
 Serial.print("Use this URL to connect: ");
 Serial.print("http://");
 Serial.print(WiFi.localIP());
 Serial.println("/");

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

// Read the first line of the request
 String request = client.readStringUntil('\r');
 Serial.println(request);
 client.flush();

// Match the request

int value = LOW;
 if (request.indexOf("/LED=ON") != -1) {
      digitalWrite(D0, HIGH);
      digitalWrite(D1, HIGH);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, HIGH);
 value = HIGH;
 }
 if (request.indexOf("/LED=OFF") != -1) {
      digitalWrite(D0, LOW);
      digitalWrite(D1, LOW);
      digitalWrite(D2, LOW);
      digitalWrite(D3, LOW);
 value = LOW;
 }

// Set ledPin according to the request
 //digitalWrite(ledPin, value);

// Return the response
 client.println("HTTP/1.1 200 OK");
 client.println("Content-Type: text/html");
 client.println(""); // do not forget this one
 client.println("<!DOCTYPE HTML>");
 client.println("<html>");

client.print("Led pin is now: ");

if(value == HIGH) {
 client.print("On");
 } else {
 client.print("Off");
 }
 client.println("<br><br>");
 client.println("Click <a href=\"/LED=ON\">here</a> Turn Light OFF<br>");
 client.println("Click <a href=\"/LED=OFF\">here</a> Turn Light ON<br>");
 client.println("</html>");

delay(1);
 Serial.println("Client disonnected");
 Serial.println("");
}

