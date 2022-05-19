#Игра в Крестики-Нолики
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_field(field):
    print("- - - - - - -")
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("- - - - - - -")

def get_input(player_element):
    valid = False
    while not valid:
        player_answer = input(f"Куда поставим {player_element}?\n")
        try:
            player_answer = int(player_answer)
        except:
            print ("Необходимо ввести число от 1 до 9. Попробуйте, пожалуйста, еще раз.\n")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer-1]) not in "XO"):
                field[player_answer-1] = player_element
                valid = True
            else:
                print ("Эта клетка в поле уже занята")
        else:
            print ("Необходимо ввести число от 1 до 9. Попробуйте, пожалуйста, еще раз.\n")

def win_check(field):
    place = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in place:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False

def game(field):
    counter = 0
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
            get_input("X")
        else:
            get_input("O")
        counter += 1
        if counter > 4:
            tmp = win_check(field)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_field(field)

game(field)

