with open('data/titanic.csv') as csv_file:
    for _ in csv_file:
        pass
    csv_file.seek(0)
    for _ in csv_file:
        pass
    print(csv_file.tell())
