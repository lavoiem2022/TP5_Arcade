import arcade
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
WINDOW_TITLE = "Je suis Arcane"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
arcade.set_background_color(arcade.color.SKY_BLUE)
arcade.start_render()


arcade.draw_lrtb_rectangle_filled(
    0,
    SCREEN_WIDTH, SCREEN_HEIGHT / 4,
    0,
    arcade.csscolor.DARK_GOLDENROD)

arcade.finish_render()
arcade.run()


