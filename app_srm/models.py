from datetime import date

from typing import Dict
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DateTime,  Date, Text, Boolean

from .paths import URl_DB

engine = create_engine(url=URl_DB)

Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


class BaseTable(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

    def to_json(self) -> Dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '{attr}'.format(attr={c.name: getattr(self, c.name) for c in self.__table__.columns})


class TypeContract(BaseTable):
    __tablename__ = 'types_contracts'

    type_contract = Column(String(100), unique=True, nullable=False)

    contract = relationship('Contract', backref="types_contracts")
    contract_delivery = relationship('ContractMZDelivery', backref="types_contract")
    contract_services = relationship('ContractMZServices', backref="types_contract")
    contract_sanatorium = relationship('ContractSanatorium', backref="types_contract")
    contract_44 = relationship('Contract44', backref="types_contract")


class Company(BaseTable):
    __tablename__ = 'companies'

    name = Column(String(150), nullable=False)
    full_name = Column(String(250), nullable=False)
    inn = Column(Integer, default=0) # unique=True
    smsp_flag = Column(Boolean, default=False)

    contract = relationship('Contract', backref="company")
    contract_delivery = relationship('ContractMZDelivery', backref="company")
    contract_services = relationship('ContractMZServices', backref="company")
    contract_sanatorium = relationship('ContractSanatorium', backref="company")
    contract_44 = relationship('Contract44', backref="company")


class Maneger(BaseTable):
    __tablename__ = 'managers'

    name = Column(String(150), unique=True, nullable=False)

    contract = relationship('Contract', backref="manager")
    contract_delivery = relationship('ContractMZDelivery', backref="manager")
    contract_services = relationship('ContractMZServices', backref="manager")
    contract_sanatorium = relationship('ContractSanatorium', backref="manager")
    contract_44 = relationship('Contract44', backref="manager")


class Contract(BaseTable):
    __tablename__ = 'contracts'

    number = Column(String(100), unique=True)
    incoming_number = Column(String(100))
    company_id = Column(Integer, ForeignKey('companies.id'))
    subject = Column(Text)
    comment = Column(Text)
    date_start = Column(Date)
    date_of_conclusion = Column(Date, default=date.today())
    date_end = Column(Date)
    summa = Column(Integer, default=0)
    manager_id = Column(Integer, ForeignKey('managers.id'))
    type_contract_id = Column(Integer, ForeignKey('types_contracts.id'))
    # search_subject = Column(Text)


class ContractMZDelivery(BaseTable):
    __tablename__ = 'contracts_mz_delivery'

    number = Column(String(100), unique=True, nullable=False)
    incoming_number = Column(String(100))
    company_id = Column(Integer, ForeignKey('companies.id'))
    subject = Column(Text)
    comment = Column(Text)
    date_start = Column(Date)
    date_of_conclusion = Column(Date, default=date.today())
    date_end = Column(Date)
    summa = Column(Integer, default=0)
    manager_id = Column(Integer, ForeignKey('managers.id'))
    type_contract_id = Column(Integer, ForeignKey('types_contracts.id'))
    # search_subject = Column(Text)


class ContractMZServices(BaseTable):
    __tablename__ = 'contracts_mz_services'

    number = Column(String(100), unique=True, nullable=False)
    incoming_number = Column(String(100))
    company_id = Column(Integer, ForeignKey('companies.id'))
    subject = Column(Text)
    comment = Column(Text)
    date_start = Column(Date)
    date_of_conclusion = Column(Date, default=date.today())
    date_end = Column(Date)
    summa = Column(Integer, default=0)
    manager_id = Column(Integer, ForeignKey('managers.id'))
    type_contract_id = Column(Integer, ForeignKey('types_contracts.id'))
    # search_subject = Column(Text)


class ContractSanatorium(BaseTable):
    __tablename__ = 'contracts_sanatorium'

    number = Column(String(100), unique=True, nullable=False)
    incoming_number = Column(String(100))
    company_id = Column(Integer, ForeignKey('companies.id'))
    subject = Column(Text)
    comment = Column(Text)
    date_start = Column(Date)
    date_of_conclusion = Column(Date, default=date.today())
    date_end = Column(Date)
    summa = Column(Integer, default=0)
    manager_id = Column(Integer, ForeignKey('managers.id'))
    type_contract_id = Column(Integer, ForeignKey('types_contracts.id'))
    # search_subject = Column(Text)


class Contract44(BaseTable):
    __tablename__ = 'contracts_44'

    number = Column(String(100), unique=True, nullable=False)
    incoming_number = Column(String(100))
    company_id = Column(Integer, ForeignKey('companies.id'))
    subject = Column(Text)
    comment = Column(Text)
    date_start = Column(Date)
    date_of_conclusion = Column(Date, default=date.today())
    date_end = Column(Date)
    summa = Column(Integer, default=0)
    manager_id = Column(Integer, ForeignKey('managers.id'))
    type_contract_id = Column(Integer, ForeignKey('types_contracts.id'))
    # search_subject = Column(Text)


class AdditionalContract(BaseTable):
    __tablename__ = 'additionals_contract'

    number = Column(String(150), unique=True, nullable=False)
    number_contract_id = Column(Integer, ForeignKey('contracts.id'))
    what_it_does = Column(Text)
    date_additional = Column(Date, default=date.today())
    new_date = Column(Date)
    summa = Column(Integer, default=0)
    comment = Column(Text)


class AdditionalMZDelivery(BaseTable):
    __tablename__ = 'additionals_mz_delivery'

    number = Column(String(150), unique=True, nullable=False)
    number_contract_id = Column(Integer, ForeignKey('contracts_mz_delivery.id'))
    what_it_does = Column(Text)
    date_additional = Column(Date, default=date.today())
    new_date = Column(Date)
    summa = Column(Integer, default=0)
    comment = Column(Text)


class AdditionalMZServices(BaseTable):
    __tablename__ = 'additionals_mz_services'

    number = Column(String(150), unique=True, nullable=False)
    number_contract_id = Column(Integer, ForeignKey('contracts_mz_services.id'))
    what_it_does = Column(Text)
    date_additional = Column(Date, default=date.today())
    new_date = Column(Date)
    summa = Column(Integer, default=0)
    comment = Column(Text)


class AdditionalSanatorium(BaseTable):
    __tablename__ = 'additionals_sanatorium'

    number = Column(String(150), unique=True, nullable=False)
    number_contract_id = Column(Integer, ForeignKey('contracts_sanatorium.id'))
    what_it_does = Column(Text)
    date_additional = Column(Date, default=date.today())
    new_date = Column(Date)
    summa = Column(Integer, default=0)
    comment = Column(Text)


class Additional44(BaseTable):
    __tablename__ = 'additionals_44'

    number = Column(String(150), unique=True, nullable=False)
    number_contract_id = Column(Integer, ForeignKey('contracts_44.id'))
    what_it_does = Column(Text)
    date_additional = Column(Date, default=date.today())
    new_date = Column(Date)
    summa = Column(Integer, default=0)
    comment = Column(Text)
