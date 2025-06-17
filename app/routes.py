from fastapi import APIRouter, HTTPException
from .models import Operation

router = APIRouter()

@router.post("/add")
def add(data: Operation):
    return {"result": data.a + data.b}

@router.post("/subtract")
def subtract(data: Operation):
    return {"result": data.a - data.b}

@router.post("/multiply")
def multiply(data: Operation):
    return {"result": data.a * data.b}

@router.post("/divide")
def divide(data: Operation):
    if data.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"result": data.a / data.b}
