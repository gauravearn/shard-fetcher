def shard_card(url):
    # A python way to web scrap the shard, some of the categories
    # dont have description otherwise i would have made a dataframe
    # otherwise the functions can be used irrespective for the name tags
    # to find the corresponding names in github
    import re
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    url_fetch =  urlopen(url)
    shard_card = BeautifulSoup(url_fetch, "html.parser").find_all("div", class_="shard-card")
    url_fetch =  urlopen(url)
    shard_desc = BeautifulSoup(url_fetch, "html.parser").find_all("div", class_="description")
    shard_store = [i for i in (i.split("\n") for i in list(map(str,shard_card))) for j in i if "shard-name" in j]
    shard_name, shard_des = [j.split()[1] for i in shard_store for j in i if "shard-name" in j],\
                                       [j.split()[2] for i in shard_store for j in i if "shard-name" in j]
    shard_description = [i.split("\n") for i in (list(map(str,shard_desc)))]
    shard_description_final = list(filter(None,(map(''.join,[re.findall(r'[A-Za-z]{0,}',i) for i in [i for i in (j for i in shard_description for j in i if "description" not in j) if "div" not in i]]))))
    return shard_desc
