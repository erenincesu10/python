

def sutunNo(sutun):
    sutun = sutun.upper()
    ussu = len(sutun)-1
    toplam = 0

    for harf in sutun:
        toplam += (26**ussu)*(ord(harf)-ord('A')+1)
        ussu -= 1

    return toplam

for n in range(5):
    print(sutunNo(input("Sütun başlığını giriniz :")))


#print(ord('A'))A harfine karşılık gelecek kodu döndürür
