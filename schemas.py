from pydantic import BaseModel


class OutputSchema(BaseModel):
    msg: str