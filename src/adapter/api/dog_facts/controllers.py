from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_one_dog_fact():
    return [{"fact": "hey"}, {"fact": "ho"}]
