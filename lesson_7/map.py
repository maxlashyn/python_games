from options import *
from functions import *


class Map:
    def __init__(self):
        self.field = []
        self.user_pos = (0, 0)
        self.monster_pos = (0, 0)
        self.treasure_pos = []
        self.monster = None

    def get_pos_nearest_treasure(self, x, y):
        distance = max(MAP_WIDTH, MAP_HEIGHT)
        nearest_treasure_pos = ()
        if len(self.treasure_pos) == 0:
            return None

        for pos in self.treasure_pos:
            new_distance = get_distance(pos, (x, y))
            if distance > new_distance:
                distance = new_distance
                nearest_treasure_pos = pos

        return nearest_treasure_pos

    def generate(self):
        self.field = [
            [GRASS for i in range(MAP_WIDTH + 1)] for j in range(MAP_HEIGHT + 1)
        ]
        for i in range(MAX_TREES):
            x, y = get_random_pos()
            self.field[y][x] = TREE
        for i in range(MAX_STONES):
            x, y = get_random_pos()
            self.field[y][x] = STONE
        for i in range(MAX_TREASURES):
            x, y = get_random_pos()
            while self.field[y][x] == TREASURE:
                x, y = get_random_pos()
            else:
                self.field[y][x] = TREASURE
                self.treasure_pos.append((x, y))
        for i in range(MAX_LETTERS):
            x, y = get_random_pos()
            while self.field[y][x] in (LETTER, TREASURE):
                x, y = get_random_pos()
            else:
                self.field[y][x] = LETTER

    def show(self):
        print(''.join(['-' for i in range(MAP_WIDTH)]))
        field_with_smog = self.get_field_with_smog()
        for y in range(MAP_HEIGHT + 1):
            print("".join(field_with_smog[y]))
        print(''.join(['-' for i in range(MAP_WIDTH)]))

    def append(self, character):
        x, y = MAP_WIDTH // 2, MAP_HEIGHT // 2
        while self.field[y][x] in (LETTER, TREASURE, USER, MONSTER):
            x, y = get_random_pos()
        if type(character).__name__ == 'User':
            self.set_user_position(character, x, y)
        else:
            self.set_monster_position(character, x, y)

    def get_objects(self, x, y):
        if x < 0 or x > MAP_WIDTH:
            return STONE
        if y < 0 or y > MAP_HEIGHT:
            return STONE
        return self.field[y][x]

    def move_to(self, user, x, y):
        user_pos = user.get_position()
        self.field[user_pos[1]][user_pos[0]] = GRASS
        self.set_user_position(user, x, y)

    def set_user_position(self, user, x, y):
        self.user_pos = (x, y)
        self.field[y][x] = USER
        user.set_position(x, y)

    def get_field_with_smog(self):
        field_with_smog = []
        for y in range(MAP_HEIGHT + 1):
            field_with_smog.append(self.field[y].copy())
            for x in range(MAP_WIDTH + 1):
                if x < self.user_pos[0] - SMOG_RADIUS or x > self.user_pos[0] + SMOG_RADIUS:
                    field_with_smog[y][x] = SMOG
                elif y < self.user_pos[1] - SMOG_RADIUS or y > self.user_pos[1] + SMOG_RADIUS:
                    field_with_smog[y][x] = SMOG
        return field_with_smog

    def remove(self, x, y):
        if self.field[y][x] in (TREE, LETTER):
            self.field[y][x] = GRASS
        if self.field[y][x] == TREASURE:
            self.field[y][x] = GRASS
            self.treasure_pos.remove((x, y))


    def set_monster_position(self, character, x, y):
        self.monster_pos = (x, y)
        self.field[y][x] = MONSTER
        self.monster = character
        self.monster.set_position(x, y)

    def monster_dead(self):
        self.field[self.monster_pos[1]][self.monster_pos[0]] = GRASS
        self.monster = None
        self.monster_pos = (0, 0)