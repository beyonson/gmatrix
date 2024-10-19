from random import randint
from time import sleep

def main():
    while(1):
        for i in range(0, 79):
            rand_char = chr(randint(0, 177))
            print(rand_char, end = "")
        sleep(.1)

if __name__=="__main__":
    main()
    sys.exit(0)
