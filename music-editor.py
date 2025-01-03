from tkinter import *
import pygame
import os

# Initialize the main window
root = Tk()
root.title("Music Editor")
root.geometry("500x300")

# Initialize the pygame mixer
pygame.mixer.init()

# Create a menu bar
menubar = Menu(root)
root.config(menu=menubar)

# Add an organize menu to the menu bar
organize_menu = Menu(menubar, tearoff=0)
organize_menu.add_command(label="Open Folder")
organize_menu.add_command(label="Organize")
menubar.add_cascade(label="Organize", menu=organize_menu)

# Create a listbox to display the music files
listbox = Listbox(root, bg="black", fg="white", width=100, height=15)
listbox.pack()

# Load button images
try:
    play_btn_image = PhotoImage(file="play.png")
    pause_btn_image = PhotoImage(file="pause.png")
    next_btn_image = PhotoImage(file="next.png")
    prev_btn_image = PhotoImage(file="prev.png")
    print("Images loaded successfully")
except Exception as e:
    print(f"Error loading images: {e}")

# Create a frame to hold the control buttons
control_panel_frame = Frame(root)
control_panel_frame.pack()

# Add control buttons to the frame
play_button = Button(control_panel_frame, image=play_btn_image, borderwidth=0)
play_button.grid(row=0, column=1, padx=7, pady=10)

pause_button = Button(control_panel_frame, image=pause_btn_image, borderwidth=0)
pause_button.grid(row=0, column=2, padx=7, pady=10)

next_button = Button(control_panel_frame, image=next_btn_image, borderwidth=0)
next_button.grid(row=0, column=3, padx=7, pady=10)

prev_button = Button(control_panel_frame, image=prev_btn_image, borderwidth=0)
prev_button.grid(row=0, column=0, padx=7, pady=10)

# Start the Tkinter main loop
root.mainloop()