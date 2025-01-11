from apple import Apple
class Snake:
    length: int
    
    def __init__(self,length):
        self.length = length

    def move(self):
        pass

    def eat(self, apple:Apple):
        self.length = self.length + apple.nutrition

    def dead(self):
        #print(Game over)
        #print(self.length)
        pass

    def draw(self):
        pass

