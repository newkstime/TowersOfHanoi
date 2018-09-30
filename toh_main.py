from towers_of_hanoi import TowersOfHanoi

def main():
    for num_disks in range(3, 25):
        new_game = TowersOfHanoi(num_disks)
        if num_disks == 5:
            new_game.display_towers()
        new_game.play()

main()
