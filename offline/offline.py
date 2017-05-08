import re, bs4, requests

class SteamGameOffline()
    r"""Class used to represent one game on steam.

    Files will be read when you alloc a SteamGame object.
    Folder path should be organized by a standard structure.
    For example:
        data
        | app
        | | 204090
        | | | 204090.info
        | | | 204090_review
        | | | | *reviews files*
        | | ...
        | sub
        | | ...
        | bundle
        | | ...
    You can read games id, tag, url, img, reviews and so on
    with this class.
    """
    
    def __init__(self, gid, gtag, path=None, debug=False):
        
    
    @property
    def gid(self):
        

    @property
    def gtag(self):
        

    @property
    def url(self):
        

    @property
    def gname(self):
        

    @property
    def status(self):
        


    # ____________________ Inner ____________________
    
    def __getHtmlText(self):
        

    def __read_name(self):
        
    # ____________________ Private Values ____________________
    # self.__[debug, url, id, tag, text, soup, status, by, path]




# ______ Under Development ______
def printTag(t):
    return 'app' if t==0 else 'sub' if t==1 else 'bundle' if t==2 else 'error'

def read_data(path):
    data = pd.read_csv(path, sep='\t', encoding='utf8')
    data.set_index('id', inplace=True)
    return data

def buildpath():
    data = read_data('..\\Games\\data_no_duplicates.dat')
    for i in range(len(data)):
        Tag = getTag(data.iat[i,0])
        Id = data.index[i]
        folder_name = '..\\Games\\{}\\{}\\'.format(Tag, Id)
        file_name = folder_name + '{}.txt'.format(Id)
        if not os.path.exists(folder_name): os.makedirs(folder_name)
        with open(file_name, 'w') as f:
            f.write('')
        if not i%100: print i

def write_log(isSuccess, url, errtype = None):
    with open('info.log', 'a') as f:
        err = ''
        err += 'OK: ' if isSucess else 'Error: ' + url
        if not isSuccess:
            err += '\n  404 not found.' if errtype == 1 else \
                   '\n  Network connection error.' if errtype == 2 else \
                   '\n  Unknown'
        f.write(err + '\n')
