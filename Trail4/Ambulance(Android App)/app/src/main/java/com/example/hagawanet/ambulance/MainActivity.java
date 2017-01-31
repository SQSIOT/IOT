package com.example.hagawanet.ambulance;

import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {


    public String read;

    public String comp = ("green");
    public String comp1 = ("red");
    public ImageView i1, i2;
    public static final int SERVERPORT = 30007;



    private ServerSocket serverSocket;
    //String touchedCoordinates;
    Handler updateConversationHandler;
    Thread serverThread = null;
    //private ImageView imageView;


    @Override
    public void onCreate(Bundle savedInstanceState) {




        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //imageView=(ImageView) findViewById(R.id.activity_main);

        i1 = (ImageView) findViewById(R.id.imageView);
        i2 = (ImageView) findViewById(R.id.imageView2);

        i1.setVisibility(View.VISIBLE);
        i2.setVisibility(View.INVISIBLE);



        updateConversationHandler = new Handler();
        this.serverThread = new Thread(new ServerThread());
        this.serverThread.start();

    }

    @Override
    protected void onStop() {
        super.onStop();
        try {
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    class ServerThread implements Runnable {

        public void run() {
            Socket socket = null;
            try {
                serverSocket = new ServerSocket(SERVERPORT);
            } catch (IOException e) {
                e.printStackTrace();
            }
            while (!Thread.currentThread().isInterrupted()) {

                try {

                    socket = serverSocket.accept();
                    CommunicationThread commThread = new CommunicationThread(socket);
                    new Thread(commThread).start();

                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    class CommunicationThread implements Runnable {

        private Socket clientSocket;
        private DataInputStream input;
        public CommunicationThread(Socket clientSocket) {

            this.clientSocket = clientSocket;

            try {
                InputStream in = this.clientSocket.getInputStream();
                this.input = new DataInputStream(in);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        public void run() {
            while (!Thread.currentThread().isInterrupted()) {
                try {
                    read = input.readLine();

                    if (read != null) {
                        updateConversationHandler.post((new updateUIThread(read)));

                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

    }

    class updateUIThread implements Runnable {
        private String msg;


        public updateUIThread(String str) {
            this.msg = str;
        }




        @Override
        public void run() {
            Log.e("RESPONSE FROM SERVER", read);
            if (read.equals(comp)) {
                i1.setVisibility(View.INVISIBLE);
                i2.setVisibility(View.VISIBLE);
            }
            else if (read.equals(comp1)) {
                i1.setVisibility(View.VISIBLE);
                i2.setVisibility(View.INVISIBLE);
            }
        }
    }
}

