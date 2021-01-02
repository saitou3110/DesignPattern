from abc import ABCMeta, abstractmethod

def main():
    book_shelf = BookShelf(4)

    book_shelf.append_book(Book(name='A'))
    book_shelf.append_book(Book(name='B'))
    book_shelf.append_book(Book(name='C'))
    book_shelf.append_book(Book(name='D'))

    it  = book_shelf.iterator()
    while it.has_next():
        book = it.next()
        print(book.get_name())

class Aggregate(metaclass=ABCMeta):
    '集合体を表すクラス'
    @abstractmethod
    def iterator(self):
        pass


class Iterator(metaclass=ABCMeta):
    '要素の数え上げを行うような、ループ変数を表すクラス'
    @abstractmethod
    def has_next(self):
        '次の要素が存在するか'
        pass

    @abstractmethod
    def next(self):
        '次の要素を返す'
        pass

class Book:
    '本を表すクラス。名前を得るだけ'
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
        
class BookShelf(Aggregate):
    '''
    本棚を表すクラス。このクラスを集合体として扱うのでaggrigateインターフェイスを実装。
    この本棚はbookフィールドを持つ。
    配列の大きさはBookShelfインスタンスを作成するときに指定。
    '''
    def __init__(self, maxsize):
        # Noneを設定。
        # bookフィールドはクラス外からの変更を防ぐためprivateに。
        self.__books = [None]*maxsize
        self.__last = 0

    def get_book_at(self, index):
        'indexの本を取得する関数'
        return self.__books[index]

    def append_book(self, book):
        '本を追加する関数'
        self.__books[self.__last] = book
        self.__last += 1

    def get_length(self):
        '本がどれくらい保存されているか返す関数'
        # lenではだめなのか？
        return self.__last

    def iterator(self):
        # BookShelfクラスに対応するBookShelfIteratorクラスのインスタンスを生成
        # 本棚の本を数えたいときに使用
        return BookShelfIterator(self)

class BookShelfIterator(Iterator):
    '''
    BookShelfクラスのスキャンを行うクラス
    BookShelfクラスと分けるのは再利用しやすくするため
    '''
    def __init__(self, book_shelf):
        self.__book_shelf = book_shelf
        self.__index = 0

    def has_next(self):
        '次の本があるかを調べる関数。あればTrue、なければFalseを返す'
        # 当然だが、ぴったりのときは次の本は存在しない
        if self.__index < self.__book_shelf.get_length():
            return True
        else:
            return False

    def next(self):
        '次の要素を返す関数'
        book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book
        
if __name__ == '__main__':
    main()
