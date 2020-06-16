import sys
import urllib.request

if __name__ == '__main__':
    urls = sys.argv[1].split(",")
    for url in urls:
        print(url)
        try:
            r = urllib.request.urlopen(url).read()
            print(r)
        except ValueError:
            print("Not posible to parse html")
            sys.exit()


