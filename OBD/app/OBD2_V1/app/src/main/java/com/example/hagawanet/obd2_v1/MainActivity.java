package com.example.hagawanet.obd2_v1;


import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.support.v4.app.ActivityCompat;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetAddress;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {


    Handler UIHandler;

    Thread Thread1 = null;

    private Button button;

    private TextView Textout15;
    private TextView Textout16;
    private TextView Textout17;
    private TextView Textout18;
    private TextView Textout19;
    private TextView Textout20;
    private TextView Textout21;
    private TextView Textout22;
    private TextView Textout23;
    private TextView Textout24;
    private TextView Textout25;
    private TextView Textout26;
    private TextView TextoutD;
    private TextView TextoutT;








    public static final int SERVERPORT = 30002;
    public static final String SERVERIP = "192.168.43.142";//"192.168.43.142";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        button = (Button) findViewById(R.id.button1);


        Textout15 = (TextView)findViewById(R.id.para15);
        Textout16 = (TextView)findViewById(R.id.para16);
        Textout17 = (TextView)findViewById(R.id.para17);
        Textout18 = (TextView)findViewById(R.id.para18);
        Textout19 = (TextView)findViewById(R.id.para19);
        Textout20 = (TextView)findViewById(R.id.para20);
        Textout21 = (TextView)findViewById(R.id.para21);
        Textout22 = (TextView)findViewById(R.id.para22);
        Textout23 = (TextView)findViewById(R.id.para23);
        Textout24 = (TextView)findViewById(R.id.para24);
        Textout25 = (TextView)findViewById(R.id.para25);
        Textout26 = (TextView)findViewById(R.id.para26);
        TextoutD = (TextView)findViewById(R.id.para1);
        TextoutT = (TextView)findViewById(R.id.para11);


        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View arg0) {
                Intent callIntent = new Intent(Intent.ACTION_CALL);
                callIntent.setData(Uri.parse("tel:8793095639"));

                if (ActivityCompat.checkSelfPermission(MainActivity.this,
                        Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED) {
                    return;
                }
                startActivity(callIntent);
            }
        });





        UIHandler = new Handler();

        this.Thread1 = new Thread(new Thread1());
        this.Thread1.start();



    }

    class Thread1 implements Runnable {

        public void run() {
            Socket sock ;

            try{

                InetAddress server_Addr = InetAddress.getByName(SERVERIP);
                sock = new Socket(server_Addr,SERVERPORT);

                Thread2 commThread = new Thread2(sock);
                new Thread(commThread).start();
                return;

            }catch (IOException e ){
                e.printStackTrace();
            }
        }

    }

    class Thread2 implements Runnable {
        private Socket client_sock;

        private BufferedReader input;

        public Thread2(Socket client_sock){
            this.client_sock = client_sock;

            try{
                this.input = new BufferedReader(new InputStreamReader(this.client_sock.getInputStream()));

            }catch (IOException e ){
                e.printStackTrace();
            }
        }

        public void run() {
            while(!Thread.currentThread().isInterrupted()){
                try {
                    String read = input.readLine();
                    if (read != null){
                        UIHandler.post((new updateUIThread(read)));

                    }
                    else {
                        Thread1 = new Thread(new Thread1());
                        Thread1.start();
                        return;

                    }
                }catch (IOException e){
                    e.printStackTrace();
                }
            }
        }
    }

    class updateUIThread implements Runnable {
        private String msg;
        private String Sub12 = "RPM";
        private String Sub13 = "SPEED";
        private String Sub14 = "MIL";
        private String Sub15 = "VIN";
        private String Sub16 = "LAT";
        private String Sub17 = "LONG";
        private String Sub18 = "ALT";
        private String Sub19 = "COOL.TEMP";
        private String Sub20 = "AIR.TEMP";
        private String Sub21 = "DEP.TIME";
        private String Sub22 = "IDLE.TIME";
        private String Sub23 = "JOUR.TIME";
        private String D = "DATE";
        private String T = "TIME";



        public updateUIThread(String str){
            this.msg = str;
        }

        @Override
        public void run() {
            if((msg.indexOf( D )) >= 0)
            {
                TextoutD.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( T )) >= 0)
            {
                TextoutT.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub12 )) >= 0)
            {
                Textout15.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub13 )) >= 0)
            {
                Textout16.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub14 )) >= 0)
            {
                Textout17.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub15 )) >= 0)
            {
                Textout18.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub16 )) >= 0)
            {
                Textout19.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub17 )) >= 0)
            {
                Textout20.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub18 )) >= 0)
            {
                Textout21.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub19 )) >= 0)
            {
                Textout22.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub20 )) >= 0)
            {
                Textout23.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub21 )) >= 0)
            {
                Textout24.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub22 )) >= 0)
            {
                Textout25.setText(msg.substring(10)+"\n");
            }
            if((msg.indexOf( Sub23 )) >= 0)
            {
                Textout26.setText(msg.substring(10)+"\n");
            }
            //Textout.setText(msg+"\n");
        }
    }
}

