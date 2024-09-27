# ENGI1020 S2024 - Starting Script of Lab 2

from engi1020.arduino.api import *

#Menu system to choose which design you wish to test
print("Welcome to Lab 2 Script!")
choice = input("Enter 1 to test Design 1 or 2 to test Design 2: ")

#Implemented decision-making based on choice!
if choice == "1":
    print("You've decided to test Design 1")
   
    #STUDENT TODO - Implement Design 1 here!
   
    threshold_value = 17
   
   
   # read button state
    button_pressed = digital_read(6) # True if button is pressed, false if not
    #Check light level and control LED accordingly
    light_sensor_value = analog_read(6)
   
    if light_sensor_value <= threshold_value or button_pressed == True:
        digital_write(4, True) #Turn the LED ON if low light or if button is pressed
       
    elif analog_read(6) > 17:
        digital_write(4, False) #Turn the LED OFF
   
 
elif choice == "2":
    print("You've decided to test Design 2")


# read the sound sensor value
sound_sensor_value = analog_read(2)

# Set threshold for for high sound level (intrusion detection)
sound_threshold = 325

# Admin password stored in system
admin_password = '437709'

# check if the sound level is above the threshold
if sound_sensor_value > sound_threshold:
    #intrusion detected, ask for admin password
    entered_password = input("intrusion detected! enter admin password: ")
   
    #check if enetered password matches the systems password
    if entered_password == admin_password:
        print("access granted. no alarm triggered.")
        buzzer_stop(5) #buzzer is off
    else:
        print("incorrect password! triggering alarm.")
        buzzer_frequency(5,400) #buzzer sounds
else:
    # if sound level is low, buzzer stays off
  
    else:
         print("Invalid choice, please rerun script and try again!")


