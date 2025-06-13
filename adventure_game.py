from colorama import init, Fore, Style
init(autoreset=True)

def start_game():
    print(Fore.CYAN + "Welcome to the " + Fore.YELLOW + "Forest of Fate!")
    print("You are a traveler seeking treasure in a mysterious forest.")
    print("You arrive at a fork in the road.")
    
    choice1 = input(Fore.GREEN + "Do you want to go left or right? (left/right): ").lower()
    
    if choice1 == "left":
        print("\n" + Fore.CYAN + "You walk along the left path and reach a river.")
        choice2 = input(Fore.GREEN + "Do you want to swim across or build a raft? (swim/raft): ").lower()
        
        if choice2 == "swim":
            print(Fore.RED + "\nOh no! The current was too strong and you were swept away. Game Over.")
        elif choice2 == "raft":
            print(Fore.CYAN + "\nYou built a raft and crossed safely.")
            choice3 = input(Fore.GREEN + "You see a cave and a castle. Where do you go? (cave/castle): ").lower()
            
            if choice3 == "cave":
                print(Fore.CYAN + "\nInside the cave, you find a sleeping dragon guarding treasure!")
                choice4 = input(Fore.GREEN + "Do you try to steal the treasure or quietly leave? (steal/leave): ").lower()
                
                if choice4 == "steal":
                    print(Fore.RED + "\nThe dragon wakes up and burns you to ashes. Game Over.")
                elif choice4 == "leave":
                    print(Fore.YELLOW + "\nYou leave quietly. Maybe next time. You survive!")
                else:
                    print(Fore.RED + "Invalid choice. Game Over.")
            elif choice3 == "castle":
                print(Fore.YELLOW + "\nInside the castle, you find gold and jewels. You win!")
            else:
                print(Fore.RED + "Invalid choice. Game Over.")
        else:
            print(Fore.RED + "Invalid choice. Game Over.")

    elif choice1 == "right":
        print(Fore.RED + "\nYou walk along the right path and fall into a trap. Game Over.")
    else:
        print(Fore.RED + "Invalid choice. Game Over.")

# Start the game loop
while True:
    start_game()
    play_again = input(Fore.BLUE + "\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(Fore.MAGENTA + "Thanks for playing! Goodbye.")
        break
