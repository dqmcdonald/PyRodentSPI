import serial


print "Start"
ser = serial.Serial('/dev/ttyACM0')

while 1 :
    line = ser.readline()
    print line
