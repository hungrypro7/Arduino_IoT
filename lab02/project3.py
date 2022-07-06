# 버튼을 누를 때마다 LED가 하나씩 켜지기
from fpioa_manager import fm
from Maix import GPIO
import utime

io_btn = 22
led_1 = 15
led_2 = 32
led_3 = 24
led_4 = 23

fm.register(io_btn, fm.fpioa.GPIO1)
fm.register(led_1, fm.fpioa.GPIO2)
fm.register(led_2, fm.fpioa.GPIO3)
fm.register(led_3, fm.fpioa.GPIO4)
fm.register(led_4, fm.fpioa.GPIO5)

btn = GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_DOWN)
led1 = GPIO(GPIO.GPIO2, GPIO.OUT)
led2 = GPIO(GPIO.GPIO3, GPIO.OUT)
led3 = GPIO(GPIO.GPIO4, GPIO.OUT)
led4 = GPIO(GPIO.GPIO5, GPIO.OUT)

count = 0
while(True):
    state_current = btn.value()
    if state_current == 1:
        if state_previous == 0:
            count = count + 1
            state_previous = 1
            print(count)
        utime.sleep_ms(100)
    else:
        state_previous = 0

    if count == 1:
        led1.value(1)
        led2.value(0)
        led3.value(0)
        led4.value(0)
    if count == 2:
        led1.value(1)
        led2.value(1)
        led3.value(0)
        led4.value(0)
    if count == 3:
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(0)
    if count == 4:
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(1)
    if count == 5:
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
    if count > 5:
        count = 1