import csv

class DataPrinter:
    def print_to_screen(self, data):
        for d in data:
            print(d)

    def print_to_file(self, data):
        with open('output.txt', 'w', encoding= 'utf -8') as file:
            writer = csv.writer(file)
            for d in data:
                writer.writerow(d)