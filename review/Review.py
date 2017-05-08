import urllib, urllib2, re, bs4
from bs4 import BeautifulSoup

# get the text of the html
def getHtmlText(url):
    try:
        response = urllib2.urlopen(urllib2.Request(url))
    except urllib2.HTTPError, e:
        print 'Error! ==> Code:%d ' % e.code
    else:
        return response.read()

def getReview(appid, offset, p, numperpage=10, browsefilter='toprated', language='english', searchText=''):
    url='http://steamcommunity.com/app/'+str(appid)+'/homecontent/'
    form_elem = [('userreviewsoffset', str(offset)),
                 ('p', str(p)),
                 ('workshopitemspage', str(p)),
                 ('readytouseitemspage', str(p)),
                 ('mtxitemspage', str(p)),
                 ('itemspage', str(p)),
                 ('screenshotspage', str(p)),
                 ('videospage', str(p)),
                 ('artpage', str(p)),
                 ('allguidepage', str(p)),
                 ('wenguidepage', str(p)),
                 ('integratedguidepage', str(p)),
                 ('discussionspage', str(p)),
                 ('numperpage', str(numperpage)),
                 ('browsefilter', browsefilter),
                 ('appid', str(appid)),
                 ('appHubSubSection', str(numperpage)),
                 ('l', language),
                 ('appHubSubSection', str(numperpage)),
                 ('browsefilter', browsefilter),
                 ('filterLanguage', 'default'),
                 ('searchText', searchText),
                 ('forceanon', '1')]
    m_url = url + "?" + urllib.urlencode(form_elem)
    print m_url
    text = getHtmlText(m_url)
    return text

def printRev(review):
    print 
    
def getReviewsFromTop(appid, p, numperpage=10, browsefilter='toprated', language='english', searchText=''):    
    # To find a ResultSet that not exist to create a new empty one:
    soup = BeautifulSoup('','html.parser')
    Reviews = []
    for i in range(p):
        content = getReview(appid, i*numperpage, i+1, numperpage, browsefilter, language, searchText)
        soup = BeautifulSoup(content,'html.parser')
        # get review
        revlist = soup.find_all('div', class_='apphub_Card modalContentLink interactable')
        
        for rev in revlist:
            revd = {}
            # print str(rev)
            helpful_d = {}
            author_d = {}
            # get "helpful" details in review, ht=help total, t=total, p=percent, f=funny
            helpful_d['ht'], helpful_d['t'], helpful_d['p'], helpful_d['f'] = map(lambda x: int(x), \
                              rev.find('div', class_='found_helpful').text.strip().replace(',','').replace(' of ',',')\
                              .replace(' people (',',').replace('%) found this review helpful',',')\
                              .replace(' people found this review funny','').split(','))
            revd['helpful'] = helpful_d
            revd['appid'] = appid
            revd['title'] = rev.find('div', class_='title').string
            revd['hours'] = float(rev.find('div', class_='hours').string[:-14])
            revd['date']  = rev.find('div', class_='date_posted').string
            revd['products'] = int(rev.find('div', class_='apphub_CardContentMoreLink ellipsis').string[:-20])
            revd['review'] = str(rev.find('div', class_='apphub_CardTextContent').br).replace('<br>','\n').replace('</br>','').strip()
            author_info = rev.find('div', class_=re.compile(r'^apphub_CardContentAuthorName'))
            author_d['name'] = author_info.a.string
            author_d['url'] = author_info.a.attrs['href']
            author_d['img'] =  rev.find('div', class_=re.compile(r'^appHubIconHolder')).img.attrs['src']
            revd['author'] = author_d
            Reviews.append(revd)
    # process
    print Reviews
    print len(Reviews)
    # return Reviews

def main():
    getReviewsFromTop(440250, 1)


if __name__ == '__main__':
    main()
                    
                    
        
    
