import sys
import tkinter as tk
from random import choice
from PIL import Image, ImageTk
import os


class AkaliSkinChooser:
    def __init__(self, master):
        self.master = master
        self.master.title("Akali Skin Chooser")

        self.bg_color = "#635985"
        self.button_bg_color = "#635985"
        self.button_fg_color = "#18122B"
        self.label_text_color = "#18122B"

        self.skin_options = ["Original Akali", "Stinger Akali", "Silverfang Akali", "Blood Moon Akali",
                             "Headhunter Akali", "Star Guardian Akali", "PROJECT AKALI", "Crime City Nightmare Akali",
                             "Coven Akali", "KDA ALL OUT Akali", "Sashimi Akali", "KDA Akali", "Nurse Akali",
                             "DRX Akali", "Prestige Akali", "All Star Akali", "Infernal Akali", "KDA Akali",
                             "True Damage Akali"]

        self.chromas = {
            "Coven Akali": ["Amethyst", "Catseye", "Destined", "Emerald", "Profane", "Rose Quartz", "Ruby",
                            "Sapphire", "Tanzanite", "Turquoise"],
            "Crime City Nightmare Akali": ["Catseye", "Emerald", "Obsidian", "Pearl", "Rose Quartz", "Ruby",
                                           "Sapphire", "Tanzanite", "Underground"],
            "DRX Akali": ["Elite"],
            "Headhunter Akali": ["Pearl", "Ruby", "Tanzanite"],
            "KDA ALL OUT Akali": ["BADDEST", "Catseye", "Pearl", "Peridot", "Rose Quartz", "Ruby", "Sapphire",
                                  "Tanzanite"],
            "Nurse Akali": ["Amethyst", "Citrine", "Emerald", "Obsidian", "Rainbow", "Rose Quartz", "Ruby",
                            "Tanzanite"],
            "PROJECT Akali": ["Amethyst", "Catseye", "Obsidian", "Pearl", "Reckoning", "Rose Quartz", "Ruby",
                              "Sapphire", "Turquoise"],
            "Star Guardian Akali": ["Brilliant", "Catseye", "Emerald", "Rose Quartz", "Ruby", "Turquoise"],
            "True Damage Akali": ["Catseye", "Emerald", "Freestyle", "Pearl", "Rose Quartz", "Ruby", "Sapphire"],
            "Prestige Akali": ["Base", "2022"],
            "Sashimi Akali": ["Base"],
            "All Star Akali": ["Base"],
            "Infernal Akali": ["Base"],
            "KDA Akali": ["Base"],
            "Original Akali": ["Base"]
        }

        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # PyInstaller --onefile mode
            self.image_path = os.path.join(sys._MEIPASS, "SkinImages")
        else:
            # Regular Python script execution
            self.image_path = "SkinImages"

        self.skin_label = tk.Label(master, text="Selected Skin:", font=("Arial", 12, "bold"), fg=self.label_text_color,
                                   bg=self.bg_color)
        self.skin_label.pack()

        self.image_label = tk.Label(master, bg=self.bg_color)
        self.image_label.pack()

        self.result_label = tk.Label(master, text="", font=("Arial", 10), fg=self.label_text_color, bg=self.bg_color)
        self.result_label.pack()

        self.button = tk.Button(master, text="Roll Skin", command=self.roll_skin, font=("Arial", 12, "bold"),
                                fg=self.button_fg_color, bg=self.button_bg_color)
        self.button.pack()

    def roll_skin(self):
        selected_skin = choice(self.skin_options)

        image_path = os.path.join(self.image_path, f"{selected_skin}.jpeg")

        try:
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except FileNotFoundError:
            self.image_label.config(image=None)

        selected_chroma = choice(self.chromas.get(selected_skin, ["Base"]))
        display_text = f"{selected_skin} ({selected_chroma})"
        self.result_label.config(text=display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = AkaliSkinChooser(root)
    root.configure(bg=app.bg_color)
    root.geometry("1235x831")  # Set the initial window size
    root.resizable(False, False)  # Make the window not resizable
    root.mainloop()
