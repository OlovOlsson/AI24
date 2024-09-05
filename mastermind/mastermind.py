import random

# Slumpar fram en rad som spelaren ska försöka gissa.
# Denna metod kan utvecklas beroende på vilka regler som gäller för raden.
def get_random_row(valid_colors:list, elements_in_row:int): 
    the_row = [random.choice(valid_colors) for i in range(elements_in_row)]
   
    return the_row

# Kontrollerar om den av spelaren inmatade raden är giltig. Returnerar False eller True
def check_if_valid(my_guess:list, valid_colors:list, elements_in_row:int):
    if len(my_guess)!=elements_in_row:
        return False
    
    for color in my_guess:
        if not color in valid_colors:
            return False
    
    return True


# Rättar den inmatade raden och skriver ut resultatet
def check_row(guessed_row:list, correct_row:list):
    
    copy_of_guess = guessed_row.copy()
    

    right_place = 0 #Rätt färg på rätt plats 
    right_color = 0 # Rätt färg men på fel plats


    for index, (guessed_color, correct_color) in enumerate(zip(guessed_row, correct_row)):
        if guessed_color == correct_color:
            right_place +=1
            guessed_row[index]="0"
            correct_row[index] ="0"


 
    
    for i, guessed_color in enumerate(guessed_row):
        for j, correct_color in enumerate(correct_row):

            if guessed_color != "0" and correct_color!="0" and guessed_color==correct_color:
                right_color +=1


                guessed_row[i] = "0"
                correct_row[j] = "0"

                break


    print(f'Du har {right_place} rätt färg på rätt plats')
    print(f'Du har {right_color} rätt färg på fel plats')
    print(f'Här är din rad: {copy_of_guess}')
    print()






def main():

    num_of_row = 12



    valid_colors = ['1','2','3','4','5','6']
    elements_in_row = 4

    the_row = get_random_row(valid_colors, elements_in_row)
    #the_row = ['1','2','3','4']  # Kan avkommenteras för att kontrollera programmet


    for attempts_left in range(num_of_row,0,-1):
        print(f'Du har {attempts_left} försök kvar ')
        while True:
            raw_input = input("Gissa på en rad med fyra sifror 1-6 (t.ex. 1561)")

            my_guess = [i for i in raw_input]

            valid_guess = check_if_valid(my_guess, valid_colors, elements_in_row)

            if valid_guess:
                break
            else:
                print('Ogilitigt försök, försök igen')
        

        if my_guess== the_row:
            print(f'Grattis du hittade färgföljden på {num_of_row-attempts_left+1} försök.')
            print(f'Den rätta färgföljden var {the_row}')
            break
        else:
            check_row(my_guess.copy(), the_row.copy())


    else:
        # Körs enbart om den rätta raden inte hittades.
        print("Du har nu slut på försök, du lyckades inte hitta färgföljden denna gång.")


if __name__=='__main__':
    main()

