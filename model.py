class Matrika:

    """ Preprost razred za lažjo obdelavo
    in razumevanje problemov z matrikami """

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
        # dodano za bolj elegantno množenje s števili
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
        sled = 0
        for i in range(self.vrstice):
            sled += self.matrika[i][i]
            return sled

    def determinanta(self):
        # s pomočjo rekurzije izračunamo determinante matrik (skoraj) poljubnih velikosti
        if self.vrstice != self.stolpci:
            raise Exception("Determinanto imajo le kvadratne matrike!")
        elif self.vrstice == 1:
            return self.matrika[0][0]
        elif self.vrstice == 2:
            return self.matrika[0][0] * self.matrika[1][1] - self.matrika[0][1] * self.matrika[1][0]

        else:
            # dela, ampak a veš zakaj?

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

    def inverz(self):
        if self.vrstice != self.stolpci:
            raise Exception("Ne-kvadratna matrika!")
        elif self.determinanta() == 0:
            raise Exception("Singularna matrika!")

        else:
            n = self.vrstice
            A = self.matrika
            A2 = A

            # naredimo identiteto velikosti n * n
            I = []
            for i in range(n):
                vrstica = []
                for j in range(n):
                    vrstica.append(1 if i == j else 0)
                I.append(vrstica)
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


a = Matrika([[1, 1, 2], [1, 1, 3], [0, 1, 5]])
b = Matrika([[1, 4], [2, 1]])
print(a.inverz())
    



