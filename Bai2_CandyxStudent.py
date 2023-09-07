import sys
run = True
while run:
    try:
        SoKeo = int(input('Nhap so keo: '))
        SoHocSinh = int(input('NHap so hoc sinh:'))
        SoKeoCHoMoiHocSinh = int(SoKeo/SoHocSinh)
        SoKeoConLai = SoKeo % SoHocSinh
        print("So keo moi hoc sinh nhan duoc: ", SoKeoCHoMoiHocSinh)
        print(('So keo con lai: ', SoKeoConLai))
    except ZeroDivisionError:
        print("Co loi exception", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        print("So hoc sinh la 0 nene khong chay duoc")
    except ValueError:
        print("Co loi exception", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        print("Ban can phai nhap so")
    option = input("Bam 'c' de continue, bam 'k' de stop")
    run = True if option == 'c' else False
print("Chuong trinh ket thuc")
