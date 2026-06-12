def printer_error(s):
    error = 0
    error = sum(1 for i in s if ord(i) >= 110 and ord(i) <= 122)
    return f'{error}/{len(s)}'

# s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
# print(printer_error(s))

"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
"""

def accum(st):
    stringLetter = ""
    for i in enumerate(st):
        stringLetter += (i[1] * (int(i[0]) + 1)).capitalize()
        if i[0] != len(st) - 1:
            stringLetter += "-"
    return stringLetter

# print(accum("abcd"))


"""
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    lst = []

    if len(s) % 2 != 0:
        s += "_"

    for i in range(0, len(s), 2):
        lst += [s[i:i+2]]

    return lst
        
# tests = (
#     ("asdfadsf", ['as', 'df', 'ad', 'sf']),
#     ("asdfads", ['as', 'df', 'ad', 's_']),
#     ("", []),
#     ("x", ["x_"]),
# )

# for inp, exp in tests:
#     print(solution(inp))


"""
Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
"""

def to_jaden_case(string):
    newString = ""
    for i in range(0, len(string)):
        if i == 0 or ord(string[i - 1]) == 32:
            newString += string[i].upper()
        else:
            newString += string[i].lower()

    return newString
            
# quote = "How can mirrors be real if our eyes aren't real"
quote = "hYmalsEmpY id PhWF SHIPyhElr VlZj R UyFxfJv HAqfiBkfxG YPBXfLMo ZFwj UrkRr V G jqtIkaok XZZqq MLJ g kTCHU eMNlphF HNGzZ MpxxYUH PIOxh VMYBD Ihpy NTK PYzZxKiReP AHxED zSGXUL p LTGjZHawh OetKQAZY qicIuq vIdhFPq pgIPB oRP ypW VzqIeAplAu IOZe mFZcAoPMD QxbvY PGEhHXi NyfG h wKM EtNAfurt rXxQ fsuaYOPFYQ Z oA sea Z TRVE v isQvLI moJjct lGjczxvULV jEYQIy Ke IRUMmck dX DgqFCUeZ m LGD ByDkY Bg jccIkWfLYZ ryUCTVSi JZuirEvL Sgy gXkaCtI ziQBmzj cRaNks LuEIm CsQFa AxTT tuWfhw HoNT LfP iRJxSj MKfszv uyydH OPNXrM zMXxC MH lgl qdj TAhPcQ"
# print(to_jaden_case(quote))

""" 
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

"""
def find_short(s):
    count = len(s)
    for i in s.split(" "):
        if count > len(i):
            count = len(i)
    return count

# print(find_short("i want to travel the world writing code one day"))
# print(find_short("bitcoin take over the world maybe who knows perhaps"))


"""
If we list all the natural numbers below 10 that are multiples of 3 or 5
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If a number is a multiple of both 3 and 5, only count it once.
"""

def solution(number):
    count = set()

    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            count.add(i)

    return sum(count)

# print(solution(10))

"""
Write a function that accepts an array of 10 integers (between 0 and 9)
that returns a string of those numbers in the form of a phone number.
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
"""

def create_phone_number(n):
    no = ""; count = 0
    for i in range(0, len(n), 3):
        n1 = ""

        for j in n[i : i + 3]:
            n1 += str(j)
            
        no += f'({n1})' if count == 0 else f' {n1}-' if count == 1 else f'{n1}'
        count += 1

    return no

# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) # (123) 456-7890 
# "({}{}{}) {}{}{}-{}{}{}{}".format(*n) => one line answer

"""
Usually when you buy something, you're asked whether your credit card number
phone number or answer to your most secret question is still correct. 
However, since someone could look over your shoulder, you don't want that shown on your screen. 
Instead, we mask it.
Your task is to write a function maskify, which changes all but the last four characters into '#'.

"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!"
"""

# return masked string
def maskify(cc):
    
    if len(cc) > 4:
        return ("#" * len(cc[:-4])) + cc[-4:]
    
    return cc
# print(maskify("SF$SDfgsd2eA"))


"""
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
They would like your help with an application form that will tell prospective members which category they will be placed.
To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input
Input will consist of a list of pairs. 
Each pair contains information for a single potential member. 
Information consists of an integer for the person's age and an integer for the person's handicap.

Output
Output will consist of a list of string values (in Haskell and C: Open or Senior) 
stating whether the respective member is to be placed in the senior or open category.

Example
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
"""

def open_or_senior(data):
    return ["Senior" if i[0] >= 55 and i[1] > 7 else "Open" for i in data]

# [value_if_true if condition else value_if_false for item in iterable]
print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))