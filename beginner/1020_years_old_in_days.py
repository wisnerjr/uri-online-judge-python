age_in_days = int(input())

years = int(age_in_days / 365)
age_in_days -= years * 365
months = int(age_in_days / 30)
age_in_days -= months * 30
days = int(age_in_days)

print("%i ano(s)" % years)
print("%i mes(es)" % months)
print("%i dia(s)" % days)