import turtle


def get_mouse_click_coor(x, y):
    print(x , y)


screen = turtle.Screen()
screen.setup(width=800, height=953)
screen.title("India State Games")
image = "india-outline-map.gif"
screen.addshape(image)
turtle.shape(image)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()