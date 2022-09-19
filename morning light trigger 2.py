from gpiozero import LED
import schedule
import time

#assigning gpio 17 to the relay
relay = LED(17)

#this section defines the funtions to flick the relay on and off
def relay_on():
  relay.on()
def relay_off():
  relay.off()

#this schedules the light to come on at 07:00am until 09:00am every day
schedule.every().day.at("20:50").do(relay_on)
schedule.every().day.at("09:00").do(relay_off)

#while True loop means that the code runs continuously
while True:
  schedule.run_pending()
  time.sleep(1)
  
  

