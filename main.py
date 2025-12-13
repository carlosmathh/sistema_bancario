from abc import ABC, abstractmethod


# CONTA-------------------------------------------------
class Account(ABC):
    def __init__(self, agency, account_num, balance):
        self.agency = agency
        self.account_num = account_num
        self.balance = balance

    @abstractmethod
    def withdraw(self, value):
        if value <= 0:
            raise ValueError('Valor do saque não pode ser negativo ou zero')


    def deposit(self, value):
        self.balance = self.balance + value
        return self.balance        


# Conta-------------------------------------------------
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# BANCO-------------------------------------------------
class Bank(): #agregar classe de cliente e contas
    def __init__(self,list_customer, list_account):
        self.list_customer = list_customer
        self.list_account = list_account
        self._agency_branch = '0001-9'


    def authentication(self, cliente):

                # Checar se o cliente é daquele banco
        if cliente not in self.list_customer: 
            raise ValueError('Cliente inexistente no nosso banco')

        # Checar se a conta é daquele banco
        if cliente.account not in self.list_account:
            raise ValueError('Cliente inexistente no nosso banco')


        # Checar se a agência é daquele banco
        if cliente.account.agency != self._agency_branch:
            raise ValueError('Agência incorreta')
        
        
        # Se a conta pertence ao cliente 
        # if cliente.account != cliente.account:
        #     raise ValueError('Account não pentence ao cliente banco')

        return True

    def withdraw_bank(self, client, value):
        if self.authentication(client):
            return client.account.withdraw(value)


    def deposit_bank(self, client, value):
        if self.authentication(client):
            return client.account.deposit(value)
        


# CLIENTE-------------------------------------------------
class Client(Person):
    # agregação de cliente com conta
    def __init__(self, name, age, account):
        super().__init__(name, age)
        self._name = name
        self._age = age
        self._account = account

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valor):
        if valor < 0:
            raise ValueError('A idade não pode ser negativa')
        self._age = valor

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Nome não pode ser vazio')
        self._name = value
    

    @property
    def account(self):
        return self._account




# CONTAS-------------------------------------------------
class CurrentAccount(Account):
    # conta corrente deve ter limite extra
    def __init__(self, agency, account_num, balance, credit_limit):
        super().__init__(agency, account_num, balance)
        self.credit_limit = credit_limit

    def withdraw(self, value):
        super().withdraw(value)

        if value <= self.balance:
            self.balance -= value              
            return self.balance

        missing_value = value - self.balance

        if missing_value > self.credit_limit:
            raise ValueError('Saldo mais limite insuficientes')

        self.balance = 0
        self.credit_limit -= missing_value
        return self.balance

            

class SavingsAccount(Account):
    def __init__(self, agency, account_num, balance):
        super().__init__(agency, account_num, balance)

    def withdraw(self, value):
        super().withdraw(value)

        if self.balance < value:
            raise ValueError('Valor Digitado menor que o valor em saldo')
        
        self.balance = self.balance - value
        return self.balance
