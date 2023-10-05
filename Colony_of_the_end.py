# MIT License
#
# Copyright (c) 2023 wojtixmaxim
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random
import pickle

# Initialize resources and colonists
coal = 0
heat_generator = 0
steel = 0
food = 0
water = 0
mechanisms = 0
oxygen_bottles = 0
air_generator_algae = 0
algae = 0
toolkits = 0
fruit_plants_jars = 0
vegetable_plants_jars = 0
nut_plants_jars = 0
tree_like_plants_jars = 0
mining_machines = 0
num_colonists = 0
colonists = []

# Initialize player's temperature and mood
temperature_planet = random.randint(-30, 50)  # Starting temperature depending on the planet
temperature = temperature_planet  # Initial temperature equals planet's temperature
mood = 50  # Starting mood

# Initialize unique places on the planet
unique_places = [
    "Crystal Cave",
    "Ancient Spaceship Wreck",
    "Volcanic Thermal Springs",
    "Great Valley",
    # Add more unique places
]

# Initialize planets
planets = {
    "1": {
        "Name": "Icy Planet",
        "Oxygen": 20,
        "Carbon Dioxide": 80,
    },
    "2": {
        "Name": "Temperate Planet",
        "Oxygen": 50,
        "Carbon Dioxide": 50,
    },
    "3": {
        "Name": "Hot Planet",
        "Oxygen": 80,
        "Carbon Dioxide": 20,
    },
    "4": {
        "Name": "Variable Planet",
        "Oxygen": random.randint(1, 100),
        "Carbon Dioxide": random.randint(1, 100),
    },
    "5": {
        "Name": "Tropical Planet",
        "Oxygen": 50,
        "Carbon Dioxide": 50,
    },
}

# Function to display planet information
def display_planet_info():
    print(f"Planet: {current_planet['Name']}")
    print(f"Oxygen Level: {current_planet['Oxygen']}%")
    print(f"Carbon Dioxide Level: {current_planet['Carbon Dioxide']}%")



# Function to save the game
def save_game():
    save_data = {
        "resources": {
            "coal": coal,
            "heat_generator": heat_generator,
            "steel": steel,
            "food": food,
            "water": water,
            "mechanisms": mechanisms,
            "oxygen_bottles": oxygen_bottles,
            "air_generator_algae": air_generator_algae,
            "algae": algae,
            "toolkits": toolkits,
            "fruit_plants_jars": fruit_plants_jars,
            "vegetable_plants_jars": vegetable_plants_jars,
            "nut_plants_jars": nut_plants_jars,
            "tree_like_plants_jars": tree_like_plants_jars,
            "mining_machines": mining_machines,
        },
        "colonists": colonists,
        "temperature": temperature,
        "mood": mood,
        "current_planet": current_planet,
    }

    with open("savegame.dat", "wb") as save_file:
        pickle.dump(save_data, save_file)
    print("Game saved.")

# Function to load the game
def load_game():
    global coal, heat_generator, steel, food, water, mechanisms, oxygen_bottles, air_generator_algae, algae
    global toolkits, fruit_plants_jars, vegetable_plants_jars, nut_plants_jars, tree_like_plants_jars, mining_machines
    global colonists, temperature, mood, current_planet

    try:
        with open("savegame.dat", "rb") as save_file:
            save_data = pickle.load(save_file)

        coal = save_data["resources"]["coal"]
        heat_generator = save_data["resources"]["heat_generator"]
        steel = save_data["resources"]["steel"]
        food = save_data["resources"]["food"]
        water = save_data["resources"]["water"]
        mechanisms = save_data["resources"]["mechanisms"]
        oxygen_bottles = save_data["resources"]["oxygen_bottles"]
        air_generator_algae = save_data["resources"]["air_generator_algae"]
        algae = save_data["resources"]["algae"]
        toolkits = save_data["resources"]["toolkits"]
        fruit_plants_jars = save_data["resources"]["fruit_plants_jars"]
        vegetable_plants_jars = save_data["resources"]["vegetable_plants_jars"]
        nut_plants_jars = save_data["resources"]["nut_plants_jars"]
        tree_like_plants_jars = save_data["resources"]["tree_like_plants_jars"]
        mining_machines = save_data["resources"]["mining_machines"]

        colonists = save_data["colonists"]
        temperature = save_data["temperature"]
        mood = save_data["mood"]
        current_planet = save_data["current_planet"]

        print("Game loaded.")
    except FileNotFoundError:
        print("No saved game found.")

# Introduction
print("Welcome! You are an artificial intelligence tasked with guiding these few people to build a colony in this harsh world.")

# Choose the planet type
print("Choose the planet type:")
for key, planet in planets.items():
    print(f"{key}. {planet['Name']}")
planet_type = input("Select the planet number: ")

# Initialize resources based on the planet type
current_planet = planets[planet_type]
if planet_type == "1":
    coal = random.randint(100, 400)  # Random value between 100 and 400
    heat_generator = 1
    steel = random.randint(100, 400)  # Random value between 100 and 400
    food = random.randint(100, 400)  # Random value between 100 and 400
    water = random.randint(100, 400)  # Random value between 100 and 400
    mechanisms = random.randint(100, 400)  # Random value between 100 and 400
    oxygen_bottles = random.randint(100, 400)  # Random value between 100 and 400
    air_generator_algae = 1
    algae = 500
    toolkits = 30
    fruit_plants_jars = 10
    vegetable_plants_jars = 10
    nut_plants_jars = 10
    tree_like_plants_jars = 10
    mining_machines = 5
    # Add other resources you want to initialize randomly at this place

if planet_type == "2":
    coal = random.randint(100, 400)  # Random value between 100 and 400
    heat_generator = 1
    steel = random.randint(100, 400)  # Random value between 100 and 400
    food = random.randint(100, 400)  # Random value between 100 and 400
    water = random.randint(100, 400)  # Random value between 100 and 400
    mechanisms = random.randint(100, 400)  # Random value between 100 and 400
    oxygen_bottles = random.randint(100, 400)  # Random value between 100 and 400
    air_generator_algae = 1
    algae = 500
    toolkits = 30
    fruit_plants_jars = 10
    vegetable_plants_jars = 10
    nut_plants_jars = 10
    tree_like_plants_jars = 10
    mining_machines = 5
    # Add other resources you want to initialize randomly at this place

if planet_type == "3":
    coal = random.randint(100, 400)  # Random value between 100 and 400
    heat_generator = 1
    steel = random.randint(100, 400)  # Random value between 100 and 400
    food = random.randint(100, 400)  # Random value between 100 and 400
    water = random.randint(100, 400)  # Random value between 100 and 400
    mechanisms = random.randint(100, 400)  # Random value between 100 and 400
    oxygen_bottles = random.randint(100, 400)  # Random value between 100 and 400
    air_generator_algae = 1
    algae = 500
    toolkits = 30
    fruit_plants_jars = 10
    vegetable_plants_jars = 10
    nut_plants_jars = 10
    tree_like_plants_jars = 10
    mining_machines = 5
    # Add other resources you want to initialize randomly at this place

if planet_type == "4":
    coal = random.randint(100, 400)  # Random value between 100 and 400
    heat_generator = 1
    steel = random.randint(100, 400)  # Random value between 100 and 400
    food = random.randint(100, 400)  # Random value between 100 and 400
    water = random.randint(100, 400)  # Random value between 100 and 400
    mechanisms = random.randint(100, 400)  # Random value between 100 and 400
    oxygen_bottles = random.randint(100, 400)  # Random value between 100 and 400
    air_generator_algae = 1
    algae = 500
    toolkits = 30
    fruit_plants_jars = 10
    vegetable_plants_jars = 10
    nut_plants_jars = 10
    tree_like_plants_jars = 10
    mining_machines = 5
    # Add other resources you want to initialize randomly at this place

if planet_type == "5":
    coal = random.randint(100, 400)  # Random value between 100 and 400
    heat_generator = 1
    steel = random.randint(100, 400)  # Random value between 100 and 400
    food = random.randint(100, 400)  # Random value between 100 and 400
    water = random.randint(100, 400)  # Random value between 100 and 400
    mechanisms = random.randint(100, 400)  # Random value between 100 and 400
    oxygen_bottles = random.randint(100, 400)  # Random value between 100 and 400
    air_generator_algae = 1
    algae = 500
    toolkits = 30
    fruit_plants_jars = 10
    vegetable_plants_jars = 10
    nut_plants_jars = 10
    tree_like_plants_jars = 10
    mining_machines = 5
    # Add other resources you want to initialize randomly at this place


# Choose the scenario
print("Choose the scenario:")
print("1. Three passengers from the Aurora 3010 ship have landed on this planet.")
print("2. A lone survivor from the last ship, Epilor 4182, was sent to this planet.")
scenario = input("Select the scenario number: ")

# Initialize resources and colonists based on the scenario
if scenario == "1":
    # Scenario with three passengers
    num_colonists = 3
    colonists = []
    for i in range(num_colonists):
        name = input(f"Enter a name for colonist {i + 1}: ")
        # Initialize statistics
        colonist_stats = {
            "Building": random.randint(1, 10),
            "Knowledge": random.randint(1, 10),
            "Cooking": random.randint(1, 10),
            "Strength": random.randint(1, 10),
            "Energy Management": random.randint(1, 10),
        }
        colonist = {
            "Name": name,
            "Stats": colonist_stats,
            "Basic Statistic": random.choice(list(colonist_stats.keys())),
            "Age": random.randint(20, 70),
        }
        colonists.append(colonist)

    # Resource increase at the end of the turn
    food -= num_colonists
    water -= num_colonists
    # Add other resources

elif scenario == "2":
    # Scenario with a lone survivor
    num_colonists = 1
    colonists = []
    for i in range(num_colonists):
        name = input("Enter a name for the colonist: ")
        # Initialize statistics
        colonist_stats = {
            "Building": random.randint(1, 10),
            "Knowledge": random.randint(1, 10),
            "Cooking": random.randint(1, 10),
            "Strength": random.randint(1, 10),
            "Energy Management": random.randint(1, 10),
        }
        colonist = {
            "Name": name,
            "Stats": colonist_stats,
            "Basic Statistic": random.choice(list(colonist_stats.keys())),
            "Age": random.randint(20, 70),
        }
        colonists.append(colonist)

# Start the game
print("Let's begin! Good luck building a colony on this unfriendly planet.")
while True:
    # Simulate weather and its impact on the player
    temperature += random.randint(-5, 5)
    mood += random.randint(-10, 10)
    temperature = max(-30, min(50, temperature))  # Limit temperature to the range [-30, 50]
    mood = max(0, min(100, mood))  # Limit mood to the range [0, 100]


    # Display available options
    print("\nAvailable options:")
    print("1. Build an oxygen generator and a heat generator")
    print("2. View resources")
    print("3. Explore")
    print("4. End the turn")
    print("5. Save the game")
    print("6. Load the game")
    print("7. End the game")
    choice = input("Select the option number: ")

    if choice == "1":
        # Build an oxygen generator and a heat generator
        if steel >= 100 and algae >= 50 and toolkits >= 10:
            print("You are building oxygen and heat generators.")
            oxygen_bottles += 20
            heat_generator += 3
            steel -= 100
            algae -= 50
            toolkits -= 10
        else:
            print("You don't have enough resources or tools to build the generators.")

    elif choice == "2":
        # View resources
        print("\nYour resources:")
        print(f"Coal: {coal}")
        print(f"Steel: {steel}")
        print(f"Water: {water}")
        print(f"Food: {food}")
        print(f"Mechanisms: {mechanisms}")
        print(f"Air Bottles: {oxygen_bottles}")
        print(f"Fruit Plant Jars: {fruit_plants_jars}")
        print(f"Vegetable Plant Jars: {vegetable_plants_jars}")
        print(f"Nut Plant Jars: {nut_plants_jars}")
        print(f"Tree-like Plant Jars: {tree_like_plants_jars}")
        print(f"Toolkits: {toolkits}")
        print(f"Algae Oxygen Generator: {air_generator_algae}")
        print(f"Heat Generator: {heat_generator}")
        # Add other resources

    elif choice == "3":
        # Exploration
        chance_to_find_colonist = 5 if current_planet["Name"] == "Tropical Planet" else 10
        if random.randint(1, 100) <= chance_to_find_colonist:
            print("During exploration, an abandoned colonist was found!")
            new_colonist = {
                "Name": f"Colonist {len(colonists) + 1}",
                "Stats": {
                    "Building": random.randint(1, 10),
                    "Knowledge": random.randint(1, 10),
                    "Cooking": random.randint(1, 10),
                    "Strength": random.randint(1, 10),
                    "Energy Management": random.randint(1, 10),
                },
                "Basic Statistic": random.choice(["Building", "Knowledge", "Cooking", "Strength", "Energy Management"]),
                "Age": random.randint(20, 70),
            }
            colonists.append(new_colonist)
        else:
            print("No one was found during exploration.")

        if current_planet["Name"] == "Tropical Planet":
            # Simulate the impact of a colonist on the tropical planet's balance
            current_planet["Oxygen"] -= 1
            current_planet["Carbon Dioxide"] += 1
            if current_planet["Oxygen"] < 50 or current_planet["Carbon Dioxide"] > 50:
                print("Warning! The planet's balance is disturbed. Disaster is imminent.")
            if current_planet["Oxygen"] < 30 or current_planet["Carbon Dioxide"] > 70:
                print("Disaster! The planet is no longer habitable.")
                print("The game ends in 5 turns.")
                break

        if current_planet["Name"] == "Tropical Planet":
            current_planet["Oxygen"] += 2
            current_planet["Carbon Dioxide"] -= 2

    elif choice == "4":
        # End the turn
        # You can add logic for temperature and colonists' mood changes here
        temperature += random.randint(-5, 5)  # Simulate temperature change at the end of the turn
        mood += random.randint(-5, 5)  # Simulate mood change at the end of the turn

        # Simulate consumption of food and water by colonists
        food -= num_colonists
        water -= num_colonists

        # Simulate oxygen and heat production
        oxygen_bottles += 20
        coal -= 5
        # Add more production logic

        # Simulate aging of colonists
        for colonist in colonists:
            colonist["Age"] += 1
            if colonist["Age"] >= 100:
                print(f"{colonist['Name']} died of old age.")

        # Simulate tree-like plant resources
        if tree_like_plants_jars > 0:
            current_planet["Carbon Dioxide"] -= tree_like_plants_jars
            if current_planet["Carbon Dioxide"] < 0:
                current_planet["Carbon Dioxide"] = 0
        # Simulate plant resources

    elif choice == "5":
        # Save the game
        save_game()

    elif choice == "6":
        # Load the game
        load_game()

    elif choice == "7":
        # End the game
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice. Please select one of the available options.")
