import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
    "Rain on Your Parade",
    "Wake Up Call",
    "Scot free",
    "You Cant Teach an Old Dog New Tricks",
    "Back To the Drawing Board",
    "Up In Arms",
    "A Hundred and Ten Percent",
    "Burst Your Bubble",
    "If You Cant Stand the Heat Get Out of the Kitchen",
    "A Bite at the Cherry",
    "Let Her Rip",
    "Fish Out Of Water",
    "Go Out On a Limb",
    "A Busy Bee",
    "A Home Bird",
    "Love Birds",
    "Hear Hear",
    "On Cloud Nine",
    "Lovey Dovey",
    "Barking Up The Wrong Tree",
    "Right Off the Bat",
    "Birds of a Feather Flock Together",
    "Dont Count Your Chickens Before They Hatch",
    "Every Cloud Has a Silver Lining",
    "All Greek To Me",
        ]
        self.active_phrase = random.choice(self.phrases).lower()
        self. guesses = {" "}
        self.phrase_instance = Phrase(list(self.active_phrase), self)
    
    def welcome(self):
        print("Welcome to this wacky game of wacky guesses")
        print(f"There are currently {len(self.phrases)} phrases in this game")
        add_phrase = input("Would you like to add a phrase (y/n): ").lower()
        if add_phrase == "y":
            new_phrase = input("Enter the new phrase here: ")
            new_phrase = ''.join(char.lower() if char.isalpha() or char.isspace() else '' for char in new_phrase)
            if new_phrase.strip() == "":
                print("Aww, so you were just kidding. That's okay, we can take a joke")
            else:
                correction = False
                while not correction:
                    print(f"Thank you! We adjusted the phrase if needed, so it will look like this: {new_phrase}")
                    agree = input("Do you agree with this (y/n)?: ").lower()
                    if agree == "n":
                        new_phrase = input("Okay, please input the phrase again here: ")
                    else:
                        correction = True
                print("Phrase has been added")
                self.phrases.append(new_phrase)
        else:
            print("Ok, lets start the game, please see below the phrase you will have to guess:")
            


    def start(self):
        self.welcome()
        missed = self.missed
        guess_phrase = False
        while guess_phrase == False:
            self.phrase_instance.display()
            print(f"You currently have {missed} missed guesses")
            user_guess = self.get_guess()
            self.guesses.add(user_guess)
            print(f"User's guess: {user_guess}")
            if user_guess not in self.active_phrase:
                missed +=1
            print(f"You currently have {missed} guesses")
            self.phrase_instance.display()
            user_phrase = input("Would you like to guess the phrase? Y/N: ").lower()
            if missed == 5:
                print("Aww. you didnt get it in 5 guesses")
                print(f"The phrase was {self.active_phrase}")
                failed_again = input("Would you like to try again? Y/N?: ").lower()
                if failed_again == "y":
                    print("Ok good luck this time!")
                    self.active_phrase = random.choice(self.phrases).lower()
                    self. guesses = {" "}
                    self.phrase_instance = Phrase(list(self.active_phrase), self)
                    self.start()
                else:
                    print("OK Ok, we get it, losing is never fun, hope you will still have an EXCELLENT DAY!")
                    guess_phrase = True 
            elif user_phrase == "y":
                guessing = input("OK, what is your guess: ").lower()
                if guessing == self.active_phrase:
                    guess_phrase = True
                    print(f"Congratulations! You did it! And you did it with {missed} missed guesses!")
                    try_again = input("Do you want to try again? Y/N: ").lower()
                    if try_again == "y":
                        print("Alright, we will restart it all!")
                        self.active_phrase = random.choice(self.phrases).lower()
                        self. guesses = {" "}
                        self.phrase_instance = Phrase(list(self.active_phrase), self)
                        self.start()
                    else:
                        print("Oh, you made the panda cry, we now have a sad panda. Well, hope you still enjoy your day :)")
                        guess_phrase = True  

    def get_guess(self):
        user_guess = input ("lets hear your guess: ").lower()
        return user_guess






