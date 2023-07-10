import os, csv

with open("100MostStreamedSongs.csv") as file:
  reader = csv.DictReader(file)

  for row in reader:
    folder = row["Artist(s)"]
    try:
      os.mkdir(folder)
      print(f"Directory {folder} created successfully.")
    except FileExistsError:
      print(f"Directory {folder} already exists.")
    f = open(folder+"/"+row["Song"]+".txt", "w")