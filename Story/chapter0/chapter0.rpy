label chapter0:
 
  scene bg_fuego

  mc.character "No"

  mc.character "No, no, no"

  mc.character "Mierda, esto no puede estar pasando"

  incognito.character "¡Cuidado!"

  scene negro

  play sound slip

  mc.character "¡Agh!"

  incognito.character "¡¿ Dónde está el extintor?!"

  incognito.character "Dios mío, ¡fuego!"

  play sound metal_pipe

  incognito.character "¿Qué ha sido eso?"

  play sound bereal

  incognito.character "¿Quién pal berreal?"

  incognito.character "Tío, no es momento de berreal"

  incognito.character "..."

  incognito.character "Bueno, en realidad no me importa salir"

  incognito.character "¿Qué estáis haciendo?"

  play sound click_photo

  incognito.character "..."

  incognito.character "Que alguien me saque de aquí, estáis todos locos"

  incognito.character "¡El extintor!, lo he encontrado. Está por aquí"

  incognito.character "Pásamelo, corre"

  play sound fire_extinguisher

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

  #Añadir fundido en negro#

  scene negro

  #FIN ESCENA 1

  mc.character "..."

  scene bg_patio_medicos

  show ch_jl_happy

  incognito.character "Por fin te encuentro, no sabía que las ambulancias llegaban hasta aquí."

  incognito.character "Eres el/la/le que estaba dentro con nosotros, ¿no?"

  joseluis.character "soy Jose Luis, de ingeniería informática."

  joseluis.character "¿Tú eres...?"

  #INSERTAR NOMBRE DEL JUGADOR

  #INSERTAR ESTUDIOS DEL JUGADOR

  joseluis.character "Conque (nombre del jugador)... Y estudias (nombre de los estudios), nunca te había visto por aquí. A partir de ahora me fijaré más cuando pase por la uni. ¡Encantado!"

  show ch_jl_surprised

  joseluis.character "¡Eh! Te han dado una manta y todo, genial."

  hide ch_jl_surprised 
 
  show ch_jl_happy

  joseluis.character "Ah, por cierto... Esto es para tí"
  

  #     - Insertar imagen de jose luis dandote una taza de chocolate 

  # · Todo lo que hay que implementar sobre los OBJETOS ·
  #     - Insertar menú de objetos
  #     - Insertar taza de chocolate como objeto
  #     - Insertar tutorial para el menú de objetos

  #     - Insertar escena en caso de que el jugador le de la taza a jose luis


  hide ch_jl_happy

  show ch_jl_think

  joseluis.character "Espero que te encuentres mejor, casi me mareo cuando he visto que te desmayabas ahí dentro"

  menu:
    "Estoy mejor, gracias":
      call option_1
    "Todavía me siento sin fuerzas":
      call option_2

  show ch_jl_think

  joseluis.character "Pues si quieres, cuando te encuentres mejor podríamos quedar y hablar de lo que ha pasado ahí dentro…"

  scene bg_patio

  show ch_bazooka

  bazooka.character "¿Realmente se está poniendo el sol, o simplemente le está dando a la luna la oportunidad de brillar?"
  
  bazooka.character "Hola soy [bazooka.name] pero todos me llaman [bazooka.alias] y tengo [bazooka.age]"

  joseluis.character "Hola dame tu @ del  lol chama"

  panero.character "La vida me da miedo"
  
  menu:
    "Me quiero morir":
      call option_3
    "Te comia las mierdas":
      call option_4
  
  
  bazooka.character "Dios q puta mierdas soy el ultimo return"


  #FIN CHAPTER 0
  return

 