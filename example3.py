#example3
from functools import reduce

soyad=['Aygun','Çiçek','Deniz','Atar','Dener','Yılmaz']
toplam_satis_miktari = [['Ayse ', 3,6,7],['Ece ', 5,2,4],['Arya ', 6,5],['Ali ', 3],['Can ',5,7,9,11],['Aybar ',2,3]]

                   # ADIM 1 #
#sm=list(map(lambda u:[u[0]]+[reduce(lambda m,y:m+y,u[1:])],toplam_satis_miktari))
#print(sm)
                      # ADIM 2 #

#su=list(map(lambda l,e:l[0]+ e[0:],toplam_satis_miktari,soyad))
#print(su)
                       # ADIM 1 + ADIM2 #
s=list(map(lambda u,m:[u[0]+ m[0:]]+[reduce(lambda e,y:e+y,u[1:])],toplam_satis_miktari,soyad))
print(s)
