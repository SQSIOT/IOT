package com.sqs.smartofficeappv2;

import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextView;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.Thing;

public class MainActivity extends AppCompatActivity {

    public TCPClient mTcpClient;

    String ON1 = "l1on\r";
    String OFF1 = "l1off\r";
    String ON2 = "l2on\r";
    String OFF2 = "l2off\r";
    String ON3 = "l3on\r";
    String OFF3 = "l3off\r";
    String msg = "Client\r";

    Switch switchButton, switchButton2,switchButton3;
    TextView textView, textView2, textView3;
    Button buttonClose, buttonConnect;

    String switchOn = "Light 1 is ON";
    String switchOff = "Light 1 is OFF";
    String switchOn1 = "Light 2 is ON";
    String switchOff1 = "Light 2 is OFF";
    String switchOn2 = "AC is ON";
    String switchOff2 = "AC is OFF";


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        new connectTask().execute("");


// For Connect button
        buttonConnect = (Button) findViewById(R.id.button);
        buttonConnect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                connect();
            }
        });


// For Light 1
        switchButton = (Switch) findViewById(R.id.switchButton);
        textView = (TextView) findViewById(R.id.textView);
        switchButton.setChecked(false);
        //new connectTask(this).execute("");
        switchButton.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean bChecked) {
                if (bChecked) {
                    textView.setText(switchOn);
                    turnLEDOn();

                } else {
                    textView.setText(switchOff);

                    turnLEDOff();
                }
            }
        });


        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.



        // For Light 2
        switchButton2 = (Switch) findViewById(R.id.switchButton2);
        textView2 = (TextView) findViewById(R.id.textView2);

        switchButton2.setChecked(false);
        //new connectTask(this).execute("");
        switchButton2.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean bChecked) {
                if (bChecked) {
                    textView2.setText(switchOn);
                    turnLEDOn2();
                } else {
                    textView2.setText(switchOff);

                    turnLEDOff2();
                }
            }
        });

        if (switchButton2.isChecked()) {
            textView2.setText(switchOn1);
        } else {
            textView2.setText(switchOff1);
        }



// For AC
        switchButton3 = (Switch) findViewById(R.id.switchButton3);
        textView3 = (TextView) findViewById(R.id.textView3);

        switchButton3.setChecked(false);
       // new connectTask(this).execute("");
        switchButton3.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean bChecked) {
                if (bChecked) {
                    textView3.setText(switchOn2);
                    turnLEDOn3();

                } else {
                    textView3.setText(switchOff2);
                    turnLEDOn3();

                }
            }
        });

        if (switchButton3.isChecked()) {
            textView3.setText(switchOn2);
        } else {
            textView3.setText(switchOff2);
        }


// For Close Button
        buttonClose = (Button) findViewById(R.id.button2);
       // new connectTask(this).execute("");
        buttonClose.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mTcpClient.sendMessage("ClientClose\r");
                mTcpClient.stopClient();
                finish();

               // moveTaskToBack(true);
            }
        });
    }




    public void turnLEDOn() {
        //Log.e("turnLEDOn", "Inside turnLEDOn");
     //   new connectTask(this).execute("");
        mTcpClient.sendMessage(ON1);
       // Log.e("TurnLEDOn", "LED 1 On");

    }

    public void turnLEDOff() {

        //Log.e("turnLEDOff", "Inside turnLEDOff");
      //  new connectTask(this).execute("");
        mTcpClient.sendMessage(OFF1);
      //  Log.e("TurnLEDOff", "LED 1 Off");
    }

    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    public Action getIndexApiAction() {
        Thing object = new Thing.Builder()
                .setName("Main Page") // TODO: Define a title for the content shown.
                // TODO: Make sure this auto-generated URL is correct.
                .setUrl(Uri.parse("http://[ENTER-YOUR-URL-HERE]"))
                .build();
        return new Action.Builder(Action.TYPE_VIEW)
                .setObject(object)
                .setActionStatus(Action.STATUS_TYPE_COMPLETED)
                .build();
    }

    @Override
    public void onStart() {
        super.onStart();
      //  Log.e("onStart", "Inside");

        // ATTENTION: This was auto-generated to implement the App Indexing API.

    }

    @Override
    public void onStop() {
        super.onStop();
       // Log.e("onStop", "Inside ");

        // ATTENTION: This was auto-generated to implement the App Indexing API.

    }
   public void turnLEDOn2(){
      //  new connectTask(this).execute("");
        mTcpClient.sendMessage(ON2);
    }

    public void turnLEDOff2(){
       // new connectTask(this).execute("");
        mTcpClient.sendMessage(OFF2);
     }

   public void turnLEDOn3(){
       // new connectTask(this).execute("");
        mTcpClient.sendMessage(ON3);
   }

    public void turnLEDOff3(){
       // new connectTask(this).execute("");
        mTcpClient.sendMessage(OFF3);
    }

    public void connect(){
      //  new connectTask(this).execute("");
        mTcpClient.sendMessage(msg);
    }


    public class connectTask extends AsyncTask<String, String, TCPClient> {
        @Override
        protected TCPClient doInBackground(String... message) {

            //we create a TCPClient object and
            mTcpClient = new TCPClient(new TCPClient.OnMessageReceived() {
                @Override
                //here the messageReceived method is implemented
                public void messageReceived(String message) {
                    Log.e("onStop", "Inside ");
                    //this method calls the onProgressUpdate
                    publishProgress(message);
                    mTcpClient.sendMessage("Client Connected\r" );
                }
            });
            mTcpClient.run();
            return null;
        }

    }
}

