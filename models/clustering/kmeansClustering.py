import pandas as pd
from sklearn.cluster import KMeans


class KMeansClustering:
    def __init__(self, file):
        self.df = pd.read_csv(file)
        self.KMModel = None

    def printDataframe(self):
        print(self.df.head)

    def clusterDataFrame(self, nClusters):
        kmeans = KMeans(n_clusters=nClusters,
                        init='k-means++', random_state=42)
        kmeans.fit(self.df)
        self.KMModel = kmeans

    def getClusterCenters(self):
        return self.KMModel.cluster_centers_.tolist()
