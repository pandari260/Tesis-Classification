
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, recall_score
import marshal
import pandas as pd


def report_to_df(report):
    report = re.sub(r" +", " ", report).replace("avg / total", "avg/total").replace("\n ", "\n")
    report_df = pd.read_csv(StringIO("Classes" + report), sep=' ', index_col=0)        
    return(report_df)

def showResult(i, directory, test, resultClassify, dataTest):
    print("----------- Test nº {} dimension {} {} -------------\n ".format(str(i), directory, str(test)))
    print("Accuracy: {}".format(accuracy_score(resultClassify, dataTest)))
    print("Confusion matrix: \n {} ".format(confusion_matrix(resultClassify, dataTest)))
    print("Metrics report: \n {} ".format(classification_report(resultClassify, dataTest)))
    
    report = classification_report(resultClassify, dataTest,  output_dict=True)

    clsf_report = pd.DataFrame(report).transpose()
        
       # clsf_report.to_csv('outputRunTest.csv', index= False)

    for i, j in clsf_report.iterrows():
        print(i, j)
        print()

    print("\n\n")