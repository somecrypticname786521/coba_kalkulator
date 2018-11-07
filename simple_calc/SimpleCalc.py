class SimpleCalc:
    def run(self):
        self.__init()
        expression = input("Masukkan operasi matematika yang diinginkan: ")
        print(expression)
        hasil = self.__compute(expression)
        print("hasil: " + str(hasil))

    def __init(self):
        """
        Mengeluarkan kalimat pembukaan
        >>> SimpleCalc()._SimpleCalc__init()
        Welkam tu mobail lejen
        """
        print("Welkam tu mobail lejen")

    def __compute(self, string_expression):
        """
        Menghitung hasil dari ekspresi yang ditulis

        >>> SimpleCalc()._SimpleCalc__compute("1")
        1
        >>> SimpleCalc()._SimpleCalc__compute("11+1")
        12
        >>> #SimpleCalc()._SimpleCalc__compute("2^3")
        #8
        >>> #SimpleCalc()._SimpleCalc__compute("root(4,2)")
        #2
        >>> #SimpleCalc()._SimpleCalc__compute("root(8,3)")
        #2
        """
        return eval(string_expression)