import datetime

def logg_way(way):
    def logger(old_function):
        def new_function(*args, **kwargs):
            with open(way, 'a', encoding='utf8') as f:
                now = f.write(str(datetime.datetime.now()) + '\n')
                foo_name = f.write(old_function.__name__+ '\n')
                arg = f.write(str(args) + str(kwargs) + '\n')
                return_foo = f.write(str(old_function()) + '\n\n')
            return
        return new_function
    return logger


@logg_way('text.txt')
def foo(*args, **kwargs):
    print('первая функция')
    return True
@logg_way('text1.txt')
def foo1(*args, **kwargs):
    print('вторая функция')
    return False

if __name__ == '__main__':
    print(foo(1, a=8))
    print(foo1(9, a=9))
