💊 Smart Medicine Dispenser

The Smart Medicine Dispenser project combines hardware and software to automate the dispensing of medicine. Using a series of servos and an OLED display, this system is designed to manage and dispense medicine according to a preset schedule.

Features
Automated Servo Control: Six servos control various compartments of the dispenser, allowing for precise and sequential opening and closing. The servos are programmed to move in specific sequences based on the time of day.

Interactive OLED Display: An OLED display provides real-time feedback on the dispenser's status, including the current operation and time of day. The display updates dynamically as the servos move.

Push Button Interface: The dispenser is equipped with two push buttons:

Button 1: Initiates a series of pre-defined servo movements for dispensing medicine.
Button 2: Triggers a more complex sequence of movements, gradually adjusting servo angles to simulate different dispensing actions throughout the day.
Time-Based Actions: The system moves servos to different angles based on a weekly schedule, including morning, afternoon, and evening settings for each day of the week. This ensures that the medicine is dispensed at the right times.

Code Overview
The code is divided into several parts:

Initialization: Configures the servos and OLED display. The servos are controlled using PWM signals, and the OLED display is initialized to provide feedback.

Servo Control: Functions to set the angle of each servo are defined. The angles are used to control the dispensing mechanisms.

Button Interaction: Includes functions to handle button presses and execute servo movements based on user input. The system moves servos in a specific sequence when the button is pressed.

Sequence Execution: Contains logic to gradually move servos to desired angles and update the OLED display with corresponding status messages.

The Smart Medicine Dispenser is ideal for automating daily medication routines, making it easier to manage doses and times without manual intervention.
