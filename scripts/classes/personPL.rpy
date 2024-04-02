init python:

  # PersonPL - Personajes Ligables (PL) - Categoría para personajes que requieran del atributo AFINIDAD, básicamente los 3 LI.

  class PersonPL (Person):
    """
      Representa a un personaje del juego.

      Atributos:
        character (Character) : Objeto que usa renpy para definir texto
        alias (string): Alias del personaje funcionará como identificador del personaje
        name (string): Nombre del personaje
        surnames (string): Apellidos del personaje
        age (num): 
        affinity (num): Valor de 0 a 100 que determina el nivel de afinidad con el personaje principal 
    """
    def __init__(self, character, alias, name, surnames, age, affinity):
      super().__init__( character, alias, name, surnames, age)
      self.__affinity = affinity
 

    @property
    def affinity(self):
      return self.__affinity
    

    
    def addAffinity(self, val):
      self.__affinity += val


    
