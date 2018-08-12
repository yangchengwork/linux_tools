# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import os
import struct
 
BS = AES.block_size
pad =lambda s: s +(BS - len(s)% BS)* chr(BS - len(s)% BS)
unpad =lambda s : s[0:-ord(s[-1])]
 
# key = os.urandom(16)# the length can be (16, 24, 32)
#key='xxxxx'#32位或者0-f的数值，对应16字节
key = '\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10'
# text ='content==顶你哦，记得回访哦xxxxx'
text = 'ABCDEFGHIJKLMNOP'
emptyStr = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00';
emptyBytes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
t = emptyBytes[:];
t[0] = 1;
t[1] = 7;
print(t, emptyBytes);
st = [];
for i in t:
    st.append(bytes.decode(struct.pack('B', i)));
text = ''.join(st);
print(''.join(st));

key = struct.pack("16B", 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16);

cipher = AES.new(key, AES.MODE_ECB)#ECB模式 
 
# encrypted = cipher.encrypt(pad(text)) #.encode('hex')
encrypted = cipher.encrypt(text) #.encode('hex')
# buf = bytes(encrypted);
buf = struct.unpack("16B", encrypted);
# print(encrypted)  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'
# print(encrypted.decode("utf-8"))  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'
print(len(buf), buf)
 
decrypted = unpad(cipher.decrypt(encrypted))
print(decrypted)  # will be 'to be encrypted'
