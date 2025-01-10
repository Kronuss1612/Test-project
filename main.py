from snake import Snake
from apple import Apple
from map import Map

FPS = 24

if __name__ == '__main__':

    map = Map(36)

    snake = Snake(4)

    apple = Apple(nutrition = 1)

    map.draw()

    apple.draw()

    snake.draw()

    #loop until closed
    #show map, show snake and move snake grow snake, spawn apple and despawn when eaten 