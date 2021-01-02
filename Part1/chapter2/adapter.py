from abc import ABCMeta, abstractmethod
'''
継承を使ったもの
'''
def main():
    p = PrintBanner('Hello')
    p.print_weak()
    p.print_string()
# Bannerクラス 
class Banner:
    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print('({})'.format(self.__string))

    def show_with_aster(self):
        print('*{}*'.format(self.__string))

# Printインターフェイス。抽象クラス。
class Print(metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_string(self):
        pass
    
class PrintBanner(Print):
    def __init__(self, string):
        self.__banner = Banner(string)

    def print_weak(self):
        self.__banner.show_with_paren()

    def print_string(self):
        self.__banner.show_with_aster()

if __name__ == '__main__':
    main()
