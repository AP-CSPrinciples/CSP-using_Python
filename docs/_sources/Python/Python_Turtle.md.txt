# Python Turtle Basics


## Pythod Turtle Graphic Methods

Here's a comprehensive list of Python's Turtle Graphics module methods, divided into categories for easier reference. These methods are often used to control the turtle's movements, set its appearance, draw shapes, and control the window. This list includes methods available up to Python 3.10.

### 1. **Turtle Motion and Positioning**

| Method | Description |
|--------|-------------|
| `forward(distance)` or `fd(distance)` | Move the turtle forward by the specified distance. |
| `backward(distance)` or `bk(distance)` or `back(distance)` | Move the turtle backward by the specified distance. |
| `right(angle)` or `rt(angle)` | Turn the turtle clockwise by the specified angle. |
| `left(angle)` or `lt(angle)` | Turn the turtle counterclockwise by the specified angle. |
| `goto(x, y)` or `setpos(x, y)` or `setposition(x, y)` | Move the turtle to the specified coordinates. |
| `setx(x)` | Set the turtle’s x-coordinate. |
| `sety(y)` | Set the turtle’s y-coordinate. |
| `setheading(angle)` or `seth(angle)` | Set the turtle’s heading to the specified angle. |
| `home()` | Move the turtle to the origin (0, 0) and set its heading to 0 degrees. |
| `circle(radius, extent=None, steps=None)` | Draw a circle with the specified radius. Optional extent to draw only part of the circle, and steps for polygon approximation. |
| `dot(size=None, color=None)` | Draw a dot with the specified size and color. |
| `stamp()` | Stamp a copy of the turtle shape onto the canvas and return its stamp ID. |
| `clearstamp(stampid)` | Delete a specific stamp by its ID. |
| `clearstamps(n=None)` | Delete all stamps or the last `n` stamps if `n` is provided. |
| `undo()` | Undo the last turtle action. |
| `speed(speed)` | Set the turtle’s speed. `0` means no animation, `1` is slow, `10` is fast. |

### 2. **Turtle State and Status**

| Method | Description |
|--------|-------------|
| `position()` or `pos()` | Return the current position as a tuple `(x, y)`. |
| `towards(x, y)` | Return the angle towards the specified point. |
| `xcor()` | Return the turtle’s x-coordinate. |
| `ycor()` | Return the turtle’s y-coordinate. |
| `heading()` | Return the turtle’s current heading angle. |
| `distance(x, y)` | Return the distance from the turtle’s position to the specified point. |
| `isdown()` | Return `True` if the pen is down, `False` otherwise. |
| `isvisible()` | Return `True` if the turtle is visible, `False` otherwise. |

### 3. **Turtle Pen Control**

| Method | Description |
|--------|-------------|
| `pendown()` or `pd()` or `down()` | Lower the pen to draw when the turtle moves. |
| `penup()` or `pu()` or `up()` | Raise the pen to prevent drawing when the turtle moves. |
| `pensize(width)` or `width(width)` | Set the width of the pen. |
| `pen(pen=None, **pendict)` | Return or set the pen’s attributes (color, width, etc.). |
| `pen(pencolor, fillcolor)` | Set both pen color and fill color. |
| `pencolor(color)` | Set the pen color. |
| `fillcolor(color)` | Set the fill color. |
| `begin_fill()` | Start filling a shape. |
| `end_fill()` | Fill the shape drawn after `begin_fill()` is called. |
| `color(pencolor, fillcolor)` | Set both the pen and fill color. |
| `reset()` | Reset the turtle’s state, clearing the drawing and resetting attributes. |
| `clear()` | Clear the drawing without changing the turtle’s position. |
| `write(arg, move=False, align='left', font=('Arial', 8, 'normal'))` | Write text at the turtle's current position. |

### 4. **Turtle Appearance**

| Method | Description |
|--------|-------------|
| `shape(name)` | Set the turtle’s shape (`'arrow'`, `'turtle'`, `'circle'`, `'square'`, `'triangle'`, `'classic'`). |
| `shapesize(stretch_wid=None, stretch_len=None, outline=None)` or `turtlesize(...)` | Stretch the turtle’s shape. |
| `shearfactor(factor)` | Set or get the shear factor for the turtle's shape. |
| `tilt(angle)` | Tilt the turtle shape by the specified angle. |
| `tiltangle(angle=None)` | Set or get the tilt angle of the turtle shape. |
| `get_shapepoly()` | Return the current shape as a polygon. |
| `showturtle()` or `st()` | Make the turtle visible. |
| `hideturtle()` or `ht()` | Make the turtle invisible. |
| `resizemode(rmode)` | Set the resize mode (`'auto'`, `'user'`, `'noresize'`). |

### 5. **Screen Control and Events**

| Method | Description |
|--------|-------------|
| `Screen()` | Return the Screen object used for window control. |
| `bye()` | Close the Turtle Graphics window. |
| `bgcolor(color)` | Set or get the background color. |
| `bgpic(picname)` | Set or get the background image. |
| `title(title)` | Set the title of the window. |
| `clearscreen()` | Clear the screen. |
| `onclick(fun, btn=1, add=None)` | Bind a function to a mouse click. |
| `onkey(fun, key)` | Bind a function to a key press. |
| `listen()` | Set focus on the screen to capture key presses. |
| `mainloop()` | Start the main event loop. |
| `tracer(n=None, delay=None)` | Set the screen update delay to control animation speed. |
| `update()` | Force an update of the screen. |

### 6. **Miscellaneous**

| Method | Description |
|--------|-------------|
| `begin_poly()` | Start recording the vertices of a polygon. |
| `end_poly()` | Stop recording and store the polygon shape. |
| `get_poly()` | Return the recorded polygon. |
| `delay(delay=None)` | Set the delay value for screen updates. |
| `window_width()` | Return the width of the turtle window. |
| `window_height()` | Return the height of the turtle window. |
| `getcanvas()` | Return the Canvas object of the turtle window. |
| `getscreen()` | Return the TurtleScreen object. |

### Additional Notes

- **`Screen()` Object Methods**: The `Screen` object returned by `turtle.Screen()` has many methods for window and event control, such as `bgcolor`, `title`, `onkey`, `onscreenclick`, and `listen`.
- **Aliases**: Many methods have shorthand aliases (e.g., `fd` for `forward`, `bk` for `backward`).
  
This list provides a solid foundation for creating various Turtle Graphics applications in Python.

