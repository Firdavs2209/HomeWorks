s=[6,2,5,5,4,5,6,3,7,6]
N=int(input("Sonni kiriting: "))
S=0
while N>0:
    a=N%10
    N=N//10
    S+=s[a]
print(S)