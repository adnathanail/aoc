import math
from aocd.models import Puzzle
from PIL import Image

puzzle = Puzzle(year=2024, day=14)
input_data = puzzle.input_data
width = 101
height = 103


def step(x, y, dx, dy):
    return ((x + dx) % width, (y + dy) % height)


positions = []
velocities = []
for row in input_data.splitlines():
    pos_str, vel_str = row.split(" ")
    pos = tuple([int(a) for a in pos_str[2:].split(",")])
    vel = tuple([int(a) for a in vel_str[2:].split(",")])
    positions.append(pos)
    velocities.append(vel)


def poss_to_image(poss, output_path):
    # Create a new image with white background
    img = Image.new("RGB", (width, height), color="white")
    pixels = img.load()

    # Fill in black squares for drone positions
    for x, y in poss:
        pixels[x, y] = (0, 0, 0)

    # Save the image
    img.save(output_path)
    print(f"Image saved to {output_path}")


for n in range(1000):
    poss_to_image(positions, f"2024/day14/steps/step_{n}.png")
    for k in range(len(positions)):
        positions[k] = step(positions[k][0], positions[k][1], velocities[k][0], velocities[k][1])


# 6532
