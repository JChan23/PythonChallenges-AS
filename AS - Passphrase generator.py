#Create a pass phrase generator that helps students to create secure passwords. Bonus 50 if it uses an external file	
import random

names = [
    "John", "Mary", "Robert", "Jennifer", "Michael",
    "Linda", "William", "Patricia", "David", "Elizabeth",
    "Richard", "Susan", "Joseph", "Jessica", "Thomas",
    "Sarah", "Charles", "Karen", "Christopher", "Nancy",
    "Daniel", "Lisa", "Matthew", "Margaret", "Anthony",
    "Betty", "Donald", "Dorothy", "Mark", "Sandra",
    "Paul", "Ashley", "George", "Kimberly", "Kenneth",
    "Donna", "Steven", "Emily", "Edward", "Helen",
    "Brian", "Michelle", "Ronald", "Deborah", "Timothy",
    "Carol", "Jason", "Laura", "Jeffrey", "Stephanie"
]

transport = [
    "drove to",
    "walked to",
    "biked to",
    "took the bus to",
    "rode a taxi to",
    "flew to",
    "hitched a ride to",
    "ran to",
    "skated to",
    "cycled to",
    "hiked to",
    "sailed to",
    "paddled to",
    "traveled by train to",
    "crawled to",
    "swam to",
    "escorted to",
    "marched to",
    "paraglided to",
    "teleported to"
]

places = [
    "1st street",
    "2nd avenue",
    "3rd road",
    "4th lane",
    "5th drive",
    "6th boulevard",
    "7th way",
    "8th place",
    "9th court",
    "10th circle",
    "11th crescent",
    "12th terrace",
    "13th alley",
    "14th path",
    "15th highway",
    "16th trail",
    "17th lane",
    "18th avenue",
    "19th road",
    "20th street"
]

actions = [
    "to buy groceries",
    "to read a book",
    "to watch a movie",
    "to cook dinner",
    "to take a walk",
    "to write a letter",
    "to sing a song",
    "to dance in the rain",
    "to learn a new skill",
    "to travel to a new city",
    "to solve a puzzle",
    "to draw a picture",
    "to meet a friend",
    "to exercise regularly",
    "to visit a museum",
    "to play a musical instrument",
    "to meditate in the morning",
    "to take a nap",
    "to write a poem",
    "to plant a garden",
    "to learn a new language",
    "to go for a swim",
    "to cook a new recipe",
    "to paint a masterpiece",
    "to volunteer at a shelter",
    "to build a sandcastle",
    "to explore a forest",
    "to bake cookies",
    "to take a yoga class",
    "to plan a road trip"
]

print('Passphrase:', names[random.randint(0, 49)], transport[random.randint(0, 19)], places[random.randint(0, 19)], actions[random.randint(0, 29)])
