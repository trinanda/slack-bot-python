import os


# check_all_files = os.listdir("/home/eko/monetizemore/web_app/adscrape/apps/ans/fetchers")
# # check_all_files = os.listdir("/home/eko/monetizemore/web_app/adscrape/apps/ans/testing/")
#
# output = []
# for x in check_all_files:
#     output.append(x)
#
# list_of_fetcher = output
#
# print(list_of_fetcher)

# with open("/home/eko/monetizemore/web_app/adscrape/apps/ans/fetchers/bidfluence_com.py") as openfile:
with open("/home/eko/monetizemore/web_app/starterbot/testing-title.py") as openfile:
    for line in openfile:
        for part in line.split():
            if "TITLE=" in part:
                print(part)

