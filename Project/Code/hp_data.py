import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import datetime as dt


class hp_data:
    def __init__(self):
        """Initialize the class."""
        self.df_characters = pd.read_csv(
            "../Harry_Potter_Movies/shortversioncharacters.csv")
        self.df_spells = pd.read_csv("../Harry_Potter_Movies/Spells.csv")
        self.df_movies = pd.read_csv("../Harry_Potter_Movies/Movies.csv")
        self.df_potions = pd.read_csv("../Harry_Potter_Movies/Potions.csv")
        self.df_characters = pd.read_csv("../Harry_Potter_Movies/shortversioncharacters.csv")
        self.df_year = pd.read_csv("../Harry_Potter_Movies/Characters_detail.csv")

    def get_house_data(self, house):
        """Return a dataframe of characters in a house."""
        return self.df_characters.loc[self.df_characters["house"] == house]

    def find_age(self, name):
        """Return the age of a character."""
        return self.df_year.loc[self.df_year["Name"] == name]["Birth"]
