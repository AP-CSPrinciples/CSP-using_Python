# 🐢 Python Turtle Graphics — Comprehensive Guide 

The `turtle` module in Python is a **built-in library** that makes it easy to introduce programming to beginners. You control a **"turtle" that moves and draws** on the screen.  It is perfect for learning loops, functions, geometry, and logic through visual feedback.

**🔹 Getting Started**

```python
import turtle

t = turtle.Turtle()  # Create a turtle object
turtle.done()        # Keep the window open at the end
```


**🧠 What Is the "Turtle"?**

The turtle is a cursor (triangle by default) that moves around the screen.

* It can go forward or backward
* Turn right or left
* Draw lines as it moves
* Change shape, color, and size

You control the turtle with **methods**.



**🔑 Common Mistake: `self.forward(100)` ❌**

That only works inside a class. For Turtle, you must use:

```python
t = turtle.Turtle()
t.forward(100)  # ✅
```


### 🔧 Core Turtle Methods by Category

1. 🧭 **Turtle Motion & Positioning**

| Method                          | Description                            |
| ------------------------------- | -------------------------------------- |
| `forward(distance)` or `fd()`   | Move forward                           |
| `backward(distance)` or `bk()`  | Move backward                          |
| `right(angle)` or `rt()`        | Turn right (clockwise)                 |
| `left(angle)` or `lt()`         | Turn left (counterclockwise)           |
| `goto(x, y)` or `setpos()`      | Move to absolute position              |
| `setx(x)` / `sety(y)`           | Set x or y coordinate                  |
| `setheading(angle)` or `seth()` | Face a specific direction in degrees   |
| `home()`                        | Go to (0, 0) and face right            |
| `circle(radius, extent, steps)` | Draw a circle or arc                   |
| `dot(size, color)`              | Draw a dot                             |
| `stamp()`                       | Stamp turtle shape at current location |
| `clearstamp(stampid)`           | Remove a specific stamp                |
| `clearstamps(n)`                | Clear all or last `n` stamps           |
| `undo()`                        | Undo last action                       |
| `speed(0-10)`                   | Set turtle animation speed             |



2. 🧠 **Turtle State & Status**

| Method                  | Description                           |
| ----------------------- | ------------------------------------- |
| `position()` or `pos()` | Current (x, y) position               |
| `xcor()` / `ycor()`     | Get x or y coordinate                 |
| `heading()`             | Get current angle turtle is facing    |
| `towards(x, y)`         | Angle from current position to (x, y) |
| `distance(x, y)`        | Distance to point                     |
| `isdown()`              | Whether pen is down (drawing)         |
| `isvisible()`           | Whether the turtle is visible         |



3. ✍️ **Pen Control (Drawing Tools)**

| Method                               | Description                             |
| ------------------------------------ | --------------------------------------- |
| `penup()` or `pu()`                  | Lift the pen (stop drawing)             |
| `pendown()` or `pd()`                | Lower the pen (start drawing)           |
| `pensize(width)` / `width()`         | Set pen thickness                       |
| `pencolor(color)`                    | Set pen (line) color                    |
| `fillcolor(color)`                   | Set fill color                          |
| `begin_fill()` / `end_fill()`        | Fill shape drawn between these calls    |
| `color(pen, fill)`                   | Set pen and fill color together         |
| `clear()`                            | Clear drawing but keep turtle position  |
| `reset()`                            | Clear everything and reset turtle state |
| `write(text, move=False, align=...)` | Write text on screen                    |



4. 🐢 **Turtle Appearance**

| Method                         | Description                                     |
| ------------------------------ | ----------------------------------------------- |
| `shape(name)`                  | Set turtle shape (e.g., `'turtle'`, `'circle'`) |
| `shapesize(wid, len, outline)` | Stretch turtle's size                           |
| `shearfactor(factor)`          | Tilt shape diagonally                           |
| `tilt(angle)`                  | Tilt shape clockwise                            |
| `showturtle()` or `st()`       | Make turtle visible                             |
| `hideturtle()` or `ht()`       | Hide the turtle                                 |
| `resizemode('auto'/'user')`    | Control size behavior                           |
| `get_shapepoly()`              | Get shape as polygon points                     |



5. 🖼️ **Screen Control & Events**

| Method                               | Description                        |
| ------------------------------------ | ---------------------------------- |
| `Screen()`                           | Get turtle window control object   |
| `bgcolor(color)`                     | Set background color               |
| `bgpic(filename)`                    | Set background image               |
| `title("Window Title")`              | Set window title                   |
| `onclick(func)` / `onkey(func, key)` | Bind click or key event            |
| `listen()`                           | Focus screen to capture keys       |
| `mainloop()` or `done()`             | Start main loop (keep window open) |
| `tracer(n, delay)` / `update()`      | Control animation redraw speed     |
| `bye()`                              | Close turtle window                |



6. 🧩 **Miscellaneous / Advanced**

| Method                               | Description                            |
| ------------------------------------ | -------------------------------------- |
| `begin_poly()`                       | Start recording points for a shape     |
| `end_poly()` / `get_poly()`          | Stop and return polygon                |
| `getcanvas()`                        | Access underlying Tkinter canvas       |
| `getscreen()`                        | Get screen object (same as `Screen()`) |
| `delay(ms)`                          | Set animation delay in milliseconds    |
| `window_width()` / `window_height()` | Get window size                        |



🟢 **Example: Draw a Filled Star**

```python
import turtle

t = turtle.Turtle()
t.color("gold")
t.begin_fill()

for _ in range(5):
    t.forward(100)
    t.right(144)

t.end_fill()
turtle.done()
```



🛑 **Common Pitfalls and Fixes**

| Mistake                                    | Fix                                       |
| ------------------------------------------ | ----------------------------------------- |
| Forgetting `turtle.done()`                 | Window closes immediately after drawing   |
| Using `turtle.forward()` without an object | Use `t = turtle.Turtle()` first           |
| Mixing up `left()` and `right()`           | Practice turning to understand directions |
| Drawing before `pendown()` or `penup()`    | Know when the turtle is supposed to draw  |
| Expecting `char` type in Python            | Use strings of length 1 (e.g., `"A"`)     |



---

