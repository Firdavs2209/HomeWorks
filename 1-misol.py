a=int(input("a="))
b=int(input("b="))
orta_arifmetik=(a+b)/2
orta_geometrik=(a*b)**(1/2)
if orta_arifmetik>orta_geometrik:
    print(">")
elif orta_arifmetik<orta_geometrik:
    print("<")
else:
    print("=")