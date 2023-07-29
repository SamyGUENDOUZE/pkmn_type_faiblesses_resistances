print("Si le pkmn n'a pas de deuxième type : tapez [aucun]")
print("Ecrire le type du pkmn sans accent\n")

while True : 

    type1 = input('Quel est le type #1 du pokemon : ')
    type2 = input('Quel est le type #2 du pokemon : ')
    print("")

    list_of_types = []
    list_of_weaknesses = []

    normal_type = "normal"
    normal_weaknesses = [1,1,1,1,1,1,2,1,1,1,1,1,1,0,1,1,1,1]
    list_of_types.append(normal_type)
    list_of_weaknesses.append(normal_weaknesses)

    plante_type = "plante"
    plante_weaknesses = [1,0.5,2,0.5,0.5,2,1,2,0.5,2,1,2,1,1,1,1,0.5,0.5]
    list_of_types.append(plante_type)
    list_of_weaknesses.append(plante_weaknesses)

    feu_type = "feu"
    feu_weaknesses = [1,0.5,0.5,2,1,0.5,1,1,2,1,1,0.5,1,1,1,1,0.5,1]
    list_of_types.append(feu_type)
    list_of_weaknesses.append(feu_weaknesses)

    eau_type = "eau"
    eau_weaknesses = [1,2,0.5,0.5,2,0.5,1,1,1,1,1,1,1,1,1,1,0.5,1]
    list_of_types.append(eau_type)
    list_of_weaknesses.append(eau_weaknesses)

    electrik_type = "electrik"
    electrik_weaknesses = [1,1,1,1,0.5,1,1,1,2,0.5,1,1,1,1,1,1,0.5,1]
    list_of_types.append(electrik_type)
    list_of_weaknesses.append(eau_weaknesses)

    glace_type = "glace"
    glace_weaknesses = [1,1,2,1,1,0.5,2,1,1,1,1,1,2,1,1,1,2,1]
    list_of_types.append(glace_type)
    list_of_weaknesses.append(glace_weaknesses)

    combat_type = "combat"
    combat_weaknesses = [1,1,1,1,1,1,1,1,1,2,2,0.5,0.5,1,1,0.5,1,2]
    list_of_types.append(combat_type)
    list_of_weaknesses.append(combat_weaknesses)

    poison_type = "poison"
    poison_weaknesses = [1,0.5,1,1,1,1,0.5,0.5,2,1,2,0.5,1,1,1,1,1,0.5]
    list_of_types.append(poison_type)
    list_of_weaknesses.append(poison_weaknesses)

    sol_type = "sol"
    sol_weaknesses = [1,2,1,2,0,2,1,0.5,1,1,1,1,0.5,1,1,1,1,1]
    list_of_types.append(sol_type)
    list_of_weaknesses.append(sol_weaknesses)

    vol_type = "vol"
    vol_weaknesses = [1,0.5,1,1,2,2,0.5,1,0,1,1,0.5,2,1,1,1,1,1]
    list_of_types.append(vol_type)
    list_of_weaknesses.append(vol_weaknesses)

    psy_type = "psy"
    psy_weaknesses = [1,1,1,1,1,1,0.5,1,1,1,0.5,2,1,2,1,2,1,1]
    list_of_types.append(psy_type)
    list_of_weaknesses.append(psy_weaknesses)

    insecte_type = "insecte"
    insecte_weaknesses = [1,0.5,2,1,1,1,0.5,1,0.5,2,1,1,2,1,1,1,1,1]
    list_of_types.append(insecte_type)
    list_of_weaknesses.append(insecte_weaknesses)

    roche_type = "roche"
    roche_weaknesses = [0.5,2,0.5,2,1,1,2,0.5,2,0.5,1,1,1,1,1,1,2,1]
    list_of_types.append(roche_type)
    list_of_weaknesses.append(roche_weaknesses)

    spectre_type = "spectre"
    spectre_weaknesses = [0,1,1,1,1,1,0,0.5,1,1,1,0.5,1,2,1,2,1,1]
    list_of_types.append(spectre_type)
    list_of_weaknesses.append(spectre_weaknesses)

    dragon_type = "dragon"
    dragon_weaknesses = [1,0.5,0.5,0.5,0.5,2,1,1,1,1,1,1,1,1,2,1,1,2]
    list_of_types.append(dragon_type)
    list_of_weaknesses.append(dragon_weaknesses)

    tenebres_type = "tenebres"
    tenebres_weaknesses = [1,1,1,1,1,1,2,1,1,1,0,2,1,0.5,1,0.5,1,2]
    list_of_types.append(tenebres_type)
    list_of_weaknesses.append(tenebres_weaknesses)

    acier_type = "acier"
    acier_weaknesses = [0.5,0.5,2,1,1,0.5,2,0,2,0.5,0.5,0.5,0.5,1,0.5,1,0.5,0.5]
    list_of_types.append(acier_type)
    list_of_weaknesses.append(acier_weaknesses)

    fee_type = "fee"
    fee_weaknesses = [1,1,1,1,1,1,0.5,2,1,1,1,0.5,1,1,0,0.5,2,1]
    list_of_types.append(fee_type)
    list_of_weaknesses.append(fee_weaknesses)

    aucun_type = "aucun"
    aucun_weaknesses = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    list_of_types.append(aucun_type)
    list_of_weaknesses.append(aucun_weaknesses)

    # Pour faire correspondre les index du type1 et type2 dans la liste des types
    index = list_of_types.index(type1)
    index2 = list_of_types.index(type2)

    # Pour accéder à la liste des faiblesses correspondantes
    weaknesses = list_of_weaknesses[index]
    weaknesses2 = list_of_weaknesses[index2]

    double_weakness_list = []
    weakness_list = []
    double_resistance_list = []
    resistance_list = []
    immunity_list = []

    for i, (j, k) in enumerate(zip(weaknesses, weaknesses2)):
        if j * k == 0:
            immunity_list.append(list_of_types[i])
        elif j * k == 0.25:
            double_resistance_list.append(list_of_types[i])
        elif j * k == 0.5:
            resistance_list.append(list_of_types[i])
        elif j * k == 2:
            weakness_list.append(list_of_types[i])
        elif j * k == 4:
            double_weakness_list.append(list_of_types[i])

    if len(double_weakness_list) != 0 :
        print("Double(s) faiblesse(s) : ", ", ".join(double_weakness_list), "\n")
    if len(weakness_list) != 0 :
        print("Faiblesse(s) : ", ", ".join(weakness_list), "\n")
    if len(double_resistance_list) != 0 :
        print("Double(s) résistance(s) : ", ", ".join(double_resistance_list), "\n")
    if len(resistance_list) != 0 :
        print("Résistance(s) : ", ", ".join(resistance_list), "\n")
    if len(immunity_list) != 0 : 
        print("Immunité(s) : ", ", ".join(immunity_list), "\n")    