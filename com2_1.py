import serial

ser = serial.Serial(
    port='COM2',\
    baudrate=1200,\
    parity=serial.PARITY_ODD,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.SEVENBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
count=1

while True:
    for line in ser.read():

        # print(str(count) + str(': ') + chr(line) )
        # print(chr(line))
        print(line)
        
        count = count+1

ser.close()
