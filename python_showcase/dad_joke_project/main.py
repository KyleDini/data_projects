import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("Dad Joke Generator" )
header = colored(header, color="cyan")
print(header)

user_input = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()
num_jokes = res["total_jokes"]

results = res["results"]

if num_jokes > 1:
    print(f"I found {num_jokes} containing '{user_input}'. Here's one: \n")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke containing '{user_input}'. Here it is: \n")
    print(results[0]["joke"])
else:
    print(f"There are no jokes containing '{user_input}'")