# import serial
# import time
# ser = serial.Serial('COM4',9600)
# try:
#     while True:
#         line = ser.readline().decode().strip()
#         #ser.write() ser.write()로 아두이노에 데이터 전송 기능, encode()후 전송rint("Received:", line)
#         if line.startswith("Temperature"):
#             p
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     ser.close()

import serial
ser = serial.Serial('COM4',9600)
try:
    while True:
        color = input("RGB LED 값을 입력해주세요:")
        colors = ser.write(color.encode())

        print(colors)
        #line = ser.readline().decode()

       #print(line)
except KeyboardInterrupt:
    ser.close()