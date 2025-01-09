from typing import Sequence
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Pc
from api.v1.pcs.schemas import PcCreate, PcUpdate, PcUpdatePartial


async def get_pcs(session: AsyncSession) -> Sequence[Pc]:
    stmt = select(Pc).order_by(Pc.created_at.desc())
    result = await session.scalars(stmt)
    return result.all()


async def get_pc(session: AsyncSession, pc_id: UUID) -> Pc | None:
    return await session.get(Pc, pc_id)


async def create_pc(session: AsyncSession, pc_in: PcCreate) -> Pc:
    pc = Pc(**pc_in.model_dump())
    session.add(pc)
    await session.commit()
    return pc


async def update_pc(
    session: AsyncSession,
    pc: Pc,
    pc_update: PcUpdate | PcUpdatePartial,
    partial: bool = False,
) -> Pc:
    for key, value in pc_update.model_dump(exclude_unset=partial).items():
        setattr(pc, key, value)
    await session.commit()
    return pc


async def delete_pc(session: AsyncSession, pc: Pc) -> None:
    await session.delete(pc)
    await session.commit()
