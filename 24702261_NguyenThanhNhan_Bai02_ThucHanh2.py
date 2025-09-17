import re
def tong_So( s):
    res = 0
    for i in s:
        if i.isdigit():
            res += int(i)
    return res

def main():
    s = str(input("Nhap chuoi s: "))
    print(tong_So(s))
    ip_with_zeroes = str(input("Nhap dia chi IP:"))
    ip = re.sub('[.]0+', '.', ip_with_zeroes)
    print(ip)
main()
