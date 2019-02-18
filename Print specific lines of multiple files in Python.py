import glob
from itertools import islice
#
# # May as well use iglob since we'll stop processing at 30 files anyway
# # files = glob.iglob('/Users/path/to/*/files.txt')
files = glob.iglob('/home/eko/monetizemore/web_app/adscrape/apps/ans/fetchers/adsense.py')
#
# # Stop after no more than 30 files, use enumerate to track file num
# for i, file in enumerate(islice(files, 30)):
#     with open(file,'r') as f:
#         # Skip the first i lines of the file, then print the next line
#         print(next(islice(f, i, None)))


import glob
import linecache

line = 18
# for file in glob.glob('/Users/path/to/*/files.txt'):
for file in glob.glob('/home/eko/monetizemore/web_app/adscrape/apps/ans/fetchers/vertoz_com.py'):
    print(linecache.getline(file, line))
    line += 1
    if line > 30:  # if you really need to limit it to only 30
        break


