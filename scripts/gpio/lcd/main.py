import lcddriver
from time import sleep

# 'Connect' ldc display
lcd = lcddriver.lcd()

# Clear display
lcd.lcd_clear()

# Example of how to write each row:
lcd.lcd_display_string("----- EXAMPLE ------", 1)
lcd.lcd_display_string("WOW                 ", 2)
lcd.lcd_display_string("                 WOW", 3)
lcd.lcd_display_string("--------------------", 4)


# Wait 5 seconds
sleep(5)


# Demo of which (ASCII) character can be displayed

# ASCII 0,...,15 - length=16
all_blocks = ""
for i in range(0, 16):
    all_blocks += chr(i)

# ASCII 16,...,32 - length=17
empty = ""
for i in range(16, 33):
    empty += chr(i)

# ASCII 33,...,47 + 58,...,64 + 91,...,96 + 123,...,127 - length=33
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}
all_symbols = ""
for i in range(33, 48):
    all_symbols += chr(i)
for i in range(58, 65):
    all_symbols += chr(i)
for i in range(91, 97):
    all_symbols += chr(i)
for i in range(123, 128):
    all_symbols += chr(i)

# ASCII 48,..,57 + 91,...,96 + 123,...,127 - length=10
# 0123456789
all_numbers = ""
for i in range(48, 58):
    all_numbers += chr(i)

# ACII 65,...,90 + 97,...,122 - length=52
# ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
all_letters = ""
for i in range(65, 91):
    all_letters += chr(i)
for i in range(97, 123):
    all_letters += chr(i)

# for a better iterating save everything with a descripton in a list
all_characters = [("Blocks", all_blocks), ("Symbols", all_symbols),
                  ("Numbers", all_numbers), ("Letters", all_letters), ("Empty", empty)]

# print length and characters to the console
for x in all_characters:
    print(x[0], "\n\t-> length=" + str(len(x[1])), "\n\t-> " + x[1])

# display all 128 characters grouped until the script gets blocked with [Strg] + [C]
while True:
    for x in all_characters:
        lcd.lcd_clear()
        lcd.lcd_display_string(x[0] + ":", 1)
        begin = 0
        for i in range(2, 5):
            end = begin + 20
            lcd.lcd_display_string(x[1][begin:end], i)
            begin = end
        # wait 2 seonds before continuing
        sleep(2)
