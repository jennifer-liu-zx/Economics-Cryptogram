import random
import string
import datetime

random.seed(330)


def encrypt(s):
    s_letters = list(s.upper())

    x = list(string.ascii_uppercase)
    y = list(string.ascii_uppercase)

    d = {}
    for key in x:
        chosen = random.choice(y)
        while key==chosen:
            chosen = random.choice(y)
        d[key] = chosen
        y.remove(chosen)

    for key in string.punctuation:
        d[key] = key

    list_string = [d[char] if char in d else char for char in s_letters]
    new_string = "".join(list_string)

    return new_string


def when(week: int):
    res = "Week "
    res += str(week)
    res += ", "
    week_0 = datetime.datetime(2025, 1, 8)
    date = week_0 + datetime.timedelta(days=7*week)
    res += str(date)[0:10]
    res += ": "
    return res


string_week1 = "Everything is worth what its purchaser will pay for it."
string_week2 = "There ain’t no such thing as a free lunch."
string_week3 = "It is not from the benevolence of the butcher, \
the brewer, or the baker that we expect our dinner, \
but from their regard to their own self-interest."
string_week4 = "Inflation is taxation without legislation."
string_week5 = "A rising tide lifts all boats."
string_week6 = "Everyone wants to live at the expense of the state. \
They forget that the state lives at the expense of everyone."
string_week7 = "In the long run, we are all dead."
string_week8 = "Every good cause is worth some inefficiency."
string_week9 = "Sometimes pessimism or optimism gets popular, and it's contagious."
string_week10 = "From each according to his ability, to each according to his needs."
string_week11 = "All models are wrong, some are useful."
string_week12 = "Economics runs the world."
string_week13 = "If all economists were laid end to end, they would still not reach a conclusion."
string_week14 = "The ideas of economists and political philosophers, \
both when they are right and when they are wrong are more powerful than is commonly understood. \
Indeed, the world is ruled by little else."
string_week15 = "Economists agree about economics - and that's a science - \
and they disagree about economic policy because that's a value judgement..."
string_week16 = "The curious task of economics is to demonstrate to men \
how little they really know about what they imagine they can design."


print(when(1) + encrypt(string_week1))
print(when(2) + encrypt(string_week2))
print(when(3) + encrypt(string_week3))
print(when(4) + encrypt(string_week4))
print(when(5) + encrypt(string_week5))
print(when(6) + encrypt(string_week6))
print(when(7) + encrypt(string_week7))
print(when(8) + encrypt(string_week8))
print(when(9) + encrypt(string_week9))
print(when(10) + encrypt(string_week10))
print(when(11) + encrypt(string_week11))
print(when(12) + encrypt(string_week12))
print(when(13) + encrypt(string_week13))
print(when(14) + encrypt(string_week14))
print(when(15) + encrypt(string_week15))
print(when(16) + encrypt(string_week16))
