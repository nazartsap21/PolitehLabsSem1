from lab4 import ColdStore

coldstore_1 = ColdStore('Samsung', 60, 130, 700)
coldstore_2 = ColdStore('LG', 50, 100, 500)
coldstore_3 = ColdStore('xiaomi', 55, 120, 600)


if __name__ == '__main__':

    print(str(coldstore_1))
    print(repr(coldstore_1))

    print(str(coldstore_2))
    print(repr(coldstore_2))

    print(str(coldstore_3))
    print(repr(coldstore_3))
