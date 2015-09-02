import sys, csv
import xml.etree.ElementTree as ET


def getrefs(filename):
  
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        refs = ()
        max = 10000 # Currently < 3000 grants, allow for more in future
        n = 0
        for row in reader:
            n += 1
            refs += (row['ProjectReference'],)
            if n == max:
                break
    return refs


def refSearch(phraseterm, proxies=None):
    import requests

    svcbase = \
    'http://impact.ref.ac.uk/casestudiesapi/REFAPI.svc/SearchCaseStudies'
    url = svcbase + '?' + phraseterm + '&format=XML'
#    print 'Len(url) = %d.\n' % len(url) # RAL web cache breaks if len(url) > 2700 (or > 101 terms)

    response = requests.get(url, proxies=proxies)
    if response.status_code == 200:
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
 
def getSearchPhrase(refs, i, stride):
    reftargets = ' '.join(refs[i:i+stride])
    reftargets = reftargets.replace('/', '\/')
    return 'phrase='+reftargets

def main():
 
    tagbase = '{http://schemas.datacontract.org/2004/07/REFAPIService}'
    cstag = 'CaseStudyId'

    refs = getrefs(sys.argv[1])

    stride = 100
    stop = len(refs)
 
    allcsids = ()
    for i in range(0, stop, stride):	# Run searches in blocks of 100 terms each
                                        # (otherwise, URL is too long for RAL web cache)

	phrase = getSearchPhrase(refs, i, stride)
        searchResults = refSearch(phrase, {"http": "http://wwwcache.rl.ac.uk:8080/"} )
    
        root = ET.fromstring(searchResults)

        nelements = len( list(root) )

        nfound = 0
        if nelements != 0:

            csids = getCSIDs(root, tagbase, cstag)
            if csids is not None and len(csids) > 0:
        
                for kid in csids:
                     if kid is not None:
                         nfound += 1
                         allcsids += (kid, )
  
    allcsids = list(sum(allcsids,()))

    print 'Number of matching Case Study IDs = %d.\n' % len(allcsids)

    for c in allcsids:
        if c is not None:
            print c

if __name__ == "__main__":
    main()
