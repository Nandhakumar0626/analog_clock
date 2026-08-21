from tkinter import *
import math
from datetime import datetime


# Window Setup

WIDTH = 600
HEIGHT = 600

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

RADIUS = 250

root = Tk()
root.title("Analog Clock")
root.geometry("600x600")
root.configure(bg="black")
root.resizable(True, True)

canvas = Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="black",
    highlightthickness=0
)
canvas.pack()


# Draw Clock Face

def draw_clock_face():

    canvas.create_oval(
        CENTER_X - RADIUS,
        CENTER_Y - RADIUS,
        CENTER_X + RADIUS,
        CENTER_Y + RADIUS,
        width=5,
        outline="white"
    )

    # Minute Marks
    for i in range(60):

        angle = math.radians(i * 6 - 90)

        outer_x = CENTER_X + RADIUS * math.cos(angle)
        outer_y = CENTER_Y + RADIUS * math.sin(angle)

        if i % 5 == 0:

            inner = RADIUS - 25
            width = 3

        else:

            inner = RADIUS - 12
            width = 1

        inner_x = CENTER_X + inner * math.cos(angle)
        inner_y = CENTER_Y + inner * math.sin(angle)

        canvas.create_line(
            inner_x,
            inner_y,
            outer_x,
            outer_y,
            fill="white",
            width=width
        )

    # Numbers
    for number in range(1, 13):

        angle = math.radians(number * 30 - 90)

        x = CENTER_X + (RADIUS - 50) * math.cos(angle)
        y = CENTER_Y + (RADIUS - 50) * math.sin(angle)

        canvas.create_text(
            x,
            y,
            text=str(number),
            fill="white",
            font=("Arial", 18, "bold")
        )
     
# Draw Clock Hands

def draw_hands():

    now = datetime.now()

    hour = now.hour % 12
    minute = now.minute
    second = now.second

    hour_angle = math.radians((hour + minute / 60) * 30 - 90)
    minute_angle = math.radians(minute * 6 - 90)
    second_angle = math.radians(second * 6 - 90)

    # Hour Hand
    hour_x = CENTER_X + 120 * math.cos(hour_angle)
    hour_y = CENTER_Y + 120 * math.sin(hour_angle)

    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        hour_x,
        hour_y,
        fill="white",
        width=8
    )

    # Minute Hand
    minute_x = CENTER_X + 170 * math.cos(minute_angle)
    minute_y = CENTER_Y + 170 * math.sin(minute_angle)

    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        minute_x,
        minute_y,
        fill="white",
        width=5
    )

    # Second Hand
    second_x = CENTER_X + 200 * math.cos(second_angle)
    second_y = CENTER_Y + 200 * math.sin(second_angle)

    canvas.create_line(
        CENTER_X,
        CENTER_Y,
        second_x,
        second_y,
        fill="red",
        width=2
    )

    # Center Circle
    canvas.create_oval(
        CENTER_X - 8,
        CENTER_Y - 8,
        CENTER_X + 8,
        CENTER_Y + 8,
        fill="white",
        outline="white"
    )



# Update Clock

def update_clock():

    canvas.delete("all")

    draw_clock_face()

    draw_hands()

    root.after(1000, update_clock)


# Start Clock

def start_clock():

    canvas.delete("all")

    draw_clock_face()

    draw_hands()

    root.after(1000, start_clock)



# Main Program

start_clock()

root.mainloop()
