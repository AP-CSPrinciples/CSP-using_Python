# 🎮 PyGame: An Introduction

**🔹 What is PyGame?**

**PyGame** is a free, open-source library for Python that helps you build **2D games and multimedia applications**. It has powerful tools that will allow you to use:

   * Graphics and animation
   * Sounds and music
   * User input (keyboard, mouse)
   * Sprites and collisions
   * Game loops and timers


✅ Recommended Python Versions for PyGame
    * Python 3.7 to 3.11 → ✅ Fully supported and stable
        * These are the most commonly used versions with PyGame.
        * PyGame is regularly tested against these versions.
        
✅ **Use PyGame when Turtle isn’t enough** — if you want smoother animation, images, sound, or interactivity, PyGame is a better fit.

---

**🛠 Installation**

Install with pip:

```bash
pip install pygame
```

If you're using a specific Python version:

```bash
python3.11 -m pip install pygame
```

**🔍 Check Compatibility with Your Python Version**

Run this in your terminal or Python shell:

```python
import pygame
print(pygame.ver)
print(pygame.get_sdl_version())
```


🔗 [Official Guide](https://www.pygame.org/wiki/GettingStarted)



**🧱 PyGame Basics**

**Initial Setup**

```python
import pygame
pygame.init()
```

**Create a Window**

```python
width, height = 500, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Game")
```

**Main Game Loop**

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
```



**🖼 Drawing & Displaying Graphics**

**Background Images**

```python
bg = pygame.transform.smoothscale(pygame.image.load("bg.jpg"), (width, height))
window.blit(bg, (0, 0))  # Draw background at (0,0)
```

**Display Update**

```python
pygame.display.update()  # Refreshes screen
```

⛔ Forgetting to call `blit()` or `update()` will result in no visible changes!

---

**🧍 Working with Sprites (Player, Objects)**

**Load and Resize**

```python
player = pygame.transform.smoothscale(pygame.image.load("player.png"), (100, 100))
```

**Draw (Blit) to Screen**

```python
window.blit(player, (player_x, player_y))
```

> Blit your background **before** your player or the player will disappear!



**🕹 Keyboard Input & Movement**

```python
def movement():
    keys = pygame.key.get_pressed()
    global player_x, player_y
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5
```

Inside your main loop, call `movement()` before updating the display.



**🍎 Project: Apple Collect Starter**

You can use the code below to create an interactive game:

```python
import pygame
pygame.init()

width, height = 500, 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Apple Collect")

bg = pygame.transform.smoothscale(pygame.image.load("bg.jpg"), (width, height))
player = pygame.transform.smoothscale(pygame.image.load("player.png"), (100, 100))
apple = pygame.transform.smoothscale(pygame.image.load("apple.png"), (50, 50))

player_x, player_y = 200, 200

def movement():
    keys = pygame.key.get_pressed()
    global player_x, player_y
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

running = True
while running:
    window.blit(bg, (0, 0))
    movement()
    window.blit(player, (player_x, player_y))
    window.blit(apple, (100, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
```



**🧠 Intermediate Topics**

**🎯 Collision Detection**

```python
player_rect = pygame.Rect(player_x, player_y, 100, 100)
apple_rect = pygame.Rect(100, 100, 50, 50)

if player_rect.colliderect(apple_rect):
    print("Apple Collected!")
```

**📦 Using Classes for Sprites**

```python
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
```



### 🔥 Advanced Topics

**🎵 Adding Sound**

```python
pygame.mixer.init()
collect_sound = pygame.mixer.Sound("collect.wav")
collect_sound.play()
```

**🎲 Random Placement**

```python
import random
apple_x = random.randint(0, 450)
apple_y = random.randint(0, 450)
```

**⏱ Frame Rate Control**

```python
clock = pygame.time.Clock()
clock.tick(60)  # Limit to 60 frames per second
```

**📚 Organizing Code into Modules**

Split code into:

* `main.py`
* `player.py`
* `utils.py`

**🧪 Leveling Up Projects**

Encourage students to:

* Add timers or scores
* Create multiple levels
* Add enemies
* Track high scores with file I/O



**🧰 Final Tips for Teaching**

* Use visuals for explaining coordinates and layering.
* Show examples of sprite sheets or sprite animations.
* Let students modify assets to personalize their games.
* Use pre-built templates and have them “remix” the code.

