import argparse
import requests
from time import time
from os import stat, curdir, sep


def download_file(url):
    if not url:
        return
    start_time = time()
    r = requests.get(url)
    elapsed_time = time() - start_time
    file_length = r.headers.get('Content-Length')
    download_speed = (int(file_length) * 8) / elapsed_time
    print "Download Speed: " + str(download_speed) + " Bits/sec"


def upload_file(url, data, headers):
    if not url or not data:
        return
    start_time = time()
    r = requests.post(url, data=data, headers=headers)
    elapsed_time = time() - start_time
    upload_speed = (int(headers['Content-Length']) * 8) / elapsed_time
    print "Upload Speed: " + str(upload_speed) + " Bits/sec"


def main():
    FILE_NAME = "image.jpg"
    parser = argparse.ArgumentParser(description="Python HTTP client implementation. Please specify server IP and port")
    parser.add_argument('-i', '--server-ip', default='None', required=True, help='Server IP')
    parser.add_argument('-p', '--server-port', help='Server Port')
    args = parser.parse_args()
    download_url = "http://" + args.server_ip + ":" + args.server_port + "/" + FILE_NAME
    download_file(url=download_url)

    upload_url = "http://" + args.server_ip + ":" + args.server_port
    with open(FILE_NAME, "rb") as file_handler:
        post_data = {'upload_file': file_handler.read()}
    file_size = stat(curdir + sep + FILE_NAME).st_size
    headers = {'Content-Length': str(file_size)}
    upload_file(upload_url, post_data, headers)

if __name__ == "__main__":
    main()