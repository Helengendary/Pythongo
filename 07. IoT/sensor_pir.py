from machine import Pin
import time

pir_sensor = Pin(14, Pin.IN)

def read_pir_sensor():
    while True:
        print(pir_sensor.value())
        if pir_sensor.value() == 1:
            print("Movimento detectado!")
        else:
            print("Nenhum movimeto!")
            
        time.sleep(1)
        
read_pir_sensor()