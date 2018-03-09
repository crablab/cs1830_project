class GameState:
    def __init__(self,intro,main):
        self.intro=intro
        self.main=main
    def introToMain(self):
        self.intro=False
        self.main=True
    def mainToIntro(self):
        self.main=False
        self.intro=True

    def encode(self):
        dict={'idClass': 10, 'intro': self.intro, 'main': self.main}
        return dict