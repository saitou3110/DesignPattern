from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass

class Factory(metaclass=ABCMeta):
    def create(self, owner):
        p = self.create_product(owner)
        self.register_product(owner)
        return p

    @abstractmethod
    def create_product(self):
        pass

    @abstractmethod
    def register_product(self):
        pass

class IDCard(Product):
    def __init__(self, owner):
        self.owner = owner
        print(self.owner + 'のカードを作ります。')

    def use(self):
        print(self.owner + 'のカードを使います。')

class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.owners.append(product)

def main():
    factory = IDCardFactory()
    card1 = factory.create('結城浩')
    card2 = factory.create('とむら')
    card3 = factory.create('佐藤花子')
    card1.use()
    card2.use()
    card3.use()

if __name__ == '__main__':
    main()
