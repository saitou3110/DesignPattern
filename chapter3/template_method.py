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
    def print(self):# サブクラスに実装を任せるメソッド2
        pass

    @abstractmethod
    def close(self):# サブクラスに実装を任せるメソッド3
        pass

    def display(self):# この抽象クラスで実装しているメソッド
        self.open()# まずopenして

        for _ in range(5):# 5回printする
            self.print()

        self.close()# 最後にclose

class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print('<<')

    def print(self):
        print(self.ch)

    def close(self):
        print('>>')
