class Kalkulyator:
    def __init__(self):
        self.raqam1 = 0
        self.raqam2 = 0
        self.amal = ""

    def qo'shish(self):
        self.raqam1 = float(input("Birinchi sonni kiriting: "))
        self.raqam2 = float(input("Ikkinchi sonni kiriting: "))
        print(f"{self.raqam1} + {self.raqam2} = {self.raqam1 + self.raqam2}")

    def ayirish(self):
        self.raqam1 = float(input("Birinchi sonni kiriting: "))
        self.raqam2 = float(input("Ikkinchi sonni kiriting: "))
        if self.raqam2 != 0:
            print(f"{self.raqam1} - {self.raqam2} = {self.raqam1 - self.raqam2}")
        else:
            print("Ikkala son ham 0 bo'lishi mumkin emas.")

    def ko'paytirish(self):
        self.raqam1 = float(input("Birinchi sonni kiriting: "))
        self.raqam2 = float(input("Ikkinchi sonni kiriting: "))
        print(f"{self.raqam1} * {self.raqam2} = {self.raqam1 * self.raqam2}")

    def bo'lish(self):
        self.raqam1 = float(input("Birinchi sonni kiriting: "))
        self.raqam2 = float(input("Ikkinchi sonni kiriting: "))
        if self.raqam2 != 0:
            print(f"{self.raqam1} / {self.raqam2} = {self.raqam1 / self.raqam2}")
        else:
            print("Ikkala son ham 0 bo'lishi mumkin emas.")

def main():
    kalkulyator = Kalkulyator()
    while True:
        print("1. Qo'shish")
        print("2. Ayirish")
        print("3. Ko'paytirish")
        print("4. Bo'lish")
        print("5. Chiqish")
        tanlov = input("Tanlovni kiriting: ")
        if tanlov == "1":
            kalkulyator.qo'shish()
        elif tanlov == "2":
            kalkulyator.ayirish()
        elif tanlov == "3":
            kalkulyator.ko'paytirish()
        elif tanlov == "4":
            kalkulyator.bo'lish()
        elif tanlov == "5":
            break
        else:
            print("To'g'ri tanlovni kiriting.")

if __name__ == "__main__":
    main()
