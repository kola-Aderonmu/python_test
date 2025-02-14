from pydantic import BaseModel, HttpUrl
from datetime import datetime


class URLBase(BaseModel):
    target_url: HttpUrl


class URL(URLBase):
    shortt_url: str
    created_at: datetime


    class Config:
        from_attributes = True

class URLCreate(URLBase):
    pass        

    