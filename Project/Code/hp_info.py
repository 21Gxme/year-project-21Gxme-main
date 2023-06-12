import pandas as pd


class hp_info:
    def __init__(self):
        """Initialize the class."""
        self.df_cha = pd.read_csv(
            '../Harry_Potter_Movies/shortversioncharacters.csv')
        self.df_po = pd.read_csv('../Harry_Potter_Movies/Potions.csv')
        self.df_sp = pd.read_csv('../Harry_Potter_Movies/Spells.csv')
        self.name = self.df_cha['name']
        self.potion = self.df_po['Name']
        self.spell = self.df_sp['Name']

    def get_name(self):
        return self.name

    def name_in_list(self):
        return self.name.to_list()

    def get_potion(self):
        return self.potion

    def potion_in_list(self):
        return self.potion.to_list()

    def get_spell(self):
        return self.spell

    def spell_in_list(self):
        return self.spell.to_list()

    def character_name(self):
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

    def potion_name(self):
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

    def spell_name(self):
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

    def get_potions_data(self, Name_of_potion):
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
