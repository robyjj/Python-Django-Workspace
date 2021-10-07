income = 10000
good_credit = True
has_criminal_Record = True


if income > 1000 and good_credit:
    print('Eligible for loan')

if income > 1000 or good_credit:
    print('Eligible for loan')

if not has_criminal_Record and good_credit:
    print('Eligible for loan')