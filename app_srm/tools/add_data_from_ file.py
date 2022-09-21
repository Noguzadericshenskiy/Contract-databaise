import os
import datetime
import openpyxl


from typing import Tuple, List, Any

# from ..models import session, Company, Responsible, TypeContract, Contract
#     # ContractSanatorium, ContractMZServices, ContractMZDelivery, Contract44, \
#     # AdditionalContract, AdditionalSanatorium, AdditionalMZServices, AdditionalMZDelivery, Additional44

from app_srm.models import session, Company, TypeContract, Maneger, Contract


path_f = '../download/contract.xlsx'
range_val = (1, 309)
errors_list = []


def check_num_contract(num_contract: str) -> Tuple[str, bool]:
    """ Проверяет номер контракта (внутренний, внешний)"""
    pattern = 'КПК-'

    if pattern in num_contract:
        flag = True
    else:
        flag = False

    return num_contract, flag


def check_date_conclusion(date_up: datetime.datetime):
    """Проверяет, является ли типом дата"""
    if isinstance(date_up, datetime.datetime):
        flag = True
        date_out = date_up

    else:
        flag = False
        date_out = None

    return date_out, flag


def check_sum(num: Any) -> Tuple[int, bool]:
    flag = True
    clear_num = 0
    if isinstance(num, (float, int)):
        clear_num = int(num * 100)
    else:
        flag = False

    return clear_num, flag


def check_company(firm):
    company = session.query(Company).\
        filter(Company.name == firm).one_or_none()
    if company:
        return company.id
    else:
        new_company = Company(name=firm, full_name=firm)
        session.add(new_company)
        session.commit()
        id = new_company.id
        return id


def add_managers():
    manager = Maneger(name="НЛО")
    session.add(manager)


def add_types_contract():
    types_contract = [{"type_contract": "Продажа"},
                      {"type_contract": "Услуги"},
                      {"type_contract": "Сервис"}]
    session.bulk_insert_mappings(TypeContract, types_contract)
    session.commit()


def download_data_contract():
    add_managers()
    add_types_contract()

    book = openpyxl.open(path_f, read_only=True)
    sheet = book.active
    count = 1

    for row in range(range_val[0] + 1, range_val[1] + 1):
        num: Tuple[str, bool] = check_num_contract(str(sheet[row][0].value))
        firm = sheet[row][1].value
        company_id: int = check_company(firm)
        data_conclusion = check_date_conclusion(sheet[row][2].value)
        data_end = check_date_conclusion(sheet[row][3].value)
        summ: Tuple[int, bool] = check_sum(sheet[row][4].value)
        comment = sheet[row][6].value
        count += 1

        if data_conclusion[1] and data_end[1] and summ[1]:
            if num[1]:
                new_contract = Contract(number=num[0], company_id=company_id,
                                        date_of_conclusion=data_conclusion[0], date_end=data_end[0],
                                        date_start=data_conclusion[0],
                                        summa=summ[0], comment=comment)

            else:
                new_contract = Contract(incoming_number=num[0], company_id=company_id,
                                        date_of_conclusion=data_conclusion[0],
                                        date_end=data_end[0], date_start=data_conclusion[0],
                                        summa=summ[0], comment=comment)
            session.add(new_contract)
            session.commit()

        else:
            errors_list.append((num, firm, data_conclusion, data_end))


if __name__ == "__main__":
    start = datetime.datetime.now()
    download_data_contract()

    # r = download(path_f, range_val)
    # for i in errors_list:
    #     print(i)

    print(datetime.datetime.now() - start)
