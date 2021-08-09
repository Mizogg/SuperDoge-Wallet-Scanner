#DOGE Sequential Balance/Received checker 14/05/2021 Mizogg&Chad mizogg.co.uk sequential
import bit
from bit import *
from bit.format import bytes_to_wif
import hashlib
from bitcoinlib.encoding import pubkeyhash_to_addr_bech32, addr_bech32_to_pubkeyhash, change_base
import atexit
from time import time
from datetime import timedelta, datetime
import requests
import json

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))

def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)

def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))

start = time()
atexit.register(end_log)
log("Start Program")
 
def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
F = []
P = x
  
while P<y:
        P+=1
        ran = P
        pk = Key.from_int(ran)
        key = Key.from_int(ran)
        upub = pk._pk.public_key.format(compressed=False)                               # Uncompressed publickey
        cpub = pk._pk.public_key.format(compressed=True)                                # Compressed publickey
        crmd = HASH160(cpub)                                                            # compressed HASH160
        urmd = HASH160(upub)                                                            # uncompressed HASH160
        dogecaddr = bit.base58.b58encode_check(b'\x1e' + crmd)                          #Dogecoin compressed
        dogeuaddr = bit.base58.b58encode_check(b'\x1e' + urmd)                          #Dogecoin uncompressed
        ammount = 0.00000000 
        Dogecoin = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogecaddr)) #received or balance
        resedoge = Dogecoin.json()
        balanceDoge = dict(resedoge)['received'] #received or balance
        Dogecoin1 = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogeuaddr)) #received or balance
        resedoge1 = Dogecoin1.json()
        balanceDoge1 = dict(resedoge1)['received'] #received or balance
        print ("\n " + colour_cyan + "Sequential DOGE Scan" + colour_red + "---Good--Luck--Happy--Hunting--Mizogg.co.uk&Chad---" + colour_cyan + "With Balance/Received Checker" + colour_reset) # Running Display Output
        print ('Dogecoin Compressed Address' + ' : '  + colour_cyan + str (dogecaddr) + ' : ' + colour_red +  str(balanceDoge) + colour_reset) #Dogecoin Compressed address display
        print ('Dogecoin UnCompressed Address' + ' : '  + colour_cyan + str (dogeuaddr) + ' : ' + colour_red +  str(balanceDoge1) + colour_reset) #Dogecoin  UnCompressed address display
        print('PrivateKey' + ' : ' + colour_cyan + key.to_hex() + colour_red + " : Date&Time" + seconds_to_str(), '\n' + colour_reset ) # Running Display Output
        if float(balanceDoge) > float(ammount):
            print("Matching Key ==== Found!!!\n PrivateKey: " + key.to_hex()) #Dogecoin Compressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nDogecoin Compressed address: ' + str (dogecaddr))
            f.write('\n==================================')
            f.close()
        if float(balanceDoge1) > float(ammount):
            print("Matching Key ==== Found!!!\n PrivateKey: " + key.to_hex()) #Dogecoin  UnCompressed address winner
            f=open(u"winner.txt","a")
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nDogecoin  UnCompressed address: ' + str (dogeuaddr))
            f.write('\n==================================')
            f.close()