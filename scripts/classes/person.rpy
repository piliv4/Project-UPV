init python:
  class Person (object):
    """
      Representa a un personaje del juego.

      Atributos:
        name (string): Nombre del personaje
        affinity (num): Valor de 0 a 100 que determina el nivel de afinidad con el personaje principal 
    """
    def __init__(self, character, alias, name, surnames, age, affinity):
      self.alias = alias
      self.name = name
      self.surnames = surnames
      self.age = age
      self.__affinity = affinity
      self.__character = character

    @property
    def character(self):
      return self.__character
    
    @property
    def affinity(self):
      return self.__affinity

    @character.setter
    def setCharacter(self, val):
      self.__character = val

    @affinity.setter
    def addAffinity(self, val):
      self.__affinity += val

    
