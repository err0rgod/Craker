import argparse
import hashlib






def main(hash,hash_type):

    parser = argparse.ArgumentParser(description="Hash Cracker ")
    
    parser.add_argument("-hash","--hash_content",required=True,type=str,help="Enter the Hash to crack")
    parser.add_argument("-type","--hash_type",required=True,type=str,help="Type of the Hash")
    parser.add_argument("-w","--wordlist_path",type=str,help="Mention the path of the wordlist to brute force the passwords")
    parser.add_argument("-t","--threads",type=int,default=30,help="Enter the Number of threads")
    parser.add_argument("-s","--string",type=str,help="Enter the possible string content if possible")


    args = parser.parse_args()

    hash = args.hash_content
    hash_type = args.hash_type
    wordlist = args.wordlist
    threads = args.threads





    def 