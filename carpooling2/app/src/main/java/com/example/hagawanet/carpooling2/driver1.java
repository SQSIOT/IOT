package com.example.hagawanet.carpooling2;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class driver1 extends second_main {
    // source
    private EditText input_source;
    // destination
    private EditText input_destination;
    //start time
    private EditText input_time;
    // Sign In
    private Button bt_enter;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.driver);
        // Initialization
        input_source = (EditText) findViewById(R.id.input_source);
        input_destination = (EditText) findViewById(R.id.input_destination);
        input_time = (EditText) findViewById(R.id.input_time);
        bt_enter = (Button) findViewById(R.id.bt_enter);
        bt_enter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Stores User name
                String source = String.valueOf(input_source.getText());
                // Stores Password
                String destination = String.valueOf(input_destination.getText());
                String time = String.valueOf(input_time.getText());
                Intent i = null;
                i = new Intent(driver1.this, MapsActivity.class);
                startActivity(i);

            }
        });
    }
}
