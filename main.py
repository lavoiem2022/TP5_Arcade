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

def text(x, y):
    arcade.draw_text("Mehdi Serge Insane Project !!!", 700, IMAGE_HEIGHT - 500, arcade.color.PURPLE_HEART)

def draw_cloud(x, y):
    #Cloud
    arcade.draw_ellipse_filled(x - 50, y, x / 20 * 3, 35, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(x + 50, y, x / 20 * 3, 35, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(x + 150, y, x / 20 * 3, 35, arcade.csscolor.WHITE)

def draw_grass(x, y):
    points = [(928, 170.7), (928, 256), (896, 256), (896, 298.7), (864, 298.7), (851.2, 213.3), (812.8, 213.3), (800, 256),
              (774.4, 256), (761.6, 298.7), (729.6, 256), (704, 256), (691.2, 291.1), (678.4, 256), (659.2, 221.9), (640, 256),
              (640, 170.7)]
    arcade.draw_polygon_filled(points, arcade.color.BUD_GREEN)
    points1 = [(460, 85), (460, 128), (490, 128), (450, 149), (432, 148), (425, 108), (406, 100),
              (400, 128),
              (360, 128), (380, 149), (360, 128), (352, 128), (350, 140), (339, 128), (328, 111),
              (320, 128),
              (320, 85)]
    arcade.draw_polygon_filled(points1, arcade.color.BUD_GREEN)


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

    draw_grass(500,350)

    text(1024, 600)



    arcade.finish_render()
    arcade.run()


if __name__ == "__main__":
    main()

