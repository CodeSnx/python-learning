"""
python 两大特性和四大基本语法
两大特性：动态、强类型
四大基本语法：命名规则、缩进规则、特殊关键字、特殊运算符
Day38——1/60（重新开始系统学习）
"""


class Book(object):
    # 定义类的参数
    def __init__(self, book_id, book_name, book_store_count):
        self.book_id = book_id
        self.book_name = book_name
        self.book_store_count = book_store_count
    # 重写加法操作

    def __add__(self, book):
        return self.book_store_count + book.book_store_count


python_intro_book = Book(1, 'python入门书', 100)
ml_intro_book = Book(2, '机器学习入门书', 200)
# 求两本书的总价
sales_cnt = python_intro_book + ml_intro_book
print(sales_cnt)
