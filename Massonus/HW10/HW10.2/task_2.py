import random


class Ghost(object):
    def __init__(self):
        match random.randint(1, 4):
            case 1:
                self.color = 'red'
            case 2:
                self.color = 'yellow'
            case 3:
                self.color = 'purple'
            case 4:
                self.color = 'white'
