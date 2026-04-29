from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    user_id: int
    total: float = Field(gt=0)


class OrderOut(BaseModel):
    id: int
    user_id: int
    total: float

    class Config:
        from_attributes = True