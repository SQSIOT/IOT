package com.sqs.smartofficeappv2;

/**
 * Created by singhs01 on 01-09-2016.
 */
import android.util.Log;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class TCPClient {

    private String serverMessage;
    public static final String SERVERIP = "192.168.163.150"; //your computer IP address
    public static final int SERVERPORT = 80; //Port No.
    //public static final int HWID = 42;
    String response = "";
    private OnMessageReceived mMessageListener = null;
    private boolean mRun = false;
    int mCount = 0;

    PrintWriter out;
    BufferedReader in;
    public boolean flag = true;


    /**
     *  Constructor of the class. OnMessagedReceived listens for the messages received from server
     */
    public TCPClient(OnMessageReceived listener) {
        mMessageListener = listener;
    }

    /**
     * Sends the message entered by client to the server
     * @param message text entered by client
     */
    public void sendMessage(String message){

        if (out != null && !out.checkError()) {
            Log.e("TCP Client", "SendMessage if: Enter");
            out.println(message);
            out.flush();
//            out.println(message);
            Log.e("TCP Client", "SendMessage if: Exit");

        }
    }

    public void stopClient(){
        mRun = false;
    }

    public void run () {

        mRun = true;

        while (true) {
            mRun = true;
            try {
                //here you must put your computer's IP address.
                InetAddress serverAddr = InetAddress.getByName(SERVERIP);
               /*Log.e("TCP Client", SERVERIP);

                Log.e("TCP Client", "C: Connecting...");
                Log.e("TCP Client", "Inside");
                Log.d("TCP Client", "SERVERPORT" + SERVERPORT);
                Log.d("TCP Client", "SERVERaddress" + serverAddr);*/




                //create a socket to make the connection with the server
                Socket socket = new Socket(serverAddr, SERVERPORT);
               // Log.e("TCP Client", "Inside socket");

                try {

                    //send the message to the server
                    out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())), true);

                   // Log.e("TCP Client", "C: Sent.");

                   // Log.e("TCP Client", "C: Done.");

                    //receive the message which the server sends back
                    in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

                    //in this while the client listens for the messages sent by the server
                    while (mRun) {
                        serverMessage = in.readLine();

                        if(mCount == 1000000)
                            stopClient();
                        mCount++;
                        mCount = mCount%1000000;

                        if (serverMessage != null && mMessageListener != null) {
                            //call the method messageReceived from MyActivity class
                           // Log.e("TCP Client", "mRun while: Enter");
                            mMessageListener.messageReceived(serverMessage);
                           // Log.e("TCP Client", "mRun while: Exit");
                            stopClient();
                        }
                        serverMessage = null;
                    }

                    //Log.e("RESPONSE FROM SERVER", "S: Received Message: '" + serverMessage + "'");

                    socket.close();
//                    mRun = true;

                } catch (UnknownHostException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                    response = "UnknownHostException: " + e.toString();


                } finally {
                    //the socket must be closed. It is not possible to reconnect to this socket
                    // after it is closed, which means a new socket instance has to be created.
                    socket.close();
                    out.print("socket closed");
                    //stopClient();

                }

            } catch (Exception e) {

                flag = false;
                Log.e("TCP", "C: Error", e);




            }



        }


    }

    //Declare the interface. The method messageReceived(String message) will must be implemented in the MainActivity
    //class at on asynckTask doInBackground
    public interface OnMessageReceived {
        void messageReceived(String message);
    }
}
