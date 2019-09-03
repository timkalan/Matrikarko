import random

class Matrika:

    """ Preprost razred za lažjo obdelavo in razumevanje
        problemov z matrikami. """

    def __init__(self, matrika):
        self.matrika = matrika
        self.vrstice = len(matrika)
        self.stolpci = len(matrika[0])
    
    def __str__(self):
        mat = ""
        for vrstica in self.matrika:
            mat += str(vrstica) + '\n'
        return mat
    
    def __repr__(self):
        return "Matrika({0})".format(self.matrika)

    def __eq__(self, other):
        return self.matrika == other.matrika

    def __getitem__(self, indeks):
        return self.matrika[indeks]

    def __setitem__(self, indeks, item):
        self.matrika[indeks] = item

    def __add__(self, other):
        """ Sešteje matriki po komponentah. """

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
        """ Omogoča množenje matrik z drugimi matrikami, skalarji in vektorji. """

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
                trans = other.transponiraj()
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

    def __rmul__(self, other):
        # dodano za bolj elegantno množenje s števili (komutativnost)
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

    def sled(self):
        """ Izračuna vsoto diagonalnih elementov kvadratne matrike. """
        
        if not self.kvadratna():
            raise Exception("Sled računamo le kvadratnim matrikam!")
        else:
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
                vrstica.append(self[j][i])
            transponiranka.append(vrstica)
        return Matrika(transponiranka)

    def determinanta(self):
        """ S pomočjo rekurzije izračuna determinante matrik (skoraj) poljubnih velikosti. """

        if not self.kvadratna():
            raise Exception("Determinanto imajo le kvadratne matrike!")
        elif self.vrstice == 1:
            return self.matrika[0][0]
        elif self.vrstice == 2:
            return self.matrika[0][0] * self.matrika[1][1] - self.matrika[0][1] * self.matrika[1][0]

        else:
            A = self.matrika
            total = 0
            indeksi = list(range(len(A)))

            for stolpci in indeksi:
                A2 = A 
                A2 = A2[1:]
                visina = len(A2)
 
                for i in range(visina): 
                    A2[i] = A2[i][0:stolpci] + A2[i][stolpci+1:] 
 
                sign = (-1) ** (stolpci % 2)
                A2 = Matrika(A2)
                sub_det = A2.determinanta()
                total += sign * A[0][stolpci] * sub_det 
 
            return total

    def inverz_hitri(self):
        if not self.kvadratna():
            raise Exception("Ne-kvadratna matrika!")
        elif self.determinanta() == 0:
            raise Exception("Singularna matrika!")

        else:
            n = self.vrstice
            A = self.matrika
            A2 = A
            I = Matrika.naredi_identiteto(n)
            I = I.matrika
            I2 = I

            indeksi = list(range(n))
            for diagonala in range(n):
                diagonalaS = 1.0 / A2[diagonala][diagonala]
                for j in range(n):
                    A2[diagonala][j] *= diagonalaS
                    I2[diagonala][j] *= diagonalaS
                for i in indeksi[:diagonala] + indeksi[diagonala+1:]:
                    vrsticaS = A2[i][diagonala]
                    for j in range(n):
                        A2[i][j] = A2[i][j] - vrsticaS * A2[diagonala][j]
                        I2[i][j] = I2[i][j] - vrsticaS * I2[diagonala][j]

            
            A = Matrika(A)
            I2 = Matrika(I2)
            if Matrika(I) == A * I2:
                return I2

    def minor(self, i, j):
        m = self
        return Matrika([vrstica[:j] + vrstica[j+1:] for vrstica in (m[:i]+m[i+1:])])

    def inverz(self):
        """ Z uporabo pridružene matrike kofaktorjev in determinante izračuna inverz matrike,
            če ta obstaja. """

        if not self.kvadratna():
            raise Exception("Ne-kvadratna matrika!")
        elif self.determinanta() == 0:
            raise Exception("Singularna matrika!")
        else:
            m = self.vrstice
            pridruzenka = []
            for i in range(m):
                vrstica = []
                for j in range(m):
                    vrstica.append((-1) ** (i + j) * self.minor(i, j).determinanta())
                pridruzenka.append(vrstica)
            pridruzenka = Matrika(pridruzenka)
            skalar = 1 / self.determinanta()
            return skalar * pridruzenka.transponiraj()

    def cramer(self, b):
        """ S pomočjo Cramerjevega pravila reši sistem Ax = b, ki ima
            n enačb z n neznankami, oziroma ugotovi, da nima enolične rešitve.
            Če uspe, vrne vektor, ki predstavlja rešitev (torej x). """

        if self.determinanta() == 0:
            return "Sistem nima enolične rešitve!"
        elif len(b) != self.vrstice:
            raise Exception("Dolžina vektorja b se ne ujema!")
        elif not self.kvadratna():
            raise Exception("Rešujem samo kvadratne sisteme!")
        else:
            n = self.vrstice
            x = []
            for i in range(n):
                A = self.transponiraj()
                A = A[:i] + [b] + A[i+1:]
                A = Matrika(A)
                x.append(A.determinanta() / self.determinanta())
            return x
                
    def normalna(self):
        """ Preveri, če matrika komutira s svojo transponiranko. """

        # samo za realne matrike
        return self * self.transponiraj() == self.transponiraj() * self

    def simetricna(self):
        return self == self.transponiraj()

    def ortogonalna(self):
        return self.transponiraj() == self.inverz()

    def kvadratna(self):
        # za lažjo berljivost delov kode
        return self.vrstice == self.stolpci

    @classmethod
    def naredi_identiteto(cls, m):
        # za lažjo berljivost funkcije inverz
        vrstice = [[0]*m for x in range(m)]
        i = 0
        for vrstica in vrstice:
            vrstica[i] = 1
            i += 1
        return cls(vrstice)

    @classmethod
    def naredi_nakljucno(cls, m, n, od=0, do=9):
        """ Naredi naključno matriko velikosti m * n, z vrednostmi
            med min in max. """

        # uporabna metoda za testiranje programa
        matrika = []
        for _ in range(m):
            vrstica = []
            for _ in range(n):
                vrstica.append(random.randrange(od, do))
            matrika.append(vrstica)
        return cls(matrika)


A = Matrika([[3,6,7], [7,1,9], [6,0,7]])
