import uuid

from sqlalchemy import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column


class IdUuidPkMixin:
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
