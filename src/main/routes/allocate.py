from http import HTTPStatus

from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.domain.models import OrderLine, allocate
from src.infra.database.config import Settings
from src.infra.database.repositories.repository import SqlAlchemyRepository
from src.main.models.order_line import OrderLine as OrderLineSchema

get_session = sessionmaker(bind=create_engine(Settings().database_url))
router = APIRouter()


@router.post("/allocate")
def allocate_endpoint(order_lines: list[OrderLineSchema]):
    session = get_session()
    batches = SqlAlchemyRepository(session).list()
    lines = [OrderLine(**order_line) for order_line in order_lines]

    batch_reference = allocate(lines, batches)

    session.commit()

    return HTTPStatus.CREATED, {"batchref:": batch_reference}
