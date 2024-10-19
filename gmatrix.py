import sys
import os
from random import randint, random
from time import sleep


illegal_chars = ['\'', '\"', '(', ')', '|', ';', ':']


def main():
    # matrix info [length][spaces 0/1][char to be drawn]
    matrix_info = [ [0]*78 for i in range(2)]

    while(1):
        term_buf = ""
        for i in range(0, 77):
            # done being drawn, needs reassigned
            if matrix_info[0][i] == 0:
                spaces_or_nah = random() >= 0.15
                rand_len = randint(10, 40)
                matrix_info[0][i] = rand_len
                matrix_info[1][i] = spaces_or_nah
            elif matrix_info[1][i] == True:
                term_buf = term_buf + ' '
                # decrement length to be drawn
                matrix_info[0][i] = matrix_info[0][i] - 1
            else:
                rand_char = chr(randint(33, 90))
                if rand_char in illegal_chars:
                    rand_char = '0'
                term_buf = term_buf + rand_char
                # decrement length to be drawn
                matrix_info[0][i] = matrix_info[0][i] - 1

        sleep(0.1)
        cmd = "echo \"" + term_buf + "\""
        os.system(cmd)


if __name__=="__main__":
    main()
    sys.exit(0)
