from colorama import Back
from os import system, name as os_name
class SenseHat:

    low_light = False

    def set_pixels(self, pixels):
        if os_name == 'posix':
            system('clear')
        else:
            system('cls')

        

        for i in range(64):
            if i % 8 == 0:
                print(Back.BLACK + " ")
            if pixels[i] == (255, 255, 255):
                print(Back.WHITE + " ", end='')
            elif pixels[i] == (0, 255, 0):
                print(Back.GREEN + " ", end='')
            elif pixels[i] == (255, 0, 0):
                print(Back.RED + " ", end='')
            elif pixels[i] == (255, 255, 0):
                print(Back.YELLOW + " ", end='')
            elif pixels[i] == (0, 0, 0):
                print(Back.BLACK + " ", end='')
            elif pixels[i] == (0, 0, 255):
                print(Back.BLUE + " ", end='')
            else:
                print(Back.BLACK + " ", end='')
        print(Back.BLACK + " ")

        # for i in range(64):
        #     if i % 8 == 0:
        #         print("\033[2;31;40m ")
        #     if pixels[i] == (255, 255, 255):
        #         print("\033[2;31;47m ", end='')
        #     elif pixels[i] == (0, 255, 0):
        #         print("\033[2;31;42m ", end='')
        #     elif pixels[i] == (255, 0, 0):
        #         print("\033[2;31;41m ", end='')
        #     elif pixels[i] == (255, 255, 0):
        #         print("\033[2;31;43m ", end='')
        #     elif pixels[i] == (0, 0, 0):
        #         print("\033[2;31;40m ", end='')
        #     elif pixels[i] == (0, 0, 255):
        #         print("\033[2;31;44m ", end='')
        #     else:
        #         print("\033[2;31;40m ", end='')
        # print("\033[2;31;40m ")
