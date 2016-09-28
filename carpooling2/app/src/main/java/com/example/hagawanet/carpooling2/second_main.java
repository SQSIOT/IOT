package com.example.hagawanet.carpooling2;

import android.os.Bundle;
import android.app.Activity;
import android.content.Intent;
import android.view.Menu;
import android.view.View;
import android.widget.Button;

public class second_main extends Activity implements View.OnClickListener {
    Button bt_driver;
    Button bt_passenger;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.select);
        bt_driver = (Button) findViewById(R.id.bt_driver);
        bt_passenger = (Button) findViewById(R.id.bt_passenger);
        bt_driver.setOnClickListener(this);
        bt_passenger.setOnClickListener(this);
       /* bt_passenger.setOnClickListener(this);
        bt_driver.setOnClickListener(this);*/

    }
@Override
    public void onClick(View v) {
        Intent in = null;
        switch(v.getId()) {
            case R.id.bt_driver:
                in = new Intent(this, driver1.class);
                break;
            case R.id.bt_passenger:
                in = new Intent(this, passenger1.class);
                break;
        }


        startActivity(in);

        }

}



   /* @Override
    protected void onStart() {//activity is started and visible to the user

        super.onStart();
        }
    @Override
    protected void onResume() {//activity was resumed and is visible again
        super.onResume();

    }
    @Override
    protected void onPause() { //device goes to sleep or another activity appears
        super.onPause();

        }
    @Override
    protected void onStop() { //the activity is not visible anymore
        super.onStop();

    }@Override
    protected void onDestroy() {//android has killed this activity
        super.onDestroy();
        }
}*/


