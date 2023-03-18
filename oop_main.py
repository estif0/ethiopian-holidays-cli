from tabulate import tabulate

class Date:
    #Initialization of year and datas that are going to be needed for futher calulations
    ameteMihiret=0
    eleteTwesag = {'እሁድ': 7, 'ሰኞ': 6, 'ማክሰኞ': 5,'ረቡዕ': 4, 'ሐሙስ': 3, 'አርብ': 2, 'ቅዳሜ': 8}
    ameteWengelList = {0: 'ዘመነ ዮሐንስ', 1: 'ዘመነ ማቴዎስ', 2: 'ዘመነ ማርቆስ', 3: 'ዘመነ ሉቃስ'}
    newYearDayName = {1: 'እሁድ', 2: 'ሰኞ', 3: 'ማክሰኞ',4: 'ረቡዕ', 5: 'ሐሙስ', 6: 'አርብ', 0: 'ቅዳሜ'}
    months = {1: 'መስከረም', 2: 'ጥቅምት', 3: 'ህዳር', 4: 'ታህሳስ', 5: 'ጥር', 6: 'የካቲት',7: 'መጋቢት', 8: 'ሚያዝያ', 9: 'ግንቦት', 10: 'ሰኔ', 11: 'ሀምሌ', 12: 'ነሐሴ'}
    yon = {'እሁድ': 5, 'ሰኞ': 6, 'ማክሰኞ': 7, 'ረቡዕ': 1, 'ሐሙስ': 2, 'አርብ': 3, 'ቅዳሜ': 4}
    astifeWer = {'መስከረም': 2, 'ጥቅምት': 4, 'ህዳር': 6, 'ታህሳስ': 8, 'ጥር': 10, 'የካቲት': 12,'መጋቢት': 14, 'ሚያዝያ': 16, 'ግንቦት': 18, 'ሰኔ': 20, 'ሀምሌ': 22, 'ነሐሴ': 24}
    nameOfTheDay = newYearDayName
    eyweredEyareg = {"abiyTsom": [14, ["የካቲት", "መጋቢት"], 1, 5], "debreZeyit": [11, ["የካቲት", "መጋቢት", "ሚያዝያ"], 28, 2], "hosaina": [2, ["መጋቢት", "ሚያዝያ"], 19, 23], "seqlet": [7, ["መጋቢት", "ሚያዝያ"], 24, 28], "fasika": [9, ["መጋቢት", "ሚያዝያ"], 26, 30], "erkibeKahinat": [3, ["ሚያዝያ", "ግንቦት"], 20, 24], "erget": [18, ["ግንቦት", "ሰኔ"], 5, 9], "peraclitos": [28, ["ግንቦት", "ሰኔ"], 15, 19], "tsomeHawariyat": [29, ["ግንቦት", "ሰኔ"], 16, 20], "tsomeDihinet": [1, ["ግንቦት", "ሰኔ"], 18, 22], }
    def dayName(self,monthDayString):   #Finds the name of the day with the parameter being month and day strinf
        month, day = monthDayString.split()
        return self.nameOfTheDay[(self.yon[self.newYearDayName[self.ameteTotal % 7]]+self.astifeWer[month]+int(day)) % 7]
    def findTsomeNenewe(self,bealeMetqe, mebajaHamer):  #Finds when Tsome nenewe Begins
        m, d = bealeMetqe.split()
        if int(d) == 0 or int(d) == 30:
            return f"የካቲት {mebajaHamer}"
        elif mebajaHamer > 30:
            return f"የካቲት {mebajaHamer%30}"
        elif m == "መስከረም":
            return f"ጥር {mebajaHamer}"
        elif m == "ጥቅምት":
            return f"የካቲት {mebajaHamer}"
    def findNameOfTheDay(self, day, month): #finds the name of the day like the first function but the parameter is separated day and month
        return self.nameOfTheDay[(self.yon[self.newYearDayName[self.ameteTotal % 7]]+self.astifeWer[month]+day) % 7]
    def findBealeMetqe(self): #Finds Beale Metqe which is needed for further calculation
        if 30 > self.metqe >= 15:
            return f"{self.months[1]} {self.metqe}"
        elif 13 > self.metqe >= 2:
            return f"{self.months[2]} {self.metqe}"
        else:
            return f"{self.months[1]} 30"
    def findTewsak(self):   #Finds Tewsak which is needed for further calculation
        m, d = self.bealeMetqe.split()
        return self.eleteTwesag[self.findNameOfTheDay(int(d), m)]
    def DayOfTheHoliday(self,beal): #Finds the day of the holiday using a dictionary from above
        dayOfTheHoliday = self.eyweredEyareg[beal][0]+self.mebajaHamer
        if dayOfTheHoliday > 30:
            dayOfTheHoliday = dayOfTheHoliday % 30
        if self.eyweredEyareg[beal][2] <= dayOfTheHoliday <= 30:
            MDHoliday = f"{self.eyweredEyareg[beal][1][0]} {dayOfTheHoliday}"
        elif 1 <= dayOfTheHoliday <= self.eyweredEyareg[beal][3]:
            MDHoliday = f"{self.eyweredEyareg[beal][1][1]} {dayOfTheHoliday}"
        return f"{self.dayName(MDHoliday)} {MDHoliday}"
    def findDebireZeyit(self):  #Finds when debrezeyit occurs
        month,day=self.findTsomeNenewe(self.bealeMetqe, self.mebajaHamer).split()
        nenewe=int(day)+41
        increment=0
        while(nenewe>30):
            nenewe-=30
            increment+=1
        month=self.months[(self.astifeWer[month]/2)+increment]
        fullDay=f"{month} {nenewe}"
        return f"{self.dayName(fullDay)} {month} {nenewe}"
    def __init__(self, ameteMihiret):   #Calculates All the holidays in the year
        self.ameteMihiret = ameteMihiret
        self.ameteAlem = self.ameteMihiret+5500
        self.ameteWengel, self.meteneRabit = [self.ameteWengelList[self.ameteAlem % 4], self.ameteAlem//4]
        self.ameteTotal = self.ameteAlem+self.meteneRabit+2
        self.newYearDay = f"{self.newYearDayName[self.ameteTotal%7]} {self.months[1]} 1"
        self.medeb = self.ameteAlem % 19
        self.wenber = 18 if self.medeb == 0 else self.medeb-1
        self.abeqte = (self.wenber*11) % 30 if self.wenber*11 >= 30 else self.wenber*11
        self.metqe = 30-self.abeqte
        self.bealeMetqe = self.findBealeMetqe()
        self.tewsak = self.findTewsak()
        self.mebajaHamer = self.tewsak if self.tewsak == 0 or self.tewsak == 30 else (self.metqe+self.tewsak) % 30
        self.tsomeNenewe = f"{self.dayName(self.findTsomeNenewe(self.bealeMetqe, self.mebajaHamer))} {self.findTsomeNenewe(self.bealeMetqe, self.mebajaHamer)}"
        self.abiyTsom = self.DayOfTheHoliday('abiyTsom')
        self.hosaina = self.DayOfTheHoliday('hosaina')
        self.seqlet = self.DayOfTheHoliday('seqlet')
        self.fasika = self.DayOfTheHoliday('fasika')
        self.erkibeKahinat = self.DayOfTheHoliday('erkibeKahinat')
        self.erget = self.DayOfTheHoliday('erget')
        self.peraclitos = self.DayOfTheHoliday('peraclitos')
        self.tsomeHawariyat = self.DayOfTheHoliday('tsomeHawariyat')
        self.tsomeDihinet = self.DayOfTheHoliday('tsomeDihinet')
        self.gena = f"{self.dayName('ታህሳስ 29')} ታህሳስ 29" if self.ameteWengel != 'ዘመነ ዮሐንስ' else f"{self.dayName('ታህሳስ 28')} ታህሳስ 28"
        self.timket = f"{self.dayName('ጥር 11')} ጥር 11"
        self.kanaZegelila = f"{self.dayName('ጥር 12')} ጥር 12"
        self.mesqel = f"{self.dayName('መስከረም 17')} መስከረም 17"
        self.bealeTsinset = f"{self.dayName('መጋቢት 29')} መጋቢት 29"
        self.bealeSimeon = f"{self.dayName('የካቲት 8')} የካቲት 8"
        self.bealeGirizat = f"{self.dayName('ጥር 6')} ጥር 6"
        self.genbotLidata = f"{self.dayName('ግንቦት 1')} ግንቦት 1"
        self.derbreTabor = f"{self.dayName('ነሐሴ 13')} ነሐሴ 13"
        self.TsomeLidet = f"{self.dayName('ህዳር 16')} ህዳር 16" if self.ameteWengel != 'ዘመነ ዮሐንስ' else f"{self.dayName('ህዳር 15')} ህዳር 15"
        self.dayOfTimket = self.dayName('ጥር 11')
        self.TsomeGehad = f"{self.dayName('ጥር 10')} ጥር 10" if self.dayOfTimket == 'አርብ' or self.dayOfTimket == 'ረቡዕ' else 'የለም'
        self.tsomeFilseta = f"{self.dayName('ነሐሴ 1')} ነሐሴ 1"
        self.tsomeFilsetaMefchiya = f"{self.dayName('ነሐሴ 16')} ነሐሴ 16"
        self.debreZeyit = self.findDebireZeyit()
        self.printTitleList = ["እንቁጣጣሽ", "መስቅል", "የገና ፆም", "ገና", "ጾመ ገሃድ", "ጥምቀት", "ቃና ዘገሊላ", "ጾመ ነነዌ", "በዓለ ስምዖን","ጾመ አብይ(ሁዳዴ)", "በአለ መስቀል ደብረዘይት", "በዓለ ትንሰት", "ሆሳዕና", "ስቅለት", "ፋሲካ", "ግንቦት ልደታ", "ርክበ ካህናት", "ዕርገት", "ጰራቅሊጦስ", "ጾመ ሃዋርያት(የሰኔ ጾም)", "ጾመ ድህነት","ጾመ ፍልሰታ", "ደብልታቦር(ቡሄ)", "ጾመ ፍልሰታ መፍቻ",]
        self.printValueList = [self.newYearDay, self.mesqel, self.TsomeLidet, self.gena, self.TsomeGehad, self.timket, self.kanaZegelila, self.tsomeNenewe, self.bealeSimeon, self.abiyTsom, self.debreZeyit, self.bealeTsinset,self.hosaina, self.seqlet, self.fasika, self.genbotLidata, self.erkibeKahinat, self.erget, self.peraclitos, self.tsomeHawariyat, self.tsomeDihinet, self.tsomeFilseta, self.derbreTabor, self.tsomeFilsetaMefchiya]
    def print(self):    #Used to print all the calculated holidays from above
        print(tabulate({"የበዓላት ስም": self.printTitleList, "የሚውሉበት ቀናት": self.printValueList},headers="keys", tablefmt="fancy_grid"))

def enter():    #Checks for invalid input when users are asked to enter the year
    try:
        global gh
        gh = gh = Date(int(input("Enter the year: ")))
    except:
        print("Please enter a valid Year!")
        enter()
        
# Start of code
print("Welcome!\nThis program let's you know major holidays and festivals in the ethiopian calendar.")
while 1:
    enter()
    gh.print()
    option = input("Do you want to continue? Press (N) to exit or press any key to continue: ")
    if option.upper() == 'N':
        break
    else:
        continue