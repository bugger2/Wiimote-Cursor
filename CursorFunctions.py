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
  quit()
circle_width = 5
roll=(wii.state['acc'][0])
pitch=(wii.state['acc'][1])
turtle.begin_fill()
wii.rpt_mode = cwiid.RPT_BTN
turtle.goto(150,150)
while True:
  buttons = wii.state['buttons']
  
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
    
  if (color == 1 & cwiid.BTN_A != True):
    turtle.pendown()
    colorRGB = 255,165,0
    turtle.fillcolor(colorRGB)
    circle(circle_width)  
  if (color == 2 & cwiid.BTN_A != True):
    turtle.pendown()
    colorRGB = 255,255,255
    turtle.fillcolor(colorRGB)
    circle(circle_width)
  if (color == 3 & cwiid.BTN_A != True):
    turtle.pendown()
    colorRGB = (0,0,255)
    turtle.fillcolor(colorRGB)
    circle(circle_width)
  if (color == 4 & cwiid.BTN_A != True):
    turtle.pendown()
    colorRGB = (128,0,128)
    turtle.fillcolor(colorRGB)
    circle(circle_width)
  if (color == 5 & cwiid.BTN_A != True):
    turtle.pendown()
    colorRGB = (255,192,203)
    turtle.fillcolor(colorRGB)
    circle(circle_width)
  if (color == 6 & cwiid.BTN_A != True):
    turtle.pendown()
    colorRGB = (255,0,0)
    turtle.fillcolor(colorRGB)
    circle(circle_width)
  if (color == 7 & cwiid.BTN_A != True):
    turtle.pendown()
    colorRGB = (255,255,0)
    turtle.fillcolor(colorRGB)
    circle(circle_width)
  if (color == 8 & cwiid.BTN_A != True):
    turtle.pendown()
    colorRGB = (0,255,0)
    turtle.fillcolor(colorRGB)
    circle(circle_width)
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
    turtle.fillcolor(colorRGB)
    turtle.pendown()
    circle(circle_width)
    time.sleep(button_delay)
   # print(wii.state)
  if (buttons & cwiid.BTN_B):
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
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    turtle.goto(150,150)
    time.sleep(button_delay)
