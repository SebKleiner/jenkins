import urllib.request
import sys


def main():
    urls = sys.argv[1].split(",")
    for url in urls:
	try:
        	print(f"====== Contents: {url} ======")
        	r = urllib.request.urlopen(url).read()
		print(r)
	except ValueError:
		print('There is an error!')
		sys.exit()


if __name__ == "__main__":
    main()