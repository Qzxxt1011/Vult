#!/usr/bin/env python

import os
import art
import cryptocode
import colored
from colored import stylize
from os import system, name, listdir
from random import randint
from time import sleep
import sys


os.system('title Vult')


aftertitle = [False, '', '']


def setaftertitle(msg, style):
    aftertitle[0] = True
    aftertitle[1] = msg
    aftertitle[2] = style


styles = {
    "title": colored.fg('cyan_3') + colored.attr('bold'),
    "prompt": colored.fg('turquoise_4'),
    "err": colored.bg('red_3b') + colored.fg('grey_3'),
    "success": colored.bg('spring_green_2b') + colored.fg('grey_3')
}


def stprint(text, style):
    print(stylize(text, styles[style]))


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

    stprint(art.text2art('Vult'), 'title')

    if aftertitle[0]:
        stprint(aftertitle[1], aftertitle[2])
        print('\n')
        aftertitle[0] = False


clear()


def stinput(text):
    return input(stylize(text, styles['prompt']))


passtest_file = open('vfiles/vultdata/_passtest.vult', 'r')
passtest = passtest_file.read()
passtest_file.close()


if passtest == 'NOPASS':
    def setpass():
        newpass = stinput(' > Set a password: ')
        if len(newpass) >= 8:
            passtest_file = open('vfiles/vultdata/_passtest.vult', 'w')
            passtest_file.write(cryptocode.encrypt('VULTISCOOL', newpass))
            passtest_file.close()
        else:
            stprint('Password must be at least 8 characters.', 'err')
            setpass()

    setpass()
    sleep(0.7)
    print('Password set! Please run Vult again to continue!')

else:
    def attemptpass():
        attempt = stinput(' > Enter your password: ')
        if cryptocode.decrypt(passtest, attempt) == 'VULTISCOOL':
            print('Correct!')
            return attempt
        else:
            stprint('Your password is incorrect.', 'err')
            attemptpass()

    key = attemptpass()

    def opts():
        clear()

        print('[1] New File')
        print('[2] Open File')
        print('[3] Delete File')
        print('[4] Rename File')
        print('[5] Exit\n')
        choice = stinput(' > Choose an option: ')

        if choice.isdigit() and int(choice) <= 5:
            if choice == '1':
                filename = stinput(' > What is the name of the new file?: ')
                file = open('vfiles/' + filename + '.vult', 'w')
                file.write(cryptocode.encrypt('--N3WF1L3--', key))
                file.close()
                setaftertitle('Successfully created a new file!', 'success')
                opts()
            elif choice == '2':
                def choose():
                    files = listdir('vfiles')
                    files.remove('temp')
                    files.remove('vultdata')

                    if len(files) == 0:
                        setaftertitle('There are no files!', 'err')
                        opts()

                    clear()

                    for i in files:
                        print('[' + str(files.index(i)) + '] ' + i)

                    filechoice = stinput('\n > Choose a file: ')
                    if filechoice.isdigit() and int(filechoice) <= len(files):
                        tempname = str(randint(1, 999999999))

                        file1 = open('vfiles/temp/' + tempname + '.txt', 'w')
                        file1.close()
                        file2 = open('vfiles/' + files[int(filechoice)], 'r')
                        file2c = file2.read()
                        file2.close()
                        if cryptocode.decrypt(file2c, key) != '--N3WF1L3--':
                            file1 = open('vfiles/temp/' + tempname + '.txt', 'w')
                            file1.write(cryptocode.decrypt(file2c, key))
                            file1.close()

                        clear()

                        os.system('notepad.exe ' + './vfiles/temp/' + tempname + '.txt')

                        file1 = open('vfiles/temp/' + tempname + '.txt', 'r')
                        file1c = file1.read()
                        file1.close()

                        file2 = open('vfiles/' + files[int(filechoice)], 'w')
                        file2.write(cryptocode.encrypt(file1c, key))
                        file2.close()

                        os.remove('vfiles/temp/' + tempname + '.txt')
                    else:
                        stprint('Invalid option.', 'err')
                        choose()
                choose()
                setaftertitle('Successfully saved file!', 'success')
                opts()

            elif choice == '3':
                def choose():
                    files = listdir('vfiles')
                    files.remove('temp')
                    files.remove('vultdata')

                    if len(files) == 0:
                        setaftertitle('There are no files!', 'err')
                        opts()

                    clear()

                    for i in files:
                        print('[' + str(files.index(i)) + '] ' + i)

                    filechoice = stinput('\n > Choose a file: ')
                    if filechoice.isdigit() and int(filechoice) <= len(files):
                        os.remove('./vfiles/' + files[int(filechoice)])
                    else:
                        stprint('Invalid option.', 'err')
                        choose()
                choose()
                setaftertitle('Successfully deleted file!', 'success')
                opts()
            elif choice == '4':
                def choose():
                    files = listdir('vfiles')
                    files.remove('temp')
                    files.remove('vultdata')

                    if len(files) == 0:
                        setaftertitle('There are no files!', 'err')
                        opts()

                    clear()

                    for i in files:
                        print('[' + str(files.index(i)) + '] ' + i)

                    filechoice = stinput('\n > Choose a file: ')
                    if filechoice.isdigit() and int(filechoice) <= len(files):
                        newname = stinput(' > What would you like to rename this file to?: ')
                        os.rename('./vfiles/' + files[int(filechoice)], './vfiles/' + newname + '.vult')
                    else:
                        stprint('Invalid option.', 'err')
                        choose()
                choose()
                setaftertitle('Successfully renamed file!', 'success')
                opts()
            elif choice == '5':
                setaftertitle('Farewell!', 'success')
                clear()
                sys.exit()

            else:
                setaftertitle('Invalid option.', 'err')
                opts()
        else:
            setaftertitle('Invalid option.', 'err')

    opts()