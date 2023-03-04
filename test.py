def findNewYear(ameteTotal):
    return ameteTotal % 7


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
    return eleteTwesag[findNameOfTheDay(int(d), m)]


def findMebajaHamer(tewsak):
    return tewsak if tewsak == 0 or tewsak == 30 else (metqe+tewsak) % 30


def findTsomeNenewe(bealeMetqe, mebajaHamer):
    m, d = bealeMetqe.split()
    if int(d) == 0 or int(d) == 30:
        return f"የካቲት {mebajaHamer}"
    elif mebajaHamer > 30:
        return f"የካቲት {mebajaHamer%30}"
    elif m == "መስከረም":
        return f"ጥር {mebajaHamer}"
    elif m == "ጥቅምት":
        return f"የካቲት {mebajaHamer}"


def findAmeteWengel():
    return ameteWengelList[ameteAlem % 4]


def findNameOfTheDay(day, month):
    a = yon[newYearDayName[findNewYear(ameteTotal)]]
    b = astifeWer[month]
    c = day
    d = (a+b+c) % 7
    return nameOfTheDay[d]


def findAbiyTsom(mebajaHamer):
    sum = eyweredEyareg["abiyTsom"][0] + mebajaHamer
    if 1 <= sum < 30:
        return f"የካቲት {sum}"
    elif sum >= 30:
        return f"መጋቢት {sum%30}"


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

eyweredEyareg = {"abiyTsom": [14, ["የካቲት", "መጋቢት"], 1, 5],
                 "debreZeyit": [11, ["የካቲት", "መጋቢት", "ሚያዝያ"], 1, 2],
                 "hosaina": [2, ["መጋቢት", "ሚያዝያ"], 19, 23],
                 "seqlet": [7, ["መጋቢት", "ሚያዝያ"], 24, 28],
                 "fasika": [9, ["መጋቢት", "ሚያዝያ"], 26, 30],
                 "erkibeKahinat": [3, ["ሚያዝያ", "ግንቦት"], 20, 24],
                 "erget": [18, ["ግንቦት", "ሰኔ"], 5, 9],
                 "peraclitos": [28, ["ግንቦት", "ሰኔ"], 15, 19],
                 "tsomeHawariyat": [29, ["ግንቦት", "ሰኔ"], 16, 20],
                 "tsomeDihinet": [1, ["ግንቦት", "ሰኔ"], 18, 22], }


def findTheDayOfTheHoliday(beal):
    dayOfTheHoliday = eyweredEyareg[beal][0]+mebajaHamer
    if dayOfTheHoliday >= 30:
        dayOfTheHoliday = dayOfTheHoliday % 30
    if eyweredEyareg[beal][2] <= dayOfTheHoliday <= 30:
        return f"{eyweredEyareg[beal][1][0]} {dayOfTheHoliday}"
    elif 1 <= dayOfTheHoliday <= eyweredEyareg[beal][3]:
        return f"{eyweredEyareg[beal][1][1]} {dayOfTheHoliday}"


# Start of the code:
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
mebajaHamer = findMebajaHamer(tewsak)
tsomeNenewe = findTsomeNenewe(bealeMetqe, mebajaHamer)
print(ameteAlem)
print(ameteWengel)
print(ameteTotal)
print(newYearDay)
print(medeb)
print(wenber)
print(abeqte)
print(metqe)
print(bealeMetqe)
print(tewsak)
print(mebajaHamer)
print(tsomeNenewe)
