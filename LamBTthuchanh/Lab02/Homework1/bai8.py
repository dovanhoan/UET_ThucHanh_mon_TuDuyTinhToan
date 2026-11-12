ho_ten_chu_ho = input()
chi_so_trc = int(input())
chi_so_sau = int(input())
so_dien = chi_so_sau - chi_so_trc
if 0 < so_dien <= 50:
    so_tien = so_dien * 1984
elif 51 <= so_dien <= 100:
    so_tien = 50 * 1984 + (so_dien - 50) * 2050
elif 101 <= so_dien <= 200:
    so_tien = 50 * 1984 + 50 * 2050 + (so_dien - 100) * 2380
elif 201 <= so_dien <= 300:
    so_tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + (so_dien - 200) * 2998
elif 301 <= so_dien <= 400:
    so_tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + (so_dien - 300) * 3350
elif so_dien >= 401:
    so_tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + 100 * 3350 + (so_dien - 400) * 3460
tong_tien_sau_vat = round(so_tien * 1.08)
print(f'Ho va ten: {ho_ten_chu_ho}')
print(f'Tien phai tra la: {tong_tien_sau_vat} ')