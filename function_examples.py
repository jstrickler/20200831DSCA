import typing as T

def get_message():
    return "Hello DSCA world!"


m = get_message()
print(m)
print(get_message())


def nothing():
    return


n = nothing()
if n is None:
    print("no return value")
    print(n, type(n))
else:
    print("found something")


def greet():
    print("Hello everybody!!")

greet()

def show_message():
    m = get_message()
    print(m)


show_message()


def addem(a: int, b: int) -> int:
    return a + b


result = addem(5, 10)
print(result)

# print(addem(5, 10, 15))
# print(addem(12))


print(addem("foo", "bar"))


def spam(names: T.List[str]) -> str:
    print(names)


spam(['a', 'b', 'c'])
spam([1, 2, 3])
spam("abc")
print()

def ham(*params):
    print("args:", params)


ham(5)
ham(5, 10, 15, 20)
ham()
print()


def eggs(a, b, *c):
    print(a, b)
    print("c:", c)


eggs(1, 2, 3, 4, 5)
eggs(1, 2)


def doit(value, *, debug=False):
    print(value, debug)


doit(25)
doit(99, debug=True)
print()


def set_config(**kwargs):
    print(kwargs)


set_config(filename="wombat.txt", username="mr_wombat", state="NC", city="Durham")


def read_csv(file_or_buffer, sep=',', delimiter=None, header="inter"):
    pass






