nam_sinh = int(input())
nam_hien_tai = int(input())
tuoi = nam_hien_tai - nam_sinh
if tuoi >= 18:
    print(f'ban {tuoi} tuoi, ban da du tuoi bau cu')
else:
    print(f'ban {tuoi} tuoi, ban chua du tuoi bau cu')