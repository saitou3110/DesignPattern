from abc import ABCMeta, abstractmethod
'''
継承を使ったもの
'''
def main():
    '''
    あくまでPrintというインターフェイスを使っているだけ。
    show_with_hogeは見えないようにしてある。
    PrintBannerがどうなっているかmainは知らなくてもいい。
    '''
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
    
# Bannerクラスを継承、printインターフェイスを実装
class PrintBanner(Print, Banner):
    def __init__(self, string):
        self.__banner = Banner(string)

    def print_weak(self):
        self.__banner.show_with_paren()

    def print_string(self):
        self.__banner.show_with_aster()

if __name__ == '__main__':
    main()
