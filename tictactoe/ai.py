'''
Napiš funkci tah_pocitace, která dostane řetězec s herním polem, vybere pozici, na kterou hrát, a vrátí
herní pole se zaznamenaným tahem počítače.
Použij jednoduchou náhodnou „strategii”:
1. Vyber číslo od 0 do 19.
2. Pokud je dané políčko volné, hrej na něj.
3. Pokud ne, opakuj od bodu 1.
Hlavička funkce by tedy měla vypadat nějak takhle:
def tah_pocitace(pole):
"Vrátí herní pole se zaznamenaným tahem počítače"
'''

import random

def run_pc(field):
    symbol = 'o'
    import random
    while True:
        try:
            ask_number = random.randint(0,19)
            if field[ask_number] == '-':
                field = (field[:ask_number] + symbol + field[ask_number + 1:])
                break
            else: 
                message = print('You have chosen a position', ask_number, 'which is taken. You go again.')
                pass
        except ValueError:
            print('What kind of error is this?!')
            pass
    return field
#run_pc('-------------------o')

'''
#not finished, not used
def run_pc_strategy(field):
    if "-" not in field:
        raise ValueError("It's a tie!")
    while True:
        if 'xx-' in field:
            position = field.index('xx-') + 2 
            field = (field[:position] + 'o' + field[position + 1:])
        elif '-xx' in field:
            position = field.index('-xx')
            field = (field[:position] + 'o' + field[position + 1:])
        elif '-xx-' in field:
            decision = random.randint(0,2)
            if decision == 1:
                position = field.index('-xx-')
            if decision == 0:
                position = field.index('-xx-') + 2
            field = (field[:position] + 'o' + field[position + 1:])
        elif 'oxx-' in field:
            position = field.index('oxx-') + 3
            field = (field[:position] + 'o' + field[position + 1:])
        elif '-xxo' in field: 
            position = field.index('-xxo')
            field = (field[:position] + 'o' + field[position + 1:])
            
        else:
            position = random.randint(0,19)
            field = (field[:position] + 'o' + field[position + 1:])
            
    return field
 '''
