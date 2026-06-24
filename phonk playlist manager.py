# The main list to store songs
playlist = []

def add_track(track):
    playlist.append(track)
    print(f"Volume up! Added '{track}' to the playlist.")

def view_queue():
    print("\n--- Current Phonk Queue ---")
    if not playlist:
        print("The playlist is currently empty.")
    else:
        # A for loop to print each song with a number next to it
        for i in range(len(playlist)):
            print(f"{i + 1}. {playlist[i]}")
    print("---------------------------\n")

# The main loop that keeps the menu active
while True:
    print("Options: [1] Add Track  [2] View Queue  [3] Exit")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        song = input("Enter the name of the track: ")
        add_track(song)
    elif choice == '2':
        view_queue()
    elif choice == '3':
        print("Closing the playlist manager...")
        break
    else:
        print("Invalid input. Please try again.")