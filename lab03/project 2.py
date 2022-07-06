# 초음판 센서 활용

from fpioa_manager import fm
from Maix import GPIO
import utime
from machine import Timer

count = 0

def on_timer(timer):
    global count
    count = count + 1

def test_irq(pin_num):
    global count
    tim.stop()
    if count > 10:
        distance = ((340*count)/1000)/2
        print(distance)
    count = 0

def ultra_send():
    for _ in range(1):
        trig.value(1)
        utime.sleep_us(10)
        trig.value(0)
        utime.sleep_us(10)
    tim.start()

io_echo_pin = 14
io_trig_pin = 13
fm.register(io_echo_pin, fm.fpioa.GPIOHS0)
fm.register(io_trig_pin, fm.fpioa.GPIO0)

tim = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=20, unit=Timer.UNIT_US, callback=on_timer, arg=on_timer)

echo = GPIO(GPIO.GPIOHS0, GPIO.IN)
trig = GPIO(GPIO.GPIO0, GPIO.OUT)
echo.irq(test_irq, GPIO.IRQ_FALLING, GPIO.WAKEUP_NOT_SUPPORT, 10)

while True:
    ultra_send()
    utime.sleep(1)
