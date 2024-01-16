
class Phrase:
    def __init__(self, active_phrase, game_instance):
        self.phrase = active_phrase
        self.game_instance = game_instance

    def display(self):
        for letter in self.phrase:
            if letter.lower() in self.game_instance.guesses:
                print(f"{letter}", end=" ")
            elif letter == " ":
                print(" ", end=" ")
            else:
                print("_", end=" ")
        print()  # Add a newline after displaying the phrase




