#import dials
from ddials import *
##
ddial_rpm(10)
ddial_acce(20)
ddial_thro(40)
ddial_mph(20)

##########################
date_1_p= 'DATE:'
dtext1(date_1_p,850,80,0,0)
##date_1_v= '25-1-2017'
##dtext1(date_1_v,1050,80,0,0)

time_1_p= 'TIME:'
dtext1(time_1_p,850,102,0,0)
##time_1_v= '20:09'
##dtext1(time_1_v,1050,102,0,0)
##########################
##
##vpara= '*Parameters*'
##dtext1(vpara,850,120,88,28)
##
##v_val= '*Values*'
##dtext1(v_val,1050,120,88,28)

#Vehicle Status#########################
st_1= 'Vehicle Status:'
dtext1(st_1,850,140,0,0)
mil_p= 'MIL:'
dtext1(mil_p,850,162,0,0)
mil_v= 'OFF'
dtext1(mil_v,1050,162,0,0)
bat_p= 'BATTERY VOLTAGE:'
dtext1(bat_p,850,182,0,0)
bat_v= '14.2V'
dtext1(bat_v,1050,182,0,0)
cool_1_p= 'COOLANT TEMP:'
dtext1(cool_1_p,850,202,0,0)
cool_1_p= '207 F'
dtext1(cool_1_p,1050,202,0,0)
cool_1_p= 'INTAKE AIR TEMP:'
dtext1(cool_1_p,850,222,0,0)
cool_1_p= '173 F'
dtext1(cool_1_p,1050,222,0,0)

#Journey Status############################
st_2= 'Journey Status:'
dtext1(st_2,850,260,0,0)
journ_p= 'JOURNEY TIME:'
dtext1(journ_p,850,282,0,0)
journ_v= '15 min'
dtext1(journ_v,1050,282,0,0)
idle_p= 'IDLE TIME:'
dtext1(idle_p,850,302,0,0)
idle_v= '5 min'
dtext1(idle_v,1050,302,0,0)
run_p= 'RUN TIME:'
dtext1(run_p,850,322,0,0)
run_v= '10 min'
dtext1(run_v,1050,322,0,0)

#vehicle Status###########################

#Vehicle Info#############################
st_3= 'Vehicle Information'
dtext1(st_3,850,360,0,0)
vin_p= 'VIN'
dtext1(vin_p,850,382,0,0)
vin_v= 'CDB892BDCBJCBC'
dtext1(vin_v,1050,382,0,0)

#Location Status###########################
st_4= 'Location Status:'
dtext1(st_4,850,420,0,0)
alti_p= 'LONGITUDE:'
dtext1(alti_p,850,442,0,0)
##alti_v= '00000.1212'
##dtext1(alti_v,1050,442,0,0)
lati_p= 'LATITUDE:'
dtext1(lati_p,850,462,0,0)
##lati_v= '00000.1232'
##dtext1(lati_v,1050,462,0,0)
longi_p= 'ALTITUDE:'
dtext1(longi_p,850,482,0,0)
##longi_v= '2178.210'
##dtext1(longi_v,1050,482,0,0)

###################################
##v1= 'Ravindra_sir'
##    
##dtext1(v1,850,100,88,28)
##
##v2= 'tulsi'
##
##dtext1(v2,850,120,88,28)
####################################
