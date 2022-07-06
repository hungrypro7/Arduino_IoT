# LED가 동시에 켜졌다가 꺼지기
from fpioa_manager import fm
from Maix import GPIO
import utime

io_led_red = 15
io_led_green = 32
io_led_blue = 24
io_led_red2 = 23

fm.register(io_led_red, fm.fpioa.GPIO0)
fm.register(io_led_green, fm.fpioa.GPIO1)
fm.register(io_led_blue, fm.fpioa.GPIO2)
fm.register(io_led_red2, fm.fpioa.GPIO3)

led_r = GPIO(GPIO.GPIO0, GPIO.OUT)
led_s = GPIO(GPIO.GPIO1, GPIO.OUT)
led_t = GPIO(GPIO.GPIO2, GPIO.OUT)
led_u = GPIO(GPIO.GPIO3, GPIO.OUT)

while(True):
    led_r.value(1)
    led_s.value(1)
    led_t.value(1)
    led_u.value(1)
    utime.sleep_ms(500)

    led_r.value(0)
    led_s.value(0)
    led_t.value(0)
    led_u.value(0)
    utime.sleep_ms(500)
