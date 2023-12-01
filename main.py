# This file was created by: Roan Kher, Matthew Suh, and Jack Gately
# Sources: Chris Bradfield, reviewed and optimized by ChatGPT


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


def on_fantasy_button_click():
    label.config(text="Stats!", font=border_font, bg="White")
    projections_button.place(x=150, y=100)
    stats_button.place_forget()
    search_entry.place(x=800, y=50)  # Adjust x and y coordinates for the search bar
    create_fantasy_boxes()
    label.after(3000, reset_label_text2)


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
    box_texts = ["Points", "Passing", "Rushing", "FG", "Points Allowed", "Pass TD Allowed", "Rush TD Allowed"]
    for i, text in enumerate(box_texts):
        box = tk.Label(window, text=text, font=button_font, bg="light gray", width=15, height=2)
        box.place(x=50, y=200 + i * 50)  # Adjust the y-coordinate to position the boxes


def destroy_fantasy_boxes():
    for widget in window.winfo_children():
        if "label" in str(widget):
            widget.destroy()


# Create the main window
window = tk.Tk()
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
