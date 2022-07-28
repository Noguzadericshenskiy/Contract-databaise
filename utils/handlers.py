import logging
import datetime

from typing import List, Tuple, Any

from .objects import Company, TypeContract, Responsible, Contract, Additional


log = logging.getLogger("handlers")
logging.basicConfig(level=logging.INFO)


def converter_list_additional(data: Tuple[str, Any, str, Any, Any, Any, int, int]) -> List[Additional]:
    """Конвертирует полученные из БД кортежи в объекты класса"""
    list_obj = []

    for additional in data:
        a = Additional()
        a.id_additional = additional[0]
        a.number_additional = additional[1]
        a.num_contract = additional[2]
        a.what_it_does = additional[3]

        a.date_additional = additional[4]

        a.new_date = additional[5]
        a.sum_additional = additional[6]
        a.comment = additional[7]

        list_obj.append(a)

    return list_obj


def converter_list_contract(data: List[Tuple]) -> List[Contract]:
    """Конвертирует полученные из БД кортежи в объекты класса """
    list_obj = []

    for contract in data:

        a = Contract()

        a.id_contract = contract[0]
        a.num_contract = contract[1]
        a.incoming_number_contract = contract[2]
        a.company = contract[3]
        a.subject_contract = contract[4]
        a.comment = contract[5]
        a.start_date_contract = contract[6]
        a.date_of_conclusion_contract = contract[7]
        a.end_date_contract = contract[8]
        a.sum_contract = contract[9]
        a.responsible = contract[10]
        a.type_contract = contract[11]

        list_obj.append(a)

    return list_obj


def converter_list_type_contract(data) -> List[TypeContract]:
    """Конвертирует полученные из БД кортежи в объекты класса """
    list_obj = []

    for variety in data:
        a = TypeContract()
        a.id_type = variety[0]
        a.type_contract = variety[1]
        list_obj.append(a)

    return list_obj


def converter_list_responsible(data) -> List[Responsible]:
    """Конвертирует полученные из БД кортежи в объекты класса """
    list_obj = []

    for human in data:
        a = Responsible()
        a.name_responsible = human[1]
        a.id_responsible = human[0]
        list_obj.append(a)

    return list_obj


def converter_list_of_companies(data: List[Tuple]) -> List[Company]:
    """Конвертирует полученные из БД кортежи в объекты класса """
    list_obj = []

    for firm in data:
        obj = Company()

        obj.id_company = firm[0]
        obj.name_company = firm[1]
        obj.full_name_company = firm[2]
        obj.inn_company = firm[3]
        obj.smsp_flag_company = firm[4]

        list_obj.append(obj)

    return list_obj



