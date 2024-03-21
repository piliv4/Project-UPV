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

  $ incognito.character("¿Cómo va %s %s?" % (mc.getArticle() , mc.getGenderedSuffixedWord("otr" , "singular", False)))

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


  $ incognito.character("Eres %s que estaba dentro con nosotros, ¿no?" % mc.getArticle())  

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

  joseluis.character "Pues si quieres, cuando te encuentres mejor podríamos quedar y hablar de lo que ha pasado ahí dentro…."

  #[SPRITE JOSE LUIS SONROJADO] 

  joseluis.character "Perdona, inhalar todo ese humo me ha dejado tonto perdido."

  incognito.character "Como si no lo estuvieras ya de antes."

  #[SPRITE JOSE LUIS MOLESTO]

  joseluis.character "¡Bazooka! Tú a callar."

  #[SPRITE BAZOOKA, CHARMING]

  bazooka.character "Buenas, soy Bazooka, de artes. Estoy currándomelo para ser cada día más rarito."

  #[SPRITE PAN SIGH]

  incognito.character "Pues lo estás clavando, tío."

  #[SPRITE PAN: CONTENTO]

  panero.character "Yo soy Pan, de agrónomos, encantado."

  #[SPRITE PAN: PENSATIVO]

  panero.character "Parece que nosotros cuatro somos los únicos que nos hemos visto envueltos en este lío…."

  joseluis.character "¿Cómo sabes eso, Einstein?"

  #[SPRITE PAN: MOCKING]

  panero.character "Porque le he preguntado al guardia de seguridad hace un rato, Elvis."

  #[SPRITE JL: CONFUSO]

  joseluis.character "…."


  joseluis.character "¿Elvis?"

  #[SPRITE PAN: MOLESTO]

  panero.character "Quien sea, no se me ocurre gente inteligente ahora mismo, que estoy nervioso."

  #[SPRITE BAZOOKA: ORGULLOSO]

  bazooka.character "Pero si me tienes aquí delante, bobo."

  #[SPRITE PAN: MOLESTO]

  panero.character "Eres la última persona en la que pensaría."

  #[SPRITE JL: NEUTRAL]

  joseluis.character "Chicos, cortad el rollo. Vamos a lo importante."
  joseluis.character "¿Te ha dicho algo más el de seguridad?"

  #[SPRITE PAN: PENSATIVO]

  panero.character "Sí."
  panero.character "Me ha dicho que dentro de un rato pasarán a hacernos preguntas sobre lo que sabemos del incendio."

  #[SPRITE JL: Pensativo]

  joseluis.character "El incendio…."

  #[SPRITE JL: NEUTRAL]

  joseluis.character "Ha pasado todo muy rápido, casi se me sale el corazón del pecho. Lo tengo todo nublado, prácticamente no me acuerdo de nada."

  #[SPRITE BAZOOKA: NEUTRAL]

  bazooka.character "[mc.name], ¿Tú recuerdas algo?"

  mc.character "Lo cierto es que yo también lo tengo borroso, pero si me esfuerzo seguro que recuerdo algo."

  #CAMBIO DE ESCENA: FLASHBACK A CUANDO ESTABA EN LA BIBLIOTECA (aquí se comienza a explicar la premisa principal)

  #ESCENA: biblioteca, plano general

  mc.character "Había suspendido 2 asignaturas y tengo los exámenes de recuperación la semana que viene. Así que fui a la biblioteca a estudiar."

  #ESCENA: Sala de biblioteca

  mc.character "Entré a una de las salas de estudio, a la M22."

  panero.character "Sí, nosotros también fuimos allí. Nos gusta ir a esa porque es pequeña y está más alejada."
  panero.character "Parece que hay más privacidad, así te puedes concentrar mejor."

  #ESCENA: Mesa de biblioteca

  mc.character "Me senté en una de las mesas."
  mc.character "Saqué el estuche, la libreta, el portátil y su cargador."
  mc.character "!!!"

  joseluis.character "¿Qué pasa? ¿Te has acordado de algo?"

  #ESCENA: imagen ENCHUFES conectados

  mc.character "Cuando fui a poner a cargar el portátil, me di cuenta de que el enchufe de mi mesa no funcionaba, así que lo puse a cargar en la mesa de detrás."

  bazooka.character "Donde estábamos nosotros…."

  mc.character "No le había dado importancia al principio, pero quizás el enchufe que no funcionaba tiene algo que ver con lo del incendio."

  joseluis.character "Deberíamos comentarle eso al guardia."

  bazooka.character "¡Ah! Me acabo de acordar."
  bazooka.character "¡Tu móvil! También dejaste cargando el móvil en nuestra mesa."

  mc.character "¡Es verdad, mi móvil!"
  mc.character "Lo dejé cargando allí porque el cargador no era lo suficientemente largo como para llegar hasta mi mesa. Se quedó donde estábais."

  panero.character "¡Cierto!"
  panero.character "¿Recuerdas algo más?"

  mc.character "No mucho, en realidad. Empecé a estudiar y estuve así una media hora, hasta que empezó a sonar la alarma y a oler a quemado."

  #ESCENA: Imagen fuego en biblioteca

  mc.character "Desde ese momento, todo lo que recuerdo son imágenes borrosas sobre el incendio."

  #ESCENA: negro

  #CAMBIO DE ESCENA: Vuelta al presente. 

  #ESCENA:imagen con ambulancias y tal

  #SPRITE: [PAN PENSATIVO]

  panero.character "Lo que más me preocupa de todo esto son nuestras cosas."

  #SPRITE : BAZOOKA PENSATIVO

  bazooka.character "Sí, las necesitamos para estudiar."

  #SPRITE LOLERO: MUY PREOCUPADO

  joseluis.character "El portátil, el móvil, el ratón…."
  joseluis.character "Joder, tengo ahí hasta la alfombrilla buena."

  #SPRITE LOLERO: MUY PREOCUPADO -> UNHINGED

  joseluis.character "¿Cuándo la voy a volver a ver?"
  joseluis.character "Peor… ¿Y si la he perdido en el incendio?"
  joseluis.character "Tío, mi movil… ¿Qué voy a hacer con las diarias?"

  #SPRITE: NEUTRAL

  panero.character "Calma, [joseluis.name]. Vamos a hablar con el guardia, seguro que nos dará una solución."

  #SPRITE LOLERO: CATATÓNICO

  joseluis.character "Voy a perder la racha, no voy a conseguir supermonedas suficientes, no voy a poder conseguir a Kasinos…."

  #SPRITE LOLERO: AÚN MÁS CATATÓNICO

  joseluis.character "¡¿Qué voy a hacer sin Kasinos?! No me voy a poder pasar esta zona, además -."

  #SPRITE PAN: PREOCUPADO

  panero.character "[bazooka.name], llama al guardia, antes de que le dé algo a [joseluis.name]"

  #SPRITE GUARDIA O IMAGEN CURRADA GUARDIA?

  #GP = GUARDIA PROSEJUR (evitando copy jeje)

  gp.character "Bueno chavales, ¿Estáis mejor después de todo este susto?"

  panero.character "Sí, gracias agente."

  joseluis.character "[panero.name], no es un agente, es un guardia de la uni. Lo vemos todos los días, ¿recuerdas?"

  #¿Esto sería mejor que lo dijera Bazooka? y que lolero no diga nada? Así es como que se mantiene el chiste de que el lolero sigue catatónico

  bazooka.character "No se preocupe agente, mi amigo es así de despistado todos los días, está bien, no tiene de qué preocuparse."

  joseluis.character "Pero bueno, ¿yo hablo para las paredes? ¡No es un agente!"

  bazooka.character "Prosiga agente."

  gp.character "…."
  gp.character "Veo que estáis mejor. ¿Tú también, el/la/le de atrás?"

  mc.character "Sí, estoy mejor, gracias."

  gp.character "Fenomenal."
  gp.character "Pues dado que sois los únicos afectados, necesito que poco a poco y de la forma más objetiva posible, me vayáis contando lo que recordáis que ha pasado antes, durante y después del incendio."

  panero.character "Por supuesto señor, verá…."

  #ESCENA: IMAGEN EN NEGRO

  mc.character "Le contamos al guardia todo lo que había pasado."
  mc.character "Que estábamos en la M22, en las mesas del fondo, le contamos sobre el enchufe que no funcionaba y cómo al cabo del rato, todo parecía estar en llamas…."

  #ESCENA: IMAGEN ESPECIAL DEL GUARDIA

  gp.character "Vaya, conque un enchufe que podría estar en mal estado."
  gp.character "Le comentaré eso a los bomberos."

  joseluis.character "¡Espere!"
  joseluis.character "¿Y nuestras cosas?"

  gp.character "Mucho me temo que no vais a poder acceder a vuestras cosas hasta que los bomberos digan lo contrario."
  gp.character "Además, teniendo en cuenta lo que me habéis comentado, si no está ya hecho, probablemente hagan un corte de luz en todo el edificio."
  gp.character "Calculo que no podréis acceder en, como mínimo, 72 horas."

  bazooka.character "72 horas y es jueves."
  bazooka.character "Eso significa que podremos ir a recuperar nuestras cosas el domingo."
  bazooka.character "Y el domingo estará todo cerrado, con lo que tampoco podremos acceder."

  panero.character "Asi que nos queda el lunes."




  #FIN CHAPTER 0
  return

 