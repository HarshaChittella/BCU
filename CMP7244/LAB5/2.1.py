class BMI:

    def __init__(self, height, weight):
        self.height = float(height)
        self.weight = float(weight)
        self.bmi = 0.0

    def set_weight():
        weight = float(input('Enter the Weight in KGs: '))
        return weight

    def set_height():
        height = float(input('Enter the height in cms: '))
        return height

    def calc_bmi(self):
        bmi = self.weight/((self.height/100)**2)
        return bmi


def main():
    wt = BMI.set_weight()
    ht = BMI.set_height()
    body = BMI(ht, wt)
    print(body.calc_bmi())


main()
