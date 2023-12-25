label chapter0:
 
  
  scene bg_fuego

  mc.character "No"

  mc.character "No, no, no"

  mc.character "Mierda, esto no puede estar pasando"

  incognito.character "¡Cuidado!"

  scene negro

  #Añadir sonido de golpetazo

  mc.character "¡Agh!"

  incognito.character "¡¿ Dónde está el extintor?!"

  incognito.character "Dios mío, ¡fuego!"

  #Añadir sonido de metal pipe

  incognito.character "¿Qué ha sido eso?"

  #Añadir sonido de notificacion del berreal

  incognito.character "¿Quién pal berreal?"

  incognito.character "Tío, no es momento de berreal"

  incognito.character "..."

  incognito.character "Bueno, en realidad no me importa salir"

  incognito.character "¿Qué estáis haciendo?"

  #Añadir sonido de foto

  incognito.character "..."

  incognito.character "Que alguien me saque de aquí, estáis todos locos"

  incognito.character "¡El extintor!, lo he encontrado aquí"

  incognito.character "Pásamelo, corre"

  #Añadir sonido de fsssshhhh de extintor

  #En la siguiente línea de diálogo habría que usar pronombres para el mc
  # y no sé como hacer eso todavía, así que lo dejo así

  incognito.character "¿Cómo va el/la/le otro/otra/otre?"

  scene sc_tetaspan

  incognito.character "Esta/e sigue inconsciente"

  incognito.character "Aguanta un poco, en nada salimos"

  #Añadir sonido de varios golpes seguidos, como para indicar que se está 
  #rompiendo una puerta a golpes

  incognito.character "¡La puerta! La he abierto!"

  mc.character "Ugh... El humo"

  mc.character "Hace que se me cierren los ojos"

  scene sc_tetaspanborrosas

  incognito.character "¿Tú que vas a abrir?"

  mc.character "no puedo más"

  scene bg_patio

  show ch_bazooka

  bazooka.character "¿Realmente se está poniendo el sol, o simplemente le está dando a la luna la oportunidad de brillar?"
  
  bazooka.character "Hola soy [bazooka.name] pero todos me llaman [bazooka.alias] y tengo [bazooka.age]"

  joseluis.character "Hola dame tu @ del  lol chama"

  panero.character "La vida me da miedo"
  
  menu:
    "Me quiero morir":
      call option_1
    "Te comia las mierdas":
      call option_2
  
  
  bazooka.character "Dios q puta mierda"
  return

label option_1:
  bazooka.character "Te odio"
  return
  
label option_2:
  bazooka.character "ZAAAAAMNNNN"
  return

 