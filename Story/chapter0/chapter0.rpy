label chapter0:
  scene bg room

  bazooka.character "Hola soy [bazooka.name] pero todos me llaman [bazooka.alias] y tengo [bazooka.age]"

  bazooka.character "Añade una historia, imágenes y música, ¡y puedes presentarlo al mundo!"

  menu:
    "Me quiero morir":
      call option_1
      return
    "Te comia las mierdas":
      call option_2
      return
  
  
  bazooka.character "Dios q puta mierdon"
  return

label option_1:
  bazooka.character "Te odio"
  return
  
label option_2:
  bazooka.character "ZAAAAAMNNNN"
  return
  