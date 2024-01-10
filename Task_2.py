import pandas as pd

def countVowels(string):
    count = 0
    
    for char in str(string):
        if ((char.lower() == 'a') or (char.lower() == 'e') or (char.lower() == 'i') or (char.lower() == 'o') or (char.lower() == 'u')):
            count +=1
    
    return count

def addVowelCountColumn(filePath, column, outputFilePath):
    moviesDataframe = pd.read_csv(filePath)
    moviesDataframe['vowels'] = moviesDataframe[column].apply(countVowels)
    print(moviesDataframe)
    moviesDataframe.to_csv(outputFilePath, index=False)


#csv file path
csvFilePath = 'data/titles.csv'
outputFilePath = 'data/output.csv'

#Specify the column name in the csv file for which count of vowels is required
addVowelCountColumn(csvFilePath, 'title', outputFilePath)



#