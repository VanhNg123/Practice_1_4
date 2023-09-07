age = int(input('Nhap vao so tuoi cua ban: '))
height = int(input('Nhap vao can nang cua ban: '))
weight = float(input('Nhap vao can nang cua ban: '))
experience = int(input('Nhap vao so nam kinh nghiem cua ban: '))
if 30 < age < 40:
    if experience == 2 and height >= 1.60 and weight >= 50:
        print("Pass")
    elif experience == 5 and height >= 1.55 and weight <= 45:
        print('Pass')
    else:
        print('Reject')
elif 18 <= age <= 30:
    if height >= 1.55 and weight <= 45:
        print("pass")
    else:
        print('Rejet')
else:
    print('Reject')