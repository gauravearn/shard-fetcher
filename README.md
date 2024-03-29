# shard-fetcher
a python way to web scrap the shard, some of the categories  dont have description otherwise i would have made a dataframe otherwise the functions can be used irrespective for the name tags to find the corresponding names in github. I will although add the categories, as it is there for every shard, so will add those and then you will have the indexed dataframe of the all the recent shard with a single click. if they allow the users to add the description for eveything then add this line of code to the end and you will get a complete indexed dataframe. 

```
shard_info_layout = {}
    for i in range(len(shard_name)):
        shard_info_layout[shard_name[i]] = [[shard_des[i], shard_description_final[i]]]
    return shard_info_layout
```
To run the same
```
shard_card("https://shardbox.org/")
```

Thank you [Margret Riegert](https://github.com/nobodywasishere) for providing the link.

Gaurav Sablok \
Academic Staff Member \
Bioinformatics \
Institute for Biochemistry and Biology \
University of Potsdam \
Potsdam,Germany 
