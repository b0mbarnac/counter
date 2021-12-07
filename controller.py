from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.man()

    def click_decr(self):
        self.model.decr()
        return self.model.get_count()

    def click_incr(self):
        self.model.incr()
        return self.model.get_count()
