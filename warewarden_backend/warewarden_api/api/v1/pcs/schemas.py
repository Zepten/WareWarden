from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PcBase(BaseModel):
    name: str | None
    description: str | None


class PcCreate(PcBase):
    pass


class PcUpdate(PcCreate):
    pass


class PcUpdatePartial(PcCreate):
    name: str | None = None
    description: str | None = None


class PcRead(PcBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: UUID
    created_at: datetime
    modified_at: datetime
