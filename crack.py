import argparse
import hashlib
from concurrent.futures import ThreadPoolExecutor
import os
import sys
from tqdm import tqdm
import threading
import itertools



stop_flag = threading.Event()



def words(wordlist):
    with open(wordlist, 'r',encoding='utf-8', errors='ignore') as f:
        return [line.strip('\n') for line in f]
        


def check_word(word, hash_func, target_hash, pbar=None):
    hashed_word = hash_func(word.encode()).hexdigest()
    if hashed_word == target_hash.lower():
        print(f"[+] Password found: {word}")
        stop_flag.set()
    if pbar:
        pbar.update(1)



'''def check_word(word, hash_func, target_hash):
    hashed_word = hash_func(word.encode()).hexdigest()
    if hashed_word == target_hash.lower():
        print(f"[+] Password found: {word}")
        stop_flag.set()
'''




def brute_char(length, charset, hash_func, target_hash,pbar=None):
    for combi in itertools.product(charset, repeat=length):
        if stop_flag.is_set():
            return
        candidate = ''.join(combi)
        hashed = hash_func(candidate.encode()).hexdigest()
        if hashed == target_hash.lower():
            print(f"[+] Password Found: {candidate}")
            stop_flag.set()
            return
        if pbar:
            pbar.update(1)





def main():

    parser = argparse.ArgumentParser(description="Hash Cracker ")
    
    parser.add_argument("-hash","--hash_content",required=True,type=str,help="Enter the Hash to crack")
    parser.add_argument("-type","--hash_type",required=True,type=str,help="Type of the Hash")
    parser.add_argument("-w","--wordlist_path",type=str,help="Mention the path of the wordlist to brute force the passwords")
    parser.add_argument("-t","--threads",type=int,default=30,help="Enter the Number of threads")
    parser.add_argument("-s","--string",type=str,help="Enter the possible string content if possible")
    parser.add_argument("-mx","--max_lenght",type=int,help="Enter the max lenght of the hash answer")
    parser.add_argument("-mi","--min_lenght",type=int,help="Enter the min lenght of the hash answer")
    parser.add_argument("-mb","--mode_brute",action="store_false",help="To enable brute force method by char set")




    args = parser.parse_args()

    hash = args.hash_content
    hash_type = args.hash_type
    wordlist = args.wordlist_path
    threads = args.threads
    max_lenght = args.max_lenght
    min_lenght = args.min_lenght
    brute_mode = args.mode_brute
    charset = args.string





    hash_funcs = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha224": hashlib.sha224,
        "sha384": hashlib.sha384,
        "sha512": hashlib.sha512
    }

    hash_func = hash_funcs.get(hash_type)


    '''
    with ThreadPoolExecutor(max_workers=30) as executor:
        for word in words(wordlist):
            hashed_word = hash_func(word.encode()).hexdigest()
            if hashed_word == hash.lower():
                print(f"[+] Password found: {word}")
                return'''



    '''with ThreadPoolExecutor(max_workers=30) as executor:
        for word in words(wordlist):
            executor.submit(check_word, word)'''
    


    if charset and (min_lenght is None or max_lenght is None):
        print("[-] Brute-force mode requires --min_lenght and --max_lenght.")
        return

    

    with ThreadPoolExecutor(max_workers=threads) as executor:
        if charset:
            for length in range(min_lenght, max_lenght + 1):
                if stop_flag.is_set():
                    break
                executor.submit(brute_char, length, charset, hash_func, hash,pbar)
                pbar.close(9)
                
        else:
            wordlist_data = words(wordlist)
            with tqdm(total=len(wordlist_data), desc="📘 Wordlist Attack") as pbar:
                for word in wordlist_data:
                    if stop_flag.is_set():
                        break
                    executor.submit(check_word, word, hash_func, hash, pbar)









            '''for word in words(wordlist):
                if stop_flag.is_set():
                    break
                executor.submit(check_word, word, hash_func, hash)
'''


        







    #print(words(wordlist))





if __name__ == "__main__":
    main()