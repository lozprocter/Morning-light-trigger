from gpiozero import LED
import schedule
import time

#assigning gpio 17 to the relay
relay = LED(17)

#this section defines the funtion "flick_relay"
def flick_relay():
  relay.on()

#this schedules the flick_relay func to run at 07:00am every day
schedule.every().day.at("07:00").do(flick_relay)

#while True loop means that the code runs continuously
#time.sleep function defines how long the light is kept on for
while True:
  schedule.run_pending()
  time.sleep(7200)
  
  

