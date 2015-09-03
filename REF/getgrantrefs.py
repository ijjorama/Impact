import csv, sys


def getProjId(row, projectIdLabel):
    return row[projectIdLabel]

def getRow(reader, projectIdLabel, projectId):
    pass

def getrefs(filename):
  
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        n = 0
        refs = ()
        for row in reader:
            n += 1
            refs += (row['ProjectReference'],)
    return refs

def main():
    filename = sys.argv[1]
    refs = getrefs(filename)

    assert (len(refs) == 2851)

    stride = 100
    for i in range(0, len(refs), stride):
        print "%d\t%s.\n" % (i, refs[i:i+stride])

    refterm = ' or '.join(refs)

#    print refterm

if __name__ == "__main__":
    main()
