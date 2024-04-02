init python:

  #Person - Personajes normales - Categoría para personajes que NO necesiten del atributo AFINIDAD, como el main character o realmente cualquier otro que no sean los 3 LI
  class Item (object):
    """
      Representa a un objeto del juego.

      Atributos:
        name (srting) : Nombre del ítem
        description (string): Descripción del item
        baseAffinty (string): Afinidad base a sumar
    """
    def __init__(self, name, description, baseAffinity):
      self.name = name
      self.description = description
      self.baseAffinity = baseAffinity

    @property
    def baseAffinity(self):
      return self.__baseAffinity

    @baseAffinity.setter
    def baseAffinity(self, val):
      self.__baseAffinity = val 


    

