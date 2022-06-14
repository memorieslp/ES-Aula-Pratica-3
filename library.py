import numpy as np

class Book:
    __slots__ = [
        'name',
        'author',
    ]
    
    def __init__(self, name, author):
        self.name = name
        self.author = author

def read_imput():
    name = input()
    author = input()
    return name, author    
        
def main():
    Book = read_imput()
    print("easy")
    
if __name__ == '__main__':
    main()