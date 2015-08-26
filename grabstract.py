import sys

def getPage(url, proxies=None):
    import requests

    response = requests.get(url, proxies=proxies)
#    if response.status_code != 200:
#        print "Well, that didn't work"
#        sys.exit("blast!")
 
    return response.text 

def getAbstract(text):
    from xml.etree import cElementTree as ET

    project = ET.fromstring(text)
    abs = project.findall('{http://gtr.rcuk.ac.uk/gtr/api/project}abstractText')
    return abs[0].text

def main():
    url ="http://gtr.rcuk.ac.uk/gtr/api/projects/04D6290F-68B6-47AC-8D60-00796E01532E/" 
    projectText = getPage(url, {"http": "http://wwwcache.rl.ac.uk:8080/"} )
    if len(projectText) == 0:
        sys.exit("projectText is zero-length")
    else:
        pass # print projectText[:40]
    abstract = getAbstract(projectText) if projectText is not None else None

    print abstract
if __name__ == "__main__":
    main()
