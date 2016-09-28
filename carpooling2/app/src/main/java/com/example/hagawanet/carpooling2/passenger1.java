package com.example.hagawanet.carpooling2;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.example.hagawanet.carpooling2.R;
import com.example.hagawanet.carpooling2.second_main;

public class passenger1 extends second_main {
    // source
    private EditText input_source;
    // destination
    private EditText input_destination;
    //start time
    private EditText input_people;
    // Sign In
    private Button bt_enter;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.passenger);
        // Initialization
        input_source = (EditText) findViewById(R.id.input_source);
        input_destination = (EditText) findViewById(R.id.input_destination);
        input_people = (EditText) findViewById(R.id.input_people);
        bt_enter = (Button) findViewById(R.id.bt_enter);
        bt_enter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Stores User name
                String source = String.valueOf(input_source.getText());
                // Stores Password
                String destination = String.valueOf(input_destination.getText());
                String time = String.valueOf(input_people.getText());
               /* Intent i = null;
                i = new Intent(LoginActivity.this, second_main.class);
                startActivity(i);*/

            }
        });
    }
}
