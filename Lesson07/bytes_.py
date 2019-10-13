s = 'абракадабра abracadabra'
# s = 'abracadabra'  # для примера с latin-1
print(type(s), repr(s))

# не сработает, так как в нашей строке не все символы кодировки latin-1, а также есть кирилица в utf-8
# b = bytes(s, 'latin-1')
b = bytes(s, 'utf-8')
print(type(b), repr(b))

bb = b'\xd0\xb0\xd0\xb1\xd1\x80\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb4\xd0\xb0\xd0\xb1\xd1\x80\xd0\xb0 abracadabra'
ss = bb.decode('utf-8')
print(ss)

print(s.encode('WINDOWS-1251'))