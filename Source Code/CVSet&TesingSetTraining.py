import xlrd
import SVM
import KeywordProcessor
import PCADataProcessor
import jieba
import jieba.analyse

'''
    This part is the global variables.
'''
# Get the name of the Excel file.
dataFile = "./问题扩展.xlsx"
# Store all the values into a list.
data = []
# Open the Excel file.
excelFile = xlrd.open_workbook(filename = dataFile)
# Get the sheet by index.
sheet = excelFile.sheet_by_index(0)

'''
    This part is used to test the Crocess Validation Set.
'''
def CVTestingTraining():
    # Get the users' operations.
    operation = int(input("Please choose an operation('1' for CV set, '2' for Testing set): "))
    # Get all the value of the column.
    for index in range(1,121):
        data.append(sheet.row(index)[operation].value)
    # Store the new data which has been cut.
    cutData = []
    # Store the prediction value.
    prediction = []
    # Get the classifier.
    classifier = SVM.DoSVM()
    # Get the vectoricer.
    vectorizer = KeywordProcessor.DataTransformer()[1]
    # Get the PCA transformer.
    pcaTransform = PCADataProcessor.PCADataProcessor()[1]
    # Use the jieba to split all the string.
    for index in range(0,120):
        # Split the string.
        seg_list = jieba.cut_for_search(data[index])
        # Restore the splited string into the data.
        cutData.append(" ".join(seg_list))
        # Get the transformed data.
        transformData = vectorizer.transform(cutData)
        # Get the data matrix.
        dataMatrix = transformData.toarray()
        # Do the PCA.
        newData = pcaTransform.transform(dataMatrix)
        # Get the prediction.
        prediction.append(classifier.predict(newData)[0])
        # Clear the list.
        cutData.clear()
    # Return the prediction.
    return prediction

# Test the function.
#print(CVTestingTraining())