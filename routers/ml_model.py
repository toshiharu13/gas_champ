from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter(prefix='/gas_mon', tags=['monotoring'])


@router.get('/default')
async def default_request():
    return {'message': 'Семь секунд, полет нормальный!'}