# The central list to store movie names
watchlist = []

def add_movie(movie_title):
    watchlist.append(movie_title)
    print(f"Added '{movie_title}' to your watchlist!")

def view_list():
    print("\n🎬 --- Your Watchlist ---")
    if not watchlist:
        print("Your watchlist is empty! Time to add some movies.")
    else:
        # A loop to display movies with a reference number
        for i in range(len(watchlist)):
            print(f"[{i + 1}] {watchlist[i]}")
    print("-------------------------\n")

def watch_movie(number_choice):
    # Convert the user's list number (1, 2, 3) into a Python index (0, 1, 2)
    index = number_choice - 1
    
    # Check if the number typed actually exists in our list length
    if 0 <= index < len(watchlist):
        # .pop() removes an item from a list at a specific index
        removed_movie = watchlist.pop(index)
        print(f"🍿 Hope you enjoyed watching '{removed_movie}'! Removed from list.")
    else:
        print("Invalid movie number.")

# The main terminal interface loop
while True:
    print("Menu: [1] Add Movie  [2] View Watchlist  [3] Watch/Remove Movie  [4] Exit")
    action = input("What would you like to do? (1/2/3/4): ")
    
    if action == '1':
        name = input("Enter the movie title: ")
        add_movie(name)
        
    elif action == '2':
        view_list()
        
    elif action == '3':
        if not watchlist:
            print("\nNothing to remove, your watchlist is empty.\n")
        else:
            view_list()
            choice = int(input("Enter the number of the movie you just watched: "))
            watch_movie(choice)
            
    elif action == '4':
        print("Goodbye! Enjoy your movies!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")