def ocjena (br_bodova):
           
           if br_bodova >= 50:
                      print("Dovoljan(2)")
           elif br_bodova >= 65:
                      print("Dobar(3)")
           elif br_bodova >= 80:
                      print("Vrlodobar(4)")
           elif br_bodova >= 90:
                      print("Odlican(5)")
           else:
                      print("Nedovoljan(1)")
           
from csv import reader
datoteka = open("rezultati.csv", "r")
    
reader_1 = reader(datoteka)
    
rezultati_1 = list(map(tuple, reader_1))
    

rezultat = []
for ime, prezime, bodovi in rezultati_1:
	rezultat.append((prezime, ime, bodovi))
	
rezultat.sort()

ocjene = []

for student in rezultat:
           rjecnik = {}
           rjecnik["prezime"] = student[0]
           rjecnik["ime"] = student[1]
           rjecnik["Ocjena"] = ocjena(int(student[2]))
           ocjene.append(rjecnik)

rezultat_2 = []

for student in ocjene:
           rezultat_2.append((student["prezime"], student["ime"], student["Ocjena"]))

print(rezultat_2)
