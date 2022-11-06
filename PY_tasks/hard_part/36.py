# Помните игру с конфетами из модуля "Математика и Информатика"?
# a) Создайте такую игру для игры человек против человека
# b) Добавьте игру против бота
# c) Подумайте как наделить бота "интеллектом"

# a) Создайте такую игру для игры человек против человека:
# import random
#
# greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!"\n'
#             'Основные правила игры:\n'
#             'Нам будет дано некоторое количество конфет,\n'
#             'за один ход мы можем взять не более определённого количества, '
#             'о котором мы с вами договоримся.\n'
#             'Проигрывает тот, кто забирает последнюю конфету\n.'
#             'Итак, начнём!')
#
# messages = ["It's your turn to take candies", 'Take candies',
#             'How many candies will you take?', 'Take candies, no shame!', "It's your turn!"]
#
#
# def play_game(n, m, players, messages):
#     count = 0
#
#     while n > 0:
#         print(f'{players[count % 2]}, {random.choice(messages)}')
#         move = int(input())
#         if move > n or move > m:
#             print(f'That is too much! You can take no more than {m} candy(-ies), we have {n} candy(-ies) total')
#             attempt = 3
#             while attempt > 0:
#                 if n >= move <= m:
#                     break
#                 print(f'Try again, you have {attempt} tries')
#                 move = int(input())
#                 attempt -= 1
#             else:
#                 return print(f'You have no attempts. Game over!')
#         n = n - move
#         if n > 0:
#             print(f'{n} candy(-ies) left')
#         else:
#             print('All candies are gone...')
#         count += 1
#     return players[not count % 2]
#
#
# if __name__ == '__main__':
#     print(greeting)
#
#     player1 = input('Player 1:\n')
#     player2 = input('Player 2:\n')
#     players = [player1, player2]
#
#     candies = int(input('How many candies?\n '))
#     max_candies = int(input('How many candies you allowed to take per turn?\n '))
#
#     winner = play_game(candies, max_candies, players, messages)
#     if not winner:
#         print('Nobody has won...')
#     else:
#         print(f'Congratulations! This time {winner} wins! He got all candies!')


# b) pass
# c) Intelligent bot game:
from random import choice

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!"\n'
            'Основные правила игры:\n'
            'Нам будет дано некоторое количество конфет,\n'
            'за один ход мы можем взять не более определённого количества, '
            'о котором мы с вами договоримся.\n'
            'Проигрывает тот, кто забирает последнюю конфету\n.'
            'Итак, начнём!')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def introduce_players():
    player1 = input('Player one:\n')
    player2 = 'IBot'
    print(f'{player1} vs {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, введите любую другую цифру\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    print(count)
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, \
                    у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]


print(greeting)

players = introduce_players()
rules = get_rules(players)

winner = play_game(rules, players, messages)
if not winner:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winner}! Ему достаются все конфеты!')
