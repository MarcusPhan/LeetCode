def romanToInt(s: str) -> int:
    counter = 0

    four = s.count("IV")
    nine = s.count("IX")
    fourty = s.count("XL")
    ninety = s.count("XC")
    fourHundred = s.count("CD")
    nineHundred = s.count("CM")

    counter = counter + 4*four + 9*nine + 40*fourty + 90*ninety + 400*fourHundred + 900*nineHundred
            
    s1 = s.replace("IV", "")
    s2 = s1.replace("IX", "")
    s3 = s2.replace("XL", "")
    s4 = s3.replace("XC", "")
    s5 = s4.replace("CD", "")
    s6 = s5.replace("CM", "")
            
    for i in s6:
        if i == "I":
            counter += 1
        elif i == "V":
            counter += 5
        elif i == "X":
            counter += 10
        elif i == "L":
            counter += 50
        elif i == "C":
            counter += 100
        elif i == "D":
            counter += 500
        else:
            counter += 1000

    return counter