import sys

if __name__ == '__main__':
	num = int(sys.argv[1])
	for i in range(num):
		print(i, i*i)


# import sys
# import urllib.request
#
# if __name__ == '__main__':
# 	urls = sys.argv[1].split(",")
# 	for url in urls:
# 		print(url)
# 		r = urllib.request.urlopen(url).read()
# 		print(r)

