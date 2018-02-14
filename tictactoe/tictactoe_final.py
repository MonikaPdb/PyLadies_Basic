'''
misto pro import knihoven :)
'''

import sys 
from ai import run_pc
'''
Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19), a symbol (x nebo o) a vrátí
herní pole (t.j. řetězec) s daným symbolem umístěným na danou pozici
'''

def run(field, number, symbol):
    while 'xxx' or 'ooo' not in field: 
        field = (field[:number] + symbol + field[number + 1:])
        return field
#run('-------------', 5, 'x')
    

'''
Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec
podle stavu hry:
'''
def resume(field):
    if 'xxx' in field:
        return 'x'
    elif 'ooo' in field: 
        return 'o'
    elif '-' not in field:
        return 'tie'
    else:
        return '!'
#resume('xoxoxoxoxox')

'''
Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče, na kterou pozici chce hrát,
a vrátí herní pole se zaznamenaným tahem hráče.
Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená políčka. Pokud uživatel
zadá špatný vstup, funkce mu vynadá a zeptá se znova.
'''

def run_player(field):
    symbol = 'x'
    while True:
        try:
            ask_number = int(input('Which position do you want to have your symbol this turn? '))
            if True: 
                if ask_number >= 0 and ask_number <= 19:
                    if field[ask_number] == '-':
                        field = (field[:ask_number] + symbol + field[ask_number + 1:])
                        break
                    else:
                        message = print('Invalid move, go again: ')
                        pass
                else:
                    message = print('Invalid move, go again: ')
                    pass
        except ValueError: 
            print('You have not inserted a number. Try again: ')
            pass
    return field
#run_player('--------x---------')

'''
Creates a new field
'''
def resetfield():
    return ('--------------------')
         
'''
Napiš funkci piskvorky1d, která vytvoří řetězec s herním polem a střídavě volá funkce tah_hrace a
tah_pocitace, dokud někdo nevyhraje nebo nedojde k remíze.
Nezapomeň kontrolovat stav hry po každém tahu.
'''

def tictactoe1D():
  
  while True:
    print("This is the game's field:")
    key = '0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19'
    print(key)
    field = 20*"-"
    print(field[0], ' ', field[1], ' ', field[2], ' ', field[3], ' ', field[4], ' ', field[5], ' ', field[6], ' ', field[7], ' ', field[8], ' ', field[9], ' ', field[10], ' ', field[11], ' ', field[12], ' ', field[13], ' ', field[14], ' ', field[15], ' ', field[16], ' ', field[17], ' ', field[18], ' ', field[19])

    while True:
      field=run_player(field)
      print(key)
      print('\n')
      print(field[0], ' ', field[1], ' ', field[2], ' ', field[3], ' ', field[4], ' ', field[5], ' ', field[6], ' ', field[7], ' ', field[8], ' ', field[9], ' ', field[10], ' ', field[11], ' ', field[12], ' ', field[13], ' ', field[14], ' ', field[15], ' ', field[16], ' ', field[17], ' ', field[18], ' ', field[19])
      check=resume(field)
      if check == 'tie':
        print("It's a tie!") 
      vyhra_hrace="xxx"
      if vyhra_hrace in field:
          print("Gamer x wins.")
          next = input("Press Q to quit, any other key to play again. ")
          if next.lower() == 'q':
              sys.exit()
              break
          else:
              field = resetfield()
         
      field = run_pc(field)
      print(key)
      print('\n')
      print(field[0], ' ', field[1], ' ', field[2], ' ', field[3], ' ', field[4], ' ', field[5], ' ', field[6], ' ', field[7], ' ', field[8], ' ', field[9], ' ', field[10], ' ', field[11], ' ', field[12], ' ', field[13], ' ', field[14], ' ', field[15], ' ', field[16], ' ', field[17], ' ', field[18], ' ', field[19])
      check=resume(field)
      if check == 'tie':
        print("It's a tie!") 
      vyhra_pocitace="ooo"
      if vyhra_pocitace in field:
          print("Gamer o wins.")
          next = input("Press Q to quit, any other key to play again. ")
          if next.lower() == 'q':
              sys.exit()
              break
          else:
              field = resetfield()
          

