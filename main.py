class Biblioteka:
    def __init__(self):
        self.egzemplarze = []

    def __str__(self):
        lista = []
        for i in self.egzemplarze:
            lista.append((tuple(i)))
        lista.sort(key=lambda krotka: krotka[0])
        string_to_return = ""
        for i in lista:
            string_to_return += str(i) + "\n"
        return string_to_return

    def dodaj_egzemplarz(self, ksiazka):
        if len(self.egzemplarze) < 1:
            self.egzemplarze.append(list(ksiazka) + [1])
            return

        for index, item in enumerate(self.egzemplarze):
            if item[0] == ksiazka[0] or item[1] == ksiazka[1]:
                item[3] += 1
                self.egzemplarze[index] = item
                return

        x = list(ksiazka) + [1]
        self.egzemplarze.append(x)


biblioteka = Biblioteka()
ilosc = int(input(""))
for a in range(0, ilosc):
    biblioteka.dodaj_egzemplarz(eval(input()))

print(biblioteka)