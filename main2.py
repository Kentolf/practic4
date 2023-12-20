import random
def play_game():
    n = random.randint(4, 30)
    print("В куче", n, "камней")
    while n > 0:
        print("Осталось", n, "камней.")
        try:
            user_move = int(input("Ваш ход: "))
        except:
            print("Вы должны ввести число")
            exit()
        else:
            while user_move < 1 or user_move > 3 or user_move > n:
                print("Некорректный ввод. Пожалуйста, выберите число от 1 до", min(3, n))
                user_move = int(input("Ваш ход: "))
            n -= user_move
            if n == 0:
                print("Поздравляем! Вы победили!")
                break
            print("Осталось", n, "камней.")
            if n <= 3:
                program_move = n
            else:
                program_move = random.randint(1, 3)
            print("Ход программы:", program_move)
            n -= program_move
            if n == 0:
                print("К сожалению, вы проиграли.")
                break
play_game()
