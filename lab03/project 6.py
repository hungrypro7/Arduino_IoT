# LCD 화면에 출력하기
import image, lcd, utime

lcd.init()
img = image.Image(size=(320, 240))
img.draw_circle((100, 100, 50), color=(255,255,0), fill=True)
lcd.display(img)
img.draw_rectangle((100,100,30,70), color=(255,0,255), fill=True)
lcd.display(img)
img.draw_line((0,0,lcd.width(),lcd.height()),thickness=5, color=(255,255,255))
lcd.display(img)
img.draw_string((100, 100, "chanyoung lee"), scale=5, color=(0,255,0))
lcd.display(img)
