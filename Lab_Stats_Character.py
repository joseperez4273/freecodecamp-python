full_dot = '●'
empty_dot = '○'
def create_character(nombre, fuerza, inteligencia, carisma):
    if not isinstance(nombre, str):
        return 'The character name should be a string'
    elif nombre == "":
        return 'The character should have a name'
    elif len(nombre) > 10:
        return 'The character name is too long' 
    elif " " in nombre:
        return 'The character name should not contain spaces'
    if not isinstance(fuerza, int) or not isinstance(inteligencia, int) or not isinstance(carisma, int):
        return 'All stats should be integers'
    elif any(stat < 1 for stat in [fuerza, inteligencia, carisma]):
        return 'All stats should be no less than 1'
    elif any(stat > 4 for stat in [fuerza, inteligencia, carisma]) :
        return 'All stats should be no more than 4'
    elif fuerza + inteligencia + carisma != 7:
        return 'The character should start with 7 points'

    return(
        f'{nombre}\n'
        f'STR {full_dot * fuerza}{empty_dot * (10 - fuerza)}\n'
        f'INT {full_dot * inteligencia}{empty_dot * (10 - inteligencia)}\n'
        f'CHA {full_dot * carisma}{empty_dot * (10 - carisma)}'
    )
print(create_character('Ren', 4, 2, 1))
    
