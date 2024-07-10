#!/usr/bin/python3
import sys
import json
from retriever import retrieve_data
from drive_integration import import_data

def main():
    urls = None
    if sys.stdin:
        urls = json.loads(sys.stdin.read())
    else:
        args = sys.argv
        url:str = ''
        if len(args) == 1:
            url = input('please provide url: ')
            urls = {url: url}
        else:
            url = args[1]
            urls = {url: url}

    for url in urls.keys():
        data = retrieve_data(url)
        import_data(data)

main()
