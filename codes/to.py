import csv

with open('ilcedagilim.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "Supermarkets"])
    writer.writerow(["Akyurt", "60"])
    writer.writerow(["Altındag", "60"])
    writer.writerow(["Ayas", "30"])
    writer.writerow(["Bala", "35"])
    writer.writerow(["Beypazarı", "50"])
    writer.writerow(["Çamlıdere", "9"])
    writer.writerow(["Çankaya", "60"])
    writer.writerow(["Çubuk", "60"])
    writer.writerow(["Elmadağ", "37"])
    writer.writerow(["Etimesgut", "60"])
    writer.writerow(["Evren", "4"])
    writer.writerow(["Güdül", "10"])
    writer.writerow(["Haymana", "31"])
    writer.writerow(["Kalecik", "16"])
    writer.writerow(["Kazan", "4"])
    writer.writerow(["Keçiören", "60"])
    writer.writerow(["Kızılcahamam", "24"])
    writer.writerow(["Mamak", "60"])
    writer.writerow(["Nallıhan", "31"])
    writer.writerow(["Polatlı", "60"])
    writer.writerow(["Pursaklar", "60"])
    writer.writerow(["Şereflikoçhisar", "20"])
    writer.writerow(["Sincan", "60"])
    writer.writerow(["Yenimahalle", "60"])
file.close()    