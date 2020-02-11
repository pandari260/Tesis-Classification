from CRIO.Modelo.SampleContainer import SampleContainer
import csv

def __getListClass(lines, clas):
    lines = list(filter(lambda line: int(line[-1]) == clas, lines))
    lines = list(map(lambda line: line[:-1], lines))
    return list(map(lambda line: tuple(map(lambda line2: float(line2), line)),  lines))

def readSample(name):
    with open(name, 'r') as csvfile:
        aux_set_data = csv.reader(csvfile, delimiter=',')
        next(aux_set_data)
        aux_set_data = list(aux_set_data)
        c0 = __getListClass(aux_set_data, 0)
        c1 = __getListClass(aux_set_data, 1) 
        return c0, c1

    