import random

pul = 100
while pul>0:
    print(f"\nPulingiz:{pul}")
    garov = int(input("Garov qoying:"))
    taxmin = int(input("Zar qiymati(1-6): "))
    zar = random.randint(1, 6)
    print(f"Zar:{zar}")
    if zar ==taxmin:
        pul +=garov * 5
        print("JACKPOT! 🎰")
    else:
        pul-=garov
        print("Yutqazdingiz!")

print("Pulingiz tugadi! O'yin tugadi")

