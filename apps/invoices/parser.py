import csv


def parser_file(file_path):
    return csv.DictReader(open(file_path, 'r'), delimiter='\t')

