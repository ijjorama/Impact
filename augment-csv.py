import csv, sys


def getProjId(row, projectIdLabel):
    return row[projectIdLabel]

def getRow(reader, projectIdLabel, projectId):
    pass

def main():

    filename = sys.argv[1]
    projectId = sys.argv[2] if len(sys.argv) == 3 else None
  
    with open(filename) as csvfile:
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
