#TP5 Arcade Mehdi Serge Lavoie 406
import arcade
IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 1024
IMAGE_TITLE = "Beautiful House With Sun"


def draw_background():
    # Le ciel
    arcade.draw_lrtb_rectangle_filled(0, IMAGE_WIDTH, IMAGE_HEIGHT,
                                      IMAGE_HEIGHT * (1 / 3), arcade.color.SKY_BLUE)
    # La terre
    arcade.draw_lrtb_rectangle_filled(0, IMAGE_WIDTH, IMAGE_HEIGHT / 3, 0, arcade.color.DARK_SPRING_GREEN)

def draw_maison(x, y):
    arcade.draw_rectangle_filled(center_x = x,center_y = y,
                                width=300, height=y-200 ,
                                color = arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(x-150,y + (y-200)/2, x+150,y +(y-200)/2, x,y + 300, color=arcade.color.YELLOW)

def draw_sun(x, y):
    radius = 75
    arcade.draw_circle_filled(x, y, radius, arcade.color.AMBER)
    # Soleil (Rayon)
    arcade.draw_line(x, y, x - 100, y, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x + 100, y, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x, y + 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x, y - 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x + 100, y + 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x + 100, y - 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x - 100, y + 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x - 100, y - 100, arcade.color.AMBER, 3)


def draw_cloud(x, y):
    #Cloud
    arcade.draw_ellipse_filled(x - 50, y, x / 20 * 3, 35, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(x + 50, y, x / 20 * 3, 35, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(x + 150, y, x / 20 * 3, 35, arcade.csscolor.WHITE)



def main():
    arcade.open_window(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_TITLE)
    arcade.start_render()

    # Arriere plan
    draw_background()

    #Soleil
    draw_sun(130, 900)

    #Nuage
    draw_cloud(700, 900)

    draw_maison(500, 400)


    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()

