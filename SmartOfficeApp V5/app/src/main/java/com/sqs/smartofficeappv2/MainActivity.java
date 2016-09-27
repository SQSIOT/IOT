package com.sqs.smartofficeappv2;

import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextView;

import com.google.android.gms.appindexing.Action;
import com.google.android.gms.appindexing.AppIndex;
import com.google.android.gms.appindexing.Thing;
import com.google.android.gms.common.api.GoogleApiClient;

public class MainActivity extends AppCompatActivity {

    public TCPClient mTcpClient;

    String ON1 = "/05150643login";
    String OFF1 = "/05150643logout";
    String ON2 = "/05237823login";
    String OFF2 = "/05237823logout";
    String ON3 = "/05237923login";
    String OFF3 = "/05237923logout";
    String ONMAIN= "/MainON";
    String OFFMAIN = "/MainOFF";

    Switch switchButton, switchButton2,switchButton3,switchButton4;
    TextView textView, textView2, textView3, textView4;
    String switchOn = "Light 1 is ON";
    String switchOff = "Light 1 is OFF";
    String switchOn1 = "Light 2 is ON";
    String switchOff1 = "Light 2 is OFF";
    String switchOn2 = "AC is ON";
    String switchOff2 = "AC is OFF";
    String switchOn3 = "Main is ON";
    String switchOff3 = "Main is OFF";

    /**
     * ATTENTION: This was auto-generated to implement the App Indexing API.
     * See https://g.co/AppIndexing/AndroidStudio for more information.
     */
    private GoogleApiClient client;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

// For Light 1
        switchButton = (Switch) findViewById(R.id.switchButton);
        textView = (TextView) findViewById(R.id.textView);

        switchButton.setChecked(true);
        new connectTask(this).execute("");
        switchButton.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean bChecked) {
                if (bChecked) {
                    textView.setText(switchOn);
                    turnLEDOff();
                } else {
                    textView.setText(switchOff);
                    turnLEDOn();
                }
            }
        });

        if (switchButton.isChecked()) {
            textView.setText(switchOn);
        } else {
            textView.setText(switchOff);
        }
        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();



    // For Light 2
    switchButton2 = (Switch) findViewById(R.id.switchButton2);
    textView2 = (TextView) findViewById(R.id.textView2);

    switchButton2.setChecked(true);
    new connectTask(this).execute("");
    switchButton2.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
        @Override
        public void onCheckedChanged(CompoundButton compoundButton, boolean bChecked) {
            if (bChecked) {
                textView2.setText(switchOn);
                turnLEDOff2();
            } else {
                textView2.setText(switchOff);
                turnLEDOn2();
            }
        }
    });

    if (switchButton2.isChecked()) {
        textView2.setText(switchOn1);
    } else {
        textView2.setText(switchOff1);
    }
    // ATTENTION: This was auto-generated to implement the App Indexing API.
    // See https://g.co/AppIndexing/AndroidStudio for more information.
    client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();


// For AC
    switchButton3 = (Switch) findViewById(R.id.switchButton3);
    textView3 = (TextView) findViewById(R.id.textView3);

    switchButton3.setChecked(true);
    new connectTask(this).execute("");
    switchButton3.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
        @Override
        public void onCheckedChanged(CompoundButton compoundButton, boolean bChecked) {
            if (bChecked) {
                textView3.setText(switchOn2);
                turnLEDOff3();
            } else {
                textView3.setText(switchOff2);
                turnLEDOn3();
            }
        }
    });

    if (switchButton3.isChecked()) {
        textView3.setText(switchOn3);
    } else {
        textView3.setText(switchOff3);
    }
    // ATTENTION: This was auto-generated to implement the App Indexing API.
    // See https://g.co/AppIndexing/AndroidStudio for more information.
    client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();

// For Main Button
    switchButton4 = (Switch) findViewById(R.id.switchButton4);
    textView4 = (TextView) findViewById(R.id.textView4);

    switchButton4.setChecked(true);
    new connectTask(this).execute("");
    switchButton4.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
        @Override
        public void onCheckedChanged(CompoundButton compoundButton, boolean bChecked) {
            if (bChecked) {
                textView4.setText(switchOn3);
                turnLEDOff4();
                switchButton.setChecked(false);
                switchButton2.setChecked(false);
                switchButton3.setChecked(false);
            } else {
                textView4.setText(switchOff3);
                turnLEDOn4();
                switchButton.setChecked(true);
                switchButton2.setChecked(true);
                switchButton3.setChecked(true);
            }
        }
    });

    if (switchButton4.isChecked()) {
        textView4.setText(switchOn3);
    } else {
        textView4.setText(switchOff3);
    }
    // ATTENTION: This was auto-generated to implement the App Indexing API.
    // See https://g.co/AppIndexing/AndroidStudio for more information.
    client = new GoogleApiClient.Builder(this).addApi(AppIndex.API).build();
}



    public void turnLEDOn() {
        Log.e("turnLEDOn", "Inside turnLEDOn");
        new connectTask(this).execute("");
        mTcpClient.sendMessage(ON1);
        Log.e("TurnLEDOn", "LED 1 On");

    }

    public void turnLEDOff() {

        Log.e("turnLEDOff", "Inside turnLEDOff");
        new connectTask(this).execute("");
        mTcpClient.sendMessage(OFF1);
        Log.e("TurnLEDOff", "LED 1 Off");
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
        Log.e("onStart", "Inside");

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        client.connect();
        AppIndex.AppIndexApi.start(client, getIndexApiAction());
    }

    @Override
    public void onStop() {
        super.onStop();
        Log.e("onStop", "Inside ");

        // ATTENTION: This was auto-generated to implement the App Indexing API.
        // See https://g.co/AppIndexing/AndroidStudio for more information.
        AppIndex.AppIndexApi.end(client, getIndexApiAction());
        client.disconnect();
    }
   public void turnLEDOn2(){
        new connectTask(this).execute("");
        mTcpClient.sendMessage(ON2);
    }

    public void turnLEDOff2(){
        new connectTask(this).execute("");
        mTcpClient.sendMessage(OFF2);
     }

   public void turnLEDOn3(){
        new connectTask(this).execute("");
        mTcpClient.sendMessage(ON3);
   }

    public void turnLEDOff3(){
        new connectTask(this).execute("");
        mTcpClient.sendMessage(OFF3);
    }

    public void turnLEDOn4(){
        new connectTask(this).execute("");
        mTcpClient.sendMessage(ONMAIN);
     }

    public void turnLEDOff4(){
        new connectTask(this).execute("");
        mTcpClient.sendMessage(OFFMAIN);
    }


    public class connectTask extends AsyncTask<String, String, TCPClient> {

        public MainActivity MainActivity;
        public connectTask(MainActivity activity) {
            MainActivity = activity;
        }


        @Override
        protected TCPClient doInBackground(String... message) {

            Log.e("connectTask", "inside doInBAk");
            //we create a TCPClient object and
            mTcpClient = new TCPClient(new TCPClient.OnMessageReceived() {
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

