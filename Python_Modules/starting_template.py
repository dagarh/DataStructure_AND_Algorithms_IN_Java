from sys import stdin


def takeinput(delimiter=" ", tipe=int):
    '''
    :param delimiter:  it is very helpful
    :param tipe: datatype of elements
    :return: it returns nothing

    '''
    # inp = input().split(delimiter)
    inp = stdin.readline().split(delimiter)
    lt = [tipe(item) for item in inp if item != '']

    if len(lt) > 1:
        return lt

    else:
        return lt[0]


def main():
    pass
    # t = takeinput()


if __name__ == '__main__':
    main()
