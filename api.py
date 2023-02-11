from fastapi import APIRouter
from controller import controller

router = APIRouter()

router.include_router(controller.router)
