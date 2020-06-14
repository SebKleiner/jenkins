import requests
import os


def main():
    urls = os.environ[1].split(',')
    for url in urls:
        print(f"====== Contents: {url} ======")
        r = requests.get(url)
        print(r.text)


if __name__ == "__main__":
    main()