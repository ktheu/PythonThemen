import time
class Bewohner:
    aktuell = time.localtime().tm_year
    def __init__(self, name, geboren):
        self.name = name
        self.geboren = geboren
        
        if not isinstance(geboren,int):
            raise TypeError(f"'geboren' muss ein Integer sein, nicht class '{type(geboren).__name__}'.")
            
        if self.alter() > 130:
            raise ValueError(f"Prüfe das Geburtsjahr. {self.geboren} ist nicht erlaubt.")
        
    def alter(self):
        return self.aktuell-self.geboren
    
lisa = Bewohner('Lisa', 2013)
print(lisa.alter())