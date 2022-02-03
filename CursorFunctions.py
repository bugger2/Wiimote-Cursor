# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# The following lines of code demonstrate many of the features realted to wiimotes, such as capturing button presses and rumbling the controller.
# I have managed to map the home button to the accelerometer - simply hold it and values will appear!

# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!
import cwiid, time, turtle, matplotlib
matplotlib.use('Agg')
button_delay = 0.1
color = 1
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except:
  print("Connection failed. Please try again.")
  quit()
circle_width = 5
print("Connection established. Feel free to draw.")

wii.rpt_mode = cwiid.RPT_BTN

#All turtle preamble
bg = turtle.Screen()
bg.bgcolor("black")
bg.title("Good Morning!")
turtle.speed(0)
turtle.begin_fill()
turtle.goto(200,200)
turtle.hideturtle()
turtle.pendown()
turtle.begin_fill()
turtle.pencolor('#FFFFFF')
turtle.fillcolor('#FFFFFF')
turtle.circle(circle_width)
while True:
  buttons = wii.state['buttons']
  
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
    
 # if (buttons & cwiid.BTN_A != True):
  #  turtle.pendown()
   # turtle.begin_fill()
    #turtle.fillcolor('#FFFFFF')
#    turtle.pencolor('#FFFFFF')
 #   turtle.circle(circle_width)
  #  turtle.end_fill()
   # turtle.clear()

  # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!
  if (buttons & cwiid.BTN_LEFT):
    color = color + 1
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    color = color + 1
    time.sleep(button_delay)
#BUTTON A CODE
  if (buttons & cwiid.BTN_A):
    turtle.begin_fill()
    turtle.pencolor('#FFFFFF')
    turtle.fillcolor('#FFFFFF')
    turtle.circle(circle_width)
    turtle.end_fill()
    time.sleep(button_delay)
#BUTTON B CODE
  if (buttons & cwiid.BTN_B):
    while (2 == 2)
      
      turtle.pendown()
      turtle.begin_fill()
      turtle.fillcolor('#FFFFFF')
      turtle.pencolor('#FFFFFF')
      turtle.circle(circle_width)
      turtle.end_fill()
      turtle.clear()
      wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
      roll=(wii.state['acc'][0]-120)
      pitch=(wii.state['acc'][1]-125)
      check = 0
      while check == 0:
        if (roll < -10):
          turtle.setheading(0)
          turtle.forward(4)
        if (roll > 10):
          turtle.setheading(180)
          turtle.forward(4)
        if (pitch < -5):
          turtle.setheading(90)
          turtle.forward(4)
        if (pitch > 10):
          turtle.setheading(270)
          turtle.forward(4)
      time.sleep(0.01)
      check = (buttons & cwiid.BTN_B)
      time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    turtle.goto(200,200)
    time.sleep(button_delay)
    
turtle.endfill()
