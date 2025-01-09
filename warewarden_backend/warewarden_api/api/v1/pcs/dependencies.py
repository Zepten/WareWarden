from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Pc, db_helper

from crud import pcs


async def pc_by_id(
    pc_id: Annotated[UUID, Path(title="The ID (UUID) of the PC to get")],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Pc:
    pc = await pcs.get_pc(session=session, pc_id=pc_id)
    if not pc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"PC {pc_id} not found!",
        )
    return pc
