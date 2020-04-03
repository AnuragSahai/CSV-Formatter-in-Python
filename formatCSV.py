import csv
import sys

inputPath = sys.argv[1]
outputPath = sys.argv[2]
with open(inputPath, encoding="utf-8") as inputFile:
    with open(outputPath, 'w', newline='', encoding="utf-8") as outputFile:
        reader = csv.DictReader(inputFile, delimiter=',')
        writer = csv.DictWriter(
            outputFile, reader.fieldnames, delimiter='|', quoting=csv.QUOTE_NONE, escapechar='^', doublequote=False, quotechar="")
        writer.writeheader()
        writer.writerows(reader)

print("Formationg complete.")
