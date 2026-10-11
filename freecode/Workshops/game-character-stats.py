class GameCharacter:
    def __init__(self, name, health = 100, mana = 50, level = 1):
        self._name = name
        self._health = health
        self._mana = mana
        self._level = level

    @property
    def name(self):
        return self._name  

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            raise ValueError("Health can't be 0")
        elif new_health > 0:
            raise ValueError("Health can't be more than 100")    
        self._health = new_health  
    @property
    def mana(self):
        return self._health
    
    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            raise ValueError("mana can't be 0")
        elif new_mana > 0:
            raise ValueError("mana can't be more than 50")   
        self._mana = new_mana     

    @property
    def level(self):
        return self._level
    
    def level_up(self):
        pass