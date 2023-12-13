# This file was created by: Roan Kher, Matthew Suh, and Jack Gately
# Sources:
# * [ChatGPT] (https://chat.openai.com/)
# * [Chris Bradfield - KidsCanCode] (https://kidscancode.org/)
# * [WageredOnTilt - YouTuber] (https://www.youtube.com/watch?v=Tuuc6QKchhU&t=417s)
# * [Nick Wan - YouTuber] (https://www.youtube.com/watch?v=3IA0V9UuoPc)
# * [W3Schools - Website] (https://www.w3schools.com/python/pandas/default.asp)
# * [TeamRankings] (https://www.teamrankings.com/nfl/team-stats/)



# Title: 

'''
We realized that we were all passionate about tracking sports scores in real time and we are all involved in fantasy sports in some way. 
We wanted to create an algorithim to predict the future scores of NFL games and stats of the players while also providing the real time scores
We are planning to use different APIs to track scores and use statistical models of linear regression to predict the yard totals of players and the results of games. 
'''
'''
Goals:
Create a predictive NFL sports betting model in python that will provide users with accurate NFL game projections and bets with positive
Expected Value (EV)
Using statistics to predict the best bets on sportsbooks websites. 
Tracking sports scores on different tables and finding links to all the games. 
Importing historical data from website and use it to predict future data

'''
# from python import
from fantasydata import *
# from scoresdata import *

import tkinter as tk
from tkinter import Canvas, Frame, Scrollbar
import pandas as pd



def on_fantasy_button_click():
    label.config(text="Stats!", font=border_font, bg="White")
    projections_button.place(x=150, y=100)
    stats_button.place_forget()
    search_entry.place(x=800, y=50)  # Adjust x and y coordinates for the search bar
    create_fantasy_boxes()
    label.after(3000, reset_label_text2)

    # Loading data into stats page
    load_data_button = tk.Button(window, text="Load Data", command=load_data, font=button_font, width=10, height=3, bg="light blue")
    load_data_button.place(x=50, y=100)  # Adjust coordinates

def reset_label_text2():
    label.config(text="Welcome to Team Statistics", bg="white")


def toggle_column():
    # Add your code here to toggle between different columns
    # For example, switch between 'Name' and 'Value'
    # This is a simple toggle; you can extend it based on your requirements
    current_column = label_var.get()
    
    if current_column == 'Name':
        label_var.set('Value')
    else:
        label_var.set('Name')
    
    update_labels()

def update_labels(event=None):
    current_column = label_var.get()

    # Destroy existing labels and canvas
    for widget in window.winfo_children():
        if isinstance(widget, (tk.Label, Canvas, Scrollbar)):
            widget.destroy()

    # Create a canvas with a scrollbar
    canvas = Canvas(window, width=900, height=600, bg="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(window, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

    

    # Create a frame to hold the labels
    frame = Frame(canvas, bg="white")
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # Update labels based on the current column
    for i, row in enumerate(data.itertuples()):
        label_text = f"{current_column}: {getattr(row, current_column)}"
        label = tk.Label(frame, text=label_text, font=button_font, bg="light gray", width=30, height=2)
        label.grid(row=i, column=0, pady=5)

    # Update the canvas scroll region after adding labels
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))


def load_data():
    # Add your code here to load data from a file
    # For example, use pandas to read a CSV file
    global data
    data = pd.read_csv(r"C:\Users\Matthew.Suh24\Downloads\2023 NFL Model (Data) - NFL Basic Back-End.csv")

    # Update labels or other widgets with the loaded data
    for i, row in enumerate(data.itertuples()):
        label_name = tk.Label(window, text=f"Name: {row[1]}", font=button_font, bg="light gray", width=30, height=2)
        label_value = tk.Label(window, text=f"Value: {row[2]}", font=button_font, bg="light gray", width=30, height=2)

        label_name.place(x=50, y=250 + i * 50)  # Adjust coordinates
        label_value.place(x=250, y=250 + i * 50)  # Adjust coordinates







def reset_label_text2():
    label.config(text="Welcome to Team Statistics", bg="white")


def on_scores_button_click():
    label.config(text="Projections", font=border_font, bg="white")
    stats_button.place(x=50, y=100)
    projections_button.place_forget()
    search_entry.place_forget()
    destroy_fantasy_boxes()
    label.after(3000, reset_label_text)


def reset_label_text():
    label.config(text="Welcome to Projections!", bg="white")


def create_fantasy_boxes():
    box_texts = ["PPG/F", "PASS TD/F", "RUSH TD/F", "FGM/F", "PPG/A", "PASS TD/A", "RUSH TD/A"]
    


def destroy_fantasy_boxes():
    for widget in window.winfo_children():  
        if "label" in str(widget):
            widget.destroy()


# Create the main window
window = tk.Tk()
label_var = tk.StringVar(value='Name')
window.title("My Python Window")
window.geometry("1000x800")

window.configure(bg="white")

button_font = ("Times New Roman", 12, "bold")
border_font = ("Times New Roman", 24, "bold")

# Create Fantasy button widget
stats_button = tk.Button(window, text="Stats", command=on_fantasy_button_click, font=button_font, width=10,
                           height=3, bg="light blue")
stats_button.place(x=50, y=100)  # Adjust x and y coordinates

# Create Game Scores button widget
projections_button = tk.Button(window, text="Projections", command=on_scores_button_click, font=button_font, width=10,
                          height=3, bg="light green")
projections_button.place(x=150, y=100)  # Adjust x and y coordinates

# Create a label widget
label = tk.Label(window, text="Welcome to our website", bg="light blue")
label.pack()



# Create a search bar (entry widget)
search_entry = tk.Entry(window, width=20, font=button_font)
# Adjust the coordinates as needed
search_entry.place(x=800, y=50)

# Start the main event loop
window.mainloop()


