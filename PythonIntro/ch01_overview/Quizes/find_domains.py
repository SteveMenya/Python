"""
For this task, you are to manually extract the domain name out of the URLs mentioned on our slide.


https://docs.python.org/3/
https://www.google.com?qws_rd=ssl#q=python
http://localhost:8005/contact/501


"""
my_data = [
    'https://docs.python.org/3/',
    'https://www.google.com?qws_rd=ssl#q=python',
    'http://localhost:8005/contact/501',
    'https://jjmenya.testing.com/3/',
    'http://www.dctc.edu/'
]


def get_domain_name(data):
    # loop through the urls coming in
    for url in data:

        if url.startswith('http://'):
            get_http_domain(url)

        elif url.startswith('https://'):
            get_https_domain(url)


def get_http_domain(url):
    # loop through string in the url and remove the left side
    remaining = url[len('http://'):]
    # print(remaining)

    # loop and remove things on left
    position = remaining.find(':')
    if position != 1:
        domain = remaining[:position]

    print(domain)


def get_https_domain(url):
    remaining = url[len('https://'):]
    # print(remaining)

    # loop and remove things on left
    position = remaining.find('/')
    if position < 0:
        position = remaining.find('?')
    if position != 1:
        domain = remaining[:position]

    print(domain)


get_domain_name(my_data)
