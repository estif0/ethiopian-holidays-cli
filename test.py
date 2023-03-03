def findNewYear(ameteTotal):
    return ameteTotal % 7


ZemeneWengel = 0


class Date:
    pass


def findMedeb(ameteAlem):
    return ameteAlem % 19


def findWenber(medeb):
    return 18 if medeb == 0 else medeb-1


def findAbeqte(wenber):
    return (wenber*11) % 30 if wenber*11 >= 30 else wenber*11


def findMetqe(abeqte):
    return 30-abeqte


def findBealeMetqe(metqe):
    if 30 > metqe >= 15:
        return f"{months[1]} {metqe}"
    elif 13 > metqe >= 2:
        return f"{months[2]} {metqe}"
    else:
        return f"{months[1]} 30"


def findTewsak():
    pass


def findMebajaHamer():
    pass


def TsomeNenewe():
    pass


def findAmeteWengel():
    pass


def findNameOfTheDay(month, ameteMihiret):
    pass


def findAmeteWengel():
    pass


eleteTwesag = []
ameteWengelList = {0: 'ዘመነ ዮሐንስ',
                   1: 'ዘመነ ማቴዎስ',
                   2: 'ዘመነ ማርቆስ',
                   3: 'ዘመነ ሉቃስ'}
newYearDayName = {1: 'እሁድ',
                  2: 'ሰኞ',
                  3: 'ማክሰኞ',
                  4: 'ረቡዕ',
                  5: 'ሐሙስ',
                  6: 'አርብ',
                  0: 'ቅዳሜ'}
consistentHolidays = []
months = {1: 'መስከረም',
          2: 'ጥቅምት',
          3: 'ህዳር',
          4: 'ታህሳስ',
          5: 'ጥር',
          6: 'የካቲት',
          7: 'መጋቢት',
          8: 'ሚያዝያ',
          9: 'ግንቦት',
          10: 'ሰኔ',
          11: 'ሀምሌ',
          12: 'ነሐሴ',
          13: 'ጷግሜ'}
findNameOfTheDayDict = {1: ''}

ameteMihiret = int(input())
ameteAlem = 5500+ameteMihiret
ameteWengel, meteneRabit = [ameteWengelList[ameteAlem % 4], ameteAlem//4]
ameteTotal = ameteAlem+meteneRabit+2
newYearDay = f"{newYearDayName[findNewYear(ameteTotal)]} {months[1]} 1 {ameteMihiret} E.C."
medeb = findMedeb(ameteAlem)
wenber = findWenber(medeb)
abeqte = findAbeqte(wenber)
metqe = findMetqe(abeqte)
bealeMetqe = findBealeMetqe(metqe)
print(newYearDay, medeb, wenber, abeqte, metqe, bealeMetqe)
