#CG = int(input(" Het CG percentage is "))



test = "  "
# Verschillende nucleotiden apart van elkaar tellen.
print(test.count("A"))
print(test.count("T"))
print(test.count("C"))
print(test.count("G"))

# GC samen geteld. 
print (test.count("C")+ (test.count("G")))

#Zodat we dadelijk het deel door het geheel kunnen delen.
#Deel is GC samen, geheel is ATCG samen.
deel = (test.count("C")+ (test.count("G")))
geheel = (test.count("A")+ (test.count("T")+ (test.count("C")+ (test.count("G")))))

print (deel / geheel)

#Komt een 0, getal uit. *100 en dan heb je het percentage.
