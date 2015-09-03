import sys, csv
import xml.etree.ElementTree as ET


def getrefs(filename):
  
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        refs = ()
        n = 0
        for row in reader:
            refs += (row['ProjectReference'],)
            n += 1
            if n == 100:
                break

    return refs


def refSearch(phraseterm, proxies=None):
    import requests

    svcbase = \
    'http://impact.ref.ac.uk/casestudiesapi/REFAPI.svc/SearchCaseStudies'
    url = svcbase + '?' + phraseterm + '&format=XML'
#    print 'Len(url) = %d.\n' % len(url) # RAL web cache breaks if len(url) > 2700 (or > 101 terms)

    response = requests.get(url, proxies=proxies)
    return response.text 

def getTagSingleText(elt, tagbase, tag):
	elt = elt.findall(tagbase+tag)
	return elt[0].text
	
def main():
 
    tagbase = '{http://schemas.datacontract.org/2004/07/REFAPIService}'
    cstag = 'CaseStudyId'

    n = 100
    refs = getrefs(sys.argv[1])
    reftargets = ' or '.join(refs)
    phrase = 'phrase='+reftargets


    searchResults = refSearch(phrase, {"http": "http://wwwcache.rl.ac.uk:8080/"} )
    
    if len(searchResults) == 0:
        sys.exit("searchResults is zero-length")
    else:
        print searchResults

    searchResults = searchResults.encode("utf-8")
    
    root = ET.fromstring(searchResults)
    
    if root is not None:
        
        if len( list(root) ) == 0:
            print 'No search results'
            print root.text
        else:
            for child in root:
                csid = getTagSingleText(child, tagbase, cstag) 
                print 'CSID=%s' % csid

    else:
    	print 'No search results'
        

if __name__ == "__main__":
    main()
