from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.models import Pc
from crud import pcs
from .dependencies import pc_by_id
from .schemas import PcRead, PcCreate, PcUpdate, PcUpdatePartial

router = APIRouter(tags=["Personal Computers (PCs)"])


@router.get("/", response_model=list[PcRead])
async def get_pcs(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await pcs.get_pcs(session=session)


@router.post("/", response_model=PcRead, status_code=status.HTTP_201_CREATED)
async def create_pc(
    pc_create: PcCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await pcs.create_pc(
        session=session,
        pc_in=pc_create,
    )


@router.get("/{pc_id}/", response_model=PcRead)
async def get_pc(
    pc: Pc = Depends(pc_by_id),
):
    return pc


@router.put("/{pc_id}/", response_model=PcRead)
async def update_pc(
    pc_update: PcUpdate,
    pc: Pc = Depends(pc_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await pcs.update_pc(
        session=session,
        pc=pc,
        pc_update=pc_update,
    )


@router.patch("/{pc_id}/", response_model=PcRead)
async def update_pc_partial(
    pc_update: PcUpdatePartial,
    pc: Pc = Depends(pc_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await pcs.update_pc(
        session=session,
        pc=pc,
        pc_update=pc_update,
        partial=True,
    )


@router.delete("/{pc_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pc(
    pc: Pc = Depends(pc_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await pcs.delete_pc(session=session, pc=pc)
    return None
