import PCADataProcessor
import KMeans
from sklearn import svm

'''
    This part is used to do the SVM algorithm to create the classifier.
'''
def DoSVM():
    # Set the SVM model.
    classifier = svm.SVC(kernel = 'linear', C = 2.0)
    # Use the orignal data and the labels to train the SVM
    classifier.fit(PCADataProcessor.PCADataProcessor()[0], KMeans.DoKMeans())
    # Return the classifier.
    return classifier

# Test the function.
#print(DoSVM())