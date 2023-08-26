import pandas as pd


class hp_info:
    def __init__(self) -> None:
        """
        The function initializes three dataframes by reading CSV files and assigns specific columns to
        variables.
        """
        self.df_cha = pd.read_csv(
            '../Harry_Potter_Movies/shortversioncharacters.csv')
        self.df_po = pd.read_csv('../Harry_Potter_Movies/Potions.csv')
        self.df_sp = pd.read_csv('../Harry_Potter_Movies/Spells.csv')
        self.name = self.df_cha['name']
        self.potion = self.df_po['Name']
        self.spell = self.df_sp['Name']

    def get_name(self) -> any:
        """
        The function `get_name` returns the name attribute of an object.
        :return: The name attribute of the object.
        """
        return self.name

    def name_in_list(self) -> any:
        """
        The function `name_in_list` returns the name attribute of an object as a list.
        :return: The method `name_in_list` is returning the `name` attribute as a list.
        """
        return self.name.to_list()

    def get_potion(self) -> any:
        """
        The function returns the value of the "potion" attribute.
        :return: The method `get_potion` is returning the value of the attribute `self.potion`.
        """
        return self.potion

    def potion_in_list(self) -> any:
        """
        The function returns a list representation of the potion.
        :return: The method `potion_in_list` is returning the result of calling the `to_list` method on
        the `self.potion` object.
        """
        return self.potion.to_list()

    def get_spell(self) -> any:
        """
        The function returns the value of the "spell" attribute.
        :return: The `get_spell` method is returning the value of the `spell` attribute.
        """
        return self.spell

    def spell_in_list(self) -> any:
        """
        The function returns the elements of the "spell" attribute as a list.
        :return: The method `spell_in_list` is returning the `spell` attribute converted to a list.
        """
        return self.spell.to_list()

    def character_name(self) -> list:
        """
        The function `character_name` creates a list of dictionaries containing information about
        characters, with default values for missing data.
        :return: a list of dictionaries, where each dictionary represents a character. Each dictionary
        contains information about the character's name, species, gender, house, date of birth,
        ancestry, patronus, actor, and image.
        """
        data = []
        for i in range(len(self.df_cha)):
            character = {}
            row = self.df_cha.iloc[i]
            character['name'] = row['name'] if not pd.isnull(
                row['name']) else 'unknown'
            character['species'] = row['species'] if not pd.isnull(
                row['species']) else 'unknown'
            character['gender'] = row['gender'] if not pd.isnull(
                row['gender']) else 'unknown'
            character['house'] = row['house'] if not pd.isnull(
                row['house']) else 'unknown'
            character['dateOfBirth'] = row['dateOfBirth'] if not pd.isnull(
                row['dateOfBirth']) else 'unknown'
            character['ancestry'] = row['ancestry'] if not pd.isnull(
                row['ancestry']) else 'unknown'
            character['patronus'] = row['patronus'] if not pd.isnull(
                row['patronus']) else 'unknown'
            character['actor'] = row['actor'] if not pd.isnull(
                row['actor']) else 'unknown'
            character['image'] = row['image'] if not pd.isnull(
                row['image']) else 'unknown'
            data.append(character)
        return data

    def potion_name(self) -> list:
        """
        The function `potion_name` creates a list of dictionaries containing information about potions,
        with default values of 'unknown' for any missing data.
        :return: a list of dictionaries, where each dictionary represents a potion. Each dictionary
        contains information about the potion, such as its name, known ingredients, effect,
        characteristics, and difficulty level.
        """
        data = []
        for i in range(len(self.df_po)):
            potion = {}
            row = self.df_po.iloc[i]
            potion['Name'] = row['Name'] if not pd.isnull(
                row['Name']) else 'unknown'
            potion['Known ingredients'] = row['Known ingredients'] if not pd.isnull(
                row['Known ingredients']) else 'unknown'
            potion['Effect'] = row['Effect'] if not pd.isnull(
                row['Effect']) else 'unknown'
            potion['Characteristics'] = row['Characteristics'] if not pd.isnull(
                row['Characteristics']) else 'unknown'
            potion['Difficulty level'] = row['Difficulty level'] if not pd.isnull(
                row['Difficulty level']) else 'unknown'
            data.append(potion)
        return data

    def spell_name(self) -> list:
        """
        The function `spell_name` takes a DataFrame `self.df_sp` and creates a list of dictionaries
        containing information about spells, with default values of 'unknown' for missing data.
        :return: a list of dictionaries, where each dictionary represents a spell. Each dictionary
        contains the spell's name, incantation, type, effect, and light. If any of these values are
        missing in the original data, the function replaces them with the string 'unknown'.
        """
        data = []
        for i in range(len(self.df_sp)):
            spell = {}
            row = self.df_sp.iloc[i]
            spell['Name'] = row['Name'] if not pd.isnull(
                row['Name']) else 'unknown'
            spell['Incantation'] = row['Incantation'] if not pd.isnull(
                row['Incantation']) else 'unknown'
            spell['Type'] = row['Type'] if not pd.isnull(
                row['Type']) else 'unknown'
            spell['Effect'] = row['Effect'] if not pd.isnull(
                row['Effect']) else 'unknown'
            spell['Light'] = row['Light'] if not pd.isnull(
                row['Light']) else 'unknown'
            data.append(spell)
        return data

    def get_potions_data(self, Name_of_potion) -> dict:
        """
        The function `get_potions_data` retrieves data about a potion based on its name.
        
        :param Name_of_potion: The parameter "Name_of_potion" is the name of the potion for which you
        want to retrieve the data
        :return: a dictionary containing information about a potion. The dictionary has keys for 'Name',
        'Known ingredients', 'Effect', 'Characteristic', and 'Difficulty level'. The values for these
        keys are either the corresponding values from the row in the dataframe that matches the given
        potion name, or the string 'unknown' if the value is missing or the row does not exist.
        """
        data = {
            'Name': None,
            'Known ingredients': None,
            'Effect': None,
            'Characteristic': None,
            'Difficulty level': None
        }
        row = self.df_po.loc[self.df_po['Name'] == Name_of_potion]
        if not row.empty:
            data['Name'] = row.iloc[0]['Name']
            data['Known ingredients'] = row.iloc[0][
                'Known ingredients'] if not pd.isnull(
                row.iloc[0]['Known ingredients']) else 'unknown'
            data['Effect'] = row.iloc[0]['Effect'] if not pd.isnull(
                row.iloc[0]['Effect']) else 'unknown'
            data['Characteristic'] = row.iloc[0][
                'Characteristics'] if not pd.isnull(
                row.iloc[0]['Characteristics']) else 'unknown'
            data['Difficulty level'] = row.iloc[0][
                'Difficulty level'] if not pd.isnull(
                row.iloc[0]['Difficulty level']) else 'unknown'
        else:
            data['Name'] = 'unknown'
            data['Known ingredients'] = 'unknown'
            data['Effect'] = 'unknown'
            data['Characteristic'] = 'unknown'
            data['Difficulty level'] = 'unknown'
        return data
