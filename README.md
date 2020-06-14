#Alembic Test

[documentation link](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## First install alembic
`pip install alembic`

## Then init alembic environment
`alembic init almebic`

## 1. Add revision
`alembic revision --autogenerate -m "Added price column"`

## 2. Migrate
`alembic upgrade head`

