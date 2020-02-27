# Resolve the problem!!
import os
import re

def run():
    # Start coding here
    with open(os.getcwd() + '/src/encoded.txt', 'r', encoding='utf-8') as f:
        encoded_text = f.read()
        secret = re.findall("[a-z]",encoded_text)
        print (''.join(secret))

if __name__ == '__main__':
    run()