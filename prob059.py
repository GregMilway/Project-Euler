# decode the vigenere cipher-text  from prob59cipher, and find the sum of the bytes of the plain-text
#we know the key length is 3, so split the cipher text by taking every 3 char, offset by 0,1,2
from string import printable

with open('prob59cipher') as f_cipher:
    cipher = f_cipher.read().strip().split(',')


ciphertext = [int(char) for char in cipher]


cipher1 = ciphertext[0::3]
cipher2 = ciphertext[1::3]
cipher3 = ciphertext[2::3]

print len(cipher1)
print len(cipher2)
print len(cipher3)


#plain1 = []
#plain2 = []
#plain3 = []
#

#for key in 'abcdefghijklmnopqrstuvwxyz':
#    keyint = ord(key)
#    tryplain = [chr(elem^keyint) for elem in cipher1]
#    if all(c in printable for c in tryplain):
#        plain1.append((''.join(tryplain),key))
#    tryplain = [chr(elem^keyint) for elem in cipher2]
#    if all(c in printable for c in tryplain):
#        plain2.append((''.join(tryplain),key))
#    tryplain = [chr(elem^keyint) for elem in cipher3]
#    if all(c in printable for c in tryplain):
#        plain3.append((''.join(tryplain),key))

plain1 = [chr(elem^ord('g')) for elem in cipher1]
plain2 = [chr(elem^ord('o')) for elem in cipher2]
plain3 = [chr(elem^ord('d')) for elem in cipher3]

plaintext = [x for t in zip(plain1, plain2, plain3) for x in t]
plaintext.append(plain1[-1])
print sum(map(ord,plaintext))
