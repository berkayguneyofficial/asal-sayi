import tkinter as tk
import random
import math

def asal_mi(n):
    """Bir sayının asal olup olmadığını kontrol eder"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def rastgele_asal_uret(baslangic, bitis):
    """Belirli bir aralıkta rastgele bir asal sayı üretir"""
    while True:
        sayi = random.randint(baslangic, bitis)
        if asal_mi(sayi):
            return sayi

def rastgele_asal_goster():
    """Etiket için rastgele bir asal sayı seçer ve gösterir"""
    baslangic = 2
    bitis = 100000000000  # 100 milyar
    asal = rastgele_asal_uret(baslangic, bitis)
    etiket.config(text=str(asal))

# GUI oluşturma
pencere = tk.Tk()
pencere.title("Rastgele Asal Sayı")
pencere.geometry("400x100")

# Bileşenleri oluşturma
etiket = tk.Label(pencere, text="Buraya tıkla ve asal sayı gör!", font=("Arial", 12))
etiket.pack(pady=10)

buton = tk.Button(pencere, text="Yeni Asal Sayı", command=rastgele_asal_goster, bg="#4CAF50", fg="white")
buton.pack()

pencere.mainloop()
