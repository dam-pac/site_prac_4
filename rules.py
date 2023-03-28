def check_rules():
    import os
    import time
    cwd = os.getcwd()
    file = os.path.join(cwd, "EULA.txt")
    f = open(file,'r')
    check = f.read()
    if check == 'yes':
        return
    else:
        import pygame
        os.system('cls')
        pygame.init()
        pygame.mixer.music.load('3f0b05a6f262260.mp3')
        pygame.mixer.music.play(-1)
        print('\n\n\n ---> RULES <---\n   1. Вы должны соблюдать правила.\n   2. Вы должны не проигрывать.\n   3. Мы не несём ответственности за технические поломки или повреждения ваших устройств.\n   4. Мы не несём ответственности за вирусное поведение программы.\n   5. Вы соглашаетесь с тем, что всю ответственность несёте Вы, пользователь программы.\n Пожалуйста, если вы соглашаетесь с правилами, напишите "yes":')
        rules_rezult = str(input('Напишите "yes" или "no": '))
        if rules_rezult == 'no':
            exit()
        elif rules_rezult == 'yes':
            cwd = os.getcwd()
            file_oldname = os.path.join(cwd, "EULA_ex.txt")
            file_newname_newfile = os.path.join(cwd, "EULA.txt")
            print(cwd + '\EULA.txt')
            input()
            try:
                os.remove(cwd + 'EULA.txt')
            except:
                pass
            os.rename(file_oldname, file_newname_newfile)
##   1. Вы должны соблюдать правила.
##   2. Вы должны не проигрывать.
##   3. Мы не несём ответственности за технические поломки или повреждения ваших устройств.
##   4. Мы не несём ответственности за вирусное поведение программы.
##   5. Вы соглашаетесь с тем, что всю ответственность несёте Вы, пользователь программы.
##   Пожалуйста, если вы соглашаетесь с правилами, напишите "yes":
