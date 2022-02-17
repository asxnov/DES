from Crypto.Cipher import DES 

def pad(text): 
    while len(text) % 8!= 0:
        text += b'x'
    return text
 
def des_ecb(text, key):  

	des = DES.new(key, DES.MODE_ECB)  
	padded_text = pad(text)
 	
	enc_text = des.encrypt(padded_text) 
	print('Шифр мәтін -', enc_text)		

	dec_text = des.decrypt(enc_text)  
	dec_main = dec_text.decode('utf-8') 
	print('Дешифрланған мәтін -', dec_main) 

des_ecb(b'Asanov E', b'SIB 18 3')  
