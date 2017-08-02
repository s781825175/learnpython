#1000以内的回数
def is_palindrome(n):
    n=str(n)
    i=len(n)
    for j in range(i):
        return (n)[j]==(n)[i-1-j]

output = filter(is_palindrome, range(1000))
print(list(output))
