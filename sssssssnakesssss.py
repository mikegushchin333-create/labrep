class Snake:
    name = 'Python' #атрибут класса
    mouse_eaten_counter = 0
    def voice(self):
        Snake.mouse_eaten_counter += 1
        return "shhh"
    def __init__(self):
        self.mouse_eaten_counter = 0
s1 = Snake()
s2 = Snake()


class Snake:
    arg = 0
    def __str__(self):
        return "some"
s1 = Snake()
print(s1)


class Snake:
    def __init__(self, snake_name, num, snake_age):
        self.name = snake_name
        self.mouse_eaten_counter = num
        self.age = snake_age
s1 = Snake()


class Snake:
    name = 'Python'
    def __init__(self):
        self.mouse_eaten_counter = 0 #атрибут экземпляра
    def voice(self): 
        self.mouse_eaten_counter += 1
        return "shhh"
    @staticmethod
    def sleep():
        return "ZzZzZ"
s1 = Snake()
s2 = Snake()