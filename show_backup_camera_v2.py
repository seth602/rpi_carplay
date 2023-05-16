
import RPi.GPIO as GPIO
import time
import vlc
  
GPIO.setmode(GPIO.BCM)
  
# The input pin which is connected with the sensor
GPIO_PIN = 12
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
   
# Main program loop
#try:
#    while True:
#        time.sleep(1)
#        print(GPIO.input(12))
        
        
# 1=no magnet/not in reverse
# 0=magnet/in reverse
i = vlc.Instance("--vout=gl")
p = i.media_player_new()
p.stop()
m = i.media_new("v4l2://")
p.toggle_fullscreen()
p.set_media(m)
camera_status=0

while True:
    time.sleep(.5)
    if GPIO.input(12) == 1:
        if camera_status == 0:
            pass
        elif camera_status == 1:
            p.stop()
            camera_status=0
    if GPIO.input(12) == 0:
        if camera_status == 0:
            p.play()
            camera_status=1
        elif camera_status == 1:
            pass
        
  
# Scavenging work after the end of the program
#except KeyboardInterrupt:
GPIO.cleanup()
