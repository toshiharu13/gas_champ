from fastapi import APIRouter, Depends, status, HTTPException

router = APIRouter(prefix='/category', tags=['category'])