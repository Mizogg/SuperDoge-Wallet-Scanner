#DOGE  Random Balance/Received checker 09/08/2021  mizogg.co.uk Random
import random
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
import colorama
from colorama import Fore, Back, Style
colorama.init()

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + Fore.BLUE + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' )
    if elapsed:
        print("\n " + Fore.RED + " [TIMING]> Elapsed time ==> " + elapsed + "\n" )


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")

x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")

count=0
total=0


def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

print(Fore.BLUE + "superdoge.py---" + Fore.RED + "Random Scan for DOGE Coin Addresses Total Received Ammount---------mizogg.co.uk" + Fore.BLUE + "---superdoge.py"  + Style.RESET_ALL + seconds_to_str())
x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")


count=0
total=0
while True:
    ran= random.randint(x,y)
    pk = Key.from_int(ran)
    key = Key.from_int(ran)
    seed=str(ran)
    upub = pk._pk.public_key.format(compressed=False)                               # Uncompressed publickey
    cpub = pk._pk.public_key.format(compressed=True)                                # Compressed publickey
    crmd = HASH160(cpub)                                                            # compressed HASH160
    urmd = HASH160(upub)                                                            # uncompressed HASH160
    dogecaddr = bit.base58.b58encode_check(b'\x1e' + crmd)                          #Dogecoin compressed
    dogeuaddr = bit.base58.b58encode_check(b'\x1e' + urmd)                          #Dogecoin uncompressed
    count+=1*int(threadCount)
    total+=2*int(threadCount)
    Dogecoin = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogecaddr)) #received or balance
    resedoge = Dogecoin.json()
    balanceDoge = dict(resedoge)['received'] #received or balance
    Dogecoin1 = requests.get("https://dogechain.info/api/v1/address/received/"+ str (dogeuaddr)) #received or balance
    resedoge1 = Dogecoin1.json()
    balanceDoge1 = dict(resedoge1)['received'] #received or balance
    print(Fore.BLUE + "\nSuperdoge.py---" + Fore.RED + "Random Scan for DOGE Coin Addresses Total Received Ammount")
    print (Fore.GREEN + "Scan Number" + ' : ' + Style.RESET_ALL + str (count) + ' : ' + Fore.GREEN + "Total Wallets Checked" + ' : ' + Style.RESET_ALL + str (total))
    print(Fore.RED + ' PrivateKey (hex) : ' + Fore.YELLOW + key.to_hex() + Style.RESET_ALL)
    print(Fore.RED + ' PrivateKey (dec) : ' + Fore.YELLOW + seed + Style.RESET_ALL)
    print ('Dogecoin Compressed Address' + ' : '  + Fore.BLUE + dogecaddr + ' : ' + Fore.RED +  str(balanceDoge) + Style.RESET_ALL) #Dogecoin Compressed address display
    print ('Dogecoin UnCompressed Address : '  + Fore.BLUE + dogeuaddr + ' : ' + Fore.RED +  str(balanceDoge1) + Style.RESET_ALL) #Dogecoin  UnCompressed address display
    print ("------Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + "---Superdoge.py"  + Style.RESET_ALL + seconds_to_str())
    
    
    if float(balanceDoge) > 0 or float(balanceDoge1) > 0:
        print (Fore.BLUE +  '\n <================================= WINNER Total Received Ammount WINNER =================================>' +  Style.RESET_ALL)
        print (Fore.GREEN + "Matching Key ==== Found!!!\n PrivateKey  (hex): " + Fore.YELLOW + key.to_hex() + Style.RESET_ALL) #Dogecoin Compressed address winner
        print (Fore.GREEN + "Matching Key ==== Found!!!\n PrivateKey  (dec): " + Fore.YELLOW + seed + Style.RESET_ALL)
        print (Fore.YELLOW + 'Congraz you have found wallet with a Total Received Ammount : ' + Style.RESET_ALL + dogecaddr + Fore.GREEN + ' : Total Received Ammount : ' + str(balanceDoge) + Style.RESET_ALL)
        print (Fore.YELLOW + 'Congraz you have found wallet with a Total Received Ammount : ' + Style.RESET_ALL + dogeuaddr + Fore.GREEN + ' : Total Received Ammount : ' + str(balanceDoge1) + Style.RESET_ALL)
        print (Fore.BLUE +  '\n <================================= WINNER Total Received Ammount WINNER =================================>' +  Style.RESET_ALL)
        f=open(u"winner.txt","a")
        f.write('\n=============DOGE Coin Address with Total Received Ammount=====================')
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nPrivateKey (dec): ' + seed)
        f.write('\nDogecoin Compressed address: ' + dogecaddr)
        f.write('\nDogecoin  UnCompressed address: ' + dogeuaddr)
        f.write('\n=============DOGE COIN Address with Total Received Ammount=====================')
        f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' ) 
        f.close()