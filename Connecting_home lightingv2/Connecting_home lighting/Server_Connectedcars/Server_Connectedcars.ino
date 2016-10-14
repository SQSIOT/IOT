#include <ESP8266WiFi.h>
const char* ssid = "SQS";
const char* password = "d0n773llN0On3";


//SQS
IPAddress ip(192, 168, 163, 150);   
IPAddress gateway(192, 168, 160, 1); 
IPAddress subnet(255,255,255,0); 
IPAddress dns1(192, 168, 192,4); 
IPAddress dns2(192, 168, 70,58);


//IOT 
//IPAddress ip(192, 168, 163, 150);   
//IPAddress gateway(192, 168, 0, 1); 
//IPAddress subnet(255,255,225,0); 
//IPAddress dns1(192, 168, 0, 1); 
//IPAddress dns2(192, 168, 0, 1);


#define D1  16
#define D2  5
#define D3  4
#define D4  0

WiFiServer server(80);
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
 
 int value = LOW;
 if (req.indexOf("/LIGHTS=OFF") != -1) {
      digitalWrite(D1, HIGH);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
 value = HIGH;
 }
 if (req.indexOf("/LIGHTS=ON") != -1) {
      digitalWrite(D0, LOW);
      digitalWrite(D1, LOW);
      digitalWrite(D2, LOW);
      digitalWrite(D3, LOW);
 value = LOW;
 }

     client.println("HTTP/1.1 200 OK");
     client.println("Content-Type: text/html");
     client.println("");
     client.println("<HTML>");
     client.println("<HEAD>");
     client.println("<TITLE>Home Lighting Login</TITLE>");
     client.println("</HEAD>");
     client.println("<BODY>");
            // client.println("<h1 style="font-family:Comic Sans Ms;text-align="center";font-size:20pt;color:#00FF00;>");
     client.println("</h1>");
     client.println("<form name=\"login\">");
     client.println("Username<input type=\"text\" name=\"userid\"/>");
     client.println("Password<input type=\"text\" password=\"pswrd\"/>");
 
     client.println("<input type=\"button\" onclick=\"check(form.userid,form.pswrd)\" value=\"Login\"/>");
     client.println("<input type=\"reset\" value=\"Reset\"/>");
     client.println("</form>");
     client.println("<script type=\"text/javascript\">");
}


 check(form.u1, form.p1)
 {
     if(form.u1 == "admin" && form.p1 == "admin"){
     client.println("<meta http-equiv=\"refresh\" content=\"0; URL='192.168.163.150'\" />");
     //window.open('192, 168, 163, 150') //opens the target page while Id & password matches
     client.println("<!DOCTYPE HTML>");
     client.println("<html>");
     client.print("LIGHTS are now: ");
     
      if(value == LOW){
        client.print("On");}
      else{ 
       client.print("Off");}
       
       client.println("<br><br>");
       client.println("Turn Light <a href=\"/LIGHTS=ON\">ON</a> <br><br><br>");
       client.println("Turn Light <a href=\"/LIGHTS=OFF\">OFF</a><br>");
       client.println("</html>");
       client.println("</script>");
       client.println("</body>");
       client.println("</html>");
    }
   else{
    client.println("Error Password or Username");}
}

