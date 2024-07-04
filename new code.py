import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.tanks = 0
        self.death_rays = 0

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def count_dice_types(dice):
    people = dice.count(1)
    cows = dice.count(2)
    chickens = dice.count(3)
    death_rays = dice.count(4)
    return people, cows, chickens, death_rays

def calculate_score(people, cows, chickens):
    score = people + cows + chickens
    if people > 0 and cows > 0 and chickens > 0:
        score += 3
    return score

def play_round(player, dice):
    print(f"\n{player.name}'ход:")
    while True:
        print(f"У тебя {len(dice)} осталось.")
        print("1. Бросьте все кости")
        print("2. Отложить танки")
        print("3. Отложить один тип кубиков")
        print("4. Конец хода")

        choice = input("Выбери число (1-4): ")

        if choice == '1':
            if len(dice) == 0:
                print("У тебя не осталось кубиков! Конец хода.")
                break
            else:
                dice = roll_dice(len(dice))
                print("Ты ходишь:", dice)
        elif choice == '2':
            tanks = dice.count(5)
            player.tanks += tanks
            dice = [d for d in dice if d != 5]
            print(f"Было отложено {tanks} танков.")
        elif choice == '3':
            people, cows, chickens, death_rays = count_dice_types(dice)
            if people > 0 or cows > 0 or chickens > 0:
                print("1. Люди (1)")
                print("2. Коровы (2)")
                print("3. Курицы (3)")
                print("4. Лучи смерти (4)")

                type_choice = input("Введите тип кубиков, которые нужно отложить(1-4): ")
                if type_choice == '1' and people > 0:
                    player.people += people
                    dice = [d for d in dice if d != 1]
                elif type_choice == '2' and cows > 0:
                    player.cows += cows
                    dice = [d for d in dice if d != 2]
                elif type_choice == '3' and chickens > 0:
                    player.chickens += chickens
                    dice = [d for d in dice if d != 3]
                elif type_choice == '4':
                    player.death_rays += death_rays
                    dice = [d for d in dice if d != 4]
                else:
                    print("Неверный выбор. Пожалуйста, попробуйте еще раз.")
            else:
                print("В этом ходу вы не можете отложить ни один из этих типов кубиков.")
        elif choice == '4':
            print("Конец хода.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")

    if player.tanks > player.death_rays:
        print(f"{player.name} У вас нет очков в этом раунде.")
        player.score = 0
    else:
        player.score += calculate_score(player.people, player.cows, player.chickens)
        print(f"{player.name}очков в этом раунде: {player.score}")

def main():
    num_players = int(input("Количество игроков: "))
    players = []
    for i in range(num_players):
        name = input(f"Введите {i+1}'имя: ")
        players.append(Player(name))

    game_over = False
    while not game_over:
        for player in players:
            dice = roll_dice(13)
            play_round(player, dice)
            if player.score >= 25:
                game_over = True
                print(f"\nКонец игры! {player.name} победил!")
                break

    if game_over and len([p for p in players if p.score >= 25]) > 1:
        print("\nЭто ничья, переброс кубиков.")
        tied_players = [p for p in players if p.score >= 25]
        for player in tied_players:
            player.death_rays = roll_dice(6).count(4)
        winner = max(tied_players, key=lambda p: p.death_rays)
        print(f"\n{winner.name} выигрывает тай-брейк!")

if __name__ == "__main__":
    main()

