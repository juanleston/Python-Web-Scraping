#Import Pandas:
import pandas as pd

#Load sitemap csv file:
sitemap = pd.read_csv(
    '/Users/juan/Documents/Data Science Portfolio/pythonscrapy/sitemap.csv',
    names = ['url'])

#Subset sitemap to only keep url's that correspond to Vietnam:
sitemap = sitemap[sitemap['url'].str.contains('vietnam')]

#Remove prefix and suffix tags:
sitemap.url = sitemap.url.map(lambda x: x.removeprefix("<url><loc>"))
sitemap.url = sitemap.url.map(lambda x: x.removesuffix(
    "</loc><changefreq>weekly</changefreq></url>"))

#Filter the url's of interest:
#Part1: Keep only the urls that have 4 slashes and text after the third one:
sitemap_filtered_1 = sitemap[sitemap['url'].str.contains(
    '[a-zA-Z0-9 -]+://[a-zA-Z0-9 -]+\.[a-zA-Z0-9 -]+/[a-zA-Z0-9 -]+/[a-zA-Z0-9 -]+/[a-zA-Z0-9 -]+/[a-zA-Z0-9 -]')]
#Export part 1 of the start url's:
sitemap_filtered_1.to_csv(
    '/Users/juan/Documents/Data Science Portfolio/pythonscrapy/starturlsvietnam1.csv',
    index=False)

#Part2: Keep only the urls that have 3 slash and text after the third one:
sitemap_filtered_2 = sitemap[sitemap['url'].str.contains(
    '(?<!\w)[a-zA-Z0-9 -]+://[a-zA-Z0-9 -]+\.[a-zA-Z0-9 -]+/[a-zA-Z0-9 -]+/[a-zA-Z0-9 -]+/[a-zA-Z0-9 -]+/(?!\w)')]
#Export part 2 of the start url's:
sitemap_filtered_2.to_csv(
    '/Users/juan/Documents/Data Science Portfolio/pythonscrapy/starturlsvietnam2.csv',
    index=False)
