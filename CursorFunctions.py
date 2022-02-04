# Coded by SpicyMileHigh, script based off of that of The Raspberry Pi Guy's.
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
#I honestly have no idea what this does and am too scared to remove it. Came from The Raspberry Pi Guys code.
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
#Stuff to do with buttons
while True:
  buttons = wii.state['buttons']

  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    # NOTE: This is how you RUMBLE the Wiimote
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

#Draws
  if (buttons & cwiid.BTN_A):
    turtle.begin_fill()
    turtle.pencolor('#FFFFFF')
    turtle.fillcolor('#FFFFFF')
    turtle.circle(circle_width)
    turtle.end_fill()
    time.sleep(button_delay)
#Moves the cursor
  if (buttons & cwiid.BTN_B):
    turtle.clear()
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('#FFFFFF')
    turtle.pencolor('#FFFFFF')
    turtle.circle(circle_width)
    turtle.end_fill()
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    roll=(wii.state['acc'][0]-120)
    pitch=(wii.state['acc'][1]-121)
    check = 0
    while check == 0:
      if (roll < 0):
        turtle.setheading(0)
        turtle.forward(roll)
      if (roll > 0):
        turtle.setheading(180)
        turtle.backward(roll)
      if (pitch < 0):
        turtle.setheading(90)
        turtle.backward(pitch)
      if (pitch > 0):
        turtle.setheading(270)
        turtle.forward(pitch)
      time.sleep(0.01)
      check = (buttons & cwiid.BTN_B)
    time.sleep(button_delay)
#sets the cursor to center of screen
  if (buttons & cwiid.BTN_HOME):
    turtle.penup()
    turtle.goto(200,200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.pencolor('#FFFFFF')
    turtle.fillcolor('#FFFFFF')
    turtle.circle(circle_width)
    turtle.end_fill()
    turtle.clear()
    time.sleep(button_delay)

turtle.endfill()
