init python:

  # PersonMC - Main character -> tendrá la información especifica del mc habrá que ver como persistirla lmao
  class PersonMC (Person):
    """
      Representa a un personaje del juego.

      Atributos:
        character (Character) : Objeto que usa renpy para definir texto
        alias (string): Alias del personaje funcionará como identificador del personaje
        name (string): Nombre del personaje
        surnames (string): Apellidos del personaje
        age (num): 
        gender string: CAMBIAR A ENUM Genero del jugador
    """
    def __init__(self, character, alias, name, surnames, age, gender, studies):
      super().__init__( character, alias, name, surnames, age)
      self.__gender = gender
      self.__inventory = Inventory()
 

    @property
    def gender(self):
      return self.__gender

    @gender.setter
    def gender(self, gender):
      self.__gender = gender

    @property
    def inventory(self):
      return self.__inventory

    @inventory.setter
    def inventory(self, inventory):
      self.__inventory = inventory
    

   
    """
      Este método devuelve el artículo del jugador
    """
    def getArticle(self):
      if self.gender == "male":
        return "el"
      elif self.gender == "female":
        return "la"
      elif self.gender == "non-binary":
        return "le"
      else:
        return "Error en getArticle personMC: VALOR DE GÉNERO NO VALIDO O NULO"

    """
      Este método recibe:
        -Word: Una palabra sin terminación en género por ejemplo si quisiesemos poner "guapo"
        pondriamos "guap"
        -Number: "singular" para palabras singulares y "plural" para plurales
      Devuelve:
        -La palabra completa con el género y número  
    """
    def getGenderedSuffixedWord(self, word, number, esMascirr):
      if word is not None:
        if self.gender == "male" and not esMascirr:
          return word + "o"        
        elif self.gender == "female":
          return word + "a"
        elif self.gender == "non-binary" or esMascirr:
          return word + "e"
        else:
          return "Error en getGenderSuffixes personMC: VALOR DE GENERO NO VALIDO O NULO"

        if number == "plural":
          return word + "s"
        elif number == "singular":
          return word
        else:
          return "Error en getGenderSuffixes personMC: VALOR DE NUMERO NO VALIDO O NULO"
      else:
        return "Error en getGenderSuffixes personMC: PALABRA ES NULA"    

   
    """
      Este método devuelve el pronombre del jugador
    """
    def getPronoun(self):
      if self.gender == "male":
        return "él"
      elif self.gender == "female":
        return "ella"
      elif self.gender == "non-binary":
        return "elle"
      else:
        return "Error en getPronoun personMC: VALOR DE GÉNERO NO VALIDO O NULO"
    
    def gift(self, item, character):
      if item in self.inventory.items:
        character.addAffinity(item.baseAffinity)
        self.inventory.removeItem(item)
      else:
        print("LMAO PETO")

    def addItemToInventory(self, item):
        self.inventory.addItem(item)

    def getItemByIndex(self, index):
      return self.inventory.getItemByIndex(index)
    
    def printItems(self):
      for item in self.inventory.items:
        print(item)
