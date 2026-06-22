#Name : Jeremy Von San Juan
#School : FEU TECH
#MACHINE PROBLEM NUMBER : 3

class converttoroman:
    def __init__(self):
        self.numbers = [(5000, 'MMMMM'), (4000, 'MMMM'), (3000, 'MMM'), (2000, 'MM'), (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def number_to_roman(self, num):
        result = ''
        for value, romannumeral in self.numbers:
            while num >= value:
                result += romannumeral
                num -= value
        return result

    def roman_to_numerals(self, roman):
        result = 0
        for value, romannumeral in self.numbers:
            while roman.startswith(romannumeral):
                result += value
                roman = roman[len(romannumeral):]
        return result


print("Name : Jeremy Von San Juan")
print("School : FEU TECH")
print("MACHINE PROBLEM NUMBER : 3")


def main():
  while True:
    case = input("1 for number -> roman 2 for roman -> number 3 to exit: ")
    if case == '1':
        num = int(input("numer -> roman: "))
        converter = converttoroman()
        if num <= 0:
            print ("The number is not a positive integer")
        elif num % 1 != 0:
            print ("The number is not a whole number")
        elif num > 5000:
            print ("The number is above 5000")
        else:
            print(f"The roman numeral for {num} is: {converter.number_to_roman(num)}")
    elif case == '2':
        roman = input("roman -> number: ").upper()
        converter = converttoroman()
        print(f"The number for {roman} is: {converter.roman_to_numerals(roman)}")
    elif case == '3':
        print("exit:")
        break
    else:
        print("Invalid input")
    
main()
