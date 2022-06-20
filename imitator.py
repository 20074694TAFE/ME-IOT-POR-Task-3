class SenseHat:

    low_light = False

    def set_pixels(self, pixels):
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc')
        for i in range(64):
            if i % 8 == 0:
                print("\033[2;31;40m ")
            if pixels[i] == (255, 255, 255):
                print("\033[2;31;47m ", end='')
            elif pixels[i] == (0, 255, 0):
                print("\033[2;31;42m ", end='')
            elif pixels[i] == (255, 0, 0):
                print("\033[2;31;41m ", end='')
            elif pixels[i] == (255, 255, 0):
                print("\033[2;31;43m ", end='')
            elif pixels[i] == (0, 0, 0):
                print("\033[2;31;40m ", end='')
            else:
                print("\033[2;31;40m ", end='')
        print("\033[2;31;40m ")
