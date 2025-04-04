import tkinter as tk
from tkinter import messagebox
import random
import PIL
from PIL import Image, ImageTk
from io import BytesIO

# Exit button code
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        window.destroy()



# Initialize the main window
window = tk.Tk()
window.title("astroquix")
window.geometry("600x600")


# Fetching the image 
def fetch_image_bg(window, window_width, window_height):
   
    
    image_url = r"C:\Users\BHARGAVI\Desktop\BHARGAVI\space dream💥🌏☀⭐\stsci-h-p2001a-m-2000x1500_0.webp"
 
    bg_image_pil =Image.open((image_url))
    bg_image_pil = bg_image_pil.resize((window_width, window_height), Image.LANCZOS)
    global bg_image

    # Display of the picture as background 
    bg_image = ImageTk.PhotoImage(bg_image_pil)
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

    bg_label.image = bg_image
    window.bind("<Configure>", lambda event: fetch_image_bg(window, window.winfo_width(), window.winfo_height()))


# Quiz data
quiz_data = [
    {
        "question": "What is the name of the process by which stars produce energy?",
        "options": ["Nuclear Fusion", "Nuclear Fission", "Combustion", "Radiation"],
        "correct answer": "Nuclear Fusion"
    },
    {
        "question": "Which planet in our solar system has the longest day (slowest rotation)?",
        "options": ["Mercury", "Venus", "Earth", "Mars"],
        "correct answer": "Venus"
    },
    {
        "question": "What is the name of the boundary around a black hole beyond which nothing can escape?",
        "options": ["Event Horizon", "Singularity", "Photon Sphere", "Accretion Disk"],
        "correct answer": "Event Horizon"
    },
    {
        "question": "What is the name of the largest volcano in the solar system, located on Mars?",
        "options": ["Olympus Mons", "Mauna Kea", "Mount Everest", "Elysium Mons"],
        "correct answer": "Olympus Mons"
    },
    {
        "question": "What is the name of the phenomenon where a star explodes at the end of its life?",
        "options": ["Black Hole", "Supernova", "Nebula", "Pulsar"],
        "correct answer": "Supernova"
    },
    {
        "question": "What is the name of the spacecraft that first landed humans on the Moon?",
        "options": ["Apollo 11", "Voyager 1", "Sputnik 1", "Hubble"],
        "correct answer": "Apollo 11"
    },
    {
        "question": "What is the name of the region in space where gravity is so strong that not even light can escape?",
        "options": ["Neutron Star", "White Dwarf", "Black Hole", "Quasar"],
        "correct answer": "Black Hole"
    },
    {
        "question": "What is the name of the largest moon in the solar system, orbiting Jupiter?",
        "options": ["Titan", "Europa", "Ganymede", "Callisto"],
        "correct answer": "Ganymede"
    },
    {
        "question": "What is the name of the theory that explains the origin of the universe?",
        "options": ["Big Bang Theory", "Steady State Theory", "String Theory", "Relativity Theory"],
        "correct answer": "Big Bang Theory"
    },
    {
        "question": "What is the name of the constellation that contains the North Star (Polaris)?",
        "options": ["Orion", "Ursa Major", "Ursa Minor", "Cassiopeia"],
        "correct answer": "Ursa Minor"
    },
    {
        "question": "What is the name of the galaxy that will collide with the Milky Way in about 4.5 billion years?",
        "options": ["Andromeda", "Triangulum", "Whirlpool", "Sombrero"],
        "correct answer": "Andromeda"
    },
    {
        "question": "What is the name of the first planet discovered using a telescope?",
        "options": ["Uranus", "Neptune", "Saturn", "Jupiter"],
        "correct answer": "Uranus"
    },
    {
        "question": "What is the name of the brightest planet in the night sky?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct answer": "Venus"
    },
    {
        "question": "What is the name of the phenomenon where the Earth passes between the Sun and the Moon, casting a shadow on the Moon?",
        "options": ["Solar Eclipse", "Lunar Eclipse", "Transit", "Aurora"],
        "correct answer": "Lunar Eclipse"
    },
    {
        "question": "What is the name of the spacecraft that explored Pluto in 2015?",
        "options": ["Voyager 1", "New Horizons", "Cassini", "Curiosity"],
        "correct answer": "New Horizons"
    },
    {
        "question": "What is the name of the star at the center of our solar system?",
        "options": ["Sirius", "Alpha Centauri", "Polaris", "Sun"],
        "correct answer": "Sun"
    },
    {
        "question": "What is the name of the largest asteroid in the asteroid belt?",
        "options": ["Ceres", "Vesta", "Pallas", "Eros"],
        "correct answer": "Ceres"
    },
    {
        "question": "What is the name of the phenomenon where charged particles from the Sun interact with Earth's atmosphere, creating colorful lights?",
        "options": ["Aurora", "Supernova", "Meteor Shower", "Solar Flare"],
        "correct answer": "Aurora"
    },
    {
        "question": "What is the name of the first human-made object to leave the solar system?",
        "options": ["Voyager 1", "Pioneer 10", "New Horizons", "Cassini"],
        "correct answer": "Voyager 1"
    },
    {
        "question": "What is the name of the dwarf planet located in the Kuiper Belt?",
        "options": ["Pluto", "Eris", "Haumea", "Makemake"],
        "correct answer": "Pluto"
    },
    {
        "question": "What is the closest star to Sun?",
        "options": ["Proxima Centauri", "Sirius", "Alpha Centauri A", "Barnard's Star"],
        "correct answer": "Proxima Centauri"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct answer": "Mars"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Jupiter", "Saturn", "Neptune"],
        "correct answer": "Jupiter"
    },
    {
        "question": "What is the name of the first artificial satellite launched into space?",
        "options": ["Apollo 11", "Vostok 1", "Sputnik 1", "Explorer 1"],
        "correct answer": "Sputnik 1"
    },
    {
        "question": "What is the name of the phenomenon where the Moon passes between the Earth and the Sun?",
        "options": ["Lunar Eclipse", "Solar Eclipse", "Transit", "Occultation"],
        "correct answer": "Solar Eclipse"
    },
    {
        "question": "Which planet has the most extensive ring system?",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "correct answer": "Saturn"
    },
    {
        "question": "What is the name of the galaxy that contains our solar system?",
        "options": ["Andromeda", "Milky Way", "Whirlpool", "Sombrero"],
        "correct answer": "Milky Way"
    },
    {
        "question": "What is the term for a group of stars that form a recognizable pattern?",
        "options": ["Galaxy", "Cluster", "Constellation", "Nebula"],
        "correct answer": "Constellation"
    },
    {
        "question": "What is the name of the largest moon of Saturn?",
        "options": ["Titan", "Rhea", "Iapetus", "Enceladus"],
        "correct answer": "Titan"
    },
    {
        "question": "What is the name of the force that keeps planets in orbit around the Sun?",
        "options": ["Electromagnetism", "Nuclear Force", "Gravity", "Friction"],
        "correct answer": "Gravity"
    },
    {
        "question": "Which planet is known for its extreme winds and storms?",
        "options": ["Venus", "Mars", "Neptune", "Uranus"],
        "correct answer": "Neptune"
    },
    {
        "question": "What is the term for a small rocky body that orbits the Sun, primarily found in the asteroid belt?",
        "options": ["Asteroid", "Comet", "Meteor", "Planet"],
        "correct answer": "Asteroid"
    },
    {
        "question": "What is the name of the region of space beyond Neptune that contains many small icy bodies?",
        "options": ["Asteroid Belt", "Kuiper Belt", "Oort Cloud", "Heliosphere"],
        "correct answer": "Kuiper Belt"
    },
    {
        "question": "What was the name of the first living creature sent into space?",
        "options": ["Belka", "Laika", "Ham", "Yuri"],
        "correct answer": "Laika"
    },
    {
        "question": "Which Indian space agency is known for its successful Mars Orbiter Mission?",
        "options": ["NASA", "ESA", "ISRO", "Roscosmos"],
        "correct answer": "ISRO"
    },
    {
        "question": "What does NASA stand for?",
        "options": ["National Aeronautics and Space Administration", "National Association of Space Astronauts", "North American Space Agency", "National Aerospace and Science Agency"],
        "correct answer": "National Aeronautics and Space Administration"
    },
    {
        "question": "What is a cubesat?",
        "options": ["A type of large satellite", "A small, cube-shaped satellite", "A satellite used for deep space exploration", "A satellite that orbits the Moon"],
        "correct answer": "A small, cube-shaped satellite"
    },
    {
        "question": "What is the Crab Nebula?",
        "options": ["A type of star", "A planetary nebula", "The remnant of a supernova explosion", "A galaxy"],
        "correct answer": "The remnant of a supernova explosion"
    },
    {
        "question": "Which ISRO satellite was launched to study the Moon?",
        "options": ["Mangalyaan", "Chandrayaan-1", "Astrosat", "GSAT"],
        "correct answer": "Chandrayaan-1"
    },
    {
        "question": "What is the name of the nebula that is famous for its bright colors and is often referred to as the 'Orion Nebula'?",
        "options": ["Horsehead Nebula", "Crab Nebula", "Lagoon Nebula", "Orion Nebula"],
        "correct answer": "Orion Nebula"
    },

]




# Fetch the image background
fetch_image_bg(window,window.winfo_width(), window.winfo_height())

# Global variables
current_question = 0
score = 0
questions_list = random.sample(quiz_data, 10)  # Randomize 10 questions

# Function to check the correct answer
def check_ans(selected_option):
    global current_question, score
    correct_answer = questions_list[current_question]["correct answer"]
    
    print(f"Current Question Index: {current_question}, Total Questions: {len(questions_list)}")  # Debugging statement

    if selected_option == correct_answer:
        score += 1
    
    current_question += 1

    if current_question < len(questions_list):
        load_question()
    else:
        messagebox.showinfo("Quiz Over", f"You have reached a blackhole! Your score is {score}/10")
        window.quit()

# Function to load the next question
def load_question():
    question_data = questions_list[current_question]
    print(f"Loading Question: {question_data['question']}")  # Debugging statement
    question_label.config(text=question_data["question"])
    for i, option in enumerate(question_data["options"]):
        buttons[i].config(text=option, command=lambda opt=option: check_ans(opt))

# Function to start the quiz
def start_quiz():
    global current_question, score
    current_question = 0
    score = 0
    start_button.pack_forget()
    for button in buttons:
        button.pack(pady=5)  
    load_question()

# Welcome page
label = tk.Label(window, text="Welcome aboard space explorer! \n Strap in for a journey into the cosmos, and \n find out what you know about the universe!!", font=("Arial", 16), wraplength=500)
label.pack(pady=20)

# Start quiz button
start_button = tk.Button(window, text="Hell Yeah!! Let's go!!", font=("Arial", 16), command=start_quiz)
start_button.pack(pady=20)

# Exit button
exit_button = tk.Button(window, text="Meh...not in the Mood -_-", font=("Arial", 16), command=exit_app)
exit_button.pack(pady=20)

# Question label
question_label = tk.Label(window, text="", font=("Arial", 16))
question_label.pack(pady=20)

# Buttons for options
buttons = []
for i in range(4):
    button = tk.Button(window, text="", font=("Arial", 14), bg="light blue")
    buttons.append(button)

window.mainloop()
