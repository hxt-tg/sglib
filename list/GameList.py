import urllib, urllib2, re, bs4, requests
from bs4 import BeautifulSoup

# get the text of the html
def getHtmlText(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text

def getTag(script):
    t = re.findall(re.compile(r'"type":"(.+?)",'),script)[0]
    return 0 if t == 'app' else 1 if t == 'sub' else 2 if t == 'bundle' else -1

def readHtml(htmltext):
    gamelist = []
    soup = BeautifulSoup(htmltext, 'html.parser')
    games = soup.find_all('a', class_='search_result_row ds_collapse_flag')
    for game in games:
        gtag = getTag(game.attrs['onmouseover'])
        if gtag == 0:
            gid = int(game.attrs['data-ds-appid'])
        elif gtag == 1:
            gid = int(game.attrs['data-ds-packageid'])
        elif gtag == 2:
            gid = int(game.attrs['data-ds-bundleid'])
            # print 'Bundle[{}]:\n '.format(gid),
            # print game.attrs['data-ds-bundle-data']
        else:
            print 'Error!'
        gname = game.find('div', class_='responsive_search_name_combined').div.span.string
        gamelist.append([gid, gtag, gname])
    return gamelist

def savefile(path, infolist):
    with open(path, 'a') as f:
        for i in infolist:
            f.write('{} {} {}\n'.format(i[0],i[1],i[2]))

def main():
    maxpage = 12
    gamelist = []
    for i in range(maxpage):
        print 'Page:', i+1
        url = 'http://store.steampowered.com/search/?filter=topsellers&page={}'.format(i+1)
        gamelist += readHtml(getHtmlText(url))
        
    savefile('..\\Games\\gamelist.dat', gamelist)

if __name__ == '__main__':
    main()

