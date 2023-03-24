ime = input("Ime datoteke: ")
fhand = open(ime)
counter = 0
zbroj = 0
for line in fhand:
    line = line.rstrip()
    if(line.startswith("X-DSPAM-Confidence")):
        counter = counter + 1
        number = line.split()
        zbroj = zbroj + float(number[1])
mid = float(zbroj) / float(counter)
print("Average X-DSPAM-Confidence: " + str(mid))