init python:

  #Person - Personajes normales - Categoría para personajes que NO necesiten del atributo AFINIDAD, como el main character o realmente cualquier otro que no sean los 3 LI
  class Person (object):
    """
      Representa a un personaje del juego.

      Atributos:
        character (Character) : Objeto que usa renpy para definir texto
        alias (string): Alias del personaje funcionará como identificador del personaje
        name (string): Nombre del personaje
        surnames (string): Apellidos del personaje
        age (num): 
    """
    def __init__(self, character, alias, name, surnames, age):
      self.name = name
      self.surnames = surnames
      self.age = age
      self.__alias = alias
      self.__character = character
      self.__expressions = Expressions(alias)

    @property
    def alias(self):
      return self.__alias

    
    @property
    def character(self):
      return self.__character
  
    @alias.setter
    def setAlias(self, val):
      self.__alias = val 


    @character.setter
    def setCharacter(self, val):
      self.__character = val

    def getExpressionPNG(self, state):
      return self.expressions.states[state]

    
