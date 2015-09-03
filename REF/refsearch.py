import sys

def refSearch(phrase, proxies=None):
    import requests

    svcbase = \
    'http://impact.ref.ac.uk/casestudiesapi/REFAPI.svc/SearchCaseStudies'
    url = svcbase + '?phrase=' + phrase + '&format=XML'
    response = requests.get(url, proxies=proxies)
    return response.text 

def getTagText(text, tag):
    from xml.etree import cElementTree as ET

    tagbase = '{http://gtr.rcuk.ac.uk/gtr/api/project}'
    project = ET.fromstring(text)
    tag = project.findall(tagbase + tag)
    return tag[0].text

def main():
 
    phrase = sys.argv[1] if len(sys.argv) == 2 else 'mlcc'
    searchResults = refSearch(phrase, {"http": "http://wwwcache.rl.ac.uk:8080/"} )
    if len(searchResults) == 0:
        sys.exit("searchResults is zero-length")

#    abstract = getTagText(searchResults, 'abstractText') if searchResults is not None else None

    print searchResults

if __name__ == "__main__":
    main()
