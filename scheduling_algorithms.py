
import sys
import os
import time
from prettytable import PrettyTable as table
"""
Format plliku, z którego pobierane są dane:
nazwa procesu
czas przybycia
czas trwania procesu
priorytet
.
.
.
nazwa procesu
czas przybycia
czas trwania procesu
priorytet

Czasy oczywiście podajemy w ms

"""


class Sym1(object):

    # name- nazwa procesu, ctime-czas przybycia, dtime-czas trwania procesu
    def __init__(self, name, ctime, dtime, priority):
        self.name = name  # nazwa procesu
        self.ctime = ctime  # czas przybycia procesu
        self.dtime = dtime  # czas trwania procesu
        self.priority = priority  # priorytet procesu

    def read(self):
        lines = []
        option = input(
            "Jeżeli chcesz dane pobrać z pliku wybierz T a jeśli chcesz wpisać samodzielnie wybierz N!")
        print()
        if option.upper() == "T":
            filename = input("Podaj nazwę pliku: ")
            text_file = open(filename, "r")
            lines = text_file.readlines()
            text_file.close()
            modlen = len(lines) % 4
            if modlen != 0:
                sys.exit("Nieprawidłowy format zapisu danych w pliku")
            length = int(len(lines)/4)
            c = 0
            for i in range(length):
                self.name.append(lines[c])
                self.ctime.append(int(lines[c+1]))
                self.dtime.append(int(lines[c+2]))
                self.priority.append(int(lines[c+3]))
                c += 4

        elif option.upper() == "N":
            numb = input("Ile procesów chcesz dodać?")
            for i in range(int(numb)):

                self.name.append(input("Podaj nazwę procesu: "))
                self.ctime.append(int(input("Podaj czas przybycia procesu: ")))
                self.dtime.append(
                    int(input("Podaj czas przetwarzania procesu: ")))
                self.priority.append(int(input("Podaj priorytet procesu:")))

        else:
            sys.exit("Podano nieprawidłową opcje!")

    def clear(self):
        name = 'raport_sym1.txt'
        text_write = open(name, "w")
        text_write.close()

    def info(self):
        """Funkcja pokazuje procesu wczytanie do programu"""
        length = int(len(self.name))
        counter = 0
        x = table()
        x.field_names = ["Nazwa procesu:",
                         "Czas przybycia:", "Czas trwania:", "Priorytet:"]
        for i in range(length):
            x.add_row([self.name[i], self.ctime[i],
                       self.dtime[i], self.priority[i]])
        print()
        print(x)
        print()

        name = 'raport_sym1.txt'
        text_write = open(name, "a")
        text = str(x)
        text_write.writelines(text)
        text_write.writelines("\n\n")
        text_write.close()

    def sort_fcfs(self):
        """Funkcja odpowiada za sortowanie tablic po czasie przybycia"""
        length = len(self.name)
        for i in range(0, length):

            x = min(self.ctime[i:])
            m = self.ctime[i]
            ix = self.ctime.index(x, i)
            self.ctime[i] = self.ctime[ix]
            self.ctime[ix] = m

            n = self.dtime[i]
            self.dtime[i] = self.dtime[ix]
            self.dtime[ix] = n

            b = self.name[i]
            self.name[i] = self.name[ix]
            self.name[ix] = b

            f = self.priority[i]
            self.priority[i] = self.priority[ix]
            self.priority[ix] = f

    def sort_sjf(self):
        """Ta funkcja odpowiada za sortowanie tablic po długości procesów"""
        length = len(self.name)
        for i in range(0, length):

            x = min(self.dtime[i:])
            m = self.dtime[i]
            ix = self.dtime.index(x, i)
            self.dtime[i] = self.dtime[ix]
            self.dtime[ix] = m

            n = self.ctime[i]
            self.ctime[i] = self.ctime[ix]
            self.ctime[ix] = n

            b = self.name[i]
            self.name[i] = self.name[ix]
            self.name[ix] = b

            f = self.priority[i]
            self.priority[i] = self.priority[ix]
            self.priority[ix] = f

    # tutaj mam juz teoretycznie posortowane tablice po parametrze czasu przybycia
    def fcfs(self):
        """Ta Funkcja symuluje działanie algorytmu FCFS"""
        length = len(self.name)
        k = 0
        t = 0
        flag = True
        s = 0
        c = 1
        allwtime = 0
        delay = 0
        suma = []
        wtime = []

        p = input(
            "Podaj dzielnik prędkości przetwarzania procesów(n=1000 wowczas 1cykl=1ms)")
        print()
        print("------------------------------Algorytm  FCFS-------------------------------")
        while flag == True:
            if self.ctime[k] <= t:
                print()
                print(f"{self.name[k]}:", end="")
                for q in range(t):
                    print(" ", end="")

                for a in range(int(self.dtime[k])):
                    print("#", end="")
                    time.sleep(1 / int(p))
                    t += 1

                # liczy czasy oczekiwania

                s += int(self.dtime[k])
                suma.append(int(s+delay))
                wtime.append(int(t-self.ctime[k]-self.dtime[k]))
                allwtime += int(wtime[k])  # całkowity czas oczekiwania
                k += 1
                print('', end="")

                if k > length-1:
                    flag = False

            else:
                print(' ', end='')
                time.sleep(1/int(p))
                delay += 1
                t += 1

        average_wtime = allwtime/length
        print()
        print()
        print()
        x = table()
        x.field_names = (
            "Lp.", "Nazwa Procesu",  "Czas przybycia", "Czas trwania", "Czas zakończenia",
            "Czas oczekiwania", "Priorytet:")
        for y in range(0, length):
            x.add_row(
                [c, self.name[y], self.ctime[y], self.dtime[y],
                 suma[y], wtime[y], self.priority[y]])
            c += 1
        print(x)
        print()
        print(f"średni czas oczekiwania wynosi: {round(average_wtime, 2)}ms")
        text_write = open('raport_sym1.txt', "a")
        text = str("\n\n\n Algorytm FCFS\n")
        text_write.writelines(text)
        text = str(x)
        text_write.writelines(text)
        text = str(
            f"\nśredni czas oczekiwania wynosi {round(average_wtime, 2)}ms")
        text_write.writelines(text)

        text_write.close()

    def sjf(self):
        """Ta funkcja symuluje działanie algorytmu sjf"""
        length = len(self.name)
        k = 0
        t = 0
        flag = True
        s = 0
        allwtime = 0
        c = 1
        delay = 0
        suma = []
        wtime = []

        p = input(
            "Podaj dzielnik prędkości przetwarzania procesów(n=1000 wowczas jeden 1 cykl = 1ms)")
        print()
        print("------------------------------Algorytm SJF-------------------------------")
        while flag == True:

            if self.ctime[k] > t:
                for x in range(k, length):
                    if self.ctime[x] <= t:

                        self.ctime.insert(k, self.ctime[x])
                        del self.ctime[x+1]

                        self.dtime.insert(k, self.dtime[x])
                        del self.dtime[x+1]

                        self.name.insert(k, self.name[x])
                        del self.name[x+1]
                        break

            if self.ctime[k] <= t:
                print()
                print(f"{self.name[k]}:", end="")
                for q in range(t):
                    print(" ", end="")

                for a in range(int(self.dtime[k])):
                    print("#", end="")
                    time.sleep(1 / int(p))
                    t += 1

                # liczy czasy oczekiwania

                s += int(self.dtime[k])
                suma.append(int(s+delay))
                wtime.append(int(t-self.ctime[k]-self.dtime[k]))
                allwtime += int(wtime[k])  # całkowity czas oczekiwania
                k += 1
                print('', end="")

                if k > length-1:
                    flag = False

            else:
                print(' ', end='')
                time.sleep(1/int(p))
                delay += 1
                t += 1

        average_wtime = allwtime/length
        print()
        print()
        print()
        x = table()
        x.field_names = (
            "Lp.", "Nazwa Procesu",  "Czas przybycia", "Czas trwania", "Czas zakończenia",
            "Czas oczekiwania", "Priorytet:")
        for y in range(0, length):
            x.add_row(
                [c, self.name[y], self.ctime[y], self.dtime[y],
                 suma[y], wtime[y], self.priority[y]])
            c += 1
        print(x)
        print()
        print(f"średni czas oczekiwania wynosi: {round(average_wtime, 2)}ms")
        text_write = open('raport_sym1.txt', "a")
        text = str("\n\n\n Algorytm SJF \n")
        text_write.writelines(text)
        text = str(x)
        text_write.writelines(text)
        text = str(
            f"\nśredni czas oczekiwania wynosi {round(average_wtime, 2)}ms")
        text_write.writelines(text)

        text_write.close()

    def sjf_priority(self):
        """Ta funkcja symuluje działanie algorytmu priorytetowego sjf"""
        length = len(self.name)
        k = 0
        t = 0
        flag = True
        s = 0
        allwtime = 0
        c = 1
        delay = 0
        m = 1
        suma = []
        wtime = []
        moment = []
        for i in self.priority:
            moment.append(i)
        p = input(
            "Podaj dzielnik prędkości przetwarzania procesów(n=1000 wowczas jeden 1 cykl = 1ms)")
        print()
        print("------------------------------Algorytm priorytetowy SJF-------------------------------")
        while flag == True:
            if k != 0:
                if t % 5 == 0:
                    for k in range(k, length):
                        if self.priority[x] >= 1:
                            if self.ctime[x] <= t:
                                self.priority[x] -= 1

            for i in range(k, length):

                x = min(self.dtime[i:])
                m = self.dtime[i]
                ix = self.dtime.index(x, i)
                self.dtime[i] = self.dtime[ix]
                self.dtime[ix] = m

                n = self.ctime[i]
                self.ctime[i] = self.ctime[ix]
                self.ctime[ix] = n

                b = self.name[i]
                self.name[i] = self.name[ix]
                self.name[ix] = b

                f = self.priority[i]
                self.priority[i] = self.priority[ix]
                self.priority[ix] = f

                g = moment[i]
                moment[i] = moment[ix]
                moment[ix] = g

            for i in range(k, length):
                x = min(self.priority[i:])
                m = self.priority[i]
                ix = self.priority.index(x, i)
                self.priority[i] = self.priority[ix]
                self.priority[ix] = m

                n = self.ctime[i]
                self.ctime[i] = self.ctime[ix]
                self.ctime[ix] = n

                b = self.name[i]
                self.name[i] = self.name[ix]
                self.name[ix] = b

                f = self.dtime[i]
                self.dtime[i] = self.dtime[ix]
                self.dtime[ix] = f

                g = moment[i]
                moment[i] = moment[ix]
                moment[ix] = g

            if self.ctime[k] > t:
                for x in range(k, length):
                    if self.ctime[x] <= t:

                        self.ctime.insert(k, self.ctime[x])
                        del self.ctime[x+1]

                        self.dtime.insert(k, self.dtime[x])
                        del self.dtime[x+1]

                        self.name.insert(k, self.name[x])
                        del self.name[x+1]

                        self.priority.insert(k, self.priority[x])
                        del self.priority[x+1]

                        moment.insert(k, moment[x])
                        del moment[x+1]
                        break

            if self.ctime[k] <= t:
                print()
                print(f"{self.name[k]}:", end="")
                for q in range(t):
                    print(" ", end="")

                for a in range(int(self.dtime[k])):
                    print("#", end="")
                    time.sleep(1 / int(p))
                    t += 1

                # liczy czasy oczekiwania

                s += int(self.dtime[k])
                suma.append(int(s+delay))
                wtime.append(int(t-self.ctime[k]-self.dtime[k]))
                allwtime += int(wtime[k])  # całkowity czas oczekiwania
                k += 1
                print('', end="")

                if k > length-1:
                    flag = False

            else:
                print(' ', end='')
                time.sleep(1/int(p))
                delay += 1
                t += 1

        average_wtime = allwtime/length
        print()
        print()
        print()
        x = table()
        x.field_names = (
            "Lp.", "Nazwa Procesu",  "Czas przybycia", "Czas trwania", "Czas zakończenia",
            "Czas oczekiwania", "Priorytet początkowy:", "Priorytet końcowy")
        for y in range(0, length):
            x.add_row(
                [c, self.name[y], self.ctime[y], self.dtime[y],
                 suma[y], wtime[y], moment[y], self.priority[y]])
            c += 1
        print(x)
        print()
        print(f"średni czas oczekiwania wynosi: {round(average_wtime, 2)}ms")
        text_write = open('raport_sym1.txt', "a")
        text = str("\n\n\n Algorytm SJF Priorytetowy\n")
        text_write.writelines(text)
        text = str(x)
        text_write.writelines(text)
        text = str(
            f"\nśredni czas oczekiwania wynosi {round(average_wtime, 2)}ms")
        text_write.writelines(text)

        text_write.close()
        for i in range(0, length):
            self.priority[i] = moment[i]


name = []
ctime = []
dtime = []
priority = []

xd = Sym1(name, ctime, dtime, priority)
xd.clear()
xd.read()
xd.info()

decision = True

while decision:
    option = input(
        "Podaj numer algorytmu, który chcesz przetestować(1-FCFS, 2-SJF, 3-SJF_Priorytetowy jeśli chcesz wyjść wpisz 4)")
    if option == '1':
        xd.sort_fcfs()
        xd.fcfs()
    elif option == '2':
        xd.sort_fcfs()
        xd.sort_sjf()
        xd.sjf()
    elif option == '3':
        xd.sjf_priority()
    elif option.lower() == '4':
        decision = False
    else:
        sys.exit(
            "Podano nieprawidłową opcję! Dozwolone są opcje 1,2,3,4")
