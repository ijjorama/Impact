import sys
import xml.etree.ElementTree as ET

def refSearch(phraseterm, proxies=None):
    import requests

    svcbase = \
    'http://impact.ref.ac.uk/casestudiesapi/REFAPI.svc/SearchCaseStudies'
    url = svcbase + '?' + phraseterm + '&format=XML'
        
    response = requests.get(url, proxies=proxies)
    return response.text 

def getTagText(text, tag):
    from xml.etree import cElementTree as ET

    tagbase = '{http://schemas.datacontract.org/2004/07/REFAPIService}'
    project = ET.fromstring(text)
    tag = project.findall(tagbase + tag)
    return tag[0].text

def getTagSingleText(elt, tagbase, tag):
	elt = elt.findall(tagbase+tag)
	return elt[0].text
	
def main():
 
    tagbase = '{http://schemas.datacontract.org/2004/07/REFAPIService}'
    cstag = 'CaseStudyId'

    phrase = sys.argv[1] if len(sys.argv) == 2 else 'phrase=crystal' # 'phrase=crystal or mlcc'
    searchResults = refSearch(phrase, {"http": "http://wwwcache.rl.ac.uk:8080/"} )
    
    if len(searchResults) == 0:
        sys.exit("searchResults is zero-length")

    searchResults = searchResults.encode("utf-8")
    
    root = ET.fromstring(searchResults)
    
    if root is not None:
        
        if len( list(root) ) == 0:
            print 'Fail'
        else:
            for child in root:
                csid = getTagSingleText(child, tagbase, cstag) 
                print 'CSID=%s' % csid

    else:
    	print 'Root is None'

if __name__ == "__main__":
    main()
