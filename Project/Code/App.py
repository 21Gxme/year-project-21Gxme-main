from io import BytesIO
from tkinter import *
from hp_data import *
from hp_info import *
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import requests
import datetime as dt


class App(hp_data):
    """
    Define the main user interface class.
    """

    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.df_for_graph = None
        self.display_frame = tk.LabelFrame(self.root, text="Display")
        self.menu_frame = tk.LabelFrame(self.root, text="Menu")
        self.root.title("Harry Potter")
        self.root.geometry("1200x675")
        self.root.resizable(False, False)
        self.display_frame.pack(fill="both", expand=True, side="left",
                                padx=5, pady=5)
        self.menu_frame.pack(fill="both", expand=True, side="right",
                             padx=5, pady=5)
        self.menu()

    def menu(self):
        """ Create a menu button allowing the user to select what they want."""
        menu_button = tk.Menubutton(self.menu_frame, text="Select menu")
        menu_button.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_list = tk.Menu(menu_button, tearoff=0)
        menu_button["menu"] = menu_list
        menu_list.add_command(label="Information", command=self.info)
        menu_list.add_command(label="Plot graph", command=self.plot_graph)
        menu_list.add_separator()
        menu_list.add_command(label="Exit", command=self.root.destroy)

    def reset_button(self):
        """ Create a reset button to reset the table."""
        reset_button = tk.Button(self.menu_frame, text="Reset",
                                 command=self.reset_display, width=10)
        reset_button.grid(row=10, column=0, padx=5, pady=10, sticky=tk.EW)

    def reset_display(self):
        """ Reset the display frame."""
        for clear in self.display_frame.winfo_children():
            clear.destroy()
        self.menu()

    def clear_menu_frame(self):
        """ Remove all widgets from the menu frame."""
        for clear in self.menu_frame.winfo_children():
            clear.destroy()
        self.menu()

    def plot_graph(self):
        """Create a UI that allows users to select the data they want
        to visualize."""
        self.clear_menu_frame()
        msg = Label(self.menu_frame,
                    text="Select the data you want to visualize.")
        msg.grid(row=1, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_graph = tk.Menubutton(self.menu_frame, text="Select menu")
        menu_graph.grid(row=2, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_list = tk.Menu(menu_graph, tearoff=0)
        menu_graph["menu"] = menu_list
        menu_list.add_command(label="Part to whole",
                              command=self.button_piechart)
        menu_list.add_command(label="Distribution",
                              command=self.button_distribution)
        menu_list.add_command(label="Time series",
                              command=self.button_timeseries)
        menu_list.add_command(label="Scatter", command=self.button_scatter)
        menu_list.add_separator()
        menu_list.add_command(label="Description",
                              command=self.button_description)
        self.reset_button()

    def info(self):
        """Create a UI that allows users to select the data they want
        to visualize."""
        self.clear_menu_frame()
        msg = Label(self.menu_frame,
                    text="Select topic what do you want to know.")
        msg.grid(row=1, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_info = tk.Menubutton(self.menu_frame, text="Select topic")
        menu_info.grid(row=2, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_list = tk.Menu(menu_info, tearoff=0)
        menu_info["menu"] = menu_list
        menu_list.add_command(label="Character", command=self.button_character)
        menu_list.add_command(label="Potion", command=self.button_potion)
        menu_list.add_command(label="Spell", command=self.button_spell)
        self.reset_button()

    def button_character(self, ):
        """Create a UI that allows users to select the data they want
        to visualize."""
        self.reset_display()
        msg = Label(self.menu_frame,
                    text="Select character what do you want to know.")
        msg.grid(row=3, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_info = tk.Menubutton(self.menu_frame, text="Select character")
        menu_info.grid(row=4, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_list = tk.Menu(menu_info, tearoff=0)
        menu_info["menu"] = menu_list
        list_of_cha = hp_info().character_name()
        for cha in list_of_cha:
            menu_list.add_command(label=cha["name"], command=lambda
                character=cha: self.display_character(character))
        self.reset_button()

    def button_potion(self):
        """Create a UI that allows users to select the data they want to
        visualize."""
        self.reset_display()
        msg = Label(self.menu_frame,
                    text="Select potion what do you want to know.")
        msg.grid(row=3, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_info = tk.Menubutton(self.menu_frame, text="Select potion")
        menu_info.grid(row=4, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_list = tk.Menu(menu_info, tearoff=0)
        menu_info["menu"] = menu_list
        list_of_potion = hp_info().potion_name()
        for potion in list_of_potion:
            menu_list.add_command(label=potion["Name"],
                                  command=lambda
                                      potion=potion: self.display_potion(
                                      potion))
        self.reset_button()

    def button_spell(self):
        """Create a UI that allows users to select the data they want to
        visualize."""
        self.reset_display()
        msg = Label(self.menu_frame,
                    text="Select spell what do you want to know.")
        msg.grid(row=3, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_info = tk.Menubutton(self.menu_frame, text="Select spell")
        menu_info.grid(row=4, column=0, padx=5, pady=5, sticky=tk.EW)
        menu_list = tk.Menu(menu_info, tearoff=0)
        menu_info["menu"] = menu_list
        list_of_spell = hp_info().spell_name()
        for spell in list_of_spell:
            menu_list.add_command(label=spell["Name"],
                                  command=lambda
                                      spell=spell: self.display_spell(
                                      spell))
        self.reset_button()

    def display_potion(self, potion):
        """Display the selected potion."""
        self.reset_display()
        name_label = Label(self.display_frame, text="Name: ",
                           font=("Monospace", 16, "bold"))
        name_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.EW)
        name_potion = Label(self.display_frame, text=f"{potion['Name']}",
                            font=("Monospace", 16))
        name_potion.grid(row=0, column=1, padx=5, pady=10, sticky=tk.EW)
        ingredients_label = Label(self.display_frame, text="Ingredients: ",
                                  font=("Monospace", 16, "bold"))
        ingredients_label.grid(row=1, column=0, padx=5, pady=10, sticky=tk.EW)
        ingredients_potion = Label(self.display_frame,
                                   text=f"{potion['Known ingredients']}",
                                   font=("Monospace", 16))
        ingredients_potion.grid(row=1, column=1, padx=5, pady=10, sticky=tk.EW)
        effect_label = Label(self.display_frame, text="Effect: ",
                             font=("Monospace", 16, "bold"))
        effect_label.grid(row=2, column=0, padx=5, pady=10, sticky=tk.EW)
        effect_potion = Label(self.display_frame, text=f"{potion['Effect']}",
                              font=("Monospace", 16))
        effect_potion.grid(row=2, column=1, padx=5, pady=10, sticky=tk.EW)
        characteristics_label = Label(self.display_frame,
                                      text="Characteristics: ",
                                      font=("Monospace", 16, "bold"))
        characteristics_label.grid(row=3, column=0, padx=5, pady=10,
                                   sticky=tk.EW)
        characteristics_potion = Label(self.display_frame,
                                       text=f"{potion['Characteristics']}",
                                       font=("Monospace", 16))
        characteristics_potion.grid(row=3, column=1, padx=5, pady=10,
                                    sticky=tk.EW)
        difficulty_label = Label(self.display_frame, text="Difficulty: ",
                                 font=("Monospace", 16, "bold"))
        difficulty_label.grid(row=4, column=0, padx=5, pady=10, sticky=tk.EW)
        difficulty_potion = Label(self.display_frame,
                                  text=f"{potion['Difficulty level']}",
                                  font=("Monospace", 16))
        difficulty_potion.grid(row=4, column=1, padx=5, pady=10, sticky=tk.EW)
        self.reset_button()

    def display_spell(self, spell):
        """Display the selected spell."""
        self.reset_display()
        name_label = Label(self.display_frame, text="Name: ",
                           font=("Monospace", 16, "bold"))
        name_label.grid(row=0, column=0, padx=5, pady=10, sticky=tk.EW)
        name_spell = Label(self.display_frame, text=f"{spell['Name']}",
                           font=("Monospace", 16))
        name_spell.grid(row=0, column=1, padx=5, pady=10, sticky=tk.EW)
        Incantation_label = Label(self.display_frame, text="Incantation: ",
                                  font=("Monospace", 16, "bold"))
        Incantation_label.grid(row=1, column=0, padx=5, pady=10, sticky=tk.EW)
        Incantation_spell = Label(self.display_frame,
                                  text=f"{spell['Incantation']}",
                                  font=("Monospace", 16))
        Incantation_spell.grid(row=1, column=1, padx=5, pady=10, sticky=tk.EW)
        Type_label = Label(self.display_frame, text="Type: ",
                           font=("Monospace", 16, "bold"))
        Type_label.grid(row=2, column=0, padx=5, pady=10, sticky=tk.EW)
        Type_spell = Label(self.display_frame, text=f"{spell['Type']}",
                           font=("Monospace", 16))
        Type_spell.grid(row=2, column=1, padx=5, pady=10, sticky=tk.EW)
        Effect_label = Label(self.display_frame, text="Effect: ",
                             font=("Monospace", 16, "bold"))
        Effect_label.grid(row=3, column=0, padx=5, pady=10, sticky=tk.EW)
        Effect_spell = Label(self.display_frame, text=f"{spell['Effect']}",
                             font=("Monospace", 16))
        Effect_spell.grid(row=3, column=1, padx=5, pady=10, sticky=tk.EW)
        Light_label = Label(self.display_frame, text="Light: ",
                            font=("Monospace", 16, "bold"))
        Light_label.grid(row=4, column=0, padx=5, pady=10, sticky=tk.EW)
        Light_spell = Label(self.display_frame, text=f"{spell['Light']}",
                            font=("Monospace", 16))
        Light_spell.grid(row=4, column=1, padx=5, pady=10, sticky=tk.EW)

    def display_character(self, character):
        """Display the selected character."""
        self.reset_display()
        img_url = character['image']
        response = requests.get(img_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((163, 227), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self.display_frame, image=img)
        panel.image = img
        panel.pack()
        name_label = Label(self.display_frame,
                           text=f"Name: {character['name']}",
                           font=("Monospace", 16, "bold"))
        name_label.pack()
        species_label = Label(self.display_frame,
                              text=f"Species: {character['species']}")
        species_label.pack()
        gender_label = Label(self.display_frame,
                             text=f"Gender: {character['gender']}")
        gender_label.pack()
        house_label = Label(self.display_frame,
                            text=f"House: {character['house']}")
        house_label.pack()
        date_of_birth_label = Label(self.display_frame,
                                    text=f"Date of birth: {character['dateOfBirth']}")
        date_of_birth_label.pack()
        ancestry_label = Label(self.display_frame,
                               text=f"Ancestry: {character['ancestry']}")
        ancestry_label.pack()
        patronus_label = Label(self.display_frame,
                               text=f"Patronus: {character['patronus']}")
        patronus_label.pack()
        actor_label = Label(self.display_frame,
                            text=f"Actor: {character['actor']}")
        actor_label.pack()

    def button_piechart(self):
        """Create a button to display the histogram."""
        self.reset_display()
        gryffindor = 0
        slytherin = 0
        ravenclaw = 0
        hufflepuff = 0
        for house in self.df_characters['house']:
            if house == 'Gryffindor':
                gryffindor += 1
            elif house == 'Slytherin':
                slytherin += 1
            elif house == 'Ravenclaw':
                ravenclaw += 1
            elif house == 'Hufflepuff':
                hufflepuff += 1
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        canvas = FigureCanvasTkAgg(figure, self.display_frame)
        houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
        values = [gryffindor, slytherin, ravenclaw, hufflepuff]
        ax.pie(values, labels=houses, autopct='%1.1f%%', startangle=90)
        ax.set_title('Houses')
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def button_timeseries(self):
        """Create a button to display the timeseries."""
        self.reset_display()
        year = self.df_year['Birth'].value_counts()
        year = year.sort_index()
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        canvas = FigureCanvasTkAgg(figure, self.display_frame)
        ax.set_xlim(1900, 2010)
        ax.set_xticks(range(1900, 2011, 10))
        ax.set_xticklabels(range(1900, 2011, 10))
        year.plot(kind='line', ax=ax, title='Year of birth in Harry Potter',
                  xlabel='Year', ylabel='Frequency')
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def button_distribution(self):
        """Create a button to display the distribution."""
        self.reset_display()
        year_counts = self.df_year['Birth']
        current_year = dt.datetime.now().year
        age = current_year - year_counts
        age = age.value_counts().sort_index()
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        canvas = FigureCanvasTkAgg(figure, self.display_frame)
        age.plot(kind='bar', ax=ax, width=0.5, title='Age distribution',
                 xlabel='Age', ylabel='Frequency')
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def button_scatter(self):
        """Create a button to display the scatterplot."""
        self.reset_display()
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        canvas = FigureCanvasTkAgg(figure, self.display_frame)
        budget = self.df_movies["Budget"]
        box_office = self.df_movies["Box Office"]
        ax.scatter(budget, box_office)
        ax.set_title('Budget vs Box office')
        ax.set_xlabel('Budget')
        ax.set_ylabel('Box office')
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def button_description(self):
        """Create a button to display the description."""
        self.reset_display()
        year_list = []
        for year in self.df_year['Birth']:
            year_list.append(year)
        year = pd.Series(year_list)
        maen = int(year.mean())
        median = int(year.median())
        max_year = int(year.max())
        min_year = int(year.min())
        sd = round(year.std(), 2)
        msg = "Description of the year of birth in Harry Potter"
        description = Label(self.display_frame, text=msg,
                            font=("Monospace", 16, "bold"))
        mean_label = Label(self.display_frame, text=f"Mean: {maen}")
        median_label = Label(self.display_frame, text=f"Median: {median}")
        sd_label = Label(self.display_frame, text=f"Standard deviation: {sd}")
        max_year_label = Label(self.display_frame, text=f"Max: {max_year}")
        min_year_label = Label(self.display_frame, text=f"Min: {min_year}")
        Age_list = []
        for year in self.df_year['Birth']:
            Age_list.append(dt.datetime.now().year - year)
        Age = pd.Series(Age_list)
        maen_age = int(Age.mean())
        median_age = int(Age.median())
        sd_age = round(Age.std(), 2)
        max_age = int(Age.max())
        min_age = int(Age.min())
        msg1 = "Description of the age of the characters in Harry Potter"
        description1 = Label(self.display_frame, text=msg1,
                             font=("Monospace", 16, "bold"))
        mean_label1 = Label(self.display_frame, text=f"Mean: {maen_age}")
        median_label1 = Label(self.display_frame, text=f"Median: {median_age}")
        sd_label1 = Label(self.display_frame,
                          text=f"Standard deviation: {sd_age}")
        max_label = Label(self.display_frame, text=f"Max: {max_age}")
        min_label = Label(self.display_frame, text=f"Min: {min_age}")
        description.pack()
        mean_label.pack()
        median_label.pack()
        max_year_label.pack()
        min_year_label.pack()
        sd_label.pack()
        description1.pack()
        mean_label1.pack()
        median_label1.pack()
        max_label.pack()
        min_label.pack()
        sd_label1.pack()
