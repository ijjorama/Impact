import sys

def getPage(url, proxies=None):
    import requests

    response = requests.get(url, proxies=proxies)
    return response.text 

def getTagText(text, tag):
    from xml.etree import cElementTree as ET

    tagbase = '{http://gtr.rcuk.ac.uk/gtr/api/project}'
    project = ET.fromstring(text)
    tag = project.findall(tagbase + tag)
    return tag[0].text

def main():
    url ="http://gtr.rcuk.ac.uk/gtr/api/projects/04D6290F-68B6-47AC-8D60-00796E01532E/" 
    projectText = getPage(url, {"http": "http://wwwcache.rl.ac.uk:8080/"} )
    if len(projectText) == 0:
        sys.exit("projectText is zero-length")

    abstract = getTagText(projectText, 'abstractText') if projectText is not None else None

    print abstract
if __name__ == "__main__":
    main()
