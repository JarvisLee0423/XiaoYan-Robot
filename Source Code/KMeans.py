import xlrd
import xlwt
import PCADataProcessor
from sklearn.cluster import KMeans

'''
    This part is used to do the k-means algorithm to create the clusters.
'''
def DoKMeans():
    # Use the k-means algorithm to get the label of each data.
    labelPredict = KMeans(n_clusters = 14, random_state = 9).fit(PCADataProcessor.PCADataProcessor()[0])
    # Return the labels.
    return labelPredict.labels_

'''
    This part is used to restore all the data.
'''

def SaveTheClusters():
    # Get the name of the Excel file.
    dataFile = "./UIC小言机器人问题答案.xlsx"
    # Store all the values into a list.
    data = []
    # Store all the answer.
    answer = []
    # Open the Excel file.
    excelFile = xlrd.open_workbook(filename = dataFile)
    # Get the sheet by index.
    sheet = excelFile.sheet_by_index(0)
    # Get all the value of the column.
    for index in range(1,121):
        data.append(sheet.row(index)[0].value)
        answer.append(sheet.row(index)[1].value)
    # Create a new Excel file.
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # Add the work sheet into the new excel file.
    sheet1 = workbook.add_sheet("分簇问题")
    sheet2 = workbook.add_sheet("问题答案")
    # Save the new Excel file.
    workbook.save("./TheClusters.xls")
    # Used to store the data and answer which will be added into the new file.
    newFileData = []
    newFileAnswer = []
    # Get the labels.
    labels = DoKMeans()
    # Add the data into the Excel file.
    for i in range(0,14):
        # Get all the labels.
        for j in range(0,120):
            # Temporaily store all the corresponding cluster's data and answers. 
            if labels[j] == i:
                newFileData.append(data[j])
                newFileAnswer.append(answer[j])
        # Store all the data and answers into the correct column in the Excel file. 
        for k in range(0,len(newFileData)):
            sheet1.write(k, i, newFileData[k])
            sheet2.write(k, i, newFileAnswer[k])
        # Clear the lists which are used to temporarily store the data and answer. 
        newFileData.clear()
        newFileAnswer.clear()
    # Save the new Excel file.
    workbook.save("./TheClusters.xls")

# Test the function.
#print(DoKMeans())
#SaveTheClusters()