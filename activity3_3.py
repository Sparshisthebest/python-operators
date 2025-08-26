print("enter the marks obtained in four subjects")
Math=int(input("Math : "))
English=int(input("English : "))
Science=int(input("Science : "))
French=int(input("French : "))


sum=Math+English+Science+French
print("the sum of all subjects :", sum)
perc=(sum/400)*100
print(end="percentage mark  =")
print(perc)