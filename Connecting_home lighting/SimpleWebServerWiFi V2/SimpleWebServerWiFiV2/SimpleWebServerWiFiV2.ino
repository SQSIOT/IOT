#include <ESP8266WiFi.h>

const char* ssid = "SQS";
const char* password = "d0n773llN0On3";

IPAddress ip(192, 168, 163, 150);   
IPAddress gateway(192, 168, 160, 1); 
IPAddress subnet(255,255,224,0); 
IPAddress dns1(192, 168, 192,4); 
IPAddress dns2(192, 168, 70,58); 



#define D1  16
#define D2  5
#define D3  4
#define D4  0
String data;

WiFiServer server(80);

void setup() {
 Serial.begin(115200);
 delay(10);

  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);

  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4,HIGH);

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

// Read the first line of the request
 String request = client.readStringUntil('\r');
 Serial.println(request);
 client.flush();

int value = LOW;
 if (request.indexOf("/LED=OFF") != -1) {
      digitalWrite(D1, HIGH);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
      data = "/LED=OFF";
        if (client.connect("http://192.168.163.171",80)) { // REPLACE WITH YOUR SERVER ADDRESS
          client.println("POST /demo.php HTTP/1.1"); 
          client.println("Host: http://192.168.163.171"); // SERVER ADDRESS HERE TOO
          client.println("Content-Type: application/x-www-form-urlencoded"); 
          client.print("Content-Length: "); 
          client.println(data.length()); 
          client.println(); 
          client.print(data); 
          client.println("</html>");
        } 
        else
        Serial.println("Client not connected");
 value = HIGH;
 }
 if (request.indexOf("/LED=ON") != -1) {
      digitalWrite(D1, LOW);
      digitalWrite(D2, LOW);
      digitalWrite(D3, LOW);
      digitalWrite(D4, LOW);
      data = "/LED=ON";
        if (client.connect("http://192.168.163.171",80)) { // REPLACE WITH YOUR SERVER ADDRESS
          client.println("POST /demo.php HTTP/1.1"); 
          client.println("Host: http://192.168.163.171"); // SERVER ADDRESS HERE TOO
          client.println("Content-Type: application/x-www-form-urlencoded"); 
          client.print("Content-Length: "); 
          client.println(data.length()); 
          client.println(); 
          client.print(data); 
          client.println("</html>");
        }
         else
        Serial.println("Client not connected");
 value = LOW;
 }
 else if (request.indexOf("/LED1=OFF") != -1) {
      digitalWrite(D1, HIGH);
 value = HIGH;
 }
 else if (request.indexOf("/LED1=ON") != -1) {
      digitalWrite(D1, LOW);
 value = LOW;
 }
 else if (request.indexOf("/LED2=OFF") != -1) {
      digitalWrite(D2, HIGH);
 value = HIGH;
 }
 else if (request.indexOf("/LED2=ON") != -1) {
      digitalWrite(D2, LOW);
 value = LOW;
 }

 else if (request.indexOf("/LED3=OFF") != -1) {
      digitalWrite(D3, HIGH);
 value = HIGH;
 }
 else if (request.indexOf("/LED3=ON") != -1) {
      digitalWrite(D3, LOW);
 value = LOW;
 }

 else if (request.indexOf("/LED4=OFF") != -1) {
      digitalWrite(D4, HIGH);
 value = HIGH;
 }
 else if (request.indexOf("/LED4=ON") != -1) {
      digitalWrite(D4, LOW);
 value = LOW;
 }

client.print("Status of all Light Before: ");

if(value == HIGH)
 client.print("Off");
else
 client.print("On");

 
 client.println("HTTP/1.1 200 OK");
 client.println("Content-Type: text/html");
 client.println(""); // do not forget this one
 client.println("<!DOCTYPE HTML>");
 client.println("<html>");

 client.println("<br><br>");
 client.println("Turn All Light OFF <a href=\"/LED=OFF\">here</a> ");
 client.println(" Turn All Light ON <a href=\"/LED=ON\">here</a><br>");
 client.println("Turn Light-1 OFF <a href=\"/LED1=OFF\">here</a> ");
 client.println(" Turn Light-1 ON <a href=\"/LED1=ON\">here</a><br>");
 client.println("Turn Light-2 OFF <a href=\"/LED2=OFF\">here</a> ");
 client.println(" Turn Light-2 ON <a href=\"/LED2=ON\">here</a><br>");
 client.println(" Turn Light-3 OFF <a href=\"/LED3=OFF\">here</a>");
 client.println(" Turn Light-3 ON <a href=\"/LED3=ON\">here</a><br>");
 client.println(" Turn Light-4 OFF <a href=\"/LED4=OFF\">here</a>");
 client.println(" Turn Light-4 ON <a href=\"/LED4=ON\">here</a><br>");
 client.println("</html>");

 Serial.println("");
}

//delay(300000); // WAIT FIVE MINUTES BEFORE SENDING AGAIN

