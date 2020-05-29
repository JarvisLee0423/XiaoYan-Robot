import xlrd
import jieba
import jieba.analyse
from sklearn.feature_extraction.text import CountVectorizer

'''
    This part is the global variables.
'''
# Get the name of the Excel file.
dataFile = "./UIC小言机器人问题答案.xlsx"
# Store all the values into a list.
data = []
# Open the Excel file.
excelFile = xlrd.open_workbook(filename = dataFile)
# Get the sheet by index.
sheet = excelFile.sheet_by_index(0)
# Get all the value of the column.
for index in range(1,121):
    data.append(sheet.row(index)[0].value)

'''
    This part is used to get the keywords.
'''
def KeywordsProcessor():
    # Store the keyword into the list.
    keywordsList = []
    # Get the string which need to be used to select the keyword.
    dataString = ''.join(data)
    # Get the keywords.
    keywords = jieba.analyse.textrank(dataString, topK = 300, withWeight = True, allowPOS = ('n', 'nt', 'nz', 'v'))
    # Store the keywords.
    for item in keywords:
        keywordsList.append(item[0])
    # Modify the keywords.
    for item in keywordsList:
        if item == "学校":
            keywordsList.remove(item)
    # Return the keywords.
    return keywordsList

'''
    This part is used to transform the data.
'''
def DataTransformer():
    # Store the new data which has been cut.
    cutData = []
    # Use the jieba to split all the string.
    for index in range(0,120):
        # Split the string.
        seg_list = jieba.cut_for_search(data[index])
        # Restore the splited string into the data.
        cutData.append(" ".join(seg_list))
    # Get the vocabulary which is used to transform data.
    vectorizer = CountVectorizer(vocabulary = KeywordsProcessor())
    # Get the transformed data.
    transData = vectorizer.transform(cutData)
    # Get the data matrix.
    dataMatrix = transData.toarray()
    # Return the keyword.
    return dataMatrix, vectorizer

# Test the function.
#print(KeywordsProcessor())
#print(DataTransformer()[0])
#print(DataTransformer()[1])