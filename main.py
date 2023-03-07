from tabulate import tabulate


def findNewYear(ameteTotal):
    return ameteTotal % 7


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


def findNameOfTheDay(day, month):
    a = yon[newYearDayName[findNewYear(ameteTotal)]]
    b = astifeWer[month]
    c = day
    d = (a+b+c) % 7
    return nameOfTheDay[d]


def findTheDayOfTheHoliday(beal):
    dayOfTheHoliday = eyweredEyareg[beal][0]+mebajaHamer
    if dayOfTheHoliday > 30:
        dayOfTheHoliday = dayOfTheHoliday % 30
    if eyweredEyareg[beal][2] <= dayOfTheHoliday <= 30:
        MDHoliday = f"{eyweredEyareg[beal][1][0]} {dayOfTheHoliday}"
    elif 1 <= dayOfTheHoliday <= eyweredEyareg[beal][3]:
        MDHoliday = f"{eyweredEyareg[beal][1][1]} {dayOfTheHoliday}"

    return f"{findNameOfTheDayForHoliday(MDHoliday)} {MDHoliday}"


def findNameOfTheDayForHoliday(monthDayString):
    month, day = monthDayString.split()
    a = yon[newYearDayName[findNewYear(ameteTotal)]]
    b = astifeWer[month]
    c = int(day)
    d = (a+b+c) % 7
    return nameOfTheDay[d]


eleteTwesag = {'እሁድ': 7, 'ሰኞ': 6, 'ማክሰኞ': 5,'ረቡዕ': 4, 'ሐሙስ': 3, 'አርብ': 2, 'ቅዳሜ': 8}

ameteWengelList = {0: 'ዘመነ ዮሐንስ', 1: 'ዘመነ ማቴዎስ', 2: 'ዘመነ ማርቆስ', 3: 'ዘመነ ሉቃስ'}

newYearDayName = {1: 'እሁድ', 2: 'ሰኞ', 3: 'ማክሰኞ',4: 'ረቡዕ', 5: 'ሐሙስ', 6: 'አርብ', 0: 'ቅዳሜ'}

months = {1: 'መስከረም', 2: 'ጥቅምት', 3: 'ህዳር', 4: 'ታህሳስ', 5: 'ጥር', 6: 'የካቲት',7: 'መጋቢት', 8: 'ሚያዝያ', 9: 'ግንቦት', 10: 'ሰኔ', 11: 'ሀምሌ', 12: 'ነሐሴ'}

yon = {'እሁድ': 5, 'ሰኞ': 6, 'ማክሰኞ': 7, 'ረቡዕ': 1, 'ሐሙስ': 2, 'አርብ': 3, 'ቅዳሜ': 4}

astifeWer = {'መስከረም': 2, 'ጥቅምት': 4, 'ህዳር': 6, 'ታህሳስ': 8, 'ጥር': 10, 'የካቲት': 12,'መጋቢት': 14, 'ሚያዝያ': 16, 'ግንቦት': 18, 'ሰኔ': 20, 'ሀምሌ': 22, 'ነሐሴ': 24}

nameOfTheDay = newYearDayName

eyweredEyareg = {"abiyTsom": [14, ["የካቲት", "መጋቢት"], 1, 5], "debreZeyit": [11, ["የካቲት", "መጋቢት", "ሚያዝያ"], 28, 2], "hosaina": [2, ["መጋቢት", "ሚያዝያ"], 19, 23], "seqlet": [7, ["መጋቢት", "ሚያዝያ"], 24, 28], "fasika": [9, ["መጋቢት", "ሚያዝያ"], 26, 30], "erkibeKahinat": [3, ["ሚያዝያ", "ግንቦት"], 20, 24], "erget": [18, ["ግንቦት", "ሰኔ"], 5, 9], "peraclitos": [28, ["ግንቦት", "ሰኔ"], 15, 19], "tsomeHawariyat": [29, ["ግንቦት", "ሰኔ"], 16, 20], "tsomeDihinet": [1, ["ግንቦት", "ሰኔ"], 18, 22], }


def findDebireZeyit(beal):  # unfinished function
    dayOfTheHoliday = eyweredEyareg[beal][0]+mebajaHamer
    if dayOfTheHoliday > 30:
        dayOfTheHoliday %= 30
    if eyweredEyareg[beal][2] <= dayOfTheHoliday <= 30:
        MDHoliday = f"{eyweredEyareg[beal][1][0]} {dayOfTheHoliday}"
    elif 1 <= dayOfTheHoliday <= 30:
        MDHoliday = f"{eyweredEyareg[beal][1][1]} {dayOfTheHoliday}"
    elif 1 <= dayOfTheHoliday <= eyweredEyareg[beal][3]:
        MDHoliday = f"{eyweredEyareg[beal][1][2]} {dayOfTheHoliday}"
    return f"{findNameOfTheDayForHoliday(MDHoliday)} {MDHoliday}"


def enter():
    try:
        global ameteMihiret
        ameteMihiret = int(input("Enter the year: "))
    except:
        print("Please enter a valid Year!")
        enter()


print("Welcome!")  # Start of the code:
print("This program let's you know major holidays and festivals in the ethiopian calendar.")
while 1:
    enter()
    ameteAlem = 5500+ameteMihiret
    ameteWengel, meteneRabit = [ameteWengelList[ameteAlem % 4], ameteAlem//4]
    ameteTotal = ameteAlem+meteneRabit+2
    newYearDay = f"{newYearDayName[findNewYear(ameteTotal)]} {months[1]} 1"
    medeb = ameteAlem % 19
    wenber = 18 if medeb == 0 else medeb-1
    abeqte = (wenber*11) % 30 if wenber*11 >= 30 else wenber*11
    metqe = 30-abeqte

    bealeMetqe = findBealeMetqe(metqe)
    tewsak = findTewsak(bealeMetqe)
    mebajaHamer = tewsak if tewsak == 0 or tewsak == 30 else (metqe+tewsak) % 30
    tsomeNenewe = f"{findNameOfTheDayForHoliday(findTsomeNenewe(bealeMetqe, mebajaHamer))} {findTsomeNenewe(bealeMetqe, mebajaHamer)}"
    abiyTsom = findTheDayOfTheHoliday('abiyTsom')
    hosaina = findTheDayOfTheHoliday('hosaina')
    seqlet = findTheDayOfTheHoliday('seqlet')
    fasika = findTheDayOfTheHoliday('fasika')
    erkibeKahinat = findTheDayOfTheHoliday('erkibeKahinat')
    erget = findTheDayOfTheHoliday('erget')
    peraclitos = findTheDayOfTheHoliday('peraclitos')
    tsomeHawariyat = findTheDayOfTheHoliday('tsomeHawariyat')
    tsomeDihinet = findTheDayOfTheHoliday('tsomeDihinet')
    gena = f"{findNameOfTheDayForHoliday('ታህሳስ 29')} ታህሳስ 29" if ameteWengel != 'ዘመነ ዮሐንስ' else f"{findNameOfTheDayForHoliday('ታህሳስ 28')} ታህሳስ 28"
    timket = f"{findNameOfTheDayForHoliday('ጥር 11')} ጥር 11"
    kanaZegelila = f"{findNameOfTheDayForHoliday('ጥር 12')} ጥር 12"
    mesqel = f"{findNameOfTheDayForHoliday('መስከረም 17')} መስከረም 17"
    bealeTsinset = f"{findNameOfTheDayForHoliday('መጋቢት 29')} መጋቢት 29"
    bealeSimeon = f"{findNameOfTheDayForHoliday('የካቲት 8')} የካቲት 8"
    bealeGirizat = f"{findNameOfTheDayForHoliday('ጥር 6')} ጥር 6"
    genbotLidata = f"{findNameOfTheDayForHoliday('ግንቦት 1')} ግንቦት 1"
    derbreTabor = f"{findNameOfTheDayForHoliday('ነሐሴ 13')} ነሐሴ 13"
    TsomeLidet = f"{findNameOfTheDayForHoliday('ህዳር 15')} ህዳር 15"
    dayOfTimket = findNameOfTheDayForHoliday('ጥር 11')
    TsomeGehad = f"{findNameOfTheDayForHoliday('ጥር 10')} ጥር 10" if dayOfTimket == 'አርብ' or dayOfTimket == 'ረቡዕ' else 'የለም'
    tsomeFilseta = f"{findNameOfTheDayForHoliday('ነሐሴ 1')} ነሐሴ 1"
    tsomeFilsetaMefchiya = f"{findNameOfTheDayForHoliday('ነሐሴ 16')} ነሐሴ 16"
    debreZeyit = findDebireZeyit("debreZeyit")

    printTitleList = ["እንቁጣጣሽ", "መስቅል", "የገና ፆም", "ገና", "ጾመ ገሃድ", "ጥምቀት", "ቃና ዘገሊላ", "ጾመ ነነዌ", "በዓለ ስምዖን","ጾመ አብይ(ሁዳዴ)", "በአለ መስቀል ደብረዘይት", "በዓለ ትንሰት", "ሆሳዕና", "ስቅለት", "ፋሲካ", "ግንቦት ልደታ", "ርክበ ካህናት", "ዕርገት", "ጰራቅሊጦስ", "ጾመ ሃዋርያት(የሰኔ ጾም)", "ጾመ ድህነት", "ጾመ ፍልሰታ", "ደብልታቦር(ቡሄ)", "ጾመ ፍልሰታ መፍቻ",]
    printValueList = [newYearDay, mesqel, TsomeLidet, gena, TsomeGehad, timket, kanaZegelila, tsomeNenewe, bealeSimeon, abiyTsom, debreZeyit, bealeTsinset,hosaina, seqlet, fasika, genbotLidata, erkibeKahinat, erget, peraclitos, tsomeHawariyat, tsomeDihinet, tsomeFilseta, derbreTabor, tsomeFilsetaMefchiya]
    print(tabulate({"የበዓላት ስም": printTitleList,"የሚውሉበት ቀናት": printValueList}, headers="keys", tablefmt="fancy_grid"))
    option = input("Do you want to continue? Press (N) to exit or press any key to continue: ")
    if option.upper() == 'N':
        break
    else:
        continue