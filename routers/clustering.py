from fastapi import APIRouter, File, UploadFile

from models.clustering.kmeansClustering import KMeansClustering


router = APIRouter(prefix='/clustering')


@router.post('/kmeans')
async def kmeans(nClusters: int, dataset: UploadFile = File(...)):
    ob = KMeansClustering(dataset.file)
    ob.clusterDataFrame(nClusters)
    return ob.getClusterCenters()
