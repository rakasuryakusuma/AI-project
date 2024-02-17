# binary converter with denomination

amount = int(input("Put your number: "))
bin0 = bin1 = bin2 = bin3 = bin4 = bin5 = bin6 = bin7 = 0

# def converter(amount):
#     if amount > 1 :
#         converter(amount//2)
#     print(amount % 2, end = '')

# converter(amount)
if amount < 256 :
    bin0 = amount // (2**7)
    amount %= (2**7)
if amount < 128 :
    bin1 = amount // (2**6)
    amount %= (2**6)
if amount < 64 :
    bin2 = amount // (2**5)
    amount %= (2**5)
if amount < 32 :
    bin3 = amount // (2**4)
    amount %= (2**4)
if amount < 16 :
    bin4 = amount // (2**3)
    amount %= (2**3)
if amount < 8 :
    bin5 = amount // (2**2)
    amount %= (2**2)
if amount < 4 :
    bin6 = amount // (2**1)
    amount %= (2**1)
if amount < 2 :
    bin7 = amount // (2**0)
    amount %= (2**0)

print(bin0)
print(bin1)
print(bin2)
print(bin3)
print(bin4)
print(bin5)
print(bin6)
print(bin7)