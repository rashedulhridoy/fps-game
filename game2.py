from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Load a basic environment
ground = Entity(model='plane', texture='grass', collider='box', scale=(50, 1, 50))

# Player setup
player = FirstPersonController()

# Gun model (ensure you have a valid gun.png for texture)
gun = Entity(
    model='quad',  # A flat 2D surface
    texture='gun.png',  # Your gun image
    scale=(0.7, 0.5),  # Bigger size
    position=(0.5, -0.4, 0.9),  # Adjusted position
    rotation=(0, -5, -5),  # Fixed angle for a better view
    parent=camera  # Attach it to the camera
)

# List to store enemies
enemies = []

# Function to spawn enemies with an 'enemy.png' texture
def spawn_enemy():
    enemy = Entity(model='quad', texture='enemy.png', scale=(1, 2), 
                   position=(random.randint(-10, 10), 1, random.randint(-10, 10)), 
                   collider='box')
    enemies.append(enemy)

def update():
    # Shooting mechanic with a single target
    if held_keys['left mouse']:
        shoot_range = 15  # Set shooting range
        
        # Raycasting from player's position forward
        hit_info = raycast(player.position, player.forward, distance=shoot_range, ignore=[player])

        if hit_info.hit and hit_info.entity in enemies:
            enemies.remove(hit_info.entity)  # Remove enemy from list
            destroy(hit_info.entity)  # Destroy the enemy in the game

# Function to handle input
def input(key):
    if key == 'escape':  # Exit the game if Esc is pressed
        application.quit()

# Spawn some enemies
for _ in range(10):
    spawn_enemy()

app.run()
