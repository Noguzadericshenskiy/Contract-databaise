import datetime


class Additional:
    def __init__(self):
        self.__number_additional = None
        self.__what_it_does = None
        self.__date_additional = None
        self.__new_date = None
        self.__sum_additional = None
        self.__comment = None
        self.__id_additional = None
        self.__num_contract = None

    @property
    def id_additional(self):
        return self.__id_additional

    @property
    def number_additional(self):
        return self.__number_additional

    @property
    def date_additional(self):
        return self.__date_additional

    @property
    def sum_additional(self):
        return self.__sum_additional

    @property
    def num_contract(self):
        return self.__num_contract

    @property
    def what_it_does(self):
        return self.__what_it_does

    @property
    def new_date(self):
        return self.__new_date

    @property
    def comment(self):
        return self.__comment

    @id_additional.setter
    def id_additional(self, id):
        self.__id_additional = id

    @number_additional.setter
    def number_additional(self, num):
        self.__number_additional = num

    @date_additional.setter
    def date_additional(self, date):
        self.__date_additional = date

    @sum_additional.setter
    def sum_additional(self, summ):
        self.__sum_additional = summ

    @num_contract.setter
    def num_contract(self, num_con):
        self.__num_contract = num_con

    @what_it_does.setter
    def what_it_does(self, whot):
        self.__what_it_does = whot

    @new_date.setter
    def new_date(self, new_d):
        self.__new_date = new_d

    @comment.setter
    def comment(self, text):
        self.__comment = text


class Contract:
    def __init__(self):
        self.__id_contract = None
        self.__num_contract = None
        self.__incoming_number_contract = None
        self.__company = None
        self.__subject_contract = None
        self.__comment = None
        self.__start_date_contract = None
        self.__date_of_conclusion_contract = None
        self.__end_date_contract = None
        self.__sum_contract = None
        self.__responsible = None
        self.__type_contract = None

    @property
    def id_contract(self):
        return self.__id_contract

    @property
    def num_contract(self):
        return self.__num_contract

    @property
    def incoming_number_contract(self):
        return self.__incoming_number_contract

    @property
    def company(self):
        return self.__company

    @property
    def subject_contract(self):
        return self.__subject_contract

    @property
    def comment(self):
        return self.__comment

    @property
    def start_date_contract(self):
        return self.__start_date_contract

    @property
    def date_of_conclusion_contract(self):
        return self.__date_of_conclusion_contract

    @property
    def end_date_contract(self):
        return self.__end_date_contract

    @property
    def sum_contract(self):
        return self.__sum_contract

    @property
    def responsible(self):
        return self.__responsible

    @property
    def type_contract(self):
        return self.__type_contract

    @id_contract.setter
    def id_contract(self, id):
        self.__id_contract = id

    @num_contract.setter
    def num_contract(self, num):
        self.__num_contract = num

    @incoming_number_contract.setter
    def incoming_number_contract(self, in_num):
        self.__incoming_number_contract = in_num

    @company.setter
    def company(self, firm):
        self.__company = firm

    @subject_contract.setter
    def subject_contract(self, subj):
        self.__subject_contract = subj

    @comment.setter
    def comment(self, text):
        self.__comment = text

    @start_date_contract.setter
    def start_date_contract(self, up_date):
        self.__start_date_contract = up_date

    @date_of_conclusion_contract.setter
    def date_of_conclusion_contract(self, date_of_conclusion):
        self.__date_of_conclusion_contract = date_of_conclusion

    @end_date_contract.setter
    def end_date_contract(self, end_date):
        self.__end_date_contract = end_date

    @sum_contract.setter
    def sum_contract(self, summ):
        self.__sum_contract = summ

    @responsible.setter
    def responsible(self, text):
        self.__responsible = text

    @type_contract.setter
    def type_contract(self, text):
        self.__type_contract = text


class Company:
    def __init__(self):
        self.__id_company = None
        self.__name_company = None
        self.__full_name_company = None
        self.__inn_company = None
        self.__smsp_flag_company = None

    @property
    def id_company(self):
        return self.__id_company

    @id_company.setter
    def id_company(self, id):
        self.__id_company = id

    @property
    def name_company(self):
        return self.__name_company

    @property
    def full_name_company(self):
        return self.__full_name_company

    @property
    def inn_company(self):
        return self.__inn_company

    @property
    def smsp_flag_company(self):
        return self.__smsp_flag_company

    @name_company.setter
    def name_company(self, name):
        self.__name_company = name

    @full_name_company.setter
    def full_name_company(self, full_name):
        self.__full_name_company = full_name

    @inn_company.setter
    def inn_company(self, inn):
        self.__inn_company = inn

    @smsp_flag_company.setter
    def smsp_flag_company(self, additional):
        self.__smsp_flag_company = additional


class TypeContract:
    def __init__(self):
        self.__id_type = None
        self.__type_contract = None

    @property
    def id_type(self):
        return self.__id_type

    @id_type.setter
    def id_type(self, id):
        self.__id_type = id

    @property
    def type_contract(self):
        return self.__type_contract

    @type_contract.setter
    def type_contract(self, type_con):
        self.__type_contract = type_con


class Responsible:
    def __init__(self):
        self.__id = None
        self.__name_responsible = None

    @property
    def id_responsible(self):
        return self.__id

    @id_responsible.setter
    def id_responsible(self, id):
        self.__id = id

    @property
    def name_responsible(self):
        return self.__name_responsible

    @name_responsible.setter
    def name_responsible(self, name):
        self.__name_responsible = name
