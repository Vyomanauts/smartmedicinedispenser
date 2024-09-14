#PART 1 --------------------------------------------------------------------
from machine import Pin, PWM
import time
from machine import Pin, PWM, SoftI2C
from ssd1306 import SSD1306_I2C
# Define the pins connected to the servos
servo_pin_1 = 5
servo_pin_2 = 4
servo_pin_3 = 13  # Assuming GPIO pin 13 for the third servo
servo_pin_4 = 18
servo_pin_5 = 15
servo_pin_6 = 19

# Initialize the servo PWM pins
servo_1 = PWM(Pin(servo_pin_1), freq=50)
servo_2 = PWM(Pin(servo_pin_2), freq=50)
servo_3 = PWM(Pin(servo_pin_3), freq=50)
servo_4 = PWM(Pin(servo_pin_4), freq=50)
servo_5 = PWM(Pin(servo_pin_5), freq=50)
servo_6 = PWM(Pin(servo_pin_6), freq=50)



#oled code---------------------------------------------------
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))  # SCL on pin 22, SDA on pin 21
oled = SSD1306_I2C(128, 64, i2c)  # Adjust dimensions if your OLED display is different


oled.fill(0)
oled.show()




# Function to set the angle of the servos
def set_angle(servo, angle):
    duty = (angle / 180) * 102 + 26
    servo.duty(int(duty))
    print("Angle set to:", angle)






#---------------------------------------------------------------------

# Function to set the angle of the servos
def set_angle(servo, angle):
    duty = (angle / 180) * 102 + 26
    servo.duty(int(duty))
    print("Angle set to:", angle)

# Loop to move all six servos sequentially from 0 to 45 degrees one by one

#------------------------------------------------------------------
#PART 3 --------------------------------------------------------
# Define the pin connected to the push button
BUTTON_PIN = 14 # Assuming GPIO pin 23 for the push button

# Initialize the push button pin
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

servo_4_at_0 = False

# Function to wait for button press with a small delay
def wait_for_button_press():
    time.sleep(0.1)  # Small delay to debounce the button
    while button.value() == 1:  # Wait for button press
        pass
    time.sleep(0.1)  # Small delay after button press




# Move servo_4 from 45 to 0 degrees
wait_for_button_press()
if not servo_4_at_0:
    for angle in range(45, -1, -1):
        set_angle(servo_4, angle)
        print("Servo_4 angle:", angle)  # Print the current angle
        time.sleep(0.1)
        oled.text("Moving to 0 (Left)", 0, 0)
        oled.show()  # Update OLED display
        oled.fill(0)

    # Update the flag to indicate that servo_4 is now at 0 degrees
    servo_4_at_0 = True
   



# Move servo_5 from 45 to 0 degrees
wait_for_button_press()
for angle in range(45, -1, -1):
    set_angle(servo_5, angle)
    time.sleep(0.1)
    oled.text("Monday", 0, 0)  # 
    oled.text("Afternoon", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)


# Move servo_6 from 0 to 45 degrees
wait_for_button_press()
for angle in range(45, -1, -1):
    set_angle(servo_6, angle)
    time.sleep(0.1)
    oled.text("Monday", 0, 0)  # 
    oled.text("Evening", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)




# Move servo_3 from 85 to 70 degrees
wait_for_button_press()
for angle in range(85, 69, -1):
    set_angle(servo_3, angle)
    time.sleep(0.1)
    oled.text("Tuesday", 0, 0)  # 
    oled.text("Morning", 0, 10)
    oled.show()  # Update OLED display
    oled.fill(0)




# Move servo_3 from 70 to 45 degrees
wait_for_button_press()
for angle in range(70, 44, -1):
    set_angle(servo_3, angle)
    time.sleep(0.1)
    oled.text("Tuesday", 0, 0)  # 
    oled.text("Afternoon", 0, 10)     
    oled.show()  # Update OLED display
    oled.fill(0)




# Move servo_3 from 45 to 0 degrees
wait_for_button_press()
for angle in range(45, -1, -1):
    set_angle(servo_3, angle)
    time.sleep(0.1)
    oled.text("Tuesday", 0, 0)  # 
    oled.text("Evening", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)




# Move servo_2 from 80 to 70 degrees
wait_for_button_press()
for angle in range(80, 69, -1):
    set_angle(servo_2, angle)
    time.sleep(0.1)
    oled.text("Wednesday", 0, 0)  # 
    oled.text("Morning", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)





# Move servo_2 from 70 to 45 degrees
wait_for_button_press()
for angle in range(70, 44, -1):
    set_angle(servo_2, angle)
    time.sleep(0.1)
    oled.text("Wednesday", 0, 0)  # 
    oled.text("Afternoon", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)





# Move servo_2 from 45 to 0 degrees
wait_for_button_press()
for angle in range(45, -1, -1):
    set_angle(servo_2, angle)
    time.sleep(0.1)
    oled.text("Wednesday", 0, 0)  # 
    oled.text("Evening", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)





# Move servo_1 from 80 to 70 degrees
wait_for_button_press()
for angle in range(80, 69, -1):
    set_angle(servo_1, angle)
    time.sleep(0.1)
    oled.text("Thursday", 0, 0)  # 
    oled.text("Morning", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)



# Move servo_1 from 70 to 45 degrees
wait_for_button_press()
for angle in range(70, 44, -1):
    set_angle(servo_1, angle)
    time.sleep(0.1)
    oled.text("Thursday", 0, 0)  # 
    oled.text("Afternoon", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)




# Move servo_1 from 45 to 0 degrees
wait_for_button_press()
for angle in range(45, -1, -1):
    set_angle(servo_1, angle)
    time.sleep(0.1)
    oled.text("Thursday", 0, 0)  
    oled.text("Evening", 0, 10) 
    oled.show()  # Update OLED display
    oled.fill(0)


#----------------------------------------------------------------------

#PART 4 ------------------------------------------------------------------
# Define the pin connected to the push button 2
BUTTON_PIN_2 = 26  # Assuming GPIO pin 24 for the push button 2

# Initialize the push button 2 pin
button_2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

# Function to wait for button 2 press with a small delay
def wait_for_button_2_press():
    time.sleep(0.1)  # Small delay to debounce the button
    while button_2.value() == 1:  # Wait for button press
        pass
    time.sleep(0.1)  # Small delay after button press


oled.text("Waiting ", 0, 0)  
oled.text("Pushbutton Two", 0, 10) 
oled.show()  # Update OLED display
oled.fill(0)

# Wait for button 2 press

# Function to move servos as per the specified sequence
# Function to move all servos gradually from their initial angles to the specified angles over 5 seconds
def move_servos_sequence():
    
    
    
    # Move servo_4 gradually from its initial angle to 45 degrees
    for angle in range(46):
        set_angle(servo_4, angle)
        time.sleep(0.1)
        oled.text("Monday", 0, 0)  
        oled.text("Morning", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
    

    # Move servo_5 gradually from its initial angle to 45 degrees
    for angle in range(46):
        set_angle(servo_5, angle)
        time.sleep(0.1)
        oled.text("Monday", 0, 0)  
        oled.text("Afternoon", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
    

    # Move servo_6 gradually from its initial angle to 45 degrees
    for angle in range(46):
        set_angle(servo_6, angle)
        time.sleep(0.1)
        oled.text("Monday", 0, 0)  
        oled.text("Evening", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
    

    # Move servo_3 gradually from its initial angle to 35 degrees
    for angle in range(36):
        set_angle(servo_3, angle)
        time.sleep(0.1)
        oled.text("Tuesday", 0, 0)  
        oled.text("Morning", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
    

    # Move servo_3 gradually from 35 to 45 degrees
    for angle in range(35, 46):
        set_angle(servo_3, angle)
        time.sleep(0.1)
        oled.text("Tuesday", 0, 0)  
        oled.text("Afternoon", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
    

    # Move servo_3 gradually from 45 to 70 degrees
    for angle in range(46, 71):
        set_angle(servo_3, angle)
        time.sleep(0.1)
        oled.text("Tuseday", 0, 0)  
        oled.text("Evening", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
    

    # Move servo_2 gradually from its initial angle to 35 degrees
    for angle in range(36):
        set_angle(servo_2, angle)
        time.sleep(0.1)
        oled.text("Wednesday", 0, 0)  
        oled.text("Morning", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
    

    # Move servo_2 gradually from 35 to 45 degrees
    for angle in range(35, 46):
        set_angle(servo_2, angle)
        time.sleep(0.1)
        oled.text("Wednesday", 0, 0)  
        oled.text("Afternoon", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
    


    # Move servo_2 gradually from 45 to 70 degrees
    for angle in range(46, 71):
        set_angle(servo_2, angle)
        time.sleep(0.1)
        oled.text("Wednesday", 0, 0)  
        oled.text("Evening", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
         

    # Move servo_1 gradually from its initial angle to 35 degrees
    for angle in range(36):
        set_angle(servo_1, angle)
        time.sleep(0.1)
        oled.text("Thursday", 0, 0)  
        oled.text("Morning", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
        
       

    # Move servo_1 gradually from 35 to 45 degrees
    for angle in range(35, 46):
        set_angle(servo_1, angle)
        time.sleep(0.1)
        oled.text("Thursday", 0, 0)  
        oled.text("Afternoon", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)
        
        
        
    


    # Move servo_1 gradually from 45 to 70 degrees
    for angle in range(46, 71):
        set_angle(servo_1, angle)
        time.sleep(0.1)
        oled.text("Thursday", 0, 0)  
        oled.text("Evening", 0, 10) 
        oled.show()  # Update OLED display
        oled.fill(0)


wait_for_button_2_press()

# Check if button 2 is pressed
if button_2.value() == 0:
    # If button 2 is pressed, move servos in the specified sequence
    move_servos_sequence()




    # Move servos in the specified sequence

#------------------------------------------------------------------------


