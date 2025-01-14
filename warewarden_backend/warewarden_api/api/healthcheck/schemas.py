from pydantic import BaseModel

class Healthcheck(BaseModel):
    status: str = "OK"
