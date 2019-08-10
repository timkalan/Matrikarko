class Matrika:

    """Preprost razred za lažjo obdelavo
    in razumevanje problemov z matrikami"""

    def __init__(self, matrika):
        self.matrika = matrika
        self.vrstice = len(matrika)
        self.stolpci = len(matrika[0])
    
    def __str__(self):
        return "Matrika velikosti {0} krat {1}".format(self.vrstice, self.stolpci)
    
    def __repr__(self):
        return "Matrika({0})".format(self.matrika)

    def __eq__(self, other):
        return self.matrika == other.matrika

    def __add__(self, other):
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
                pass



        else:
            raise Exception("Si prepričan da so velikosti/tipi pravilni?")

    def sled(self):
        sled = 0
        for i in range(self.vrstice):
            sled += self.matrika[i][i]
            return sled

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

    def inverz(self):
        pass

    def determinanta(self):
        pass
    



