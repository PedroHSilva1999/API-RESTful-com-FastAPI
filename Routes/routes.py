from fastapi import APIRouter   
from fastapi import HTTPException

router = APIRouter  ()

@router.get("/api/v1/user")
async def get_user():
    return "Cursos"