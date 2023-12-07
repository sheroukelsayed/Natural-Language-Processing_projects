import sys, re
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score, classification_report


def print_usage():
    print (
    '''Usage:
    python3 NADI2022-ST2-Scorer.py  <gold-file> <pred-file>
        ''')

## loads labels from file
def load_labels(filename):
    with open(filename) as f:
        labels = f.readlines()
    labels = [x.strip() for x in labels]
    return labels


if __name__ == '__main__':

        
    verbose = 0
    if (len (sys.argv) > 4 or len (sys.argv) <3):
        print_usage()
        exit()
        
    if (len (sys.argv) == 4 and sys.argv[3] != "-verbose"):
        print_usage()
        exit()
        
    if (len (sys.argv) == 4):
        verbose = 1

    
    gold_file = sys.argv[1]
    pred_file = sys.argv[2]
    

    gold_labels = load_labels(gold_file)
    predicted_labels = load_labels(pred_file)

    if (len(gold_labels) != len(predicted_labels)):
        print ("both files must have same number of instances")
        exit()

    ## if verbose, computes f1, recall, precision for each of the classes
    if (verbose):
        labels = list(set(gold_labels))
        accuracy = accuracy_score(gold_labels, predicted_labels) * 100 
        f1 = f1_score(gold_labels, predicted_labels, labels = labels, average = None) * 100
        recall = recall_score(gold_labels, predicted_labels, labels = labels, average = None) * 100
        precision = precision_score(gold_labels, predicted_labels, labels = labels, average = None) * 100


        print ("INDIVIDUAL PRECISION SCORE:")
        for x in range (len(labels)):
            print (labels[x], ", PRECISION SCORE: %.2f" %precision[x], "%")
            
        print ("\nINDIVIDUAL RECALL SCORE:")
        for x in range (len(labels)):
            print (labels[x], ", RECALL SCORE: %.2f" %recall[x], "%")

        print ("\nINDIVIDUAL F1 SCORE:")
        for x in range (len(labels)):
            print (labels[x], ", F1 SCORE: %.2f" %f1[x], "%")



    ## computes overall scores (accuracy, f1, recall, precision)
    accuracy = accuracy_score(gold_labels, predicted_labels) * 100
    recall = recall_score(gold_labels, predicted_labels, average = "macro") * 100
    precision = precision_score(gold_labels, predicted_labels, average = "macro") * 100

    report = classification_report(gold_labels, predicted_labels, digits=6)
    for line in report.split("\n")[2:5]:
        line = re.sub('\s+', '\t', line)
        line_info=line.split("\t")
        
        report_label=line_info[1]
        report_P=line_info[2]
        report_R=line_info[3]
        report_F1=line_info[4]
        
        if "neg" in report_label:
            rN=float(report_R)
            Nf1=float(report_F1)
        elif "pos" in report_label:
            rP=float(report_R)
            Pf1=float(report_F1)
        elif "neut" in report_label:
            rU=float(report_R)
            Uf1=float(report_F1)
    f1pn=((Nf1+Pf1)/2) * 100 #compute F1PN

    
    print ("\nOVERALL SCORES:")
    ## prints overall scores (accuracy, f1, recall, precision)
    print ("MACRO AVERAGE PRECISION SCORE: %.2f" %precision, "%")
    print ("MACRO AVERAGE RECALL SCORE: %.2f" %recall, "%")
    print ("MACRO F1-PN SCORE: %.2f" %f1pn, "%")
    print ("OVERALL ACCURACY: %.2f" %accuracy, "%\n")

    #write to a text file
    out_file = open(pred_file.split("/")[-1].split(".")[0]+"_result.txt","w")
    out_file.write("\nOVERALL SCORES:\n")
    ## prints overall scores (accuracy, f1, recall, precision)
    out_file.write("MACRO AVERAGE PRECISION SCORE: %.2f \n" %precision)
    out_file.write("MACRO AVERAGE RECALL SCORE: %.2f  \n" %recall)
    out_file.write("MACRO F1-PN SCORE: %.2f  \n" %f1pn)
    out_file.write("OVERALL ACCURACY: %.2f  \n" %accuracy)

    out_file.close()
    
   
