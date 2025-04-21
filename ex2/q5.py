num = int(input("enter the amount of money: "))

HUNDRED = 100
FIFTY = 50
TEN = 10
FIVE = 5

hundreds = num // HUNDRED
if hundreds != 0:
    num %= HUNDRED * hundreds

fifties = num // FIFTY
if fifties != 0:
    num %= FIFTY * fifties


tens = num // TEN
if tens != 0:
    num %= TEN * tens

fives = num // FIVE
if fives != 0:
    num %= FIVE * fives

ones = num

print(f"Change is composed of : {hundreds} X 100 bills {fifties} X 50 bills {tens} X 10 coins {fives} X 5 coins {ones} X 1 coins")