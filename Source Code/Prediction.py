import xlrd
import difflib
import SVM
import KeywordProcessor
import PCADataProcessor
import jieba
import jieba.analyse
import wx

'''
    This part is used to open the cluster file.
'''
# Get the cluster file.
openFile = "./TheClusters.xls"
# Open the cluster file.
clusterFile = xlrd.open_workbook(filename = openFile)
# Get the each sheet by index.
sheetForQuestion = clusterFile.sheet_by_index(0)
sheetForAnswer = clusterFile.sheet_by_index(1)

'''
    This part is used to do create the GUI.
'''
class RobotFrame(wx.Frame):
    # Create the constructor for the class.
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title = "UIC问答小言机器人", size = (400, 300))
        # Create the panel.
        panel = wx.Panel(self)
        # Create the text input table.
        self.title = wx.StaticText(panel, label = "小言为您解答疑惑", pos = (140, 20))
        self.label_user = wx.StaticText(panel, label = "提问：", pos = (50, 50))
        self.text_user = wx.TextCtrl(panel, pos = (100, 50), size = (235, 25), style = wx.TE_LEFT)
        # Set the button and bind to some event.
        self.bt_confirm = wx.Button(panel, label = '搜索', pos = (105, 130))
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.GetAnswer)
        self.bt_cancel = wx.Button(panel, label = '清空', pos = (195, 130))
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.ClearInput)
    
    # To get the answer of the users' question.
    def GetAnswer(self, event):
        # The list used to get all the ratio of string similarity.
        ratio = []
        # Get the classifier.
        classifier = SVM.DoSVM()
        # Get the vectoricer.
        vectorizer = KeywordProcessor.DataTransformer()[1]
        # Get the PCA transformer.
        pcaTransform = PCADataProcessor.PCADataProcessor()[1]
        # Get the users' question.
        testData = self.text_user.GetValue()
        # Used to store the users' question.
        example = []
        # Split the users' question.
        seg_list = jieba.cut_for_search(testData)
        # Store the users's question.
        example.append(" ".join(seg_list))
        # Transformed users' question into the matrix.
        transDataExample = vectorizer.transform(example)
        # Store the new matrix.
        dataMatrixExample = transDataExample.toarray()
        # Compress the matrix.
        newExample = pcaTransform.transform(dataMatrixExample)
        # Get the prediction value.
        result = classifier.predict(newExample)
        # Get the question and the answer from the corresponding cluster.
        Questions = sheetForQuestion.col_values(result[0])
        Answers = sheetForAnswer.col_values(result[0])
        # Do the string similarity to get the answer.
        for item in Questions:
            ratio.append(difflib.SequenceMatcher(None, testData, item).quick_ratio())
        # Ouput the answer.
        wx.MessageBox(Answers[ratio.index(max(ratio))])
    
    # Clear all the input.
    def ClearInput(self, event):
        # Clear the input text box.
        self.text_user.SetValue("")

# Call the main function.
if __name__ == "__main__":
    # Initialize the GUI.
    app = wx.App()
    # Creat a frame instance.
    frame = RobotFrame(parent = None, id = -1)
    # Show the frame.
    frame.Show()
    # Call the main loop.
    app.MainLoop()