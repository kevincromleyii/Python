import time
import random

quotes = [
    "The only way to make sense out of change is to plunge into it, move with it, and join the dance. - Alan Watts",
    "Trying to define yourself is like trying to bite your own teeth. - Alan Watts",
    "Muddy water is best cleared by leaving it alone. - Alan Watts",
    "The more a thing tends to be permanent, the more it tends to be lifeless. - Alan Watts",
    "You are an aperture through which the universe is looking at and exploring itself. - Alan Watts",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "The unexamined life is not worth living. - Socrates",
    "I think therefore I am. - René Descartes",
    "He who has a why to live can bear almost any how. - Friedrich Nietzsche",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama"
]

# Infinite loop to print quotes
while True:
    quote = random.choice(quotes)
    print(quote)
    time.sleep(5)  # Sleep for 5 seconds before printing the next quote
