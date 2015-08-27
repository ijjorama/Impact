import csv, sys

def getProjId(row, projectIdLabel):
    return row[projectIdLabel]

def getRow(reader, projectIdLabel, projectId):
    pass

def main():

    filename = sys.argv[1]

    if len(sys.argv) == 3:
        limit = int(sys.argv[2])
    else:
        limit = 100
 
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        n = 0
        for row in reader:
            n += 1
            if n > limit:
                break 
       
            projectId = getProjId(row, 'ProjectId') 
            print "projectId = %s" % projectId 


if __name__ == "__main__":
    main()
