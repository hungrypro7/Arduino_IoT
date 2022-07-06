# ADC 변환
import time, network
from Maix import GPIO
from fpioa_manager import

class wifi():
    fm.register(25, fm.fpioa.GPIOHS10)
    fm.register(8, fm.fpioa.GPIOHS11)
    fm.register(9, fm.fpioa.GPIOHS12)
    print("Use Hareware SPI for other maixduino")
    fm.register(28, fm.fpioa.SPI1_D0, force=True)
    fm.register(26, fm.fpioa.SPI1_D1, force=True)
    fm.register(27, fm.fpioa.SPI1_SCLK,force=True)
    nic = network.ESP32_SPI(cs=fm.fpioa.GPIOHS10, rst=fm.fpioa.GPIOHS11, rdy=fm.fpioa.GPIOHS12, spi=1)

print("ESP32_SPI firmware version:", wifi.nic.version())

while True:
    try:
        adc = wifi.nic.adc((0,))
    except Exception as e:
        print(e)
        continue
    for v in adc:
        print("ADC0 Value : %04d" % (v))
