import random

while True:
    pilihan = ["gunting", "kertas", "batu"]
    komputer = random.choice(pilihan)
    pemain = None
    lagi = ["yes", "no"]
    mainlagi = None
    while pemain not in pilihan:
        pemain = input("Silahkan pilih Gunting/Batu/Kertas :").lower()
        if pemain in pilihan:
            print("Game dimulai")
        elif pemain != pilihan :
            print("Pilihan hanya Gunting/Batu/Kertas!!!")

    if pemain == komputer:
        print("Kamu memilih "+pemain.upper() )
        print("Komputer memilih "+komputer.upper())
        print("Seri")

    elif pemain == "batu":
        if komputer == "kertas":
            print("Kamu memilih " + pemain.upper())
            print("Komputer memilih " + komputer.upper())
            print("Kamu Kalah")
        elif komputer == "gunting":
            print("Kamu memilih " + pemain.upper())
            print("Komputer memilih " + komputer.upper())
            print("Kamu Menang!")

    elif pemain == "gunting":
        if komputer == "kertas":
            print("Kamu memilih " + pemain.upper())
            print("Komputer memilih " + komputer.upper())
            print("Kamu Menang!")
        elif komputer == "batu":
            print("Kamu memilih " + pemain.upper())
            print("Komputer memilih " + komputer.upper())
            print("Kamu Kalah")

    elif pemain == "kertas":
        if komputer == "gunting":
            print("Kamu memilih " + pemain.upper())
            print("Komputer memilih " + komputer.upper())
            print("Kamu Kalah")
        elif komputer == "batu":
            print("Kamu memilih " + pemain.upper())
            print("Komputer memilih " + komputer.upper())
            print("Kamu Menang!")

    while mainlagi not in lagi:
        mainlagi = input("Mau main lagi? (yes/no) ").lower()
        if mainlagi == "no":
            mainlagi = mainlagi
        elif mainlagi == "yes":
            print("-----------------------------------------------------")
            mainlagi = mainlagi
        else:
            print("Pilihan hanya yes/no!")

    if mainlagi != "yes":
        break
print("Bye-bye ^>^")

