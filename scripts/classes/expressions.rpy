init python:
  class Expressions(object):
    """
      Representa las expressiones de un personaje.

      Atributos:
        alias (string): Alias del personaje funcionará como identificador del personaje 
    """
      def __init__(self, alias):
          self.alias = alias
          self.states = {
              # Esto lo que hace es en funcion de un nombre permite obtener una imagen
          
              # "idle": f"{alias}_idle.png",
              # "happy": f"{alias}_happy.png",
              # "sad": f"{alias}_sad.png",
              # "in_love": f"{alias}_in_love.png",
          }