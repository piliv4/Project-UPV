init python:
  class Person (object):
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
      self.name = name
      self.surnames = surnames
      self.age = age
      self.__alias = alias
      self.__affinity = affinity
      self.__character = character
      self.__expressions = Expressions(alias)

    @property
    def alias(self):
      return self.__affinity

    @property
    def affinity(self):
      return self.__affinity
    
    @property
    def character(self):
      return self.__character
  
    @alias.setter
    def addAlias(self, val):
      self.__alias += val 

    @affinity.setter
    def addAffinity(self, val):
      self.__affinity += val

    @character.setter
    def setCharacter(self, val):
      self.__character = val

    def getExpressionPNG(self, state):
      return self.expressions.states[state]

    
