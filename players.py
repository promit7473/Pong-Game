from turtle import Screen as Screen2


class Players:
    def __init__(self):
        self.screen2 = Screen2()
        self.screen2.setup(800, 600)
        self.player_1 = self.screen2.textinput("Name of Player 1", "Enter Your Name: ")
        self.player_2 = self.screen2.textinput("Name of Player 2", "Enter Your Name: ")
