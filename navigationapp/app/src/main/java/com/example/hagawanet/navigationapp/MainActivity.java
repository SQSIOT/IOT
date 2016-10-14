package com.example.hagawanet.navigationapp;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.design.widget.NavigationView;
import android.support.v4.view.GravityCompat;
import android.support.v4.widget.DrawerLayout;
import android.support.v7.app.ActionBarDrawerToggle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

       /* FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });*/

        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this, drawer, toolbar, R.string.navigation_drawer_open, R.string.navigation_drawer_close);
        drawer.setDrawerListener(toggle);
        toggle.syncState();

        NavigationView navigationView = (NavigationView) findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @SuppressWarnings("StatementWithEmptyBody")
    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.nav_Login) {
            Intent i = null;
            i = new Intent(MainActivity.this, Login_main.class);
            startActivity(i);




        }
        else if (id == R.id.nav_Technologies) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.sqs.com/in/technologies.php"));
            startActivity(browserIntent);


        }
        else if (id == R.id.nav_Paper) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.sqs.com/en-group/about-sqs/publications.php"));
            startActivity(browserIntent);


        }
        else if (id == R.id.nav_JobPortal) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.sqs.com/portal/career/index.php"));
            startActivity(browserIntent);


        }
        else if (id == R.id.nav_Facebook) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.facebook.com/pages/SQS-Group/100601203341881"));
            startActivity(browserIntent);

        }
        else if (id == R.id.nav_SQSWebsite) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.sqs.com/en-group/index.php"));
            startActivity(browserIntent);

        }

        else if (id == R.id.nav_LinkedIn) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.linkedin.com/start/join?session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fsqs&source=sentinel_org_block&trk=login_reg_redirect"));
            startActivity(browserIntent);


        }
        else if (id == R.id.nav_AboutUs) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.sqs.com/en-group/about-sqs.php"));
            startActivity(browserIntent);


        }
        else if (id == R.id.nav_ContactUs) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.sqs.com/en-group/_meta/search.php?search_item=contact+us"));
            startActivity(browserIntent);
        }
        else if (id == R.id.nav_Googlemaps) {
            Intent browserIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.google.co.in/maps/@18.5904973,73.694674,15z"));
            startActivity(browserIntent);

        }



        DrawerLayout drawer = (DrawerLayout) findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }
}
