
def p_to_s(i,j,k):
    M1P.ChangeDutyCycle(30)
    M2P.ChangeDutyCycle(30)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(0)
    
    while True:
        i=GPIO.input(Left_sensor)       #Reading output of left IR sensor
        j=GPIO.input(middle_sensor)     #Reading output of middle IR sensor
        k=GPIO.input(Right_sensor)      #Reading output of right IR sensor
        #print"Values of I J & k", i,j,k
            
        print"Values of I J & k\n", i,j,k
        if i ==0 and j == 0 and k == 0:             #stop        
         print "Stop"
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
        elif i ==0 and j == 0 and k == 1:             #left       
         print "left"
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(20)
         M1N.ChangeDutyCycle(20)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
        elif i ==0 and j == 1 and k == 0:             #left      
         print "left"
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(20)
         M1N.ChangeDutyCycle(20)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
        elif i ==0 and j == 1 and k == 1:             #left       
         print "left"
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(20)
         M1N.ChangeDutyCycle(20)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.2)
        
        elif i ==1 and j == 0 and k == 0:             #right      
         print "right"
         M1P.ChangeDutyCycle(20)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(20)
         time.sleep(0.1)
        
        elif i ==1 and j == 0 and k == 1:             #forward      
         print "forward"
         M1P.ChangeDutyCycle(20)
         M2P.ChangeDutyCycle(20)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         
        elif i ==1 and j == 1 and k == 0:             #right      
         print "right"
         M1P.ChangeDutyCycle(20)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(20)
         time.sleep(0.1)
        
        elif i ==1 and j == 1 and k == 1:             #forward  
         print "left"
         M1P.ChangeDutyCycle(10)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(10)
         time.sleep(0.1)
         M1P.ChangeDutyCycle(10)
         M2P.ChangeDutyCycle(10)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         
         #M1P.ChangeDutyCycle(10)
         #M2P.ChangeDutyCycle(10)
         ##M1N.ChangeDutyCycle(0)
         #M2N.ChangeDutyCycle(0)
         ##time.sleep(0.1)
    return;
