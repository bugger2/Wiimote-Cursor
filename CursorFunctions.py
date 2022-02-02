# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# The following lines of code demonstrate many of the features realted to wiimotes, such as capturing button presses and rumbling the controller.
# I have managed to map the home button to the accelerometer - simply hold it and values will appear!

# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!
import cwiid, time, turtle, matplotlib
matplotlib.use('Agg')
button_delay = 0.1
color = 1
time.sleep(1)
turtle.speed(0)
# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except:
  print("Connection failed. Please try again.")
  quit()
circle_width = 5
print("Connection established. Feel free to draw.")
turtle.begin_fill()
wii.rpt_mode = cwiid.RPT_BTN
turtle.goto(150,150)
turtle.begin_fill()
while True:
  buttons = wii.state['buttons']
  
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
    
  if (color == 1 and cwiid.BTN_A != True):
    turtle.pendown()
    turtle.fillcolor('#FFFFFF')
    turtle.circle(circle_width)  
  if (color == 2 and cwiid.BTN_A != True):
    turtle.pendown()
    turtle.fillcolor('#A020F0')
    turtle.circle(circle_width)
  if (color == 3 and cwiid.BTN_A != True):
    turtle.pendown()
    turtle.fillcolor('#0000FF')
    turtle.circle(circle_width)
  if (color == 4 and cwiid.BTN_A != True):
    turtle.pendown()
    turtle.fillcolor('#FF0000')
    turtle.circle(circle_width)
  if (color == 5 and cwiid.BTN_A != True):
    turtle.pendown()
    turtle.fillcolor('#00FF00')
    turtle.circle(circle_width)
  if (color == 6 and cwiid.BTN_A != True):
    turtle.pendown()
    turtle.fillcolor('#FFFF00')
    turtle.circle(circle_width)
  if (color == 7 and cwiid.BTN_A != True):
    turtle.pendown()
    turtle.fillcolor('#FFA500')
    turtle.circle(circle_width)
  if (color == 8 and cwiid.BTN_A != True):
    turtle.pendown()
    turtle.fillcolor('#FFC0CB')
    turtle.circle(circle_width)
  if (color < 1 or color > 8):
    color = 1
  turtle.clear()

  # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!
  if (buttons & cwiid.BTN_LEFT):
    color = color + 1
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    color = color + 1
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    turtle.fillcolor('#FFFFFF')
    roll=(wii.state['acc'][0])
    pitch=(wii.state['acc'][1])
    turtle.pendown()
    turtle.circle(circle_width)
    check = 0
    while check == 0:
      print(wii.state['acc'][0]-120)
      print(wii.state['acc'][1]-123)
      time.sleep(0.1)
      check = (buttons & cwiid.BTN_HOME)
    time.sleep(button_delay)
  if (buttons & cwiid.BTN_B):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    roll=(wii.state['acc'][0])
    pitch=(wii.state['acc'][1])
    if (roll < -5):
      turtle.seth(0)
      turtle.back(2)
    if (roll > 5):
      turtle.seth(0)
      turtle.forward(2)
    if (pitch > 5):
      turtle.seth(90)
      turtle.forward(2)
    if (pitch < -5):
      turtle.seth(90)
      turtle.back(2)

  if (buttons & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    turtle.goto(150,150)
    time.sleep(button_delay)
