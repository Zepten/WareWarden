from sqlalchemy.orm import Mapped

from .base import Base
from .mixins.id_uuid_pk import IdUuidPkMixin
from .mixins.timestamps import CreatedAtMixin, ModifiedAtMixin


class Pc(
    IdUuidPkMixin,
    CreatedAtMixin,
    ModifiedAtMixin,
    Base,
):
    name: Mapped[str]
    description: Mapped[str]
