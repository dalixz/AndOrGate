# Verwaltungsinfos
__version__ = "1.0"
__author__ = "DLI"

# Klassendeklaration für AND-Gate
class AndGate:
    def __init__(self):
        # Attribute definieren
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "YaAndGate"

    def execute(self):
        self.__Output = False
        if self.__Input1 == self.__Input0:
            if True == self.__Input0:
                self.__Output = True

    def show(self):
        print(str(self))

    def set(self, Input0, Input1, Name):
        self.__Input0 = Input0
        self.__Input1 = Input1
        self.__Name = Name

    def get(self):
        return self.__Output

    def __str__(self):
        str = "Ergibt Falsch"
        if True == self.__Output:
            str = "Ergibt Richtig"

        return str

# Klassendeklaration für OR-Gate
class OrGate:
    def __init__(self):
        # Attribute definieren
        self.__Input0 = False
        self.__Input1 = False
        self.__Output = False
        self.__Name = "YaAndGate"

    def execute(self):
        self.__Output = False
        if self.__Input0 == True:
            self.__Output = True
        if self.__Input1 == True:
            self.__Output = True

    def show(self):
        print(str(self))

    def set(self, Input0, Input1, Name):
        self.__Input0 = Input0
        self.__Input1 = Input1
        self.__Name = Name

    def get(self):
        return self.__Output

    def __str__(self):
        str = "Ergibt Falsch"
        if True == self.__Output:
            str = "Ergibt Richtig"

        return str