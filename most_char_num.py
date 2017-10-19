import collections

def most_char_num(st):
    a=collections.Counter(st).most_common(1)
    print(a)


if __name__ == '__main__':
    st='sdsdsddssssssdd'
    print(most_char_num(st))
