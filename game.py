f = open("logs", "w")
f.close()
import ctypes
import os
from Ukraine_RU import *
from game_resources import *
import sys
import random
import pygame
import time
from colorama import Fore, Back, Style, init
age1 = ages()
age2 = ages()
age3 = ages()
age4 = ages()
age5 = ages()
user = {'age' : f"{age1}"}
print(user['age'])
os.system('pause')
init()
pygame.init()
def admin_chk():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if admin_chk():
    pass
else:
    warning_sound = pygame.mixer.Sound('88220d21b812cca.mp3')
    warning_sound.play()
    print(admin_check_message)
    input(admin_check_message_press_enter)
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,
                                        __file__, None, 1)
    exit()
success_sound = pygame.mixer.Sound('556c49a24bb675c.mp3')
accept_sound = pygame.mixer.Sound('3bd3287f1db401a.mp3')
success_sound.play()
print(admin_check_message_success)
time.sleep(1)
from rules import *
check_rules()
accept_sound.play()
start_options = menu()
time.sleep(2)
exit_exit_exit = False
reserv_s_opt = prog_in_text_file()
while exit_exit_exit == False:
    if start_options == 1 and reserv_s_opt == 1:
        continue_game = 'yes'
        pygame.mixer.music.load('48bb90af8e1e401.mp3')
        pygame.mixer.music.play(-1)
        count = 0
        game_over = 0
        sound_incorrect = pygame.mixer.Sound('jg-032316-sfx-feedback-incorrect-6.mp3')
        sound_correct = pygame.mixer.Sound('line_open.mp3')
        game_over_sound = pygame.mixer.Sound('1afb121d14c2b36.mp3')
        while continue_game == 'yes':
            if count >= 10:
                continue_game = 'no'
                f = open('save', 'w+')
                f.write('2')
                f.close()
                print('SAVING...')
                time.sleep(1)
            else:
                print(Fore.YELLOW)
                print(Back.CYAN)
                print(Style.BRIGHT)
                os.system('cls')
                a = random.randrange(10, 99)
                b = random.randrange(10, 99)
                c = a + b
                game_title()
                print(f'Count: {count}')
                if count < 0:
                    continue_game = 'no'
                    game_over = 1
                    pygame.mixer.music.stop()
                    game_over_sound.play()
                    time.sleep(1)
                    from game_exit import *
                    exit = exit_with_game_over_stage_1()
                    pygame.mixer.music.stop()
                    exit_choice(exit)
                elif count > 5:
                    a = random.randrange(10,99)
                    b = random.randrange(10,99)
                    c = random.randrange(1,10)
                    d = (a+b)*c
                    print(f'RULES: {rules_calc_1}')
                    stage_rules_1()
                    print(f'Count: {count}')
                    if d == int(input(f'   ({a} + {b}) * {c} = ')):
                        print(Back.GREEN)
                        print('YEA!')
                        count += 1
                        sound_correct.play()
                        time.sleep(1)
                    else:
                        print(Back.RED)
                        print('WRONG!')
                        count -= 1
                        sound_incorrect.play()
                        time.sleep(1)
                elif count >= 0 <= 5:
                    print(f'RULES: {rules_calc}')
                    if c == int(input(f'  {a}  +  {b}  =  ')):
                        print(Fore.GREEN)
                        print('Yea!')
                        count += 1
                        sound_correct.play()
                        time.sleep(1)
                    else:
                        print(Fore.RED)
                        print('WRONG!')
                        count -= 1
                        sound_incorrect.play()
                        time.sleep(1)
        pygame.mixer.music.stop()
    elif start_options == 2 or reserv_s_opt == 2:
        pygame.mixer.music.stop()
        sound_mess = pygame.mixer.Sound('eac678556f1275c.mp3')
        continue_game = 'yes'
        print(Back.BLACK)
        os.system('CLS')
        time.sleep(3)
        while continue_game == 'yes':
            print(Back.LIGHTYELLOW_EX)
            print(Style.DIM)
            print(Fore.BLACK)
            os.system('CLS')
            sound_mess.play()
            print(f'\n\n\n\n\n\n\n\n\n\n\n                              {game_2_words_1}', end=' ')
            time.sleep(2)
            sound_mess.play()
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_2}', end=' ')
            time.sleep(2)
            sound_mess.play()
            print(Back.LIGHTYELLOW_EX, end=' ')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(Back.LIGHTYELLOW_EX, end=' ')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(game_2_words_3, end=' ')
            time.sleep(1)
            sound_mess.play()
            print(f'{game_2_words_4}', end='')
            time.sleep(1)
            sound_mess.play()
            print(f'\n                {game_2_words_5}', end=' ')
            time.sleep(1)
            sound_mess.play()
            print(Back.RED, end='')
            print(Fore.LIGHTWHITE_EX, end='')
            print(f'{game_2_words_6}', end='')
            time.sleep(1)
            sound_mess.play()
            print(Back.LIGHTYELLOW_EX, end=' ')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'{game_2_words_7}', end='')
            time.sleep(4)
            os.system('CLS')
            print(f'\n\n\n\n\n\n\n\n\n\n\n                              {game_2_words_8}',end=' ')
            print(Back.RED, end='')
            print(Fore.WHITE, end='')
            print(f'{game_2_words_9}', end=' ')
            print(Back.LIGHTYELLOW_EX, end='')
            print(Style.DIM, end='')
            print(Fore.BLACK, end='')
            print(f'{game_2_words_10}')
            print(f'                                            {game_2_words_11}')
            time.sleep(4)

            #RULES: Разрешать только тому, кому больше 16 лет и имеется нормальная или 1 проблема в психике, в течении 10 секунд
            #RULES: Разрешать за 12 секунд только тому, у кого вес менее 50 кг, и только тому, у кого имя и фамилия имеют количество букв менее 12
            #RULES: Разрешать за 5 секунд только тем, у кого iq выше твоего (0+10)
    else:
        input('')
