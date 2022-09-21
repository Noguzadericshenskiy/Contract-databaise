import datetime
import logging

from typing import List

from utils.connect import Database
from creqte_db.create_bd import drop_bd, create_bd
from utils.objects import Responsible, Company, Additional, Contract, TypeContract
from utils.handlers import converter_list_of_companies, converter_list_responsible,\
    converter_list_type_contract, converter_list_contract, converter_list_additional

log = logging.getLogger("modules")
logging.basicConfig(level=logging.INFO)


conn = Database('../bd.bd')


def add_additional_db(table: str, additional: Additional) -> None:
    """
    Записывает в базу новое дополнительное соглашение
    :param table: название таблицы куда идет запись
    :param additional: обект класса допники
    """
    request_sql = ''
    parametrs = (
        additional.number_additional,
        additional.num_contract,
        additional.what_it_does,
        additional.date_additional,
        additional.new_date,
        additional.sum_additional,
        additional.comment
    )

    if table == 'table_additional_contract':
        request_sql = """INSERT INTO table_additional_contract (
            number_additional, number_contract, what_it_does, date_additional, new_date, sum_additional, comment
            ) VALUES (?,?,?,?,?,?,?)  ;"""

    if table == 'table_additional_mz_delivery':
        request_sql = """INSERT INTO table_additional_mz_delivery (
            number_additional, number_contract, what_it_does, date_additional, new_date, sum_additional, comment
            ) VALUES (?,?,?,?,?,?,?)  ;"""

    if table == 'table_additional_mz_services':
        request_sql = """INSERT INTO table_additional_mz_services (
            number_additional, number_contract, what_it_does, date_additional, new_date, sum_additional, comment
            ) VALUES (?,?,?,?,?,?,?)  ;"""

    conn.execute(request_sql, parametrs)
    conn.commit()


def get_all_additional_db(table: str) -> List[Additional]:
    """
    Выводит список всех допников к договору согласно таблицы
    :param table: таблица поиска
    :return:
    """
    request_sql = ''
    if table == 'table_additional_contract':
        request_sql = "SELECT * FROM table_additional_contract;"

    if table == "table_additional_mz_delivery":
        request_sql = "SELECT * FROM table_additional_mz_delivery;"

    if table == 'table_additional_mz_services':
        request_sql = "SELECT * FROM table_additional_mz_services;"

    if table == 'table_additional_sanatorium':
        request_sql = "SELECT * FROM table_additional_sanatorium;"

    if table == 'table_additional_44':
        request_sql = "SELECT * FROM table_additional_44;"

    data = conn.query(request_sql)
    additional = converter_list_additional(data)

    return additional


def get_additional_db(table: str, num_contract: int) -> List[Additional]:
    """"""
    request_sql = ''
    if table == 'table_additional_contract':
        request_sql = "SELECT * FROM table_additional_contract WHERE number_contract = ?;"

    if table == "table_additional_mz_delivery":
        request_sql = "SELECT * FROM table_additional_mz_delivery WHERE number_contract = ?;"

    if table == 'table_additional_mz_services':
        request_sql = "SELECT * FROM table_additional_mz_services WHERE number_contract = ?;"

    if table == 'table_additional_sanatorium':
        request_sql = "SELECT * FROM table_additional_sanatorium WHERE number_contract = ?;"

    if table == 'table_additional_44':
        request_sql = "SELECT * FROM table_additional_44 WHERE number_contract = ?;"

    data = conn.query(request_sql, (num_contract,))
    additional = converter_list_additional(data)
    return additional


def update_additional_bd(table: str, additional: Additional):
    request_sql = ''
    parameters = (
        additional.number_additional, additional.num_contract, additional.what_it_does, additional.date_additional,
        additional.new_date, additional.sum_additional, additional.comment, additional.id_additional
                 )

    if table == 'table_additional_contract':
        request_sql = """UPDATE table_additional_contract 
        SET number_additional = ?, number_contract = ?, what_it_does = ?, date_additional = ?, new_date = ?,
        sum_additional = ?, comment = ?  
        WHERE id_additional = ?;"""

    if table == "table_additional_mz_delivery":
        request_sql = """UPDATE table_additional_mz_delivery 
        SET number_additional = ?, number_contract = ?, what_it_does = ?, date_additional = ?, new_date = ?,
        sum_additional = ?, comment = ?  
        WHERE id_additional = ?;"""

    if table == 'table_additional_mz_services':
        request_sql = """UPDATE table_additional_mz_services 
        SET number_additional = ?, number_contract = ?, what_it_does = ?, date_additional = ?, new_date = ?,
        sum_additional = ?, comment = ?  
        WHERE id_additional = ?;"""

    if table == 'table_additional_sanatorium':
        request_sql = """UPDATE table_additional_sanatorium 
        SET number_additional = ?, number_contract = ?, what_it_does = ?, date_additional = ?, new_date = ?,
        sum_additional = ?, comment = ?  
        WHERE id_additional = ?;"""

    if table == 'table_additional_44':
        request_sql = """UPDATE table_additional_44 
        SET number_additional = ?, number_contract = ?, what_it_does = ?, date_additional = ?, new_date = ?,
        sum_additional = ?, comment = ?  
        WHERE id_additional = ?;"""

    conn.execute(request_sql, parameters)
    conn.commit()


def add_company_db(name: str, full_name: str, inn: int, smsp: bool = False) -> None:
    """Добавление контрагента
     :param name: название контрагента
     :param   full_name: полное наименование контрагента
     :param   inn: ИНН организации
     :param   smsp: Принадлежность к СМСП(СМП)
    """
    search_text = (name + ' ' + full_name).lower()

    conn.execute("INSERT INTO `table_company` "
                 "(name_company, full_name_company, inn_company, smsp_flag_company, search)"
                 " VALUES (?, ?, ?, ?, ?);", (name, full_name, inn, smsp, search_text))
    conn.commit()

def check_company_db(inn: int, name: str) -> bool:
    """Проверка на есть ли подобная компания в БД"""
    ans = data = conn.query("""SELECT COUNT(*) FROM table_company 
                                WHERE inn_company = ? or name_company = ?;""",
                            (inn, name))
    if ans[0][0] == 0:
        return True
    else:
        return False


def get_all_company_bd() -> List[Company]:
    """выбрать всех контрагентов"""
    data = conn.query('SELECT * FROM `table_company`;')

    firms = converter_list_of_companies(data)

    return firms

# Пока неиспользую, необходимо проверить
def get_company_bd(id: int = None, inn: int = None, name: str = None, smsp: bool = None) -> List[Company]:
    """
    выбрать контрагентов по условию
    Поле search составное из названия и полного названия в нижних регистрах используем только для поиска
        :param id: ID
        :param inn:  ИНН контрагента
        :param name:  строка для поиска по полю search
        :param smsp:  флаг принадлежности к СМСП(МСП)
        :return -> список объектов класса Company
    """

    if id:
        data = conn.query("""SELECT * FROM table_company WHERE id_company = ?;""", (id,))

    elif inn:
        data = conn.query("""SELECT * FROM table_company WHERE inn_company = ?;""", (inn,))

    elif smsp:
        data = conn.query("""SELECT * FROM table_company WHERE smsp_flag_company = ?;""", (smsp,))

    else:
        if name:
            data = conn.query("""SELECT * FROM `table_company` 
            WHERE search LIKE ?;""", ('%'+name+'%',))

        else:
            data = conn.query("""SELECT * FROM `table_company`;""")

    firms = converter_list_of_companies(data)

    return firms


def update_company_bd(id: int, name: str = None, full_name: str = None, smsp: bool = False) -> None:
    """
    Обновляет данные о компании
        :param id: id
        :param name: название контрагента
        :param full_name: полное названи
        :param smsp: принадлежность к СМСП(СМП)
    """
    search_text = (name + ' ' + full_name).lower()

    conn.execute("""
        UPDATE table_company 
        SET name_company = ?, full_name_company = ?, smsp_flag_company = ?, search = ? 
        WHERE id_company == ?;""",
                 (name, full_name, smsp, search_text, id))
    conn.commit()


def add_contract_bd(table: str, contract: Contract) -> None:
    """
    Создаем новый договор в соответствии с таблицами договоров.
     Передавать название таблицы обязательно!
        :param table название таблицы которой принадлежит договор
        :param contract объект с параметрами договора
    """
    request_sql = ''
    search_text = str(contract.subject_contract).lower()
    parametrs = (
        contract.num_contract,
        contract.incoming_number_contract,
        contract.company,
        contract.subject_contract,
        contract.comment,
        contract.start_date_contract,
        contract.date_of_conclusion_contract,
        contract.end_date_contract,
        contract.sum_contract,
        contract.responsible,
        contract.type_contract,
        search_text
                )

    if table == 'table_contract':
        request_sql = """INSERT INTO table_contract (
        number_contract, incoming_number_contract, company, subject_contract, comment, start_date_contract, 
        date_of_conclusion_contract, end_date_contract, sum_contract, responsible, type_contract, search_subject
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""

    if table == 'table_contract_mz_delivery':
        request_sql = """INSERT INTO table_contract_mz_delivery (
        number_contract, incoming_number_contract, company, subject_contract, comment, start_date_contract, 
        date_of_conclusion_contract, end_date_contract, sum_contract, responsible, type_contract, search_subject 
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""

    if table == 'table_contract_mz_services':
        request_sql = """INSERT INTO table_contract_mz_services (
        number_contract, incoming_number_contract, company, subject_contract, comment, start_date_contract, 
        date_of_conclusion_contract, end_date_contract, sum_contract, responsible, type_contract, search_subject 
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""

    conn.execute(request_sql, parametrs)
    conn.commit()


def get_all_contract_db() -> List[Contract]:
    """"""
    data = conn.query('SELECT * FROM table_contract ORDER BY date_of_conclusion_contract, number_contract;')

    contracts = converter_list_contract(data)
    # log.info(f"contracts {contracts}")
    return contracts


def get_contract_bd(param):
    table = param[0]
    date_in = param[1]
    date_out = param[2]
    number = param[3]
    responsible = param[4]
    context = param[5]

    param_req = []
    log.info(f"param {param}")

    req = "SELECT id_contract, number_contract, incoming_number_contract, name_company, subject_contract, " \
          "comment, start_date_contract, date_of_conclusion_contract, end_date_contract, sum_contract, " \
          "name_responsible, table_type_contract.type_contract " \
          "FROM {tab} " \
          "INNER JOIN table_responsible on {tab}.responsible = table_responsible.id_responsible " \
          "INNER JOIN table_type_contract on {tab}.type_contract = table_type_contract.id_type " \
          "INNER JOIN table_company on {tab}.company = table_company.id_company " \
          "WHERE date_of_conclusion_contract BETWEEN ? AND ? ".format(tab=table)

    param_req.append(date_in)
    param_req.append(date_out)
    # if date_in and date_out:
    #     param_req.append(date_in)
    #     param_req.append(date_out)
    # elif date_in and not date_out:
    #     param_req.append(date_in)
    #     param_req.append(datetime.date.today())
    # elif not date_in and date_out:
    #     param_req.append('1990-01-01')
    #     param_req.append(date_out)
    # else:
    #     param_req.append('1990-01-01')
    #     param_req.append(datetime.date.today())

    if number:
        # log.info(f'number True')
        req += 'AND (incoming_number_contract  LIKE ? OR number_contract LIKE ?) '
        param_req.append('%' + number + '%')
        param_req.append('%' + number + '%')

    if responsible:
        # log.info(f'responsible True')
        req += 'AND (name_responsible = ?)'
        param_req.append(responsible)

    if context:
        log.info(f'context True')


    req += 'ORDER BY date_of_conclusion_contract, number_contract;'
    par = tuple(param_req)
    # log.info(f'req {req} \n{par}')
    datas = conn.query(req, par)
    contracts = converter_list_contract(datas)
    log.info(f"contracts {datas}")
    # if date_in and date_out:
    #     # log.info(f'IF1 {date_in}===={date_out}')
    #     dates = (date_in, date_out)
    #     data = conn.query(request, dates)
    #
    # elif date_in and not date_out:
    #     # log.info(f'IF2 {date_in}===={date_out}')
    #     date_new = datetime.date.today()
    #     dates = (date_in, date_new)
    #     data = conn.query(request, dates)
    #
    # elif not date_in and date_out:
    #     # log.info(f'IF3 {date_in}===={date_out}')
    #     date_new = '1990-01-01'
    #     dates = (date_new, date_out)
    #     data = conn.query(request, dates)
    #
    # else:
    #     # log.info(f'ELSE {date_in}===={date_out}')
    #     contracts = get_all_contract_db()
    #
    # contracts = converter_list_contract(data)
    # log.info(f"list_contract {data}")
    # log.info(f"list_contract {contracts}")
    return contracts


def update_contract_bd(table: str, contract: Contract):
    """"""
    request_sql = ''
    search_text = str(contract.subject_contract).lower()
    parameters = (contract.num_contract,
                  contract.incoming_number_contract,
                  contract.company,
                  contract.subject_contract,
                  contract.comment,
                  contract.start_date_contract,
                  contract.date_of_conclusion_contract,
                  contract.end_date_contract,
                  contract.sum_contract,
                  contract.responsible,
                  contract.type_contract,
                  search_text,
                  contract.id_contract
                  )

    if table == 'table_contract':
        request_sql = """UPDATE `table_contract` 
            SET number_contract = ?, incoming_number_contract = ?, company = ?, subject_contract = ?, comment = ?,
            start_date_contract = ?, date_of_conclusion_contract = ?, end_date_contract = ?, sum_contract = ?,
            responsible = ?, type_contract = ?, search_subject = ? 
            WHERE id_contract = ? ;"""

    if table == 'table_contract_mz_delivery':
        request_sql = """UPDATE `table_contract_mz_delivery` 
            SET number_contract = ?, incoming_number_contract = ?, company = ?, subject_contract = ?, comment = ?,
            start_date_contract = ?, date_of_conclusion_contract = ?, end_date_contract = ?, sum_contract = ?,
            responsible = ?, type_contract = ?, search_subject = ? 
            WHERE id_contract_mz_delivery = ? ;"""

    if table == 'table_contract_mz_services':
        request_sql = """UPDATE `table_contract_mz_services` 
            SET number_contract = ?, incoming_number_contract = ?, company = ?, subject_contract = ?, comment = ?,
            start_date_contract = ?, date_of_conclusion_contract = ?, end_date_contract = ?, sum_contract = ?,
            responsible = ?, type_contract = ?, search_subject = ? 
            WHERE id_contract_mz_services = ? ;"""

    conn.execute(request_sql, parameters)
    conn.commit()


def add_responsible_bd(name: str) -> None:
    """Добавление ответственного
        :param name -> Фамилия И.О."""
    conn.execute("INSERT INTO `table_responsible` (name_responsible) VALUES (?);", (name,))
    conn.commit()


def get_all_responsible_bd() -> List[Responsible]:
    """выборка ответственного"""
    data = conn.query('SELECT * FROM `table_responsible`;')

    people = converter_list_responsible(data)

    return people

# неиспользую
def get_responsible_bd(id: str) -> Responsible:
    """выборка ответственного по параметру"""
    data = conn.query('SELECT * FROM `table_responsible` WHERE id_responsible = ?;', (id,))

    people = converter_list_responsible(data)

    return people[0]


def check_responsible_db(name: str) -> bool:
    """Проверка на наличие в бд"""
    data = conn.query('SELECT COUNT(*) FROM table_responsible WHERE name_responsible = ?;', (name,))
    if data[0][0] == 0:
        return False
    else:
        return True


def update_responsible_bd(id_responsible: int, naw_name: str) -> None:
    """Обновляет указанную запись"""
    conn.execute("UPDATE table_responsible SET name_responsible = ? WHERE id_responsible = ?;",
                 (naw_name, id_responsible))
    conn.commit()


def add_type_contract_bd(type_con: str) -> None:
    """Добавляет тип договора
    :param type_con:
    """
    conn.execute("INSERT INTO table_type_contract (type_contract) VALUES (?);", (type_con,))
    conn.commit()


def get_all_type_contract_bd() -> List[TypeContract]:
    """ Выбирает все типы договоров"""
    data = conn.query("SELECT * FROM table_type_contract;")

    type_con = converter_list_type_contract(data)

    return type_con


def get_type_contract_bd(id: int) -> TypeContract:
    """Выбирает типы договоров
    :param id тип договора
    :return договор
    """
    data = conn.query("SELECT * FROM table_type_contract WHERE id_type = ?;", (id,))

    type_con = converter_list_type_contract(data)

    return type_con[0]


def update_type_contract_bd(id, type_con) -> None:
    """Обновляет запись тип договора
    :param id: id
    :param type_con: новый тип договора
    """
    conn.execute("UPDATE table_type_contract SET type_contract = ? WHERE id_type = ?;", (type_con, id))
    conn.commit()



def create_data_base():
    conn.executescript(drop_bd)
    conn.executescript(create_bd)
    conn.commit()


def create_cont():

    list_param = [("АТП-1234", "1234", 1, "Поставка хер чего", "БЭЗ коментария", "10.04.2022",
                   "10.02.2022", "10.04.202", 100000000, 2, 1),
                  ("АТП-1235", "1234", 1, "Поставка хер чего", "БЭЗ коментария", "10.04.2022",
                   "10.01.2022", "10.04.202", 200000000, 1, 2),
                  ("АТП-1236", "1234", 1, "Поставка хер чего", "БЭЗ коментария", "10.04.2022",
                   "10.05.2022", "10.04.202", 300000000, 2, 2)
                  ]

    for i in list_param:
        contract = Contract()

        contract.num_contract = i[0]
        contract.incoming_number_contract = i[1]
        contract.company = i[2]
        contract.subject_contract = i[3]
        contract.comment = i[4]
        contract.start_date_contract = i[5]
        contract.date_of_conclusion_contract = i[6]
        contract.end_date_contract = i[7]
        contract.sum_contract = i[8]
        contract.responsible = i[9]
        contract.type_contract = i[10]

        add_contract_bd('table_contract', contract)


# def create_additional():
#     ...

# def fill_db():
#
#     add_responsible_bd('Фидотов Д.В.')
#     add_responsible_bd('Лебедева Е.Н.')
#     add_responsible_bd('Корытник А.В.')
#     add_responsible_bd('Калинина Л.В.')
#     add_responsible_bd('Падьяров В.В.')
#     add_company_db('Ромарио', 'ООО "Ромарио', 1231)
#     add_company_db('РОМАРИО', 'ООО "РОМАРИО', 1232, True)
#     add_company_db('Мангопро', 'ООО "Мангопро', 1233, True)
#     add_company_db('Прома', 'ООО "Прома', 1234)
#     add_type_contract_bd("Поставка")
#     add_type_contract_bd("Услуги")
#     add_type_contract_bd("Сервис")
#     create_cont()
#     create_additional()


    #
    # add_contract_bd("table_contract", "АТП-1235", "1234", 1, "Поставка хер чего", "БЭЗ коментария", "10.04.2022",
    #                 "10.01.2022", "10.04.202", 200000000, 2, 1)
    # add_contract_bd("table_contract", "АТП-1236", "1234", 1, "Поставка хер чего", "БЭЗ коментария", "10.04.2022",
    #                 "10.05.2022", "10.04.202", 300000000, 2, 1)


# def out_info():
#     for i in get_all_responsible_bd():
#         print(i.id_responsible, i.name_responsible)
#     print("=" * 50)
#     for i in get_all_company_bd():
#         print(i.id_company, i.inn_company, i.name_company, i.full_name_company, i.smsp_flag_company)
#     print("="*50)
#     for i in get_company_bd(name='ром'):
#         print(i.id_company, i.inn_company, i.name_company, i.full_name_company, i.smsp_flag_company)
#     print("="*50)
#     for i in get_all_type_contract_bd():
#         print(i.id_type, i.type_contract)
#     print("="*50)
#     for i in get_type_contract_bd(type_con='Услуги'):
#         print(i.id_type, i.type_contract)
#     print("="*50)
#     for i in get_all_contract_bd():
#         print(i.id_contract, i.number_contract, i.incoming_number_contract, i.company, i.subject_contract, i.comment,
#               i.start_date_contract, i.date_of_conclusion_contract, i.end_date_contract, i.sum_contract, i.responsible,
#               i.type_contract)


# if __name__ == "__main__":
# #     create_data_base()
# #     fill_db()
# #     out_info()

    # get_all_responsible_bd()



