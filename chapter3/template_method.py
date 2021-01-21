import unicodedata
from abc import ABCMeta, abstractmethod
'''
template method
スーパークラスで処理の枠組みを定めて、サブクラスで具体的な内容を決める
'''

class AbstractDisplay(metaclass=ABCMeta):# 抽象クラス
    @abstractmethod
    def open(self):# サブクラスに実装を任せるメソッド1
        pass

    @abstractmethod
    def print_a(self):# サブクラスに実装を任せるメソッド2
        pass

    @abstractmethod
    def close(self):# サブクラスに実装を任せるメソッド3
        pass

    def display(self):# この抽象クラスで実装しているメソッド
        self.open()# まずopenして

        for _ in range(5):# 5回printする
            self.print_a()

        self.close()# 最後にclose

class CharDisplay(AbstractDisplay):# CharDisplayはAbstractDisplayのサブクラス
    def __init__(self, ch):# 表示すべき文字。コンストラクタで渡された文字chをフィールドに記憶しておく
        self.ch = ch

    def open(self):# スーパークラスでは抽象メソッドだった。ここでオーバーライドして実装。
        print('<<', end='')# 開始文字として"<<"を表示する。

    def print_a(self):# printメソッドもここで実装する。これがdisplayから繰り返し呼び出される。
        print(self.ch, end='')# フィールドに記憶しておいた文字を1個表示する。

    def close(self):# closeメソッドもここで実装
        print('>>')# 終了文字">>"を表示

class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string
        self.width =len(string.encode())

    def open(self):
        self.printLine()

    def print_a(self):
        print('|' + self.string + '|')

    def close(self):
        self.printLine()

    def printLine(self):
        print('+', end='')

        for _ in range(self.width):
            print('-', end='')

        print('+')



def main():
    d1 = CharDisplay('H')
    d2 = StringDisplay('Hello, World')
    d3 = StringDisplay('こんにちは。')
    d1.display()
    print()
    d2.display()
    print()
    d3.display()

if __name__ == '__main__':
    main()

# なんか微妙にズレるのであとでまたやる