>>> article = '''
... The chief executive of Chinese online retailer JD.com, Liu Qiangdong, was briefly arrested in the US on accusations of criminal sexual conduct.
... 
... Mr Liu, one of China's richest people, was arrested in Minneapolis shortly before midnight on Friday and released on Saturday afternoon.
... 
... JD.com said Mr Liu, also known as Richard Liu, was falsely accused. Police say the investigation is open.
... 
... JD.com, also known as Jingdong, has alliances with Tencent and Walmart.
... 
... ...
... '''
>>> article.find('Liu')
56
>>> article.find('JD')
48

# If want to monitor other article, can use the 'find' function to search the certain keyword.