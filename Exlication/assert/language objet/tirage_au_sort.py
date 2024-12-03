from random import choice

class TirageAuSort:
    possibilites = [1]
    
    def __init__(self, possibilites):
        self.possibilites = possibilites
        
        
    def tire(self):
        return choice(self.possibilites)
    
class De(TirageAuSort):
    
    def __init__(self,nb_faces):
        self.possibilits=list(range(1,nb_faces+1))
             
class Piece(TirageAuSort):
    langues = {"fr": ["Pile","Face"],
              "en": ["Head", "Tail"],
              "de": ["Kopf", "Zahl"],
              "es": ["Cara", "Zahl"],
              "sq": ["Koka", "Bishta"]
        }
     def __init__(self,langue= "fr"):
       if langue in self.langues:
         self.possibilites = self.langues[langue]
       else :
         self.possibilites = self.langues["fr]
         
de6 = De (6)
de20 = De (20)
pouf = Piece("de")
