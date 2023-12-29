label debug:
    menu:
        "Soy moger":
            call female
        "Soy onbre":
            call male
        "Soy no binarie":
            call nonbinary
    
    
    return
      
    
    bazooka.character "nice"
    return

    label female:
        $ mc.gender = "female"
        $ bazooka.character("Te trataré de %s!" % mc.getPronoun())
        return
    
    label male:
        $ mc.gender = "male"
        $ bazooka.character("Te trataré de %s!" % mc.getPronoun())
        return
      
    label nonbinary:
        $ mc.gender = "non-binary"
        $ bazooka.character("Te trataré de %s!" % mc.getPronoun()) 
        return