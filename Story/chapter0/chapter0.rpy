label chapter0:
  scene picture_1

  scene bg_exterior

  show bazooka_idle

  bazooka.character "¿Realmente se está poniendo el sol, o simplemente le está dando a la luna la oportunidad de brillar?"
  
  bazooka.character "Hola soy [bazooka.name] pero todos me llaman [bazooka.alias] y tengo [bazooka.age]"

  joseluis.character "Hola dame tu @ del  lol chama"

  Niniopan.character "La vida me da miedo"
  
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
  