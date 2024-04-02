label debug:

    $ bazooka.character("Te regalo una mierda")
    $ mc.addItemToInventory(Item("Mierda", "No veas que peste", -10))
    $ mc.addItemToInventory(Item("Poster de Jesucristo", "Poster con hombre barbudo, el letrero pone Junior Healy", 100))
    $ mc.printItems()
    $ optiongift1 = mc.getItemByIndex(0)
    $ optiongift2 = mc.getItemByIndex(1)
    menu:
        "[optiongift1.name], [optiongift1.description]" :
            $ bazooka.character("Era un regalo...")
            $ mc.gift(optiongift1, bazooka)
            

        "[optiongift2.name], [optiongift2.description]" :
            $ bazooka.character("Junior healy mi twink favvorito!!")
            $ mc.gift(optiongift2, bazooka)
    
    
    if bazooka.affinity > 50 :
        $ bazooka.character("Creo que me he cagado encima TE AMOOOO!!")
    
    $ bazooka.character("Bueno... prosigamos...")


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
    $ bazooka.character("Eres muy %s!" %  mc.getGenderedSuffixedWord("guap", "singular", False))
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