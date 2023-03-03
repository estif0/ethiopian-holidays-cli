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


def findTewsak(bealeMetqe):
    m, d = bealeMetqe.split()
    return eleteTwesag[findNameOfTheDay(d, m, ameteTotal)]


def findMebajaHamer(tewsak):
    pass


def TsomeNenewe():
    pass


def findAmeteWengel():
    pass


def findNameOfTheDay(day, month, ameteTotal):
    a = yon[newYearDayName[findNewYear(ameteTotal)]]
    b = astifeWer[month]
    c = day
    return nameOfTheDay[a+b+c]


def findAmeteWengel():
    pass


eleteTwesag = {'እሁድ': 7,
               'ሰኞ': 6,
               'ማክሰኞ': 5,
               'ረቡዕ': 4,
               'ሐሙስ': 3,
               'አርብ': 2,
               'ቅዳሜ': 8}
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
yon = {'እሁድ': 5,
       'ሰኞ': 6,
       'ማክሰኞ': 7,
       'ረቡዕ': 1,
       'ሐሙስ': 2,
       'አርብ': 3,
       'ቅዳሜ': 4}
astifeWer = {'መስከረም': 2,
             'ጥቅምት': 4,
             'ህዳር': 6,
             'ታህሳስ': 8,
             'ጥር': 10,
             'የካቲት': 12,
             'መጋቢት': 14,
             'ሚያዝያ': 16,
             'ግንቦት': 18,
             'ሰኔ': 20,
             'ሀምሌ': 22,
             'ነሐሴ': 24}
nameOfTheDay = newYearDayName


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
tewsak = findTewsak(bealeMetqe)
mebajaHamer = 0
