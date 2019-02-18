import requests
import bs4

# url = 'https://tools.monetizemore.com/db-admin/db_ans_credentials/'
url = requests.get('https://tools.monetizemore.com', auth=('eko@monetizemore.com', 'Bismillah101'))

call_url_text = url.text
#
call_bs4 = bs4.BeautifulSoup(call_url_text, 'html.parser')
#
# # name, attrs, recursive, text, limit
find = call_bs4.find_all('tr')
#
# print(find)

print(find)