class Game_Character:
    level = 1
    EXP = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def kick(self):
        print(f"{self.name} knock off the enemy's head with one move")
    def mind(self):
        print(f"{self.name} capture the minds of the other")
class wizard(Game_Character):
    def attack(self):
        print(f"{self.name} use the freeze spell")

#player1 = Game_Character("leo", 103)
#player2 = Game_Character("coke", 320)
#player1.name = "rick"
#player2.name = "james"
#print(player1.level)
#print(player2.EXP)
#print(player1.name)
#print(player2.age)
player1 = wizard("christopher", 3200)
player1.kick()
player1.mind()
player1.attack()
    