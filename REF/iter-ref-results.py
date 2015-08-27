import sys
import xml.etree.ElementTree as ET

def main():

    filename = sys.argv[1] if len(sys.argv) == 2 else 'search-mlcc.xml'

    tree = ET.parse(filename)
    root = tree.getroot()

    docbase = '{http://schemas.datacontract.org/2004/07/REFAPIService}' 
    for child in root:
        impactdetails = child.findall(docbase+'ImpactDetails')
        imptext = impactdetails[0].text
        print len(imptext)

        casestudyid = child.findall(docbase+'CaseStudyId')
        print casestudyid[0].text


if __name__ == "__main__":
    main()
