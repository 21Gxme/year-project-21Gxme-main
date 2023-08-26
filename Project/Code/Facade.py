from App import App
from hp_data import hp_data



class FacadeController:
    def __init__(self) -> None:
        """
        The code defines a class with methods to retrieve house data and find the age of a person.
        """
        self.hp_data = hp_data()
        self.app = None

    def run(self) -> None:
        """
        The function creates an instance of the App class and runs its main loop.
        """
        self.app = App()
        self.app.root.mainloop()

    def get_house_data(self, house) -> any:
        """
        The function "get_house_data" returns the data for a specific house.
        
        :param house: The "house" parameter is the identifier or name of the house for which you want to
        retrieve the data
        :return: the house data for the specified house.
        """
        return self.hp_data.get_house_data(house)

    def find_age(self, name: str) -> any:
        """
        The function "find_age" returns the age of a person given their name.
        
        :param name: The name parameter is the name of the person whose age you want to find
        :return: The find_age method is returning the age of the person with the given name.
        """
        return self.hp_data.find_age(name)

