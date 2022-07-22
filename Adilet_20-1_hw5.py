import re


# class ValidCarNumber:
#
#     def __init__(self, number ):
#         self.number = number
#
#     def is_valid(self, number):
#
#         self.is_valid = re.search(r".+([0-9]{2})KG([0-9]{3})([A-Z]{3})",self.number)
#
#
#         if self.is_valid:
#             print("Номер валидный!!")
#         else:
#             print("Номер не валидный!!")
# valid = ValidCarNumber( input("Введите номер машины:"))
# valid.is_valid()

class ValidCarNumber:
    def __init__(self, number):
        self.number = number

    def is_valid(self):
        self.is_valid = re.search(r"([0-9]{2})([A-Z]{2})([0-9]{3})([A-Z]{3})",self.number)

        if self.is_valid:
            print("Номер валидный!")
        else:
            print("Номер не валидный!")

valid = ValidCarNumber(input("Введите номер машины:"))
valid.is_valid()
# 01KG777BAD
# hhh777hhh




