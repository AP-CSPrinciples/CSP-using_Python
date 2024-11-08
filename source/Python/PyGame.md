# PyGame Basics

## Pygame
Pygame is a free and open-source Python library used for creating 2D video games. It provides modules to handle graphics, sound, user input, and more.

### Why Pygame instead of Turtle?

Pygame is commonly used to create AP CSP performance tasks. Pygame allows you to add features like images, sound, and animations, making your project more interactive and polished. By using Pygame, your project will have better graphics and functionality, allowing you to showcase your creativity to your potential.

## Pygame Installation
Official Pygame Installation Guide:
[https://www.pygame.org/wiki/GettingStarted]

- If theres any trouble, there are many youtube tutorials on Pygame Installation.
- If theres still trouble, consider asking ChatGPT or Mr.Virak for help. 

## Pygame Basics

This section will teach you some important parts of Pygame. It will also teach you how to create a basic moving game with points called "Apple Collect".

### Before you Start

This command must be called whenever you want to put something on the screen.

```python

pygame.init()
#initializes the Pygame library

window.blit(bg, (0,0))

#window is the main Pygame Window 
#bg is an object to be rendered
# (0,0) are the (x,y) coordinates

```
**Important**: The order how you blit each imagine matters. (blitting x before y will be different from blitting y before x)

 However, in order to actually render the object on the screen:

```python

pygame.display.update()

```
**Tip**: This command should always be present in the end of the Pygame Main Loop

## Pygame Window

Pygame has the ability to create a window. This window will contain all the visual graphics of your game.

```python

height = 500
length = 500

window = pygame.display.set_mode((length, height))
pygame.display.set_caption("Example Game")

```

This Code will create a window 500 pixel by 500 pixel black screen with the title of "Example Game".

#### Pygame Window Customization

You may also set the background to a certain image or color. 

```python

bg = pygame.transform.smoothscale(pygame.image.load("bg.jpeg"), (length, height))

#pygame.transform.smoothscale() will scale any image to any size
#pygame.image.load("bg.jpeg") will load the bg.jpeg
#(length, height) will the the target size of the image

```
**Tip**: Pygame can load many image types. However, jpeg and png work the best.

**Debugging**: Make sure that the image you're trying to load is in the same folder as the code. 
**Debugging**: Don't forget to blit the object!

Pygame uses a large while True loop in order to keep the game running. Below is an example of such loop:

```python
# PyGame Main Loop

keepGameRunning = True

while keepGameRunning:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          keepGameRunning = False

      pygame.display.update()
```
Pygame has many prebuilt events, (such as button pressing) and this loop, in order to not be an infinite loop, checks if the user has clicked on the red X on the top left of the Pygame Window.


### Apple Collect 

```python

import pygame

pygame.init()

height = 500
length = 500

window = pygame.display.set_mode((length, height))
pygame.display.set_caption("Apple Collect")

bg = pygame.transform.smoothscale(pygame.image.load("bg.jpeg"), (length, height))

keepGameRunning = True

while keepGameRunning:

    window.blit(bg, (0, 0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          keepGameRunning = False

      pygame.display.update()

```

### Pygame Sprites 

Using similar logic as creating the background, we can create a custom image on top the the background:

```python

player = pygame.transform.smoothscale(pygame.image.load("player.png"), (100, 100))

#scales and image called "player.png" to 100 by 100 pixels 
```
**Tip**: Make sure to blit the player AFTER the background!

#### Moving the sprite

Pygame can track user's input. For example, pygame can identify when the user is pressing the up arrow on they keyboard. We can use this functionality in order to create some basic movement for the sprite. 

```python

keys = pygame.key.get_pressed()
#Creates a variable "keys" that will check what button the player is pressing

```

