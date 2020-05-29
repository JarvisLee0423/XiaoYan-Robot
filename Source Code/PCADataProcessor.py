import KeywordProcessor
from sklearn.decomposition import PCA

'''
    This part is used to do the PCA processing.
'''
def PCADataProcessor():
    # Do the PCA to compress the data.
    pcaTransform = PCA(n_components = 90)
    # Get the data which has been compressed.
    newData = pcaTransform.fit_transform(KeywordProcessor.DataTransformer()[0])
    # Return the new data which has already done the PCA.
    return newData, pcaTransform

# Test the function.
#print(PCADataProcessor()[0])
#print(PCADataProcessor()[1])