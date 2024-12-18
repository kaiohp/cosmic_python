from sqlalchemy import Column, Integer, String, Table

from src.infra.database.metadata import metadata

order_lines = Table(
    'order_lines',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('quantity', Integer, nullable=False),
    Column('order_reference', String(255)),
)
