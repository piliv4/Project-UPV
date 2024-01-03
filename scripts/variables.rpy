label defineCharacters:
  
  #DEFINE CHARACTERS

  $ mc = PersonMC( Character(""),"", "", "", 0 , "" )

  $ incognito = Person( Character ("???"), "", "", "",20)

  $ bazooka =  PersonPL( Character("Bazooka"),"bazookalias", "Bazooka", "Bazkoare", 22, 50)

  $ panero =  PersonPL( Character("Pan"),"Panalias", "Melnik", "Panero", 21, 50)  

  $ joseluis = PersonPL( Character("Lolero"),"loleralias", "Jose Luis", "García", 19, 50)

  return

# · DEFINE IMAGES ·

image negro = "negro.png"
#DEFINE BACKGROUNDS(BG)

image bg fuego = "bg_clase_con_fuego.png" 

image bg patio = "bg_exterior.png"

image bg patio medicos = "bg_medicos_en_upv.png"

#DEFINE CHARACTERS/PERSONAJES (CH/PJ)

#sprites Bazooka
image ch bazooka = "bazooka_idle.png"

#Sprites Jose Luis
image ch jl happy = "sprite_jl_contento.png"

image ch jl blush = "sprite_jl_sonrojado.png"

image ch jl surprised = "sprite_jl_sorprendido.png"

image ch jl think = "sprite_jl_pensando"

image ch jl annoyed = "sprite_jl_molesto"

image ch jl mansplaining = "sprite_jl_mansplaining"

#DEFINE SCENES (SC)

image sc tetaspan ="sc_tetaspan.png"

image sc tetaspanborrosas = "sc_tetaspanborrosas.png"

#DEFINE OPTIONS

#chapter 0


label option_1:
  #añadir sprite Jose Luis avergonzadao
  joseluis.character "Ay madre, qué vergüenza"
  
  joseluis.character "Te debo estar dando una primera impresión terrible."
  #ocultar sprite Jose Luis avergonzado
  return


label option_2:
  show ch jl surprised

  joseluis.character "¿No sabes qué es el LoL?"

  show ch jl mansplaining

  joseluis.character "League of Legends, también conocido por sus siglas LoL, es un videojuego multijugador de arena de batalla en línea desarrollado y publicado por Riot Games"
  joseluis.character "se suele denominar de forma despectiva a los jugadores de League of Legends o LoL con el término lolero"

  #añadir sprite Jose Luis avergonzado

  joseluis.character "Estoy hablando demasiado..."

  #ocultar sprite Jose Luis avergonzado
  return

label option_3:
  show ch jl happy

  joseluis.character "¡Me alegro!"
  
  hide ch jl happy
  return
  
label option_4:
  show ch jl think

  joseluis.character "Qué mal"

  hide ch jl think
  return

label option_5:
  bazooka.character "Te odio"
  return
  
label option_6:
  bazooka.character "ZAAAAAMNNNN"
  return
