import sys
from retriever import retrieve_data
from drive_integration import import_data

def main():
    args = sys.argv
    url = args[1]
    data = retrieve_data(url)
    import_data(data)

main()
