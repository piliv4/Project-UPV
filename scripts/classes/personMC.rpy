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
    def __init__(self, character, alias, name, surnames, age, gender):
      super().__init__( character, alias, name, surnames, age)
      self.__gender = gender
 

    @property
    def gender(self):
      return self.__gender

    @gender.setter
    def gender(self, gender):
      self.__gender = gender
    

   
    def getPronoun(self):
      if self.gender == "male":
        return "él"
      elif self.gender == "female":
        return "ella"
      elif self.gender == "non-binary":
        return "elle"
      else:
        return "ERROR_GENERO_NO_ESPECIFICADO_O_NULO"

    
