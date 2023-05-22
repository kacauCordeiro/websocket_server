from pydantic import BaseModel, validator, Field
from api.utils.schema_tools import never_empty


class MessagePydantic(BaseModel):
    message:  dict = Field(title="Telefone do destinatário")

    @validator("message", allow_reuse=True)
    def _v_message(cls, v: dict) -> dict:
        return never_empty(v, "message")