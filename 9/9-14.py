from random import randint


class Dies:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print("投掷10次"+str(self.sides)+"面的骰子")
        for i in range(0, 10):
            print(str(randint(1, self.sides)))


die = Dies()
die.roll_die()
die = Dies(10)
die.roll_die()
die = Dies(20)
die.roll_die()

