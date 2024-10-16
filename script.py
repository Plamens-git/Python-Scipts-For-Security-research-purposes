import requests 
import sys 

# Change the file path to the location of your subdomains.txt file
sub_list = open("wordlist.txt").read() 
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{sys.argv[1]}" 

    try:
        response = requests.get(sub_domains)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ", sub_domains)   

