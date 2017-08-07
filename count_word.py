#计算文件夹中的单词数
def count():
    name = input("input a file name:")
    if len(name) < 1:
        name = "a.txt"
    handle = open(name)
    count_words=list()
    for line in handle:
        count_words+=line.split()
    return len(count_words)
count_test = count()
print (count_test)    
