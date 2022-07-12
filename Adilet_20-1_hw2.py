class Company:
    _company_bank = 100000
    def __init__(self,company_bank , company_name):
        self.company_bank = company_bank
        self.company_name = company_name


class Person(Company):

    _salary = 10000

    def __init__(self , first_name , last_name , salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_salary(self):
        if self._company_bank - self.salary > 0:
            print(f'Зарплата получена')
        else:
            print(f'У компании не достаточно средств!')

    def person_info(self):
        print(f'Информация о сотруднике:{self.first_name} {self.last_name} {self.salary}')
Person1 = Person('Макс' , 'Миллер' , 10000 )

Person1.get_salary()
Person1.person_info()