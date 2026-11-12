c = input()
if len(c) == 1:
    if c.isalpha():
        print(f'{c} la ky tu chu cai')
    elif c.isdigit():
        print(f'{c} la ky tu chu so')
    else:
        print(f'{c} khong phai la ky tu chu cai hoac chu so')
else:
    print('hay nhap dung 1 ky tu')
    