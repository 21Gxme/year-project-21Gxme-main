from App import App
from hp_data import hp_data


class FacadeController:
    def __init__(self):
        self.hp_data = hp_data()
        self.app = None

    def run(self):
        self.app = App()
        self.app.root.mainloop()

    def get_house_data(self, house):
        return self.hp_data.get_house_data(house)

    def find_age(self, name):
        return self.hp_data.find_age(name)

