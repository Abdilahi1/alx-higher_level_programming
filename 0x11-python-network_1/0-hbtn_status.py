#!/usr/bin/python3
"""Script for fetching url https://alx-intranet.hbtn.io/status"""

from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        html = resp.read()

    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(html), html, html.decode('utf-8')))
