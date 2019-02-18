import requests
import sys

EMAIL = 'eko@monetizemore.com'
PASSWORD = 'Bismillah101'

URL = 'https://tools.monetizemore.com/login?next=%2F'

def main():
    # Start a session so we can have persistant cookies
    session = requests.session(config={'verbose': sys.stderr})

    # This is the form data that the page sends when logging in
    login_data = {
        'loginemail': EMAIL,
        'loginpswd': PASSWORD,
        'submit': 'login',
    }

    # Authenticate
    r = session.post(URL, data=login_data)

    # Try accessing a page that requires you to be logged in
    r = session.get('https://tools.monetizemore.com/ans/list')

if __name__ == '__main__':
    main()