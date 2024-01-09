label chapter0:
 
  scene bg fuego

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

  $ incognito.character("¿Cómo va %s %s!" % (mc.getArticle() , mc.getGenderedSuffixedWord("otr" , "singular")))

  scene sc tetaspan

  incognito.character "Esta/e sigue inconsciente"

  incognito.character "Aguanta un poco, en nada salimos"

  #Añadir sonido de varios golpes seguidos, como para indicar que se está 
  #rompiendo una puerta a golpes

  incognito.character "¡La puerta! La he abierto!"

  mc.character "Ugh... El humo"

  mc.character "Hace que se me cierren los ojos"

  scene sc tetaspanborrosas

  incognito.character "¿Tú que vas a abrir?"

  mc.character "no puedo más"

  #Añadir fundido en negro#

  scene negro

  #FIN ESCENA 1

  mc.character "..."

  scene bg patio medicos

  show ch jl happy

  incognito.character "Por fin te encuentro, no sabía que las ambulancias llegaban hasta aquí."


  $ incognito.character("Eres %s  que estaba dentro con nosotros, ¿no?" % mc.getArticle())  

  joseluis.character "soy [joseluis.name], de ingeniería informática."

  #Añadir sprite Jose Luis confundido

  joseluis.character "..."

  #ocultar sprite jose luis confundido

  show ch jl annoyed

  joseluis.character "Oye, que me llamo Jose Luis, no lolero."

  show ch jl think

  joseluis.character "¿Puedes hacer que ahí abajo deje de poner eso?"

  menu:
    "No, lo siento":
      call option_1
    "¿Lolero? ¿Qué es eso?":
      call option_2

  show ch jl happy

  joseluis.character "Bueno, es igual."

  joseluis.character "¿Tú eres...?"

  $ mc.name = renpy.input("Tu nombre por favor...", length=32)
  $ mc.name = mc.name.strip()

  $ mc.studies = renpy.input("Tus estudios...", length=32)
  $ mc.studies = mc.studies.strip()

  #INSERTAR NOMBRE DEL JUGADOR

  #INSERTAR ESTUDIOS DEL JUGADOR

  joseluis.character "Conque [mc.name]... Y estudias [mc.studies], nunca te había visto por aquí. A partir de ahora me fijaré más cuando pase por la uni. ¡Encantado!"


  show ch jl surprised

  joseluis.character "¡Eh! Te han dado una manta y todo, genial."
 
  show ch jl happy

  joseluis.character "Ah, por cierto... Esto es para tí"
  

  #     - Insertar imagen de jose luis dandote una taza de chocolate 

  # · Todo lo que hay que implementar sobre los OBJETOS ·
  #     - Insertar menú de objetos
  #     - Insertar taza de chocolate como objeto
  #     - Insertar tutorial para el menú de objetos

  #     - Insertar escena en caso de que el jugador le de la taza a jose luis


  show ch jl think

  joseluis.character "Espero que te encuentres mejor, casi me mareo cuando he visto que te desmayabas ahí dentro"



  menu:
    "Estoy mejor, gracias":
      call option_3
    "Todavía me siento sin fuerzas":
      call option_4

  show ch jl think

  joseluis.character "Pues si quieres, cuando te encuentres mejor podríamos quedar y hablar de lo que ha pasado ahí dentro…"

  #FIN CHAPTER 0
  return

 