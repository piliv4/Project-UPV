label debug:
    menu:
        "Soy moger":
            call female
        "Soy onbre":
            call male
        "Soy no binarie":
            call nonbinary
    
    

    bazooka.character "nice"
    $ bazooka.character("Te trataré de %s!" % mc.getPronoun())
    $ bazooka.character("Tu articulo será %s!" % mc.getArticle())
    $ bazooka.character("Eres muy %s!" %  mc.getGenderedSuffixedWord("guap", "singular"))
    return
      
    

    label female:
        $ mc.gender = "female"
        return
    
    label male:
        $ mc.gender = "male"
        return
      
    label nonbinary:
        $ mc.gender = "non-binary"
        return