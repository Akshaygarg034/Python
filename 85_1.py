# *******************  Creating Command Line Utility for downloading a file  *******************

import argparse
import requests

def DownloadFile(url, fileName):
    if(fileName is None):
        local_filename = url.split('/')[-1]
    else:
        local_filename = fileName

    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: 
            f.write(chunk)
    f.close()
    return 

parser = argparse.ArgumentParser()

parser.add_argument("url", help="url for image to download")
parser.add_argument("-o", "--fileName", help="Name of the file", default=None)

args = parser.parse_args()

print(args.url)
print(args.fileName)
DownloadFile(args.url, args.fileName)


# Commands to execute this:

# python 85_1.py <file_url>
# python 85_1.py <file_url> -o <file_name>   # with optional argument fileName
