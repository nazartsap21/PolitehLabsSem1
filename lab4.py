class ColdStore:
    """coldstore characteristics"""
    def __init__(self, company, volume, weight, power):
        self.__company = company
        self.__volume = volume
        self.__weight = weight
        self.__power = power
        self.str_ = 'str'
        self.int_ = 777

    def get_company(self):
        return self.__company

    def get_volume(self):
        return self.__volume

    def get_weight(self):
        return self.__weight

    def get_power(self):
        return self.__power

    def __str__(self):
        return (f'Coldstore from {self.__company} with volume {self.__volume},'
                f' weight {self.__weight} and power {self.__power}')

    def __repr__(self):
        return (f'Coldstore(\'{self.__company}\', {self.__volume},'
                f' {self.__weight}, {self.__power})')

    def __del__(self):
        print('Destructor called, Cold Store deleted')
