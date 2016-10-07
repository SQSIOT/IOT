package com.sqs.smartofficeappv2;

/**
 * Created by SinghS01 on 28-09-2016.
 */

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class LoginActivity extends Activity {
    // User name
    private EditText et_Username;
    // Password
    private EditText et_Password;
    // Sign In
    private Button bt_SignIn;
    // Message
    TextView tv_Message;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        // Initialization
        et_Username = (EditText) findViewById(R.id.et_Username);
        et_Password = (EditText) findViewById(R.id.et_Password);
        bt_SignIn = (Button) findViewById(R.id.bt_SignIn);
       //tv_Message = (TextView) findViewById(R.id.tv_Message);
        bt_SignIn.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View view) {
                // Stores User name
                String username = String.valueOf(et_Username.getText());
                // Stores Password
                String password = String.valueOf(et_Password.getText());
                Intent i = null;
                i = new Intent(LoginActivity.this, MainActivity.class);
                startActivity(i);

            }
        });
    }
}
