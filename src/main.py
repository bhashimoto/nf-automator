import sys
from retriever import retrieve_data
from drive_integration import import_data

def main():
    args = sys.argv
    url:str = ''
    if len(args) == 1:
        url = input('please provide url: ')
    else:
        url = args[1]

    data = retrieve_data(url)
    import_data(data)

main()
