import unicodedata
from abc import ABCMeta, abstractmethod
'''
template method
スーパークラスで処理の枠組みを定めて、サブクラスで具体的な内容を決める
'''

class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()

        for _ in range(5):
            self.print()

        self.close()
        
