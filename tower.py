class Tower(list):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def get_name(self):
        return self.__name

    def move(self, dest_tower):
        disk = self.pop()
        dest_tower.append(disk)

    def __str__(self):
        string =  "Tower " + self.__name + ": ["
        if len(self) > 0:
            string  = string + str(self[0])
            for i in range(1,len(self)):
                string  = string + ', ' + str(self[i])

        string  = string + ']'
        return string

