class Matrika:

    """Preprost razred za lažjo obdelavo
    in razumevanje problemov z matrikami"""

    def __init__(self, matrika):
        self.matrika = matrika
        self.vrstice = len(matrika)
        self.stolpci = len(matrika[0])
    
    def __str__(self):
        return "Matrika velikosti {0} krat {1}: {2}".format(self.vrstice, self.stolpci, self.matrika)
    
    def __repr__(self):
        return "Matrika({0})".format(self.matrika)

    #def __getitem__(self, indeks):
    #    return self.vrstice[indeks]

    #def __setitem__(self, indeks, item):
    #    self.vrstice[indeks] = item

    def __eq__(self, other):
        return self.matrika == other.matrika

    def transponiraj(self):
        m = self.vrstice
        n = self.stolpci
        transponiranka = []
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append(self.matrika[j][i])
            transponiranka.append(vrstica)
        return Matrika(transponiranka)

    def __add__(self, other):
        # seveda zajeto tudi odštevanje
        if self.vrstice != other.vrstice or self.stolpci != other.stolpci:
            raise Exception("Velikosti se ne ujemajo!")
        else:
            m = self.vrstice
            n = self.stolpci
            vsota = []
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self.matrika[i][j] + other.matrika[i][j])
                vsota.append(vrstica)
            return Matrika(vsota)

    def __mul__(self, other):
        # množimo lahko s številko ali (ustrezno) matriko
        # tu zajeto tudi množenje matrike in vektorja

        #POPRAVI!

        if isinstance(other, int) or isinstance(other, float):
            zmnozek = []
            m = self.vrstice
            n = self.stolpci
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self.matrika[i][j] * other)
                zmnozek.append(vrstica)
            return Matrika(zmnozek)

        elif isinstance(other, Matrika):
            if self.stolpci == other.vrstice:
                trans = other.transponiraj
                zmnozek = []
                m = self.vrstice
                n = self.stolpci
                for i in range(m):
                    vrstica = []
                    for j in range(n):
                        vrstica.append(sum([item[0] * item[1] for item in zip(self.matrika[i], trans.matrika[j])]))
                    zmnozek.append(vrstica)
                return Matrika(zmnozek)
        else:
            raise Exception("Si prepričan da so velikosti/tipi pravilni?")

    def sled(self):
        sled = 0
        for i in range(self.vrstice):
            sled += self.matrika[i][i]
            return sled

    def determinanta(self):
        # s pomočjo rekurzije izračunamo determinante matrik (skoraj) poljubnih velikosti
        if self.vrstice != self.stolpci:
            raise Exception("Determinanto imajo le kvadratne matrike!")
        elif self.vrstice == 2:
            return self.matrika[0][0] * self.matrika[1][1] - self.matrika[0][1] * self.matrika[1][0]
        else:



    def inverz(self):
        pass

a = Matrika([[0, 1], [1, 0]])
b = Matrika([[1, 0], [0, 1], [0, 0]])
print(b.determinanta)
    



