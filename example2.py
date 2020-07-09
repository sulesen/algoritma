#example2
m=int(input("En fazla iki basamaklı bir sayı giriniz:"))
for e in range(1,m+1):
    y=e//10
    y2=e%10
    e2=y+y2
    if e2%2==0:
        print(e,"rakamlarının toplamı çift sayı olduğu için dosyaya yazılmamıştır.")
    else:
        with open(file="sumeyye.txt", mode="a") as sule:
            sule.write(str(e)+"\n")