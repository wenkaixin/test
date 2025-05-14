from pydantic import BaseModel, HttpUrl

class URLBase(BaseModel):
    target_url: HttpUrl

class URL(URLBase):
    is_active: bool
    clicks: int
    short_url: str

class URLInfo(URL):
    url_id: str 