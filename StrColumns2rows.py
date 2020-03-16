import pandas as pd



def main():
    outputFile = 'Touhou_characterNameArrange'
    df = pd.read_csv('Touhou first Name Only v1.csv')
    
    #print(df.head()['0'])
    df['0'] = df['0'].apply(lambda name:"\""+name+"\"")
    #print(df.head()['0'])

    nameList = df['0'].tolist()

    n = 0
    temp = ""
    printList =[]

    for name in nameList:
        temp = temp + " " + name
        n+=1
        if n >= 10 :
            printList.append(temp+"\n")
            temp = ""
            n = 0

    #print(printList)
    strList2File(printList,outputFile)

def strList2File(strList,fileName):
    fileTxt = open(fileName+".txt","w+")
    fileTxt.writelines(strList)
    fileTxt.close()

if __name__ == "__main__":
    main()

