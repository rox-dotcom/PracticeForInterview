class Player: #The general class, a father of two
    def __init__(self,name,level,health):
        self.name = name
        self.level = level
        self.health = health
    
    def get_name(self):
        return self.name
    
    def get_status(self):
        return self.health
    
    def can_heal(self):
        print('Theres players that can heal')
    
    def details(self):
        print("My player's name is {}".format(self.name))
        print("My level is{}".format(self.level))
        print("My current health is {}".format(self.health))


class Healer_Wizzard(Player): #The favorite child: this player's son can heal
    def __init__(self, name, level, health, magic):
        super().__init__(name, level, health)
        self.playerType = magic

    def details(self): #Inheritance, we can access values initiated in the father class
        print()
        print("My player's name is {}".format(self.name))
        print("My level is {}".format(self.level))
        print("My current health is {}".format(self.health))
        print("My player's magic is {}".format(self.playerType)) #But is also posible to add something extra to the function
        

    def can_heal(Player):
        print('This payer can heal!')

class Adventurer(Player): #The not so lovable child: this child can't heal,
                            #but it will give his heart for the battle
    def __init__(self, name, level, health, sword):
        self.playerType = sword
        
        super().__init__(name, level, health)
    
    def details(self):
        print()
        print("My player's name is {}".format(self.name))
        print("My level is {}".format(self.level))
        print("My current health is {}".format(self.health))
        print("My player's sword is {}".format(self.playerType))
        


    def can_heal(Player): #Polymorphism, behaves differently depending on the player
                            #If we we're to comment this function the default of the father class will be showed
        print('This player cannot heal, but can fight')


def main():
    Merlincito = Healer_Wizzard('Merlin', 500, 100, 'Powerfull')
    Arturito = Adventurer('Arturo', 15, 50, 'Scalibur')

    Merlincito.details()
    Merlincito.can_heal()
    
    Arturito.details()
    Arturito.can_heal()

if __name__ == '__main__':
    main()