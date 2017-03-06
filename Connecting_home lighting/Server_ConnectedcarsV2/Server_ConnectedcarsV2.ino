#include <ESP8266WiFi.h>
const char* ssid = "SQS";
const char* password = "d0n773llN0On3";
//String readString = String(30);
//Server server(80);


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



void SendOKpage(WiFiClient &client)
{
    Serial.print("Inside Sendokpage");
    String req = client.readStringUntil('\r');
              Serial.println(req);
              int value = LOW;
              //client.flush();
               if(req == "Hello I'm Pi") {
                Serial.println(req);
                digitalWrite(D1, LOW);
                digitalWrite(D2, LOW);
                digitalWrite(D3, LOW);
                digitalWrite(D4, LOW);
                client.print("Hello Pi");
                delay(10000);
               }
        
               client.println("HTTP/1.1 200 OK");
               client.println("Content-Type: text/html");
               client.println(""); // do not forget this one
               client.println("<!DOCTYPE HTML>");
               client.println("<html>");                 
               client.print("Light pin is now: ");
                                
                if(value == HIGH) {
                client.print("On");
                } 
                else {
                client.print("Off");
                }
                client.println("<br><br>");
                client.println("Click <a href=\"/Light=OFF\">here</a> Turn Light OFF<br>");
                client.println("Click <a href=\"/Light=ON\">here</a> Turn Light ON<br>");
                client.println("</html>");
                Serial.println(req);
                
                if (req.indexOf("Light=ON") != -1) {
                 digitalWrite(D0, HIGH);
                 digitalWrite(D1, HIGH);
                 digitalWrite(D2, HIGH);
                 digitalWrite(D3, HIGH);
                 value = HIGH;
                }
                if (req.indexOf("Light=OFF") != -1) {
                 digitalWrite(D0, LOW);
                 digitalWrite(D1, LOW);
                 digitalWrite(D2, LOW);
                 digitalWrite(D3, LOW);
                 value = LOW;
                }
             Serial.print("Out of box");
            }


void SendAuthentificationpage(WiFiClient &client)
{
          client.println("HTTP/1.1 401 Authorization Required");
          client.println("WWW-Authenticate: Basic realm=\"Secure Area\"");
          client.println("Content-Type: text/html");
          client.println("Connnection: close");
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<HTML>  <HEAD>   <TITLE>Error</TITLE>");
          client.println(" </HEAD> <BODY><H1>401 Unauthorized.</H1></BODY> </HTML>");
}

char linebuf[80];
int charcount=0;
boolean authentificated=false;

void loop() {
  // listen for incoming clients
  WiFiClient client = server.available();
    
  if (!client){
     //Serial.print("Client not available");
     return;
  }
  
  if (client) {
    Serial.println("new client");
    memset(linebuf,0,sizeof(linebuf));
    charcount=0;
    authentificated=false;
    // an http request ends with a blank line
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        linebuf[charcount]=c;
        if (charcount<sizeof(linebuf)-1) charcount++;
        Serial.write(c);
        // if you've gotten to the end of the line (received a newline
        // character) and the line is blank, the http request has ended,
        // so you can send a reply
        if (c == '\n' && currentLineIsBlank) {
          if (authentificated)
           SendOKpage(client);
          else
            SendAuthentificationpage(client);  
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
          if (strstr(linebuf,"Authorization: Basic")>0 && strstr(linebuf,"c2F0YXJ1bjpwYXNzd29yZA==")>0)
            authentificated=true;
          memset(linebuf,0,sizeof(linebuf));
          charcount=0;
        } 
        else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);
    // close the connection:
    client.stop();
    //Serial.println("client disonnected");
  }
}
