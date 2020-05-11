import csv

read_sample_key = ["* "]
def splitList(lista, key):    
    ret = []
    aux = []
    for item in lista:
        if not item == key:
            aux.append(item)
        elif len(aux) > 0:
            ret.append(aux)
            aux = []
    
    return ret

            


    
def __getListClass(clusters_lines, clas):       
    def removeLastChar(lines): 
        return list(map(lambda line: line[:-1], lines))
    def transformOnTuples(lines): 
        return list(map(lambda line: tuple(map(lambda line2: float(line2), line)),  lines))       
    
    clusters_lines = filter(lambda lines: lines[0][len(lines[0])-1] == str(clas) + " ",clusters_lines)
    clusters_lines = map(lambda lines: removeLastChar(lines), clusters_lines)
    return map(lambda lines: transformOnTuples(lines), clusters_lines)

def readSample(name):
    with open(name, 'r') as csvfile:
        aux_set_data = csv.reader(csvfile, delimiter=',')
        next(aux_set_data)
        clusters_lines = splitList(list(aux_set_data), read_sample_key)
        c0 = __getListClass(clusters_lines, 0)
        c1 = __getListClass(clusters_lines, 1)
        return c0, c1
    

    

    