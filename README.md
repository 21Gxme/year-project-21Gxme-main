# Harry Potter Movies
 
## Description
The Harry Potter is a collection of various types of data related to the popular 
book and movie series. A Harry Potter data set project is an exciting opportunity 
to delve into the intricacies of the Wizarding World. The project involves 
cleaning and preparing data related to the characters, spells, potions, budget, 
and box office revenue for each part of the series.


## Data Sources
The data is collected from the following sources:
- [harry-potter-movies-dataset](https://www.kaggle.com/datasets/kornflex/harry-potter-movies-dataset)
- [harry-potter-dataset](https://www.kaggle.com/datasets/maricinnamon/harry-potter-movies-dataset)
 
## Running the Application
- Install the dependencies using the following command:
```bash
install requests
```
```bash
install io
```
```bash
install pandas
```
```bash
install matplotlib
```
```bash
install Pillow
```

- Run the application using the following command:
```bash
python3 main.py
```

## Design
![Diagram.png](Diagram.png)

From the above diagram, the following classes are used:
- FacadeController
- hp_data
- App
- hp_info

![sequence.png](sequence.png)
From the above sequence diagram, the following classes are used:
- FacadeController
- App
which I use to showing when the Distribution button is clicked.
 
## Design Patterns Used
From my project, I have used the following design patterns:
- Facade Pattern

I have used the facade pattern to provide a simple interface to the complex
subsystem of the Harry Potter data set. The facade pattern is used to hide the
complexity of the system and provide a simple interface to the user.

 
## Graph Algorithm Used
Determine who has the most enemies, who has the least enemies, and who is the
friendliest with whom.

Algorithm: 
- WhateverFirstSearch (BFS, DFS)

## Other Information
Interesting in the project:
- matplotlib.backends.backend_tkagg

From this module, I have used the FigureCanvasTkAgg class to display the 
matplotlib figure in the tkinter window.

my class diagram starts from the main.py file main.py will call the FacadeController
class and the FacadeController class will call the App class which inheriting from the
hp_data class and use the hp_info class to get the data.

from my sequence diagram, I have used to showing when the Distribution button is clicked.

and from my facade pattern, I have used to hide the complexity of the system and provide
a simple interface to the user.

Container and widget choices
- tk.Frame use to create a container for other widgets.
- tk.Label use to display text or images.
- tk.Button use to add buttons to the application.
- tk.Menu use to add menus to the application.
- matplotlib.backends.backend_tkagg use to display the matplotlib figure in the tkinter window.
layout design
my layout design is have 2 frame one for the left side and one for the right side
left side frame is for the menu and the button
right side frame is for the graph and the data

Data source(s)
I use 2 data source from kaggle
- harry-potter-movies-dataset
- harry-potter-dataset
