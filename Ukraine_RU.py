##Здесь написаны фразы с программы, пожалуйста, не меняйте их!
from colorama import Fore, Back, Style, init
init()
def prog_in_text_file():
    try:
        f = open('save', 'r+')
        n = int(f.read())
        f.close()
    except:
        n = 1
    return n
admin_check_message = f'Выдайте права администратора. Это необходимо для работы программы.'
admin_check_message_press_enter = f'Нажмите enter...'
admin_check_message_success = f'Были получены права администратора. Продолжение инициализации.\n\n\n'
rules_calc = f'Вам необходимо сложить два числа. Число + Число = Ответ. В случае неверного ответа, у вас уменьшится количество очков.'
rules_calc_1 = f'Вам необходимо сложить два числа и {Back.RED}УМНОЖИТЬ{Back.CYAN} полученное число. В случае {Back.RED}НЕВЕРНОГО{Back.CYAN} ответа, у вас {Back.RED}УМЕНЬШИТСЯ{Back.CYAN} количество очков.'
exit_with_game_over_stage_1 = f'\n\n\n\n\n\n          К сожалению... Вы проиграли в самом начале. Видимо вам не дана математика.          \n                Но у вас есть маленький выбор:               \n                    1) Выйти                    \n                    2) Перезапустить                    \n'
exit_with_game_over_stage_1_input = f'  Ваш выбор (1 or 2): '
game_2_rules_1 = 'RULES: Разрешать только тому, кому больше 16 лет и имеется нормальная или 1 проблема в психике, в течении 10 секунд'
game_2_rules_2 = 'RULES: Разрешать за 12 секунд только тому, у кого вес менее 50 кг, и только тому, у кого имя и фамилия имеют количество букв менее 12'
game_2_rules_3 = 'RULES: Разрешать за 5 секунд только тем, у кого iq выше твоего (0+10)'
game_2_words_1 = 'Ты...'
game_2_words_2 = 'ТЫ!'
game_2_words_3 = 'Прошёл её?'
game_2_words_4 = 'Но...'
game_2_words_5 = 'Это не смогли сделать многие подобные'
game_2_words_6 = 'ТЕБЕ'
game_2_words_7 = ' по разуму существа.'
game_2_words_8 = 'Я могу добавить в'
game_2_words_9 = 'ТВОЮ'
game_2_words_10 = 'личную информацию данные -'
game_2_words_11 = 'iq: +10.'
game_2_words_12 = 'Данные личного пользователя {name}:'
game_2_words_13 = 'name: ENTER_THE_NAME'
game_2_words_14 = 'forname: ENTER_THE_FORNAME'
game_2_words_15 = 'age: ENTER_THE_AGE'
game_2_words_16 = 'iq: +10'
game_2_words_17 = 'Хотя'
game_2_words_18 = 'ТЫ'
game_2_words_19 = 'этого не достоин, поэтому их надо заработать.'
game_2_words_20 = 'К нам на тесты привозят огромное количество по виду'
game_2_words_21 = 'ТЕБЕ'
game_2_words_22 = 'подобных существ.'
game_2_words_23 = 'Меня удивляет,'
game_2_words_24 = 'зачем вы даёте каждому какие-то буквы,'
game_2_words_25 = 'если можно цифры...'
game_2_words_26 = 'Но вам нас не понять...'
game_2_words_27 = 'У них,'
game_2_words_28 = 'в отличии от'
game_2_words_29 = 'ТЕБЯ,'
game_2_words_30 = 'имеются свои особенности.'
game_2_words_31 = 'ТЕБЕ'
game_2_words_32 = 'нужно просто выполнить самую лёгкую задачу для вас похожих приматов,'
game_2_words_33 = 'выбор из двух кнопок.'
game_2_words_34 = 'ЧТО'
game_2_words_35 = 'МОЖЕТ'
game_2_words_36 = 'БЫТЬ'
game_2_words_37 = 'ПРОЩЕ?!'
game_2_words_38 = 'Но лишь одна ошибка...'
game_2_words_39 = 'ТЫ ПОЖАЛЕЕШЬ!'
n = prog_in_text_file()
menu_words_1 = f'          МЕНЮ ИГРЫ:\n            1) Начать игру\n            2) Загрузить игру {n}\n            3) Выйти с игры'
menu_input_words_1 = '          Ваш выбор (1/2/3): '
