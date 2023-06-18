from fastapi import APIRouter


router = APIRouter(prefix='/clustering')


@router.post('/kmeans')
async def kmeans():
    return {'Hit': 'K Means Clustering'}
