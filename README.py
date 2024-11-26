# pantalla-lcd
import machine
from machine import Pin, SoftI2C, sleep
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time


i2C_ADDR = 0X27
totalRows = 2
totalColumns = 16

i2c = SoftI2C (scl=Pin(22), sda=Pin (21), freq=10000) #inicializa el 12c
lcd = I2cLcd (i2c, i2C_ADDR, totalRows, totalColumns)

while True:
      lcd.clear()
      lcd.putstr("...angel..      ")
      lcd.putstr("...auquilla..")
      time.sleep(2)
      lcd.clear()
      lcd.putstr("......pruebas de escritura..")
      time.sleep(2)
      lcd.clear()
      for i in range(11):
          lcd.putstr(str(i))
          time.sleep(1)
          lcd.clear()
      lcd.putstr("sistemas microcontrolados")
      time.sleep(1)
