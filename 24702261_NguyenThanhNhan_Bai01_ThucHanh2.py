import random
import math 

def is_Strobogrammatic(n):
    s = str(n)
    strobogrammatic_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    rotated_s = []

    for char in s:
        if char not in strobogrammatic_map:
            return False
        rotated_s.append(strobogrammatic_map[char])

    rotated_s_reversed = "".join(rotated_s[::-1])

    return s == rotated_s_reversed
    
def is_Palindrome(n):
  chuoi_so = str(n)
  chuoi_dao_nguoc = chuoi_so[::-1]
  so_dao_nguoc = int(chuoi_dao_nguoc)
  return n == so_dao_nguoc

def PalindromePrime(list) :
    ds = []
    for i in list :
        is_prime = lambda i: i > 1 and all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1))
        if is_prime and is_Palindrome(i):
            ds.append(i)
    return ds

def isStroPrime(list):
    ds = []
    for i in list :
        is_prime = lambda i: i > 1 and all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1))
        if is_Strobogrammatic(i) and is_prime :
            ds.append(i)
    return ds

def tach(n):
    tmp = n
    cmp = 0
    while(tmp): 
        r = tmp%10
        if(r >= cmp):
            cmp = r
        else: 
            return False
        tmp //= 10
    return True

def giam_Dan(list):
    ds =[]
    for i in list :
        if(tach(i)) :
            ds.append(i)
    return ds

def Lucky_Num(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(so)**2 for so in str(n))
    return n == 1
def checkLuckyinList(list):
    ds =[]
    for i in list:
        if Lucky_Num(i):
            ds.append(i)
    return ds
def nhap_so():
    while True :
        try :
            n = int(input("Nhap so nguyen n (n tu 10 den 1000): "))
            if n < 10 or n > 1000:
                print("Chi nhan so nguyen tu 10 den 1000. Yeu cau nhap lai")
                continue
            return n
        except ValueError :
            print("Phai nhap lai so nguyen duong. yeu cau nhap lai")
def tao_list(n):
    return random.sample(range(1,5001), n)
def main(): 
    n = nhap_so()
    ds =tao_list(n)
    print(ds)
    if giam_Dan(ds) == [] :
        print("Trong list khong chua so giam dan")
    else:
        print(giam_Dan(ds))
    if PalindromePrime(ds) == []:
        print("Trong list khong chua so nguyen to doi xung")
    else:
        print(PalindromePrime(ds))
    if isStroPrime(ds) == []:
        print("Trong list khong chua so nguyen to Strobogrammatic")
    else:
        print(isStroPrime(ds))
    if checkLuckyinList(ds) == []:
        print("Trong list khong chua so may man")
    else:
        print(checkLuckyinList(ds))
        
main()
