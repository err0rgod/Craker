import argparse
import hashlib
from concurrent.futures import ThreadPoolExecutor





def words(wordlist):
    with open(wordlist, 'r') as f:
        return [line.strip('\n') for line in f]
        


def check_word(word, hash_func, target_hash):
    hashed_word = hash_func(word.encode()).hexdigest()
    if hashed_word == target_hash.lower():
        print(f"[+] Password found: {word}")



def main():

    parser = argparse.ArgumentParser(description="Hash Cracker ")
    
    parser.add_argument("-hash","--hash_content",required=True,type=str,help="Enter the Hash to crack")
    parser.add_argument("-type","--hash_type",required=True,type=str,help="Type of the Hash")
    parser.add_argument("-w","--wordlist_path",type=str,help="Mention the path of the wordlist to brute force the passwords")
    parser.add_argument("-t","--threads",type=int,default=30,help="Enter the Number of threads")
    parser.add_argument("-s","--string",type=str,help="Enter the possible string content if possible")


    args = parser.parse_args()

    hash = args.hash_content
    hash_type = args.hash_type
    wordlist = args.wordlist_path
    threads = args.threads



    if hash_type == "md5":
         hash_func = hashlib.md5
    elif hash_type == "sha1":
        hash_func = hashlib.sha1
    elif hash_type == "sha256":
        hash_func = hashlib.sha256
    else:
        print("[-] Unsupported hash type.")
        return
    ''''
    with ThreadPoolExecutor(max_workers=30) as executor:
        for word in words(wordlist):
            hashed_word = hash_func(word.encode()).hexdigest()
            if hashed_word == hash.lower():
                print(f"[+] Password found: {word}")
                return'''



    '''with ThreadPoolExecutor(max_workers=30) as executor:
        for word in words(wordlist):
            executor.submit(check_word, word)'''
    

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for word in words(wordlist):
            executor.submit(check_word, word, hash_func, hash)







    #print(words(wordlist))





if __name__ == "__main__":
    main()