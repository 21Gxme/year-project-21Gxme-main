import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import datetime as dt


class hp_data:
    def __init__(self) -> None:
        """
        The function initializes several dataframes by reading CSV files related to Harry Potter movies.
        """
        self.df_characters = pd.read_csv(
            "../Harry_Potter_Movies/shortversioncharacters.csv")
        self.df_spells = pd.read_csv("../Harry_Potter_Movies/Spells.csv")
        self.df_movies = pd.read_csv("../Harry_Potter_Movies/Movies.csv")
        self.df_potions = pd.read_csv("../Harry_Potter_Movies/Potions.csv")
        self.df_characters = pd.read_csv("../Harry_Potter_Movies/shortversioncharacters.csv")
        self.df_year = pd.read_csv("../Harry_Potter_Movies/Characters_detail.csv")

    def get_house_data(self, house: str) -> any:
        """Return a dataframe of characters in a house."""
        return self.df_characters.loc[self.df_characters["house"] == house]

    def find_age(self, name: str) -> any:
        """Return the age of a character."""
        return self.df_year.loc[self.df_year["Name"] == name]["Birth"]
