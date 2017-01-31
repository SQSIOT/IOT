package com.example.hagawanet.image_server;

import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;


public class MainActivity extends AppCompatActivity {


    Button button1;
   // Button button2;
    //Button button3;
    //Button button4;



    private TcpClient mTcpClient;
    String ON = "green";
    //String OFF = "PARKING";
    //String ON1 = "SOURCE";
    //String OFF1 = "DESTINATION";

    private String TAG = "GameActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        button1 = (Button) findViewById(R.id.button1);
       // button2 = (Button) findViewById(R.id.button2);
       // button3 = (Button) findViewById(R.id.button3);
        //button4 = (Button) findViewById(R.id.button4);
        new connectTask().execute("");

        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.e("TCP Client", "GREEN");
                playmusic();
            }
        });


        /*button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.e("TCP Client", "PARKING TO SOURCE");
                parkingtosource();
            }
        });


        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.e("TCP Client", "SOURCE TO DESTINATION");
                sourcetodestination();
            }
        });


        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.e("TCP Client", "DESTINATION TO PARKING");
                destinationtoparking();
            }
        });*/
    }
    public void playmusic(){
        Log.e("green", "BEFORE SOCKET");
        new connectTask().execute("");
        Log.e("green", "INSIDE SOCKET");
        mTcpClient.sendMessage(ON);
        Log.e("green", "AFTER SENDING SIGNAL");

    }

   /* public void parkingtosource(){
        Log.e("parkingtosource", "BEFORE SOCKET");
        new connectTask().execute("");
        Log.e("parkingtosource", "INSIDE SOCKET");
        mTcpClient.sendMessage(OFF);
        Log.e("parkingtosource", "AFTER SENDING SIGNAL");

    }

    public void sourcetodestination(){
        Log.e("sourcetodestination", "BEFORE SOCKET");
        new connectTask().execute("");
        Log.e("sourcetodestination", "INSIDE SOCKET");
        mTcpClient.sendMessage(ON1);
        Log.e("sourcetodestination", "AFTER SENDING SIGNAL");

    }

    public void destinationtoparking(){
        Log.e("destinationtoparking", "BEFORE SOCKET");
        new connectTask().execute("");
        Log.e("destinationtoparking", "INSIDE SOCKET");
        mTcpClient.sendMessage(OFF1);
        Log.e("destinationtoparking", "AFTER SENDING SIGNAL");

    }*/

    public class connectTask extends AsyncTask<String,String,TcpClient> {

        @Override
        protected TcpClient doInBackground(String... message) {

            Log.e("connectTask", "inside doInBAk");
            //we create a TCPClient object and
            mTcpClient = new TcpClient(new TcpClient.OnMessageReceived() {
                @Override
                //here the messageReceived method is implemented
                public void messageReceived(String message) {
                    //this method calls the onProgressUpdate
                    Log.e("connectTask", "inside mTCP");
                    publishProgress(message);
                }
            });
            mTcpClient.run();
            return null;
        }

    }

}
