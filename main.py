from snake import Snake
from apple import Apple
from map import Map
from window import Window

FPS = 24

if __name__ == '__main__':

    window = Window()

    map = Map(36, window)

    snake = Snake(4)

    apple = Apple(nutrition = 1)

    map.draw()

    apple.draw()

    snake.draw()

    window.mainloop()

    #loop until game closed
    #show map, show snake and move snake grow snake, spawn apple and despawn when eaten 
    #draw map, spple, snake
    #when snake hits edge of map the snake should come out of the opposite side of that edge but only the parts that went over the edge
    #the snake should die when when moving over one of its own part and a "game over" test should appear
    #The game should show a score (length of the snake) after the game over text and a all time highscore
    #the snake should only move on square and only horizontally and/or vertically the body should follow the movements of the head 1 to 1
    #snake speed move 1 square every 24 frames?
    #Movenemtn wasd or arrow keys both should work