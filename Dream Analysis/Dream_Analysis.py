import csv

dreamsDict = {}

#Open csv and map it onto the dreams dictionary
with open("dreams_interpretations.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dreamsDict.update({row["Dream Symbol"].lower(): row["Interpretation"]})

#Take user input and give them a dream interpretation
while True:
    print("Give a few dream symbols (words) separated by a space: ")
    keywords = input()
    keywords = keywords.split(" ")

    for word in keywords:
        word = word.lower()
        print("\n")
        try:
            print(word, "\n", dreamsDict[word])
        except:
            print(word, " not in list")
        print("\n")