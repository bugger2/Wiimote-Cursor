# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# The following lines of code demonstrate many of the features realted to wiimotes, such as capturing button presses and rumbling the controller.
# I have managed to map the home button to the accelerometer - simply hold it and values will appear!

# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!
import cwiid, time, turtle

button_delay = 0.1
color = 1
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()
except:
  exit()
circle_width = 5
t.begin_fill()
wii.rpt_mode = cwiid.RPT_BTN

while True:
  
  while (2 == 2):
    goto(200, 100)
    if (color == 1 & cwiid.BTN_A != True):
      colorRGB = 0,0,0
      turtle.fillcolor(colorRGB)
      circle(circle_width)  
    else if (color == 2):
      colorRGB = 255,255,255
      turtle.fillcolor(colorRGB)
      circle(circle_width)
    else if (color == 3):
      colorRGB = (0,0,255)
      turtle.fillcolor(colorRGB)
      circle(circle_width)
    else if (color == 4):
      colorRGB = (128,0,128)
      turtle.fillcolor(colorRGB)
      circle(circle_width)
    else if (color == 5):
      colorRGB = (255,192,203)
      turtle.fillcolor(colorRGB)
      circle(circle_width)
    else if (color == 6):
      colorRGB = (255,0,0)
      turtle.fillcolor(colorRGB)
      circle(circle_width)
    else if (color == 7):
      colorRGB = (255,255,0)
      turtle.fillcolor(colorRGB)
      circle(circle_width)
    else if (color == 8):
      colorRGB = (0,255,0)
      turtle.fillcolor(colorRGB)
      circle(circle_width)
    else:
      color = 1
    clear()

  buttons = wii.state['buttons']

  # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!
  if (buttons & cwiid.BTN_LEFT):
    color = color + 1
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    color = color + 1
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    turtle.fillcolor(colorRGB)
    circle(circle_width)
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    cursorX = #MIDLE OF SCREEN COORDINATES HERE
    cursorY = #MIDLE OF SCREEN COORDINATES HERE
    time.sleep(button_delay)
