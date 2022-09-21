import datetime
import os
import sqlite3

import openpyxl

from typing import Tuple, List, Any

from utils.constants import NAME_BD

from creqte_db import create_bd


path_f = '../app_srm/download/contract.xlsx'
range_val = (1, 309)
# 318
errors_list = []

add_contract_num_outgoing_sql = """
INSERT INTO `table_contract` (
    incoming_number_contract, company, start_date_contract, date_of_conclusion_contract, end_date_contract, sum_contract, 
    comment, responsible, type_contract)
VALUES (?,?,?,?,?,?,?,?,?);
"""

add_contract_mum_incoming_sql = """
INSERT INTO `table_contract` (
    number_contract, company, start_date_contract, date_of_conclusion_contract, end_date_contract, sum_contract,
    comment, responsible, type_contract)
VALUES (?,?,?,?,?,?,?,?,?);
"""

add_firm_sql = """
INSERT INTO table_company (name_company, full_name_company, inn_company, smsp_flag_company, search)
VALUES (?, ?, ?, ?, ?);
"""

get_firm = """
SELECT id_company 
FROM table_company
WHERE name_company = ?
;
"""

def check_num_contract(num_contract: str) -> Tuple[str, bool]:
    """ Проверяет номер контракта (внутренний, внешний)"""
    pattern = 'КПК-'

    if pattern in num_contract:
        flag = True
    else:
        flag = False

    return num_contract, flag


def check_date_conclusion(date_up: datetime.datetime) -> Tuple[str, bool]:
    """Проверяет, является ли типом дата"""

    if isinstance(date_up, datetime.datetime):
        flag = True
        date_out = date_up.strftime('%Y-%m-%d')
    else:
        flag = False
        date_out = ''

    return date_out, flag


def check_sum(num: Any) -> Tuple[int, bool]:
    flag = True
    clear_num = 0
    if isinstance(num, (float, int)):
        clear_num = int(num * 100)
    else:
        flag = False

    return clear_num, flag


def check_firm(c, firm):
    c.execute("""
    SELECT COUNT(*) 
    FROM table_company
    WHERE name_company = ? 
    ;""", (firm,))
    val = c.fetchone()
    # print(val[0])
    if val[0] != 0:
        return False
    else:
        return True


def download(path: str, range_tab: Tuple[int, int]) -> List[str]:

    book = openpyxl.open(path, read_only=True)
    sheet = book.active
    path_bd = os.path.join('../', NAME_BD)
    count = 1

    with sqlite3.connect(path_bd) as conn:
        cur = conn.cursor()
        cur.executescript(create_bd.drop_bd)
        cur.executescript(create_bd.create_bd)

        cur.execute('INSERT INTO table_responsible (name_responsible) VALUES (?) ;', ("НЛО",))
        cur.executemany('INSERT INTO table_type_contract (type_contract) VALUES (?);',
                        [("Продажа",), ("Услуги",), ("Сервис",)])

        for row in range(range_tab[0]+1, range_tab[1]+1):
            firm = sheet[row][1].value
            if firm:
                search = firm.lower()
            if check_firm(cur, firm):
                cur.execute(add_firm_sql, (firm, firm, None, None, search))
            # print(row)

        for row in range(range_tab[0]+1, range_tab[1]+1):
            num_contract: Tuple[str, bool] = check_num_contract(str(sheet[row][0].value))
            firm = sheet[row][1].value
            cur.execute(get_firm, (firm,))
            company = cur.fetchone()[0]
            data_conclusion = check_date_conclusion(sheet[row][2].value)
            data_end = check_date_conclusion(sheet[row][3].value)
            summ: Tuple[int, bool] = check_sum(sheet[row][4].value)
            comment = sheet[row][6].value
            print(count, num_contract)

            count += 1
            if not data_conclusion[1]:
                errors_list.append((num_contract, company, data_conclusion, data_end))

            else:
                if num_contract[1]:
                    cur.execute(add_contract_mum_incoming_sql, (
                        num_contract[0],
                        company,
                        data_conclusion[0],
                        data_conclusion[0],
                        data_end[0],
                        summ[0],
                        comment,
                        1,
                        1
                    ))

                else:
                    cur.execute(add_contract_num_outgoing_sql, (
                        num_contract[0],
                        company,
                        data_conclusion[0],
                        data_conclusion[0],
                        data_end[0],
                        summ[0],
                        comment,
                        1,
                        1
                    ))

        return errors_list


if __name__ == "__main__":
    start = datetime.datetime.now()

    r = download(path_f, range_val)
    for i in errors_list:
        print(i)

    print(datetime.datetime.now() - start)
