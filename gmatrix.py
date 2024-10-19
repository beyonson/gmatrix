from random import randint
from time import sleep

terminal_buffer = [0] * 80

def main():
    while(1):
        for i in range(0, 79):
            rand_char = chr(randint(0, 177))
            terminal_buffer[i] = rand_char
        print(*terminal_buffer)
        sleep(.1)

if __name__=="__main__":
    main()
    sys.exit(0)
