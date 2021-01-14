#!/usr/bin/python3
""" Python script that takes in a URL,
    sends a request to the URL
    and displays the body of the response. """

if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        requests_dict = r.json()
        id = requests_dict.get('id')
        name = requests_dict.get('name')
        if len(requests_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(requests_dict.get('id'), requests_dict.get('name')))
    except:
        print("Not a valid JSON")
