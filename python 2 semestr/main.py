import math
from random import random


class App:
    def __init__(self):

        print(self.reverse_words("One two three four five"))
        print(self.p_total(5, 6, 0, 2, 121, 13, 1))
        print(self.uefaEuro2016(["Poland", "Korea"], [1, 2]))
        print(self.over_the_road(3, 5))
        print(self.facebook(["One", "Two", "Three"]))
        print(self.facebook(["One"]))
        print(self.facebook([]))
        print(self.facebook(["One", "Two", "Three", "Four", "Five"]))
        self.matrix(9)
        print(self.ask_for_number())

    # 1
    def reverse_words(self, text):
        reversed_string = text.split(" ")
        list.reverse(reversed_string)
        return self.list_to_string(reversed_string)

    def list_to_string(self, items):
        output = " "
        return output.join(items)

    # 2
    def p_total(self, m1, m2, M1, M2, V, T, R):
        if M1 == 0 or M2 == 0 or V == 0:
            return 0
        return ((m1 / M1 + m2 / M2) * R * T) / V

    # 3
    def uefaEuro2016(self, countries, result):
        last_part = "teams played draw." if result[0] == result[1] else (
            f"{countries[0]} won" if result[0] > result[1] else f"{countries[1]} won!")
        output_one = f"At match {countries[0]} - {countries[1]}, {last_part}"
        return output_one

    # 4
    def ask_for_number(self):
        number = int(input("Ile losowych liczb wygenerować? (w przedziale 0 - 1000) -->  ...\n"))
        suma = 0
        for i in range(number):
            suma += int(random() * 1000)
        return suma / number

    # 5
    def over_the_road(self, address, n):
        return (n * 2 + 1) - address

    # 6
    def facebook(self, likes):
        output = ""
        if len(likes) == 1:
            output = f"{likes[0]} likes this"
        elif len(likes) == 2:
            output = f"{likes[0]} and {likes[1]} like this"
        elif len(likes) == 3:
            output = f"{likes[0]}, {likes[1]} and {likes[2]} like this"
        elif len(likes) >= 4:
            output = f"{likes[0]}, {likes[1]} and {len(likes) - 2} others like this"
        else:
            output = "no one likes this"

        return output

    # 7
    def matrix(self, N):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                print(f"{i * j}", end="\t")
            print()


def main():
    app = App()


main()
