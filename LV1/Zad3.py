polje = []
counter = 0
while True:
    try:
        vrijednost = int(input(">> "))
    except ValueError:
            break
    polje.append(vrijednost)
    counter=counter+1
    if counter==1:
        min = vrijednost
        max = vrijednost
        zbroj = vrijednost
    else:
        if vrijednost < min:
            min = vrijednost
        elif vrijednost > max:
            max = vrijednost
        zbroj = int(zbroj) + int(vrijednost)
mid = int(zbroj) / int(counter)
print("Max: "+str(max))
print("Min: "+str(min))
print("Mid: "+str(mid))
polje.sort()
print(polje)