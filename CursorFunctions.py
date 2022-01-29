# This program utilises the cwiid Python library in order to get input over bluetooth from a wiimote.
# The following lines of code demonstrate many of the features realted to wiimotes, such as capturing button presses and rumbling the controller.
# I have managed to map the home button to the accelerometer - simply hold it and values will appear!

# Coded by The Raspberry Pi Guy. Work based on some of Matt Hawkins's!
import cwiid, time, js2py

button_delay = 0.1
color = 1
print 'Please press buttons 1 + 2 on your Wiimote now ...'
time.sleep(1)

# This code attempts to connect to your Wiimote and if it fails the program quits
try:
  wii=cwiid.Wiimote()

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:
  
  while (2 == 2):
    if (color == 1 & cwiid.BTN_B != True):
      js2py.eval_js(
        fill(black);
        stroke(black);
        clear()
        ellipse(cursorX, cursorY, 5, 5);
      )
    else if (color == 2):
      js2py.eval_js(
        fill(white);
        stroke(white);
        clear()
        ellipse(cursorX, cursorY, 5, 5);
      )
    else if (color == 3):
      js2py.eval_js(
        fill(blue);
        stroke(blue);
        clear()
        ellipse(cursorX, cursorY, 5, 5);
      )
    else if (color == 4):
      js2py.eval_js(
        fill(purple);
        stroke(purple);
        clear()
        ellipse(cursorX, cursorY, 5, 5);
      )
    else if (color == 5):
      js2py.eval_js(
        fill(pink);
        stroke(pink);
        clear()
        ellipse(cursorX, cursorY, 5, 5);
      )
    else if (color == 6):
      js2py.eval_js(
        fill(red);
        stroke(red);
        clear()
        ellipse(cursorX, cursorY, 5, 5);
      )
    else if (color == 7):
      js2py.eval_js(
        fill(yellow);
        stroke(yellow);
        clear()
        ellipse(cursorX, cursorY, 5, 5);
      )
    else if (color == 8):
      js2py.eval_js(
        fill(green);
        stroke(green);
        clear()
        ellipse(cursorX, cursorY, 5, 5);
      )
    else if (color == 9):
      color = 1
    else:
      color = 1

  buttons = wii.state['buttons']

  # The following code detects whether any of the Wiimotes buttons have been pressed and then prints a statement to the screen!
  if (buttons & cwiid.BTN_LEFT):
    color = color + 1
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    color = color + 1
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    js2py.eval_js(
      ellipse(cursorX, cursorY, 5, 5)
tyg
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    cursorX = #MIDLE OF SCREEN COORDINATES HERE
    cursorY = #MIDLE OF SCREEN COORDINATES HERE
    time.sleep(button_delay)
