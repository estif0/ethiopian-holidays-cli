from tabulate import tabulate
from argparse import ArgumentParser, Namespace


class Date:
    def __init__(self, amete_mihiret):
        """This function intializes and computes all the neccessary calculations and variables to find the holidays.
        If you want to find out more on how these calculations were made, read the file in the documentation
        """
        self.amete_mihiret = amete_mihiret
        self.amete_alem = self.amete_mihiret + 5500
        self.amete_wengel, self.metene_rabit = [
            self.amete_wengel_list[self.amete_alem % 4],
            self.amete_alem // 4,
        ]
        self.amete_total = self.amete_alem + self.metene_rabit + 2
        self.new_year_day = (
            f"{self.new_year_day_name[self.amete_total%7]} {self.months[1]} 1"
        )
        self.medeb = self.amete_alem % 19
        self.wenber = 18 if self.medeb == 0 else self.medeb - 1
        self.abeqte = (
            (self.wenber * 11) % 30 if self.wenber * 11 >= 30 else self.wenber * 11
        )
        self.metqe = 30 - self.abeqte
        self.beale_metqe = self.find_beale_metqe()
        self.tewsak = self.find_tewsak()
        self.mebaja_hamer = (
            self.tewsak
            if self.tewsak == 0 or self.tewsak == 30
            else (self.metqe + self.tewsak) % 30
        )
        self.tsome_nenewe = f"{self.day_name(self.find_tsome_nenewe(self.beale_metqe, self.mebaja_hamer))} {self.find_tsome_nenewe(self.beale_metqe, self.mebaja_hamer)}"
        self.abiy_tsom = self.day_of_the_holiday("abiy_tsom")
        self.hosaina = self.day_of_the_holiday("hosaina")
        self.seqlet = self.day_of_the_holiday("seqlet")
        self.fasika = self.day_of_the_holiday("fasika")
        self.erkibe_kahinat = self.day_of_the_holiday("erkibe_kahinat")
        self.erget = self.day_of_the_holiday("erget")
        self.peraclitos = self.day_of_the_holiday("peraclitos")
        self.tsome_hawariyat = self.day_of_the_holiday("tsome_hawariyat")
        self.tsome_dihinet = self.day_of_the_holiday("tsome_dihinet")
        self.gena = (
            f"{self.day_name('ታህሳስ 29')} ታህሳስ 29"
            if self.amete_wengel != "ዘመነ ዮሐንስ"
            else f"{self.day_name('ታህሳስ 28')} ታህሳስ 28"
        )
        self.timket = f"{self.day_name('ጥር 11')} ጥር 11"
        self.kana_zegelila = f"{self.day_name('ጥር 12')} ጥር 12"
        self.mesqel = f"{self.day_name('መስከረም 17')} መስከረም 17"
        self.beale_tsinset = f"{self.day_name('መጋቢት 29')} መጋቢት 29"
        self.beale_simeon = f"{self.day_name('የካቲት 8')} የካቲት 8"
        self.beale_girizat = f"{self.day_name('ጥር 6')} ጥር 6"
        self.genbot_lideta = f"{self.day_name('ግንቦት 1')} ግንቦት 1"
        self.debre_tabor = f"{self.day_name('ነሐሴ 13')} ነሐሴ 13"
        self.tsome_lidet = (
            f"{self.day_name('ህዳር 16')} ህዳር 16"
            if self.amete_wengel != "ዘመነ ዮሐንስ"
            else f"{self.day_name('ህዳር 15')} ህዳር 15"
        )
        self.day_of_timket = self.day_name("ጥር 11")
        self.tsome_gehad = (
            f"{self.day_name('ጥር 10')} ጥር 10"
            if self.day_of_timket == "አርብ" or self.day_of_timket == "ረቡዕ"
            else "የለም"
        )
        self.tsome_filseta = f"{self.day_name('ነሐሴ 1')} ነሐሴ 1"
        self.tsome_filseta_mefchiya = f"{self.day_name('ነሐሴ 16')} ነሐሴ 16"
        self.debre_zeyit = self.findDebireZeyit()
        self.print_title_list = [
            "እንቁጣጣሽ",
            "መስቅል",
            "የገና ፆም",
            "ገና",
            "ጾመ ገሃድ",
            "ጥምቀት",
            "ቃና ዘገሊላ",
            "ጾመ ነነዌ",
            "በዓለ ስምዖን",
            "ጾመ አብይ(ሁዳዴ)",
            "በአለ መስቀል ደብረዘይት",
            "በዓለ ትንሰት",
            "ሆሳዕና",
            "ስቅለት",
            "ፋሲካ",
            "ግንቦት ልደታ",
            "ርክበ ካህናት",
            "ዕርገት",
            "ጰራቅሊጦስ",
            "ጾመ ሃዋርያት(የሰኔ ጾም)",
            "ጾመ ድህነት",
            "ጾመ ፍልሰታ",
            "ደብልታቦር(ቡሄ)",
            "ጾመ ፍልሰታ መፍቻ",
        ]
        self.print_value_list = [
            self.new_year_day,
            self.mesqel,
            self.tsome_lidet,
            self.gena,
            self.tsome_gehad,
            self.timket,
            self.kana_zegelila,
            self.tsome_nenewe,
            self.beale_simeon,
            self.abiy_tsom,
            self.debre_zeyit,
            self.beale_tsinset,
            self.hosaina,
            self.seqlet,
            self.fasika,
            self.genbot_lideta,
            self.erkibe_kahinat,
            self.erget,
            self.peraclitos,
            self.tsome_hawariyat,
            self.tsome_dihinet,
            self.tsome_filseta,
            self.debre_tabor,
            self.tsome_filseta_mefchiya,
        ]

    def day_name(self, month_day_string):
        """The function finds the name of the day like Monday,... when the parameter is a month and day string"""
        month, day = month_day_string.split()
        return self.name_of_the_day[
            (
                self.yon[self.new_year_day_name[self.amete_total % 7]]
                + self.astifeWer[month]
                + int(day)
            )
            % 7
        ]

    def find_tsome_nenewe(self, beale_metqe, mebaja_hamer):
        """The function finds the day of nenewe fasting starts"""
        m, d = beale_metqe.split()
        if int(d) == 0 or int(d) == 30:
            return f"የካቲት {mebaja_hamer}"
        elif mebaja_hamer > 30:
            return f"የካቲት {mebaja_hamer%30}"
        elif m == "መስከረም":
            return f"ጥር {mebaja_hamer}"
        elif m == "ጥቅምት":
            return f"የካቲት {mebaja_hamer}"

    def find_name_of_the_day(self, day, month):
        """Finds the name of the day like the first function but the parameter is a separated day and month variable"""
        return self.name_of_the_day[
            (
                self.yon[self.new_year_day_name[self.amete_total % 7]]
                + self.astifeWer[month]
                + day
            )
            % 7
        ]

    def find_beale_metqe(
        self,
    ):
        """The function finds Beale Metqe which is needed for further calculations to compute the day of other holidays"""
        if 30 > self.metqe >= 15:
            return f"{self.months[1]} {self.metqe}"
        elif 13 > self.metqe >= 2:
            return f"{self.months[2]} {self.metqe}"
        else:
            return f"{self.months[1]} 30"

    def find_tewsak(self):
        """Finds Tewsak which is needed for further calculation to find the day of the holidays"""
        m, d = self.beale_metqe.split()
        return self.elete_tewsag[self.find_name_of_the_day(int(d), m)]

    def day_of_the_holiday(self, beal):
        """Finds the day of the holiday using a dictionary from below"""
        day_of_the_holiday = self.eywered_eyareg[beal][0] + self.mebaja_hamer
        if day_of_the_holiday > 30:
            day_of_the_holiday = day_of_the_holiday % 30
        if self.eywered_eyareg[beal][2] <= day_of_the_holiday <= 30:
            MDHoliday = f"{self.eywered_eyareg[beal][1][0]} {day_of_the_holiday}"
        elif 1 <= day_of_the_holiday <= self.eywered_eyareg[beal][3]:
            MDHoliday = f"{self.eywered_eyareg[beal][1][1]} {day_of_the_holiday}"
        return f"{self.day_name(MDHoliday)} {MDHoliday}"

    def findDebireZeyit(self):
        """finds when the day when debre_zeyit Holiday occurs"""
        month, day = self.find_tsome_nenewe(self.beale_metqe, self.mebaja_hamer).split()
        nenewe = int(day) + 41
        increment = 0
        while nenewe > 30:
            nenewe -= 30
            increment += 1
        month = self.months[(self.astifeWer[month] / 2) + increment]
        fullDay = f"{month} {nenewe}"
        return f"{self.day_name(fullDay)} {month} {nenewe}"

    def print(self):
        """This function is used to print all the calculated holidays from above"""
        print(
            tabulate(
                {
                    "የበዓላት ስም": self.print_title_list,
                    "የሚውሉበት ቀናት": self.print_value_list,
                },
                headers="keys",
                tablefmt="fancy_grid",
            )
        )

    """The following lists and dictionaries are the data used to find the days of the holidays."""
    elete_tewsag = {
        "እሁድ": 7,
        "ሰኞ": 6,
        "ማክሰኞ": 5,
        "ረቡዕ": 4,
        "ሐሙስ": 3,
        "አርብ": 2,
        "ቅዳሜ": 8,
    }
    amete_wengel_list = {0: "ዘመነ ዮሐንስ", 1: "ዘመነ ማቴዎስ", 2: "ዘመነ ማርቆስ", 3: "ዘመነ ሉቃስ"}
    new_year_day_name = {
        1: "እሁድ",
        2: "ሰኞ",
        3: "ማክሰኞ",
        4: "ረቡዕ",
        5: "ሐሙስ",
        6: "አርብ",
        0: "ቅዳሜ",
    }
    months = {
        1: "መስከረም",
        2: "ጥቅምት",
        3: "ህዳር",
        4: "ታህሳስ",
        5: "ጥር",
        6: "የካቲት",
        7: "መጋቢት",
        8: "ሚያዝያ",
        9: "ግንቦት",
        10: "ሰኔ",
        11: "ሀምሌ",
        12: "ነሐሴ",
    }
    yon = {"እሁድ": 5, "ሰኞ": 6, "ማክሰኞ": 7, "ረቡዕ": 1, "ሐሙስ": 2, "አርብ": 3, "ቅዳሜ": 4}
    astifeWer = {
        "መስከረም": 2,
        "ጥቅምት": 4,
        "ህዳር": 6,
        "ታህሳስ": 8,
        "ጥር": 10,
        "የካቲት": 12,
        "መጋቢት": 14,
        "ሚያዝያ": 16,
        "ግንቦት": 18,
        "ሰኔ": 20,
        "ሀምሌ": 22,
        "ነሐሴ": 24,
    }
    name_of_the_day = new_year_day_name
    eywered_eyareg = {
        "abiy_tsom": [14, ["የካቲት", "መጋቢት"], 1, 5],
        "debre_zeyit": [11, ["የካቲት", "መጋቢት", "ሚያዝያ"], 28, 2],
        "hosaina": [2, ["መጋቢት", "ሚያዝያ"], 19, 23],
        "seqlet": [7, ["መጋቢት", "ሚያዝያ"], 24, 28],
        "fasika": [9, ["መጋቢት", "ሚያዝያ"], 26, 30],
        "erkibe_kahinat": [3, ["ሚያዝያ", "ግንቦት"], 20, 24],
        "erget": [18, ["ግንቦት", "ሰኔ"], 5, 9],
        "peraclitos": [28, ["ግንቦት", "ሰኔ"], 15, 19],
        "tsome_hawariyat": [29, ["ግንቦት", "ሰኔ"], 16, 20],
        "tsome_dihinet": [1, ["ግንቦት", "ሰኔ"], 18, 22],
    }


"""The code below uses the argparse module to make the program be executed in the terminal by adding arguments to 
perform a specific task."""
# -------------------------------------------------------------------------------------------------
parser = ArgumentParser(
    description="Print the days of the holidays and fastings in a year."
)
parser.add_argument(
    "yearin",
    help="prints all the holidays in the year if no other pararmeter is called",
    type=int,
)
parser.add_argument(
    "-n", "--newyear", help="prints the day of the New Year", action="store_true"
)
parser.add_argument(
    "-m", "--mesqel", help="prints the day of Mesqel", action="store_true"
)
parser.add_argument(
    "-tl", "--tsomelidet", help="prints the day of Tsome Lidet", action="store_true"
)
parser.add_argument("-g", "--gena", help="prints the day of Gena", action="store_true")
parser.add_argument(
    "-tg", "--tsomegehad", help="prints the day of Tsome Gehad", action="store_true"
)
parser.add_argument(
    "-t", "--timket", help="prints the day of Timket", action="store_true"
)
parser.add_argument(
    "-kz",
    "--kanazegelila",
    help="prints the day of Kana Zegelila",
    action="store_true",
)
parser.add_argument(
    "-tn", "--tsomenenewe", help="prints the day of Tsome Nenewe", action="store_true"
)
parser.add_argument(
    "-bs", "--bealesimeon", help="prints the day of Beale Simeon", action="store_true"
)
parser.add_argument(
    "-ta", "--tsomeabiy", help="prints the day of Tsome Abiy", action="store_true"
)
parser.add_argument(
    "-dz", "--debrezeyit", help="prints the day of Debre Zeyit", action="store_true"
)
parser.add_argument(
    "-bt", "--bealetsinset", help="prints the day of Beale Tinset", action="store_true"
)
parser.add_argument(
    "-ho", "--hosaina", help="prints the day of Hosaina", action="store_true"
)
parser.add_argument(
    "-s", "--seqlet", help="prints the day of Seqlet", action="store_true"
)
parser.add_argument(
    "-f", "--fasika", help="prints the day of Fasika", action="store_true"
)
parser.add_argument(
    "-gl",
    "--ginbotlideta",
    help="prints the day of Ginbot Lideta",
    action="store_true",
)
parser.add_argument(
    "-ek",
    "--erkibekahinat",
    help="prints the day of Erkibe Kahinat",
    action="store_true",
)
parser.add_argument(
    "-e", "--erget", help="prints the day of Erget", action="store_true"
)
parser.add_argument(
    "-p", "--peraclitos", help="prints the day of Peraclitos", action="store_true"
)
parser.add_argument(
    "-th",
    "--tsomehawariyat",
    help="prints the day of Tsome Hawariyat",
    action="store_true",
)
parser.add_argument(
    "-td", "--tsomedihnet", help="prints the day of Tsome Dihnet", action="store_true"
)
parser.add_argument(
    "-tf",
    "--tsomefilseta",
    help="prints the day of Tsome Filseta",
    action="store_true",
)
parser.add_argument(
    "-db", "--debretabor", help="prints the day of Debre Tabor", action="store_true"
)
parser.add_argument(
    "-etf",
    "--endoftsomefilseta",
    help="prints the day of end of Tsome",
    action="store_true",
)

args: Namespace = parser.parse_args()

# -------------------------------------------------------------------------------------------------

# Start of code
year = Date(args.yearin)
if args.newyear:
    print(year.new_year_day)
elif args.mesqel:
    print(year.mesqel)
elif args.tsomelidet:
    print(year.tsome_lidet)
elif args.gena:
    print(year.gena)
elif args.tsomegehad:
    print(year.tsome_gehad)
elif args.timket:
    print(year.timket)
elif args.kanazegelila:
    print(year.kana_zegelila)
elif args.tsomenenewe:
    print(year.tsome_nenewe)
elif args.bealesimeon:
    print(year.beale_simeon)
elif args.tsomeabiy:
    print(year.abiy_tsom)
elif args.debrezeyit:
    print(year.debre_zeyit)
elif args.bealetsinset:
    print(year.beale_tsinset)
elif args.hosaina:
    print(year.hosaina)
elif args.seqlet:
    print(year.seqlet)
elif args.fasika:
    print(year.fasika)
elif args.ginbotlideta:
    print(year.genbot_lideta)
elif args.erkibekahinat:
    print(year.erkibe_kahinat)
elif args.erget:
    print(year.erget)
elif args.peraclitos:
    print(year.peraclitos)
elif args.tsomehawariyat:
    print(year.tsome_hawariyat)
elif args.tsomedihnet:
    print(year.tsome_dihinet)
elif args.tsomefilseta:
    print(year.tsome_filseta)
elif args.debretabor:
    print(year.debre_tabor)
elif args.endoftsomefilseta:
    print(year.tsome_filseta_mefchiya)
else:
    year.print()
