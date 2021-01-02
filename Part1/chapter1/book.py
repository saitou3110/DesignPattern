class Book:
    '本を表すクラス。名前を得るだけ'
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
        