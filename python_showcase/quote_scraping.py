from csv import DictReader
from game_code import play_game
from scrape_and_write import scrape_quotes, write_csv

BASE_URL = "https://quotes.toscrape.com/"

# scrape_quotes()
# write_csv("quotes.csv")
# CSV appears after the program has ended

def read_quotes(filename):
    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)

quotes_list = read_quotes("quotes.csv")
play_game(quotes_list)

end_game = True
while end_game:
    again = input("Do you want to play again? Type 'y' or 'n': ")
    if again == 'y':
        play_game(quotes_list)
    else:
        end_game = False

print("\nThanks for playing :)")