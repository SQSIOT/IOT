package com.sqs.smartofficeappv2;

/**
 * Created by singhs01 on 05-10-2016.
 */
import android.annotation.SuppressLint;
import android.database.SQLException;
import android.os.StrictMode;
import android.util.Log;

import java.sql.Connection;
import java.sql.DriverManager;

public class ConnectionClass {

    String ip = "192.168.164.30";
    String classs = "net.sourceforge.jtds.jdbc.Driver";
    String db = "HRVIEW_ACTA";
    String un = "sa";
    String password = "Password123";

    @SuppressLint("NewApi")
    public Connection CONN() {

        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder()
                .permitAll().build();
        StrictMode.setThreadPolicy(policy);
        Connection conn = null;
        String ConnURL = null;
        try {
            Log.e("Login Activity", "Inside turnLEDOn");
            Class.forName(classs);
            ConnURL = "jdbc:jtds:sqlserver://" + ip + ";"
                    + "databaseName=" + db + ";user=" + un + ";password="
                    + password + ";";
            conn = DriverManager.getConnection(ConnURL);
        } catch (SQLException se) {
            Log.e("ERRO", se.getMessage());
        } catch (ClassNotFoundException e) {
            Log.e("ERRO", e.getMessage());
        } catch (Exception e) {
            Log.e("ERRO", e.getMessage());
        }
        return conn;
    }

}