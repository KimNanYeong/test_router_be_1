from fastapi import APIRouter, HTTPException, Query
from app.service.city import get_city
from app.schemas.city import Cityinfo  

router = APIRouter()
@router.get("/city", response_model=Cityinfo)
async def read_city(id: int = Query(..., description="도시 ID")):
    """
    특정 도시의 이름을 조회합니다.  
    :param id: 도시 ID
    :return: 도시 정보
    """
    city = get_city(id)
    # print(Cityinfo)
    if city == 0:
        raise HTTPException(status_code=404, detail="City not found")
        # print(city_name)
    return Cityinfo(city_id=id, city=city)