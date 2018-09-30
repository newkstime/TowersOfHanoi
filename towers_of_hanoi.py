from tower import Tower
from disk import Disk

class TowersOfHanoi:
    def __init__(self, num_disks):
        self.__num_of_disks = num_disks
        self.__num_of_moves = 0
        self.__towers = []
        self.beg_tower = Tower("A")
        self.aux_tower = Tower("B")
        self.end_tower = Tower("C")
        while num_disks > 0:
            disk = Disk(num_disks)
            self.beg_tower.append(disk)
            num_disks -= 1
        self.__towers.append(self.beg_tower)
        self.__towers.append(self.aux_tower)
        self.__towers.append(self.end_tower)

    def get_num_of_moves(self):
        return self.__num_of_moves

    def move_disks(self, num_of_disks_to_move, beg_tow, aux_tow, end_tow):
        if num_of_disks_to_move > 0:
            self.move_disks(num_of_disks_to_move - 1, beg_tow, end_tow, aux_tow)
            if beg_tow[0]:
                beg_tow.move(end_tow)
            self.__num_of_moves += 1
            self.display_towers()
            self.move_disks(num_of_disks_to_move - 1, aux_tow, beg_tow, end_tow)

    def play(self):
        self.move_disks(self.__num_of_disks, self.beg_tower, self.aux_tower, self.end_tower)
        print("Moving " + str(self.__num_of_disks) + " completed in " + str(self.__num_of_moves) + " moves!")

    def display_towers(self):
        if self.__num_of_disks == 5:
            print(self.beg_tower)
            print(self.aux_tower)
            print(self.end_tower)
            print("\n")

