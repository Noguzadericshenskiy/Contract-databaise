from typing import Tuple

from utils.objects import Additional, Contract, Company, TypeContract, Responsible
from modules import get_all_responsible_bd, get_all_type_contract_bd


def tuple_additional(additional: Additional) -> Tuple:
    if additional.sum_additional:
        summ = additional.sum_additional / 100

    else:
        summ = 0
    param_additional = (
        additional.number_additional,
        additional.what_it_does,
        additional.date_additional,
        additional.new_date,
        summ,
        additional.comment,
        additional.id_additional,
        additional.num_contract,
    )

    return param_additional


def tuple_contract(contract: Contract) -> Tuple:
    summ = contract.sum_contract / 100

    # нужно добавить форматтер дат для выхода в формате dd-mm-yyyy
    date = contract.date_of_conclusion_contract

    param_contract = (
                      contract.num_contract,
                      contract.incoming_number_contract,
                      contract.company,
                      contract.start_date_contract,
                      contract.date_of_conclusion_contract,
                      contract.end_date_contract,
                      summ,
                      contract.subject_contract,
                      contract.type_contract,
                      contract.responsible,
                      contract.comment,
                      contract.id_contract
                      )

    return param_contract


def to_fixed(num, digits=0):
    return f"{num:.{digits}f}"


def tuple_responsible():
    """Подготавливает общий список ответственных для вывода в виджеты"""
    peoples = []

    for people in get_all_responsible_bd():
        peoples.append(people.name_responsible)

    return tuple(peoples)


# нужно переделать чтоб импортировать из module
def types_contract():

    return tuple(get_all_type_contract_bd())



