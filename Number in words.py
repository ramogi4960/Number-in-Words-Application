class NumberConverter:
    base_10 = {
        '0': 'Zero', '1': 'One', '2': 'Two Twenty', '3': 'Three Thirty', '4': 'Four Forty',
        '5': 'Five Fifty', '6': 'Six Sixty', '7': 'Seven Seventy', '8': 'Eight Eighty', '9': 'Nine Ninety',
        '10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen',
        '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen',
        '19': 'Nineteen',

    }

    def tens(self, s):
        if s == '10':
            return f'{self.base_10[s]}'
        elif 11 <= int(s) < 20:
            return f'{self.base_10[s]}'
        else:
            if s[1] == '0':
                return f'{self.base_10[s[0]].split()[1]}'
            return f'{self.base_10[s[0]].split()[1]} {self.base_10[s[1]].split()[0]}'

    def hundreds(self, s: str) -> str:
        if s[1] == '0' and s[2] == '0':
            return f'{self.base_10[s[0]].split()[0]} Hundred'
        elif s[1] == '0':
            return f'{self.base_10[s[0]].split()[0]} Hundred {self.base_10[s[2]].split()[0]}'
        elif s[2] == '0':
            if s[1] == '1':
                return f'{self.base_10[s[0]].split()[0]} Hundred {self.base_10[s[1:]].split()[0]}'
            else:
                return f'{self.base_10[s[0]].split()[0]} Hundred {self.base_10[s[1]].split()[1]}'
        else:
            if 11 <= int(''.join(s[1:])) < 20:
                return f"{self.base_10[s[0]].split()[0]} Hundred {self.base_10[''.join(s[1:])]}"
            return f'{self.base_10[s[0]].split()[0]} Hundred {self.base_10[s[1]].split()[1]} ' \
                   f'{self.base_10[s[2]].split()[0]}'

    def thousands(self, s):
        if s[1:] == '000':
            return f'{self.base_10[s[0]].split()[0]} Thousand'
        if s[1:3] == '00':
            return f'{self.base_10[s[0]].split()[0]} Thousand {self.base_10[s[-1]].split()[0]}'
        if s[1] == '0':
            return f"{self.base_10[s[0]].split()[0]} Thousand {self.tens(''.join(s[2:]))}"

        return f"{self.base_10[s[0]].split()[0]} Thousand {self.hundreds(''.join(s[1:]))}"

    def tens_of_thousands(self, s):
        if s[2:] == '000':
            return f"{self.tens(''.join(s[:2]))} Thousand"
        if s[2:-1] == '00':
            return f"{self.tens(''.join(s[:2]))} Thousand {self.base_10[s[-1]].split()[0]}"
        if s[2] == '0':
            return f"{self.tens(''.join(s[:2]))} Thousand {self.tens(''.join(s[3:]))}"

        return f"{self.tens(''.join(s[:2]))} Thousand {self.hundreds(''.join(s[2:]))}"

    def hundreds_of_thousands(self, s):
        if s[3:] == '000':
            return f"{self.hundreds(''.join(s[:3]))} Thousand"
        if s[3:-1] == '00':
            return f"{self.hundreds(''.join(s[:3]))} Thousand {self.base_10[s[-1]].split()[0]}"
        if s[3] == '0':
            return f"{self.hundreds(''.join(s[:3]))} Thousand {self.tens(''.join(s[4:]))}"

        return f"{self.hundreds(''.join(s[:3]))} Thousand {self.hundreds(''.join(s[3:]))}"

    def millions(self, s):
        if len(s) == 7:  # 1,000,001
            if s[1:] == '000000':
                return f"{self.base_10[s[0]].split()[0]} Million"
            if s[1:-1] == '00000':
                return f"{self.base_10[s[0]].split()[0]} Million {self.base_10[s[-1]].split()[0]}"
            if s[1:-2] == '0000':
                return f"{self.base_10[s[0]].split()[0]} Million {self.tens(''.join(s[-2:]))}"
            if s[1:-3] == '000':
                return f"{self.base_10[s[0]].split()[0]} Million {self.hundreds(''.join(s[-3:]))}"
            if s[1:-4] == '00':
                return f"{self.base_10[s[0]].split()[0]} Million {self.thousands(''.join(s[-4:]))}"
            if s[1] == '0':
                return f"{self.base_10[s[0]].split()[0]} Million {self.tens_of_thousands(''.join(s[-5:]))}"

            return f"{self.base_10[s[0]].split()[0]} Million {self.hundreds_of_thousands(''.join(s[1:]))}"
        elif len(s) == 8:
            if s[2:] == '000000':
                return f"{self.tens(''.join(s[:2]))} Million"
            if s[2:-1] == '00000':
                return f"{self.tens(''.join(s[:2]))} Million {self.base_10[s[-1]].split()[0]}"
            if s[2:-2] == '0000':
                return f"{self.tens(''.join(s[:2]))} Million {self.tens(''.join(s[-2:]))}"
            if s[2:-3] == '000':
                return f"{self.tens(''.join(s[:2]))} Million {self.hundreds(''.join(s[-3:]))}"
            if s[2:-4] == '00':
                return f"{self.tens(''.join(s[:2]))} Million {self.thousands(''.join(s[-4:]))}"
            if s[2] == '0':
                return f"{self.tens(''.join(s[:2]))} Million {self.tens_of_thousands(''.join(s[-5:]))}"

            return f"{self.tens(''.join(s[:2]))} Million {self.hundreds_of_thousands(''.join(s[2:]))}"

        elif len(s) == 9:
            if s[3:] == '000000':
                return f"{self.hundreds(''.join(s[:3]))} Million"
            if s[3:-1] == '00000':
                return f"{self.hundreds(''.join(s[:3]))} Million {self.base_10[s[-1]].split()[0]}"
            if s[3:-2] == '0000':
                return f"{self.hundreds(''.join(s[:3]))} Million {self.tens(''.join(s[-2:]))}"
            if s[3:-3] == '000':
                return f"{self.hundreds(''.join(s[:3]))} Million {self.hundreds(''.join(s[-3:]))}"
            if s[3:-4] == '00':
                return f"{self.hundreds(''.join(s[:3]))} Million {self.thousands(''.join(s[-4:]))}"
            if s[3] == '0':
                return f"{self.hundreds(''.join(s[:3]))} Million {self.tens_of_thousands(''.join(s[-5:]))}"

            return f"{self.hundreds(''.join(s[:3]))} Million {self.hundreds_of_thousands(''.join(s[3:]))}"

    def number_in_words(self, num: int) -> str:
        # we can predefine words for integers 1 - 9
        # the highest number they can test is 2,147,483,647
        # for tens, let's start with teens
        if num <= 10:
            return self.base_10[str(num)].split()[0]
        if 11 <= num < 20:
            return self.base_10[str(num)]

        x = str(num)  # num as a string
        if len(x) == 2:
            return f'{self.tens(x)}'
            # if x[1] == '0':
            #     return f'{self.base_10[x[0]].split()[1]}'
            # return f'{self.base_10[x[0]].split()[1]} {self.base_10[x[1]].split()[0]}'
        elif len(x) == 3:  # 21 - 99
            return self.hundreds(x)
        elif len(x) == 4:  # 1000 - 9999
            return f'{self.thousands(x)}'
        elif len(x) == 5:
            return f'{self.tens_of_thousands(x)}'
        elif len(x) == 6:
            return f"{self.hundreds_of_thousands(x)}"
        elif 6 < len(x) < 10:
            return f"{self.millions(x)}"
        elif len(x) == 10:
            if x[1:] == '000000000':
                return f"{self.base_10[x[0]].split()[0]} Billion"
            if x[1:-1] == '00000000':
                return f"{self.base_10[x[0]].split()[0]} Billion {self.base_10[x[-1]].split()[0]}"
            if x[1:-2] == '0000000':
                return f"{self.base_10[x[0]].split()[0]} Billion {self.tens(''.join(x[-2:]))}"
            if x[1:-3] == '000000':
                return f"{self.base_10[x[0]].split()[0]} Billion {self.hundreds(''.join(x[-3:]))}"
            if x[1:-4] == '00000':
                return f"{self.base_10[x[0]].split()[0]} Billion {self.thousands(''.join(x[-4:]))}"
            if x[1:-5] == '0000':
                return f"{self.base_10[x[0]].split()[0]} Billion {self.tens_of_thousands(''.join(x[-5:]))}"
            if x[1:-6] == '000':
                return f"{self.base_10[x[0]].split()[0]} Billion {self.hundreds_of_thousands(''.join(x[-6:]))}"

            return f"{self.base_10[x[0]].split()[0]} Billion {self.millions(''.join(x[1:]).lstrip('0'))}"


# how to use it
# print(NumberConverter().number_in_words(2**31-1))
# output
# Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven
