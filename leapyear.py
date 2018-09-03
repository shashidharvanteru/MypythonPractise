year= int(input())
l= False
t= True
def is_leap(year):
    if year%4!=0:
       return l
    elif year%100==0:
        if year%400==0:
           return t
        else:
            return l
    else:
        return t
print(is_leap(year))
