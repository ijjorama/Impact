import sys

def getTagText(text, tag):
    from xml.etree import cElementTree as ET

    tagbase = '{http://gtr.rcuk.ac.uk/gtr/api/project}'
    project = ET.fromstring(text)
    tag = project.findall(tagbase + tag)
    return tag[0].text

def main():

    filename = sys.argv[1]
    projectId = sys.argv[2] if len(sys.argv) == 3 else None
  
    with open(filename) as xmlfile:
        reader = csv.DictReader(csvfile)
        n = 0
        for row in reader:
            n += 1

            if projectId: 
                if getProjId(row, 'ProjectId') == projectId:

                    print "Found projectId %s at line %d.\n" % (projectId, n)

            else: # Print every row
                print(row['ProjectId'])

if __name__ == "__main__":
    main()
