from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
 

import api.schemas.row as row_schema
router = APIRouter()

@router.post("/row",response_model=row_schema.CalculationResponse)
async def calculation(calc_row: row_schema.Calculation):
    return row_schema.CalculationResponse(ans=calc_row.input*calc_row.input)