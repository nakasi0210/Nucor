from typing import Optional

from pydantic import BaseModel

class Calculation(BaseModel):
    input: int

class CalculationResponse(BaseModel):
    ans: int 
