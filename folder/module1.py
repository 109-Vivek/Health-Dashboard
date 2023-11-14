import pandas as pd
import re
path=''
df = pd.read_csv(path+'newdata.csv')
diseases = open(path+'diseases.lst', 'r').readlines()[0].split('|')
medicines = open(path+'medicines.lst', 'r').readlines()[0].split('|')
symptoms = open(path+'symptoms.lst', 'r').readlines()[0].split('|')



def isDisease(d):
    for disease in diseases:
        #HAMMING DISTANCE:
        # dist_counter = 0
        # for n in range(min(len(d), len(disease))):
        #     if d[n] != disease[n]:
        #         dist_counter += 1
        # if(len(d)-dist_counter>len(d)//1.2): return True        
        if(re.search(disease, d, re.IGNORECASE)!=None):
            return True
    
    return False

def isSymptom(s):
    for symptom in symptoms:
        if(re.search(symptom, s, re.IGNORECASE)!=None):
            return True
        
    return False

def isMedicine(m):
    for medicine in medicines:
        if(re.search(medicine, m, re.IGNORECASE)!=None):
            return True
        
    return False




def check_category(s):
    r=''
    if (isDisease(s)):
        r='disease'
    elif (isMedicine(s)):
        r='medicine'
    elif (isSymptom(s)):
        r='symptom'
    else:
        r='word'
    
    return r


def getMedicines(disease):
    l=[]

    r=df[df['Disease'].str.contains(disease, case=False)]['Medicines'][0]


    l=r.split('|')
    return l


def getSymptoms(disease):
    l=[]

    r=df[df['Disease'].str.contains(disease, case=False)]['Symptoms'][0]


    l=r.split('|')
    return l



