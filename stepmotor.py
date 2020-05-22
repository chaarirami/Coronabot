import time									# Raum 210
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A = 7                                       #Pin Schrittmotor 1 rechts(Antrieb)
B = 11                                      #
C = 13                                      #
D = 15                                      #

E =                                         #Pin Schrittmotor 2 links(Antrieb)
F =                                         #
G =                                         #
H =                                         #

I =                                         #Pin Schrittmotor 3 (Förderband)
K =                                         #
L =                                         #
M =                                         #

GPIO.setup(A, GPIO.OUT)                     #Pin7  als Ausgang
GPIO.setup(B, GPIO.OUT)                     #Pin11 als Ausgang
GPIO.setup(C, GPIO.OUT)                     #Pin13 als Ausgang
GPIO.setup(D, GPIO.OUT)                     #Pin15 als Ausgang

GPIO.setup(E, GPIO.OUT)                     #Pin  als Ausgang
GPIO.setup(F, GPIO.OUT)                     #Pin als Ausgang
GPIO.setup(G, GPIO.OUT)                     #Pin als Ausgang
GPIO.setup(H, GPIO.OUT)                     #Pin als Ausgang

GPIO.setup(I, GPIO.OUT)                     #Pin  als Ausgang
GPIO.setup(K, GPIO.OUT)                     #Pin als Ausgang
GPIO.setup(L, GPIO.OUT)                     #Pin als Ausgang
GPIO.setup(M, GPIO.OUT)                     #Pin als Ausgang


"""                                         #Steuerungschema: 1. nur Strom auf Pin1
      1  2  3  4  5  6  7  8                #Steuerungschema: 2. nur Strom auf Pin1 und 2
                                            #Steuerungschema: 3. nur Strom auf Pin2   usw.
Pin1  x  x                 x
Pin2     x  x  x
Pin3           x  x  x
Pin4                 x  x  x

"""

def GPIO_SETUP(a,b,c,d,e,f,g,h,i,k,l,m):                    #Steuerungsschema als Code
    GPIO.output(A, a)
    GPIO.output(B, b)
    GPIO.output(C, c)
    GPIO.output(D, d)
    GPIO.output(E, e)
    GPIO.output(F, f)
    GPIO.output(G, g)
    GPIO.output(H, h)
    GPIO.output(I, i)
    GPIO.output(K, k)
    GPIO.output(L, l)
    GPIO.output(M, m)
    time.sleep(0.001)

def RIGHT_TURN(deg):

    full_circle = 510.0                     #getriebeübersetzung, also 510 schritte für 360°
    degree = full_circle/360*deg
    GPIO_SETUP(0,0,0,0)

    while degree > 0.0:
        GPIO_SETUP(1,0,0,0,0,0,0,0,0,0,0,0)
        GPIO_SETUP(1,1,0,0,0,0,0,0,0,0,0,0)
        GPIO_SETUP(0,1,0,0,0,0,0,0,0,0,0,0)
        GPIO_SETUP(0,1,1,0,0,0,0,0,0,0,0,0)
        GPIO_SETUP(0,0,1,0,0,0,0,0,0,0,0,0)
        GPIO_SETUP(0,0,1,1,0,0,0,0,0,0,0,0)
        GPIO_SETUP(0,0,0,1,0,0,0,0,0,0,0,0)
        GPIO_SETUP(1,0,0,1,0,0,0,0,0,0,0,0)
        degree -= 1.416

def LEFT_TURN(deg):

    full_circle = 510.0                     #getriebeübersetzung, also 510 schritte für 360°
    degree = full_circle/360*deg
    GPIO_SETUP(0,0,0,0)

    while degree > 0.0:
        GPIO_SETUP(0,0,0,0,1,0,0,0,0,0,0,0)
        GPIO_SETUP(0,0,0,0,1,1,0,0,0,0,0,0)
        GPIO_SETUP(0,0,0,0,0,1,0,0,0,0,0,0)
        GPIO_SETUP(0,0,0,0,0,1,1,0,0,0,0,0)
        GPIO_SETUP(0,0,0,0,0,0,1,0,0,0,0,0)
        GPIO_SETUP(0,0,0,0,0,0,1,1,0,0,0,0)
        GPIO_SETUP(0,0,0,0,0,0,0,1,0,0,0,0)
        GPIO_SETUP(0,0,0,0,1,0,0,1,0,0,0,0)
        degree -= 1.416
        
        
def drive(deg):

    full_circle = 510.0                     #getriebeübersetzung, also 510 schritte für 360°
    degree = full_circle/360*deg
    GPIO_SETUP(0,0,0,0)

    while degree > 0.0:
        GPIO_SETUP(1,0,0,0,1,0,0,0,0,0,0,0)
        GPIO_SETUP(1,1,0,0,1,1,0,0,0,0,0,0)
        GPIO_SETUP(0,1,0,0,0,1,0,0,0,0,0,0)
        GPIO_SETUP(0,1,1,0,0,1,1,0,0,0,0,0)
        GPIO_SETUP(0,0,1,0,0,0,1,0,0,0,0,0)
        GPIO_SETUP(0,0,1,1,0,0,1,1,0,0,0,0)
        GPIO_SETUP(0,0,0,1,0,0,0,1,0,0,0,0)
        GPIO_SETUP(1,0,0,1,1,0,0,1,0,0,0,0)
        degree -= 1.416
        
def Band(deg):

    full_circle = 510.0                     #getriebeübersetzung, also 510 schritte für 360°
    degree = full_circle/360*deg
    GPIO_SETUP(0,0,0,0)

    while degree > 0.0:
        GPIO_SETUP(0,0,0,0,0,0,0,0,1,0,0,0)
        GPIO_SETUP(0,0,0,0,0,0,0,0,1,1,0,0)
        GPIO_SETUP(0,0,0,0,0,0,0,0,0,1,0,0)
        GPIO_SETUP(0,0,0,0,0,0,0,0,0,1,1,0)
        GPIO_SETUP(0,0,0,0,0,0,0,0,0,0,1,0)
        GPIO_SETUP(0,0,0,0,0,0,0,0,0,0,1,1)
        GPIO_SETUP(0,0,0,0,0,0,0,0,0,0,0,1)
        GPIO_SETUP(0,0,0,0,0,0,0,0,1,0,0,1)
        degree -= 1.416						#(510/360*1)
		
def stop():
	GPIO_SETUP(0,0,0,0,0,0,0,0,0,0,0,0)

#MAIN #########################


RIGHT_TURN(90)               # "AnzUmdrehungen durch ausprobvieren mit Werten füllen
LEFT_TURN(90)
drive (360*AnzUmdrehungen)					# r ausmessen, 1 Umdrehung = x Meter
Band(360*AnzUmdrehungen)
stop()
    

