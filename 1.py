
a=list(range(1,100))
print(list((i==1)*'1st' or (i==2)*'2nd' or (i==3)*'3rd' or (i>3)*(str(i)+'th') for i in a))


