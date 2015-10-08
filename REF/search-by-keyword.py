import sys
import xml.etree.ElementTree as ET




def getkeywords(filename):

    with open(filename) as kwfile:
        terms = ()
        for line in kwfile:	
            terms += ( '"' + line.rstrip('\n') + '"' ,)

    return terms

def simpleSearch(phraseterm, proxies=None):
    import requests

    svcbase = \
    'http://impact.ref.ac.uk/casestudiesapi/REFAPI.svc/SearchCaseStudies'
    url = svcbase + '?' + phraseterm + '&format=XML'
    # RAL web cache breaks if len(url) > 2700 
    # print 'Len(url) = %d.\nURL=%s\n' % (len(url), url) 


    response = requests.get(url, proxies=proxies)
    if response.status_code != 200:
        print response.status_code
        print response.reason
        sys.exit("Bad response from server")
    return response.text.encode("utf-8") 

def getTagSingleText(elt, tagbase, tag):
	elt = elt.findall(tagbase+tag)
        if len(elt) > 0:
	    return elt[0].text
        else:
            return None
	
def getCSIDs(root, tagbase, cstag):

    csids = ()
    for child in root:
        csids += (getTagSingleText(child, tagbase, cstag), )
    return csids
 

def main():
 
    tagbase = '{http://schemas.datacontract.org/2004/07/REFAPIService}'
    cstag = 'CaseStudyId'

    terms = getkeywords(sys.argv[1])

    terms = " ".join(terms)
 
    allcsids = ()

    phrase = 'phrase=' + terms 
    searchResults = simpleSearch(phrase, {"http": "http://wwwcache.rl.ac.uk:8080/"} )

    root = ET.fromstring(searchResults)

    nelements = len( list(root) )

    if nelements != 0:

        csids = getCSIDs(root, tagbase, cstag)
        if csids is not None and len(csids) > 0:

            for kid in csids:
                 if kid is not None:
                     allcsids += (kid, )
  
    print 'Number of matching Case Study IDs = %d.\n' % len(allcsids)

    for c in allcsids:
        if c is not None:
            print c

if __name__ == "__main__":
    main()
