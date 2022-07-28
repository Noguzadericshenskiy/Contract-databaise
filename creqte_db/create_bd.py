drop_bd = """
    DROP TABLE IF EXISTS `table_company`;
    DROP TABLE IF EXISTS `table_responsible`;
    DROP TABLE IF EXISTS `table_additional_agreement`;
    DROP TABLE IF EXISTS `table_type_contract`;
    DROP TABLE IF EXISTS `table_log_request`;
    DROP TABLE IF EXISTS `table_users`;
    DROP TABLE IF EXISTS `table_status`;
    
    DROP TABLE IF EXISTS `table_additional_contract`;
    DROP TABLE IF EXISTS `table_additional_mz_delivery`;
    DROP TABLE IF EXISTS `table_additional_mz_services`;
    DROP TABLE IF EXISTS `table_additional_sanatorium`;
    DROP TABLE IF EXISTS `table_additional_44`;
        
    DROP TABLE IF EXISTS `table_contract`;
    DROP TABLE IF EXISTS `table_contract_mz_delivery`;
    DROP TABLE IF EXISTS `table_contract_mz_services`;
    DROP TABLE IF EXISTS `table_contract_sanatorium`;
    DROP TABLE IF EXISTS `table_contract_44`;
"""


create_bd = """
    CREATE TABLE `table_company` (
        id_company INTEGER PRIMARY KEY AUTOINCREMENT,
        name_company VARCHAR(150) NOT NULL,
        full_name_company VARCHAR(250) NOT NULL,
        inn_company INTEGER,
        smsp_flag_company BOOLEAN,
        search TEXT
    );

    CREATE TABLE `table_responsible` (
        id_responsible INTEGER PRIMARY KEY AUTOINCREMENT,
        name_responsible VARCHAR(150) NOT NULL
    );

    CREATE TABLE `table_type_contract` (
        id_type INTEGER PRIMARY KEY AUTOINCREMENT,
        type_contract  VARCHAR(100) NOT NULL
    );
        
    CREATE TABLE `table_contract` (
        id_contract INTEGER PRIMARY KEY AUTOINCREMENT,
        number_contract VARCHAR(100) UNIQUE,
        incoming_number_contract VARCHAR(100), 
        company INTEGER REFERENCES table_company (id_company),
        subject_contract TEXT,
        comment TEXT, 
        start_date_contract VARCHAR(50),
        date_of_conclusion_contract VARCHAR(50) DEFAULT CURRENT_DATE,
        end_date_contract VARCHAR(50),
        sum_contract INTEGER DEFAULT 0,
        responsible INTEGER REFERENCES  table_responsible (id_responsible),
        type_contract VARCHAR(100) REFERENCES table_type_contract (id_type),
        search_subject TEXT
    );
    
    CREATE TABLE `table_contract_mz_delivery` (
        id_contract_mz_delivery INTEGER PRIMARY KEY AUTOINCREMENT,
        number_contract VARCHAR(100) UNIQUE,
        incoming_number_contract VARCHAR(100),
        company INTEGER REFERENCES table_company (id_company),
        subject_contract TEXT,
        comment TEXT, 
        start_date_contract VARCHAR(50),
        date_of_conclusion_contract VARCHAR(50) DEFAULT CURRENT_DATE,
        end_date_contract VARCHAR(50),
        sum_contract INTEGER DEFAULT 0,
        responsible INTEGER REFERENCES  table_responsible (id_responsible),
        type_contract VARCHAR(100) REFERENCES table_type_contract (id_type),
        search_subject TEXT
    );
    
    CREATE TABLE `table_contract_mz_services` (
        id_contract_mz_services INTEGER PRIMARY KEY AUTOINCREMENT,
        number_contract VARCHAR(100) UNIQUE,
        incoming_number_contract VARCHAR(100),
        company INTEGER REFERENCES table_company (id_company),
        subject_contract TEXT,
        comment TEXT, 
        start_date_contract VARCHAR(50),
        date_of_conclusion_contract VARCHAR(50) DEFAULT CURRENT_DATE,
        end_date_contract VARCHAR(50),
        sum_contract INTEGER DEFAULT 0,
        responsible INTEGER REFERENCES  table_responsible (id_responsible),
        type_contract VARCHAR(100) REFERENCES table_type_contract (id_type),
        search_subject TEXT
    );
    
    CREATE TABLE `table_contract_sanatorium` (
        id_contract_sanatorium INTEGER PRIMARY KEY AUTOINCREMENT,
        number_contract VARCHAR(100) UNIQUE,
        incoming_number_contract VARCHAR(100),
        company INTEGER REFERENCES table_company (id_company),
        subject_contract TEXT,
        comment TEXT, 
        start_date_contract VARCHAR(50),
        date_of_conclusion_contract VARCHAR(50) DEFAULT CURRENT_DATE,
        end_date_contract VARCHAR(50),
        sum_contract INTEGER DEFAULT 0,
        responsible INTEGER REFERENCES  table_responsible (id_responsible),
        type_contract VARCHAR(100) REFERENCES table_type_contract (id_type),
        search_subject TEXT
    );
    
    CREATE TABLE `table_contract_44` (
        id_contract_44 INTEGER PRIMARY KEY AUTOINCREMENT,
        number_contract VARCHAR(100) UNIQUE,
        incoming_number_contract VARCHAR(100),
        company INTEGER REFERENCES table_company (id_company),
        subject_contract TEXT,
        comment TEXT, 
        start_date_contract VARCHAR(50),
        date_of_conclusion_contract VARCHAR(50) DEFAULT CURRENT_DATE,
        end_date_contract VARCHAR(50),
        sum_contract INTEGER DEFAULT 0,
        responsible INTEGER REFERENCES  table_responsible (id_responsible),
        type_contract VARCHAR(100) REFERENCES table_type_contract (id_type),
        search_subject TEXT
    );        
                
    CREATE TABLE `table_additional_contract` (
        id_additional INTEGER PRIMARY KEY AUTOINCREMENT,
        number_additional VARCHAR(150) NOT NULL UNIQUE,
        number_contract VARCHAR(150) NOT NULL REFERENCES `table_contract` (id_contract),
        what_it_does TEXT, 
        date_additional VARCHAR(50) DEFAULT CURRENT_DATE,
        new_date VARCHAR(50),
        sum_additional INTEGER,
        comment TEXT
    );
    
    CREATE TABLE `table_additional_mz_delivery` (
        id_additional INTEGER PRIMARY KEY AUTOINCREMENT,
        number_additional VARCHAR(150) NOT NULL UNIQUE,
        number_contract VARCHAR(150) NOT NULL REFERENCES table_contract_mz_delivery (id_contract_mz_delivery),
        what_it_does TEXT, 
        date_additional VARCHAR(50) DEFAULT CURRENT_DATE,
        new_date VARCHAR(50),
        sum_additional INTEGER,
        comment TEXT
    );

      CREATE TABLE `table_additional_mz_services` (
        id_additional INTEGER PRIMARY KEY AUTOINCREMENT,
        number_additional VARCHAR(150) NOT NULL UNIQUE,
        number_contract VARCHAR(150) NOT NULL REFERENCES table_contract_mz_services (id_contract_mz_services),
        what_it_does TEXT, 
        date_additional VARCHAR(50) DEFAULT CURRENT_DATE,
        new_date VARCHAR(50),
        sum_additional INTEGER,
        comment TEXT
    );

      CREATE TABLE `table_additional_sanatorium` (
        id_additional INTEGER PRIMARY KEY AUTOINCREMENT,
        number_additional VARCHAR(150) NOT NULL UNIQUE,
        number_contract VARCHAR(150) NOT NULL REFERENCES table_contract_sanatorium (id_contract_sanatorium),
        what_it_does TEXT, 
        date_additional VARCHAR(50) DEFAULT CURRENT_DATE,
        new_date VARCHAR(50),
        sum_additional INTEGER,
        comment TEXT
    );
        
    CREATE TABLE `table_additional_44` (
        id_additional INTEGER PRIMARY KEY AUTOINCREMENT,
        number_additional VARCHAR(150) NOT NULL UNIQUE,
        number_contract VARCHAR(150) NOT NULL REFERENCES table_contract_44 (id_contract_44),
        what_it_does TEXT, 
        date_additional VARCHAR(50) DEFAULT CURRENT_DATE,
        new_date VARCHAR(50),
        sum_additional INTEGER,
        comment TEXT
    );
    
"""

create_optional_table = """       
    CREATE TABLE `table_log_request` (
        timestamp_req VARCHAR(50) NOT NULL PRIMARY KEY,
        user_req VARCHAR(100),
        request TEXT
    );   
    
    CREATE TABLE `table_users` (
            user_name VARCHAR(100) PRIMARY KEY NOT NULL,
            status VARCHAR(100) REFERENCES table_status (status_user),
            password TEXT 
    );
        
    CREATE TABLE  `table_status` (
        status_user TEXT VARCHAR(50) NOT NULL PRIMARY KEY 
    );

"""



    # CREATE TABLE `log_request` (
    #     timestamp_req DATE PRIMARY KEY,
    #     user_req VARCHAR(50),
    #     request TEXT
    # );