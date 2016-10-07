package com.example.hagawanet.direction_map;

import android.content.pm.PackageManager;
import android.os.Bundle;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.FragmentActivity;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;

import android.app.Activity;
import android.os.Bundle;
import android.support.v4.app.FragmentManager;

import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;

import android.content.Context;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.util.Log;
import android.view.KeyEvent;
import android.view.inputmethod.EditorInfo;
import android.widget.EditText;
import android.widget.TextView;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.CameraPosition;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
//import com.google.android.maps.GeoPoint;
//import com.modivmedia.mcscan.R;

import java.util.List;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback, GoogleMap.OnMarkerClickListener {
    private GoogleMap mMap;
    public static final String TAG = "MAP";
    EditText searchLocationTv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps);
        searchLocationTv = (EditText) findViewById(R.id.searchTxt);
        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager().findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
        // Acquire a reference to the system Location Manager
        LocationManager locationManager = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);
        // Define a listener that responds to location updates
        LocationListener locationListener = new LocationListener() {
            public void onLocationChanged(Location location) {
                // Called when a new location is found by the network location provider.
                setLocationInMap(location);
            }

            public void onStatusChanged(String provider, int status, Bundle extras) {
            }

            public void onProviderEnabled(String provider) {
            }

            public void onProviderDisabled(String provider) {
            }
        };
        // Register the listener with the Location Manager to receive location updates
        if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // TODO: Consider calling
            //    ActivityCompat#requestPermissions
            // here to request the missing permissions, and then overriding
            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
            //                                          int[] grantResults)
            // to handle the case where the user grants the permission. See the documentation
            // for ActivityCompat#requestPermissions for more details.
            return;
        }
        locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 0, 0, locationListener);
searchLocationTv.setOnEditorActionListener(new TextView.OnEditorActionListener() {
            public boolean onEditorAction(TextView v, int actionId, KeyEvent event) {
                if ((event != null && (event.getKeyCode() == KeyEvent.KEYCODE_ENTER)) ||
                (actionId == EditorInfo.IME_ACTION_DONE)) {
                    Log.i(TAG, "Enter pressed");
                   GeoPoint g = getLocationFromAddress(searchLocationTv.getText().toString().trim());
               double latitude = g.getLatitudeE6() / 1E6;
                    double longitude = g.getLongitudeE6() / 1E6;
                Location location = new Location(searchLocationTv.getText().toString().trim());
                location.setLatitude(latitude);
                    location.setLongitude(longitude);
               setLocationInMap(location);
                    }
                return false;
            }
            });
        }
    /**
          * Manipulates the map once available.
          * This callback is triggered when the map is ready to be used.
          * This is where we can add markers or lines, add listeners or move the camera. In this case,
          * we just add a marker near Sydney, Australia.
          * If Google Play services is not installed on the device, the user will be prompted to install
          * it inside the SupportMapFragment. This method will only be triggered once the user has
          * installed Google Play services and returned to the app.
          */
    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;
        mMap.setOnMarkerClickListener(this);
        Log.i(TAG, "Map is ready...");
        mMap.setOnInfoWindowClickListener(
                new GoogleMap.OnInfoWindowClickListener() {
           @Override
            public void onInfoWindowClick(Marker arg0) {
           // TODO Auto-generated method stub
                arg0.hideInfoWindow();
                double dlat = arg0.getPosition().latitude;
                double dlon = arg0.getPosition().longitude;
              String slat = String.valueOf(dlat);
                String slon = String.valueOf(dlon);
                Log.i(TAG, "LAt " + dlat + "Long = " + dlon);
            }
            });
        }
    private void setLocationInMap(Location location) {
        Log.i(TAG, "Setting Location in Map...");
        LatLng myLocation = new LatLng(location.getLatitude(), location.getLongitude());
        mMap.addMarker(new MarkerOptions().position(myLocation).title(searchLocationTv.getText().toString().trim())).showInfoWindow();
        CameraPosition cameraPosition = new CameraPosition.Builder().target(myLocation).zoom(2).build();
        mMap.animateCamera(CameraUpdateFactory.newCameraPosition(cameraPosition));

        }
    //Find 5 names and return the first one for the name provided..
    private GeoPoint getLocationFromAddress(String strAddress) {
        Geocoder coder = new Geocoder(this);
        List<Address> address;
        GeoPoint p1 = null;
        try {
            address = coder.getFromLocationName(strAddress, 5);
            if (address == null) {
                return null;
                }
            Address location = address.get(0);
            location.getLatitude();
            location.getLongitude();
            p1 = new GeoPoint((int) (location.getLatitude() * 1E6),
                    (int) (location.getLongitude() * 1E6));
            } catch (Exception e) {

            }
        return p1;
        }
    @Override
    public boolean onMarkerClick(final Marker marker) {
        Log.i(TAG, "marker clicked");
        marker.showInfoWindow();
        return true;
        }
}
