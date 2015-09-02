import sys
import xml.etree.ElementTree as ET

def refSearch(phraseterm, proxies=None):
    import requests

    svcbase = \
    'http://impact.ref.ac.uk/casestudiesapi/REFAPI.svc/SearchCaseStudies'
    url = svcbase + '?' + phraseterm + '&format=XML'
        
    response = requests.get(url, proxies=proxies)
    return response.text.encode("utf-8") 

def getTagSingleText(elt, tagbase, tag):

    elt = elt.findall(tagbase+tag)
    return elt[0].text

def getCSIDs(root, tagbase, cstag):

    csids = ()
    for child in root:
        csid = getTagSingleText(child, tagbase, cstag)
        csids += (csid, )

    return csids
 	
def getCSIDsByPhrase(searchmethodurl, phraseterm, proxies=None):
    pass

def main():
 
    tagbase = '{http://schemas.datacontract.org/2004/07/REFAPIService}'
    cstag = 'CaseStudyId'

    phrase = sys.argv[1] if len(sys.argv) == 2 else 'phrase=crystal bridge' # 'phrase=crystal or mlcc'
    searchResults = refSearch(phrase, {"http": "http://wwwcache.rl.ac.uk:8080/"} )
    
    if len(searchResults) == 0:
        sys.exit("searchResults is zero-length")
    
    root = ET.fromstring(searchResults)
    
    allcsids = ()
    if len( list(root) ) != 0:
        csids = getCSIDs(root, tagbase, cstag)
        allcsids += (csids, )
    allcsids = list(sum(allcsids,()))

    print 'Len(allcsids) = %d.\n' % len(allcsids)


   

if __name__ == "__main__":
    main()
