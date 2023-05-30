from argparse import ArgumentParser, Namespace
from datetime import datetime

from tabulate import tabulate


class Date:
    def __init__(self, am):
        """This function intializes and computes all the neccessary calculations and variables to find the holidays.
        If you want to find out more on how these calculations were made, read the file in the documentation
        """
        self.am = am
        self.aa = self.am + 5500
        self.aw, self.mr = [
            self.aw_list[self.aa % 4],
            int(self.aa / 4),
        ]
        self.at = self.aa + self.mr + 2
        self.new_year_day = f"{self.NYDayName[self.at%7]}, {self.months[1]} 1"
        self.medeb = self.aa % 19
        self.wenber = 18 if self.medeb == 0 else self.medeb - 1
        self.abeqte = (
            (self.wenber * 11) % 30 if self.wenber * 11 >= 30 else self.wenber * 11
        )
        self.metqe = abs(30 - self.abeqte)
        self.beale_metqe = self.find_beale_metqe()
        self.tewsak = self.find_tewsak()
        self.mebaja_hamer = (
            self.tewsak
            if self.tewsak == 0 or self.tewsak == 30
            else (self.metqe + self.tewsak) % 30
        )
        self.tsome_nenewe_ = self.find_tsome_nenewe()
        self.tsome_nenewe = (
            f"{self.day_name(self.find_tsome_nenewe())}, {self.find_tsome_nenewe()}"
        )
        self.abiy_tsom = self.day_of_the_holiday(14)
        self.debre_zeyit = self.day_of_the_holiday(41)
        self.hosaina = self.day_of_the_holiday(62)
        self.seqlet = self.day_of_the_holiday(67)
        self.fasika = self.day_of_the_holiday(69)
        self.erkibe_kahinat = self.day_of_the_holiday(93)
        self.erget = self.day_of_the_holiday(108)
        self.peraclitos = self.day_of_the_holiday(118)
        self.tsome_hawariyat = self.day_of_the_holiday(119)
        self.tsome_dihinet = self.day_of_the_holiday(121)
        self.gena = (
            f"{self.day_name('ታህሳስ 29')}, ታህሳስ 29"
            if self.aw != "ዘመነ ዮሐንስ"
            else f"{self.day_name('ታህሳስ 28')}, ታህሳስ 28"
        )
        self.timket = f"{self.day_name('ጥር 11')}, ጥር 11"
        self.kana_zegelila = f"{self.day_name('ጥር 12')}, ጥር 12"
        self.mesqel = f"{self.day_name('መስከረም 17')}, መስከረም 17"
        self.beale_tsinset = f"{self.day_name('መጋቢት 29')}, መጋቢት 29"
        self.beale_simeon = f"{self.day_name('የካቲት 8')}, የካቲት 8"
        self.beale_girizat = f"{self.day_name('ጥር 6')}, ጥር 6"
        self.genbot_lideta = f"{self.day_name('ግንቦት 1')}, ግንቦት 1"
        self.debre_tabor = f"{self.day_name('ነሐሴ 13')}, ነሐሴ 13"
        self.tsome_lidet = (
            f"{self.day_name('ህዳር 16')}, ህዳር 16"
            if self.aw != "ዘመነ ዮሐንስ"
            else f"{self.day_name('ህዳር 15')}, ህዳር 15"
        )
        self.day_of_timket = self.day_name("ጥር 11")
        self.tsome_filseta = f"{self.day_name('ነሐሴ 1')}, ነሐሴ 1"
        self.tsome_filseta_mefchiya = f"{self.day_name('ነሐሴ 16')}, ነሐሴ 16"
        self.print_title_list = [
            "እንቁጣጣሽ",
            "መስቅል",
            "የገና ፆም",
            "ገና",
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
            (self.yon[self.NYDayName[self.at % 7]] + self.astifeWer[month] + int(day))
            % 7
        ]

    def find_tsome_nenewe(self):
        """The function finds the day of nenewe fasting starts"""
        m, d = self.beale_metqe.split()
        if self.mebaja_hamer > 30:
            return f"የካቲት {self.mebaja_hamer%30}"
        elif self.metqe == 0 or self.metqe == 30:
            return f"የካቲት {self.mebaja_hamer}"
        elif m == "መስከረም":
            return f"ጥር {self.mebaja_hamer}"
        elif m == "ጥቅምት":
            return f"የካቲት {self.mebaja_hamer}"

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
        return self.elete_tewsag[self.day_name(self.beale_metqe)]

    def day_of_the_holiday(self, tewsak):
        """Finds the day of the holiday using tewsak"""
        m, d = self.tsome_nenewe_.split()
        Cdate = int(d) + tewsak
        Mincriment = 0
        while Cdate > 30:
            Cdate -= 30
            Mincriment += 1
        if tewsak == 14:
            m = self.months[
                self.Hmonth[m] + Mincriment if self.Hmonth[m] + Mincriment < 6 else 6
            ]
        else:
            m = self.months[self.Hmonth[m] + Mincriment]
        m_d = f"{m} {Cdate}"
        return f"{self.day_name(m_d)}, {m_d}"

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
    aw_list = {
        0: "ዘመነ ዮሐንስ",
        1: "ዘመነ ማቴዎስ",
        2: "ዘመነ ማርቆስ",
        3: "ዘመነ ሉቃስ",
    }
    NYDayName = {
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
    yon = {
        "እሁድ": 5,
        "ሰኞ": 6,
        "ማክሰኞ": 7,
        "ረቡዕ": 1,
        "ሐሙስ": 2,
        "አርብ": 3,
        "ቅዳሜ": 4,
    }
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
    name_of_the_day = NYDayName
    Hmonth = {
        "መስከረም": 1,
        "ጥቅምት": 2,
        "ህዳር": 3,
        "ታህሳስ": 4,
        "ጥር": 5,
        "የካቲት": 6,
        "መጋቢት": 7,
        "ሚያዝያ": 8,
        "ግንቦት": 9,
        "ሰኔ": 10,
        "ሀምሌ": 11,
        "ነሐሴ": 12,
    }


if __name__ == "__main__":
    """The code below uses the argparse module to make the program be executed in the terminal by adding arguments to
    perform a specific task."""

    # -------------------------------------------------------------------------------------------------
    parser = ArgumentParser(
        description="Print the days of the holidays and fastings in a year."
    )
    parser.add_argument(
        "-a",
        "--all",
        help="prints all the days of the Holidays",
        action="store_true",
    )
    parser.add_argument(
        "Year",
        help="Assigns current  year when no argument is given",
        type=int,
        default=None,
        nargs="?",
    )
    parser.add_argument(
        "-n",
        "--new_year",
        help="prints the day of the New Year",
        action="store_true",
    )
    parser.add_argument(
        "-m", "--mesqel", help="prints the day of Mesqel", action="store_true"
    )
    parser.add_argument(
        "-tl",
        "--tsome_lidet",
        help="prints the day of Tsome Lidet",
        action="store_true",
    )
    parser.add_argument(
        "-g", "--gena", help="prints the day of Gena", action="store_true"
    )
    parser.add_argument(
        "-tg",
        "--tsome_gehad",
        help="prints the day of Tsome Gehad",
        action="store_true",
    )
    parser.add_argument(
        "-t", "--timket", help="prints the day of Timket", action="store_true"
    )
    parser.add_argument(
        "-kz",
        "--kana_zegelila",
        help="prints the day of Kana Zegelila",
        action="store_true",
    )
    parser.add_argument(
        "-tn",
        "--tsome_nenewe",
        help="prints the day of Tsome Nenewe",
        action="store_true",
    )
    parser.add_argument(
        "-bs",
        "--beale_simeon",
        help="prints the day of Beale Simeon",
        action="store_true",
    )
    parser.add_argument(
        "-ta",
        "--tsome_abiy",
        help="prints the day of Tsome Abiy",
        action="store_true",
    )
    parser.add_argument(
        "-dz",
        "--debre_zeyit",
        help="prints the day of Debre Zeyit",
        action="store_true",
    )
    parser.add_argument(
        "-bt",
        "--beale_tsinset",
        help="prints the day of Beale Tinset",
        action="store_true",
    )
    parser.add_argument(
        "-ho",
        "--hosaina",
        help="prints the day of Hosaina",
        action="store_true",
    )
    parser.add_argument(
        "-s", "--seqlet", help="prints the day of Seqlet", action="store_true"
    )
    parser.add_argument(
        "-f", "--fasika", help="prints the day of Fasika", action="store_true"
    )
    parser.add_argument(
        "-gl",
        "--ginbot_lideta",
        help="prints the day of Ginbot Lideta",
        action="store_true",
    )
    parser.add_argument(
        "-ek",
        "--erkibe_kahinat",
        help="prints the day of Erkibe Kahinat",
        action="store_true",
    )
    parser.add_argument(
        "-e", "--erget", help="prints the day of Erget", action="store_true"
    )
    parser.add_argument(
        "-p",
        "--peraclitos",
        help="prints the day of Peraclitos",
        action="store_true",
    )
    parser.add_argument(
        "-th",
        "--tsome_hawariyat",
        help="prints the day of Tsome Hawariyat",
        action="store_true",
    )
    parser.add_argument(
        "-td",
        "--tsome_dihnet",
        help="prints the day of Tsome Dihnet",
        action="store_true",
    )
    parser.add_argument(
        "-tf",
        "--tsome_filseta",
        help="prints the day of Tsome Filseta",
        action="store_true",
    )
    parser.add_argument(
        "-db",
        "--debre_tabor",
        help="prints the day of Debre Tabor",
        action="store_true",
    )
    parser.add_argument(
        "-etf",
        "--end_of_tsome_filseta",
        help="prints the day of end of Tsome",
        action="store_true",
    )

    args: Namespace = parser.parse_args()

    # -------------------------------------------------------------------------------------------------

    if parser.parse_args().Year is None:
        year = Date(datetime.now().year - 8)
    else:
        year = Date(args.Year)
    parameters = [
        "new_year",
        "mesqel",
        "tsome_lidet",
        "gena",
        "tsome_gehad",
        "timket",
        "kana_zegelila",
        "tsome_nenewe",
        "beale_simeon",
        "tsome_abiy",
        "debre_zeyit",
        "beale_tsinset",
        "hosaina",
        "seqlet",
        "fasika",
        "ginbot_lideta",
        "erkibe_kahinat",
        "erget",
        "peraclitos",
        "tsome_hawariyat",
        "tsome_dihnet",
        "tsome_filseta",
        "debre_tabor",
        "end_of_tsome_filseta",
    ]
    methods = [
        "new_year_day",
        "mesqel",
        "tsome_lidet",
        "gena",
        "tsome_gehad",
        "timket",
        "kana_zegelila",
        "tsome_nenewe",
        "beale_simeon",
        "abiy_tsom",
        "debre_zeyit",
        "beale_tsinset",
        "hosaina",
        "seqlet",
        "fasika",
        "genbot_lideta",
        "erkibe_kahinat",
        "erget",
        "peraclitos",
        "tsome_hawariyat",
        "tsome_dihinet",
        "tsome_filseta",
        "debre_tabor",
        "tsome_filseta_mefchiya",
    ]
    if args.all:
        year.print()
    for p, m in zip(parameters, methods):
        if getattr(args, p):
            print(getattr(year, m))
