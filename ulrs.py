import requests
import sys


def main():
    urls = sys.argv[1].split(",")
    for url in urls:
        print(f"====== Contents: {url} ======")
        r = requests.get(url)
        print(r.text)


if __name__ == "__main__":
    main()