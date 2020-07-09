"""
                                        ####soru1#####
s={"01":"Ocak","02":"Şubat","03":"Mart","04":"Nisan","05":"Mayıs","06":"Haziran",
   "07":"Temmuz","08":"Ağustos","09":"Eylül","10":"Ekim","11":"Kasım","12":"Aralık"}

u=input("Sayısal olarak gün-ay-yıl formatıyla tarih girişi yapınız:")
m=u.split("-")
e=s.get("{}".format(m[1]))
print(m[0],e,m[2])
"""
"""
                                        #####soru2####

s=int(input("Bir sayı giriniz:"))
if s >= 16:
    print("Hata! 16 'dan büyük bir sayı giriniz.")
elif s<0:
    print("Hata! Negatif sayı girilemez.")
if (9<= s <16):
    s=s*2
    u = 0
    for s in range(s):
        if s%2==0:
            s+=2
            u+=s
            print(u)
elif (0 <= s < 9):
    e = 1
    for s in range(1, s):
        e *= s + 1
        print(e*3)
"""
"""
                                             #####soru3#####
s = {"s": 19, "u": 21, "m": 13, "e": 5, "y": 25, "y": 25, "e": 5, "s": 19, "e": 5, "n": 14, "s": 19, "u": 21}
u = [[1, 2, -1], [2, 5, 2], [-1, -2, 2]]


def sifre(adsoyad):
    m = []
    for e in adsoyad:
        m.append(e)
    # print(m)

    y = []
    for e2 in adsoyad:
        y.append(s.get(e2))
    # print(y)

    sule1 = y[0:3]
    sule2 = y[3:6]
    sule3 = y[6:9]
    sule4 = y[9:12]

    y2 = [sule1, sule2, sule3, sule4]
    print(y2)
    print(u)
    sulesen = []
    for sen in y2:
        for sen2 in u:
            print("eşleşme:", sen2, sen)
            sumeyye = sen2[0] * sen[0], sen2[1] * sen[1], sen2[2] * sen[2]
            print(sumeyye)
            smye = 0
            for su in sumeyye:
                smye += su
            print(smye)
            sulesen.append(smye)
        print("liste:", sulesen)
    
ss = sifre("sumeyyesensu")
"""

                                                ##soru4###
s=[]
for u in range(1,18):
    if u==2 or u==3 or u==5 or u==7:
        s.append(u)
    if not u%2==0 and u!=1 and u%3!=0 and u%5!=0 and u%7!=0:
        s.append(u)


print(s)










