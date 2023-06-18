from fastapi import APIRouter, File, UploadFile


router = APIRouter(prefix='/frequent_pattern_mining')


@router.post('/apriori_algorithm')
async def aprioriAlgorithm(dataset: UploadFile = File(...)):
    return {"Hit": "AprioriAlgorithm"}
