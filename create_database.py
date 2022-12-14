import sqlite3
from data_gestion.gestion.data_gestion import *


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


def add_all_categories():
    # Adding CPSR categories
    categories_to_add = {"3.3.1.1": "Skin Irritation",
                         "3.3.1.2": "Mucous membrane irritation/eye irritation",
                         "3.3.2": "Skin sensitisation",
                         "3.3.3.1": "Acute oral toxicity",
                         "3.3.3.2": "Acute dermal toxicity",
                         "3.3.3.3": "Acute inhalation toxicity",
                         "3.3.4.1": "Repeated dose (28 days)",
                         "3.3.4.2": "Repeated dose (90 days)",
                         "3.3.4.3": "Repeated dose (> 12 months)",
                         "3.3.5.1": "Fertility and reproduction toxicity",
                         "3.3.5.2": "Development toxicity",
                         "3.3.6": "Mutagenicity / Genotoxicity In Vitro",
                         "3.3.7": "Carcinogenicity",
                         "3.3.8.1": "Phototoxicity / Photo-irritation and photosensitation",
                         "3.3.8.2": "Photomutagenicity / Photoclastogenicity"}

    database = "./data.db"
    conn = create_connection(database)

    if conn is not None:
        for category_nbr in categories_to_add.keys():
            conn = create_connection(database)
            add_category(conn, category_nbr, categories_to_add[category_nbr])
        conn.close()


def add_all_decision_words():
    # Addind decision words (name, categories in which it is relevant,value)
    decision_words_add = [("strong irritant", ["3.3.1.1", "3.3.1.2"], 10),
                          ("positive", "all", 8),
                          ("medium", "all", 7.5),
                          ("moderate", "all", 7.5),
                          ("irritant", ["3.3.1.1", "3.3.1.2"], 8),
                          ("weak irritant", ["3.3.1.1", "3.3.1.2"], 6),
                          ("non irritant", ["3.3.1.1", "3.3.1.2"], 1),
                          ("negative", "all", 2),
                          ("extremely irritating to the skin",
                           ["3.3.1.1"], 10),
                          ("severely irritating to the eyes", ["3.3.1.2"], 10),
                          ("potential skin irritant", ["3.3.1.1"], 6),
                          ("corrosive", ["3.3.1.1", "3.3.1.2"], 0),
                          ("non corrosive", ["3.3.1.1", "3.3.1.2"], 0),
                          ("highly corrosive", ["3.3.1.1", "3.3.1.2"], 10),
                          ("weakly corrosive", ["3.3.1.1", "3.3.1.2"], 6),
                          ("strong sensitizer", ["3.3.2"], 9),
                          ("medium sensitizer", ["3.3.2"], 7.5),
                          ("weak sensitizer", ["3.3.2"], 6),
                          ("non sensitizer", ["3.3.2"], 3),
                          ("moderate sensitizer", ["3.3.2"], 7.5),
                          ("extreme sensitizer", ["3.3.2"], 10),
                          ("predicted sensitisation", ["3.3.2"], 6),
                          ("strong toxicity", ["3.3.3.1", "3.3.3.2",
                                               "3.3.3.3", "3.3.5.1", "3.3.5.2"], 9),
                          ("medium toxicity", ["3.3.3.1", "3.3.3.2",
                                               "3.3.3.3", "3.3.5.1", "3.3.5.2"], 7.5),
                          ("moderate toxicity", ["3.3.3.1", "3.3.3.2",
                                                 "3.3.3.3", "3.3.5.1", "3.3.5.2"], 7.5),
                          ("weak toxicity", ["3.3.3.1", "3.3.3.2",
                                             "3.3.3.3", "3.3.5.1", "3.3.5.2"], 6),
                          ("non toxicity", [
                           "3.3.3.1", "3.3.3.2", "3.3.3.3"], 0),
                          ("low", "all", 4),
                          ("high", "all", 9),
                          ("absence of acute toxicity", [
                           "3.3.4.1", "3.3.4.2", "3.3.4.3"], 0),
                          ("presence of acute toxicity", [
                           "3.3.4.1", "3.3.4.2", "3.3.4.3"], 7),
                          ("sub-acute activity",
                           ["3.3.4.1", "3.3.4.2", "3.3.4.3"], 6),
                          ("chronic toxicity", [
                           "3.3.4.1", "3.3.4.2", "3.3.4.3"], 8),
                          ("absence of repeated dose toxicity", [
                              "3.3.4.1", "3.3.4.2", "3.3.4.3"], 0),
                          ("presence of repeated dose toxicity",
                           ["3.3.4.1", "3.3.4.2", "3.3.4.3"], 7),
                          ("lack of reproductive toxicity",
                           ["3.3.5.1", "3.3.5.2"], 1),
                          ("lack of develoment toxicity",
                           ["3.3.5.1", "3.3.5.2"], 1),
                          ("shown a reproductive toxicity",
                           ["3.3.5.1", "3.3.5.2"], 8),
                          ("shown a development toxicity",
                           ["3.3.5.1", "3.3.5.2"], 8),
                          ("demonstrated reproductive toxicity",
                           ["3.3.5.1", "3.3.5.2"], 8),
                          ("demonstrated development toxicity",
                           ["3.3.5.1", "3.3.5.2"], 8),
                          ("genotoxic", ["3.3.6"], 8),
                          ("non genotoxic", ["3.3.6"], 2),
                          ("progenotoxin", ["3.3.6"], 8),
                          ("genotoxic effects", ["3.3.6"], 7),
                          ("absence of genotoxicity", ["3.3.6"], 0),
                          ("presence of genotoxicity", ["3.3.6"], 7),
                          ("lack of genotoxicity", ["3.3.6"], 1),
                          ("mutagen", ["3.3.6"], 8),
                          ("non mutagen", ["3.3.6"], 0),
                          ("mutagenic coumpound", ["3.3.6"], 8),
                          ("mutagenic effects", ["3.3.6"], 8),
                          ("mutagenic activity", ["3.3.6"], 7.5),
                          ("direct-acting mutagen", ["3.3.6"], 7),
                          ("potent mutagen", ["3.3.6"], 6),
                          ("promutagen", ["3.3.6"], 6),
                          ("negative response in mutagenicity", ["3.3.6"], 2),
                          ("positive response in mutagenicity", ["3.3.6"], 8),
                          ("lack of mutagenicity", ["3.3.6"], 1),
                          ("carcinogenic", ["3.3.7"], 8),
                          ("non-carcinogenic", ["3.3.7"], 1),
                          ("procarcinogen", ["3.3.7"], 7),
                          ("carcinogen", ["3.3.7"], 8),
                          ("non-carcinogen", ["3.3.7"], 1),
                          ("carcinogenic compound", ["3.3.7"], 8),
                          ("carcinogenic effects", ["3.3.7"], 7.5),
                          ("carcinogenic activity", ["3.3.7"], 7.5),
                          ("presence of carcinogenicity", ["3.3.7"], 7),
                          ("absence of carcinogenicity", ["3.3.7"], 0),
                          ("photosensitive", ["3.3.8.1", "3.3.8.2"], 7),
                          ("photosensitizing", ["3.3.8.1", "3.3.8.2"], 7),
                          ("phototoxic", ["3.3.8.1", "3.3.8.2"], 8),
                          ("photomutagenic", ["3.3.8.1", "3.3.8.2"], 8),
                          ("not-phototoxic", ["3.3.8.1", "3.3.8.2"], 2),
                          ("not-photomutagenic", ["3.3.8.1", "3.3.8.2"], 2),
                          ("photoallergic response", [
                           "3.3.8.1", "3.3.8.2"], 7),
                          ("presence of phototoxicity",
                           ["3.3.8.1", "3.3.8.2"], 7),
                          ("presence of photomutagenicity",
                           ["3.3.8.1", "3.3.8.2"], 7),
                          ("absence of phototoxicity",
                           ["3.3.8.1", "3.3.8.2"], 0),
                          ("absence of photomutagenicity",
                           ["3.3.8.1", "3.3.8.2"], 0),
                          ("lack of phototoxicity", ["3.3.8.1", "3.3.8.2"], 1),
                          ("lack of photomutagenicity",
                           ["3.3.8.1", "3.3.8.2"], 1),
                          ("shown a phototoxicity", ["3.3.8.1", "3.3.8.2"], 8),
                          ("demonstrated phototoxicity", ["3.3.8.1", "3.3.8.2"], 8)]
    database = "./data.db"
    conn = create_connection(database)

    if conn is not None:
        categories_id = [category[0] for category in get_categories(conn)]
        for word in decision_words_add:
            if word[1] == "all":
                for category_id in categories_id:
                    conn = create_connection(database)
                    add_decision_word(conn, category_id, word[0], word[2])
            else:
                for category in word[1]:
                    conn = create_connection(database)
                    category_id = get_category_id(
                        conn, category_nbr=category)[0][0]
                    conn = create_connection(database)
                    add_decision_word(conn, category_id, word[0], word[2])


def add_all_keywords():
    keywords_to__add = [('3.3.1.1', 'skin irritation'),
                        # ('category_nbr','keyword'),
                        ('3.3.1.1', 'dermal damage'),
                        ('3.3.1.1', 'dermal burn'),
                        ('3.3.1.1', 'dermis'),
                        ('3.3.1.1', 'dermal'),
                        ('3.3.1.1', 'epidermis'),
                        ('3.3.1.1', 'epidermal'),
                        ('3.3.1.1', 'peeling'),
                        ('3.3.1.1', 'etching'),
                        ('3.3.1.1', 'sub-cutaneous'),
                        ('3.3.1.1', 'percutaneous'),
                        ('3.3.1.2', 'eye damage'),
                        ('3.3.1.2', 'eye irritation'),
                        ('3.3.1.2', 'membrane irritation'),
                        ('3.3.2', 'skin sensitisation'),
                        ('3.3.3.1', 'sub acute oral toxicity'),
                        ('3.3.3.1', 'acute oral'),
                        ('3.3.3.2', 'sub acute dermal toxicity'),
                        ('3.3.3.2', 'acute dermal'),
                        ('3.3.3.2', 'acute intramuscular'),
                        ('3.3.3.2', 'acute intravenous'),
                        ('3.3.3.2', 'acute intraperitoneal'),
                        ('3.3.3.3', 'sub acute inhalation toxicity'),
                        ('3.3.3.3', 'acute inhalation'),
                        ('3.3.4.1', 'repeat-dose toxicity (28 days)'),
                        ('3.3.4.1', 'repeat dose toxicity (28 days)'),
                        ('3.3.4.1', '28 days'),
                        ('3.3.4.2', 'repeat-dose toxicity (90 days)'),
                        ('3.3.4.2', 'repeat dose toxicity (90 days)'),
                        ('3.3.4.2', '90 days'),
                        ('3.3.4.3', 'repeat-dose toxicity (12 months)'),
                        ('3.3.4.3', 'repeat dose toxicity (12 months)'),
                        ('3.3.4.3', '> 12 months'),
                        ('3.3.5.1', 'reproduction toxicity'),
                        ('3.3.5.1', 'fertility toxicity'),
                        ('3.3.5.1', 'postnatal toxicity'),
                        ('3.3.5.1', 'reproductive toxicity'),
                        ('3.3.5.1', 'Leydig and Sertoli cells'),
                        ('3.3.5.1', 'folliculogenesis'),
                        ('3.3.5.2', 'development toxicity'),
                        ('3.3.5.2', 'developmental toxicity'),
                        ('3.3.5.2', 'malformation'),
                        ('3.3.5.2', 'teratogenic'),
                        ('3.3.5.2', 'teratogenicity'),
                        ('3.3.5.2', 'Hypothalamus-Pituitary-Gonad'),
                        ('3.3.5.2', 'HPG'),
                        ('3.3.5.2', 'Hypothalamus-Pituitary-Thyroid axis'),
                        ('3.3.5.2', 'HPT axis'),
                        ('3.3.5.2', 'prenatal toxicity'),
                        ('3.3.5.2', 'organogenesis'),
                        ('3.3.5.2', 'non-embryotoxic'),
                        ('3.3.5.2', 'weak-embryotoxic'),
                        ('3.3.5.2', 'moderate-embryotoxic'),
                        ('3.3.5.2', 'strong-embryotoxic'),
                        ('3.3.6', 'mutagenicity'),
                        ('3.3.6', 'mutagen'),
                        ('3.3.6', 'genotoxicity'),
                        ('3.3.6', 'DNA modifications'),
                        ('3.3.6', 'chromosomal aberrations'),
                        ('3.3.6', 'segregation of DNA'),
                        ('3.3.6', 'mutation'),
                        ('3.3.6', 'mutagenic'),
                        ('3.3.6', 'genotoxic'),
                        ('3.3.6', 'clastogenicity'),
                        ('3.3.6', 'clastogen'),
                        ('3.3.6', 'sister chromatid exchange'),
                        ('3.3.6', 'dominant lethal micronucleus'),
                        ('3.3.6', 'genemutation'),
                        ('3.3.6', 'cell transformation'),
                        ('3.3.6', 'cell mutation'),
                        ('3.3.6', 'DNA damage'),
                        ('3.3.7', 'carcinogenicity'),
                        ('3.3.7', 'carcinogen'),
                        ('3.3.7', 'carcinogenic'),
                        ('3.3.7', 'oncogenic'),
                        ('3.3.7', 'oncogene'),
                        ('3.3.7', 'oncogenicity'),
                        ('3.3.8.1', 'phototoxicity'),
                        ('3.3.8.1', 'photosensitisation'),
                        ('3.3.8.1', 'photoirritation'),
                        ('3.3.8.1', 'phototoxic'),
                        ('3.3.8.2', 'photomutagen'),
                        ('3.3.8.2', 'photomutagenic'),
                        ('3.3.8.2', 'photomutagenicity'),
                        ('3.3.8.2', 'photo mutagenicity'),
                        ('3.3.8.2', 'photo-mutagenicity'),
                        ('3.3.8.2', 'photo mutagen'),
                        ('3.3.8.2', 'photo-mutagen'),
                        ('3.3.8.2', 'photo mutagenic'),
                        ('3.3.8.2', 'photo-mutagenic')]

    for keyword in keywords_to__add:
        conn = create_connection("./data.db")
        add_keyword(conn, keyword[0], keyword[1])


def add_all_methods():
    methods_to__add = [('3.3.1.1', 'EPISKIN'),
                       ('3.3.1.1', 'OECD 439'),
                       ('3.3.1.1', 'OECD 404'),
                       ('3.3.1.1', 'fluorescein leakage test'),
                       ('3.3.1.1', 'flt'),
                       ('3.3.1.1', 'OECD 460'),
                       ('3.3.1.1', 'transcutaneous electrical resistance'),

                       ('3.3.1.2', 'OECD 405'),
                       ('3.3.1.2', 'Bovine Cornea Opacity Permeability'),
                       ('3.3.1.2', 'BCOP'),
                       ('3.3.1.2', 'OECD 437'),
                       ('3.3.1.2', 'LLBO'),
                       ('3.3.1.2', 'Isolated Chicken Eye'),
                       ('3.3.1.2', 'ICE'),
                       ('3.3.1.2', 'OECD 438'),
                       ('3.3.1.2', 'HET-CAM'),
                       ('3.3.1.2', 'Draize'),
                       ('3.3.1.2', 'isolated rabbit eye'),
                       ('3.3.1.2', 'IRE'),
                       ('3.3.1.2', 'membrane barrier test'),
                       ('3.3.1.2', 'OECD 435'),

                       ('3.3.2', 'direct peptide reactivity assay'),
                       ('3.3.2', 'DPRA'),
                       ('3.3.2', 'KE1'),
                       ('3.3.2', 'Adverse Outcome Pathway'),
                       ('3.3.2', 'AOP'),
                       ('3.3.2', 'Molecular Initiating Event'),
                       ('3.3.2', 'MIE'),
                       ('3.3.2', 'OECD 442C'),
                       ('3.3.2', 'human cell line activation test'),
                       ('3.3.2', 'h-CLAT'),
                       ('3.3.2', 'OECD 442E'),
                       ('3.3.2', 'keratinosense'),
                       ('3.3.2', 'OECD 442D'),
                       ('3.3.2', 'kDPRA'),
                       ('3.3.2', 'sens-is'),
                       ('3.3.2', 'gardskin'),
                       ('3.3.2', 'ADORA'),
                       ('3.3.2', 'Myeloid U937 skin sensitization test'),
                       ('3.3.2', 'U-SENS'),
                       ('3.3.2', 'interleukin-8 reporter gene assay'),
                       ('3.3.2', 'IL8-Luc assay'),
                       ('3.3.2', 'local lymph node assay'),
                       ('3.3.2', 'LLNA'),
                       ('3.3.2', 'Guinea Pig Maximisation Test'),
                       ('3.3.2', 'GPMT'),
                       ('3.3.2', 'Buehler test'),
                       ('3.3.2', 'OECD 406'),
                       ('3.3.2', 'No Expected Sensitising Induction Level'),
                       ('3.3.2', 'NESIL'),
                       ('3.3.2', 'Acceptable Exposure Level'),
                       ('3.3.2', 'AEL'),
                       ('3.3.2', 'are-nrf2 luciferase test'),
                       ('3.3.2', 'local lymph node assay'),
                       ('3.3.2', 'LLNA'),
                       ('3.3.2', 'OECD 429'),
                       ('3.3.2', 'freund\'s complete adjuvant test'),
                       ('3.3.2', 'open epicutaneous test'),
                       ('3.3.2', 'OET'),
                       ('3.3.2', 'defined approach'),
                       ('3.3.2', 'OECD 497'),

                       ('3.3.4.1', 'OECD 407'),
                       ('3.3.4.1', 'OECD 410'),
                       ('3.3.4.1', 'OECD 412'),

                       ('3.3.4.2', 'OECD 408'),
                       ('3.3.4.2', 'OECD 409'),
                       ('3.3.4.2', 'OECD 411'),
                       ('3.3.4.2', 'OECD 413'),

                       ('3.3.4.3', 'OECD 452'),
                       ('3.3.4.3', 'OECD 453'),

                       ('3.3.5.1', 'The Whole Embryo Culture test'),
                       ('3.3.5.1', 'WEC'),
                       ('3.3.5.1', 'Embryonic Stem Cell Test'),
                       ('3.3.5.1', 'EST'),
                       ('3.3.5.1', 'OECD 416'),
                       ('3.3.5.1', 'OECD 421'),
                       ('3.3.5.1', 'OECD 422'),
                       ('3.3.5.1', 'OECD 443'),

                       ('3.3.5.2', 'MicroMass test'),
                       ('3.3.5.2', 'OECD 414'),

                       ('3.3.6', 'OECD 471'),
                       ('3.3.6', 'bacterial reverse mutation test'),
                       ('3.3.6', 'Ames Test'),

                       # 3.3.6.1
                       ('3.3.6', 'Micronucleus Test'),
                       ('3.3.6', 'OECD 487'),
                       ('3.3.6', 'OECD 476'),
                       ('3.3.6', 'Mammalian Cell Gene Mutation Test'),
                       ('3.3.6', 'Hprt'),
                       ('3.3.6', 'Xprt'),
                       ('3.3.6', 'OECD 490'),
                       ('3.3.6', 'the thymidine kinase gene'),

                       # 3.3.6.2
                       ('3.3.6', 'OECD 488'),
                       ('3.3.6', 'Transgenic Rodent Somatic and Germ Cell Gene Mutation Assays'),
                       ('3.3.6', 'OECD 489'),
                       ('3.3.6', 'Mammalian Alkaline Comet Assay'),
                       ('3.3.6', 'OECD 486'),
                       ('3.3.6', 'Unscheduled DNA Synthesis Test'),
                       ('3.3.6', 'UDS test'),
                       ('3.3.6', 'OECD 474'),
                       ('3.3.6', 'micronucleus test'),
                       ('3.3.6', 'OECD 475'),
                       ('3.3.6', 'the mammalian in vivo chromosome aberration test'),

                       ('3.3.7', 'BALB/c 3T3 Cell Transformation Assay'),
                       ('3.3.7', 'BALB/c 3T3 CTA'),
                       ('3.3.7', 'Syrian Hamster Embryo CTA'),
                       ('3.3.7', 'Syrian Hamster Embryo cell transformation assay'),
                       ('3.3.7', 'Bhas 42 CTA'),
                       ('3.3.7', 'Bhas 42 cell transformation assay'),
                       ('3.3.7', 'OECD 451'),

                       ('3.3.8.1', 'OECD 432'),
                       ('3.3.8.1', '3T3 NRU Phototoxicity Test')]

    for method in methods_to__add:
        conn = create_connection("./data.db")
        add_method(conn, method[0], method[1])


def add_all_subjects():
    subjects_to_add = ["guinea pig",
                       "human",
                       "rat",
                       "mouse",
                       "rabbit",
                       "rodent",
                       "chicken",
                       "hamster"]

    for subject in subjects_to_add:
        conn = create_connection("./data.db")
        add_subject(conn, subject)


def main():
    database = "./data.db"

    sql_create_categories_table = """ CREATE TABLE IF NOT EXISTS categories (
                                        id integer primary key autoincrement not null,
                                        number text NOT NULL,
                                        name text NOT NULL,
                                        description text
                                    ); """

    sql_create_keywords_table = """ CREATE TABLE IF NOT EXISTS keywords (
                                        id integer primary key autoincrement not null,
                                        category_id int NOT NULL,
                                        name text NOT NULL,
                                        FOREIGN KEY (category_id) REFERENCES categories (id)
                                    ); """

    sql_create_requests_table = """ CREATE TABLE IF NOT EXISTS requests (
                                        id integer primary key autoincrement not null,
                                        query text NOT NULL,
                                        created_at DATETIME NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')),
                                        article_limit int NOT NULL,
                                        age_limit int NOT NULL,
                                        etape int NOT NULL DEFAULT 0
                                        ); """

    sql_create_results_table = """ CREATE TABLE IF NOT EXISTS results (
                                        id integer primary key autoincrement not null,
                                        cat_to_req_id int NOT NULL,
                                        sentence text NOT NULL,
                                        article_name text NOT NULL,
                                        article_link text NOT NULL,
                                        value int,
                                        in_what str,
                                        method text,
                                        subject text,
                                        FOREIGN KEY (cat_to_req_id) REFERENCES category_to_request (id) ON DELETE CASCADE
                                        ); """

    sql_create_category_to_request = """ CREATE TABLE IF NOT EXISTS category_to_request (
                                            id integer primary key autoincrement not null,
                                            id_request int NOT NULL,
                                            id_category int NOT NULL,
                                            comment int,
                                            FOREIGN KEY (id_request) REFERENCES requests (id) ON DELETE CASCADE ,
                                            FOREIGN KEY (id_category) REFERENCES categories (id) ON DELETE CASCADE
                                            ); """

    sql_create_methods_table = """ CREATE TABLE IF NOT EXISTS methods (
                                        id integer primary key autoincrement not null,
                                        category_id int NOT NULL,
                                        name text NOT NULL,
                                        FOREIGN KEY (category_id) REFERENCES categories (id)
                                    ); """

    sql_create_subjects_table = """ CREATE TABLE IF NOT EXISTS subjects (
                                       id integer primary key autoincrement not null,
                                       subject_name text NOT NULL
                                       );"""

    sql_create_decision_words_table = """ CREATE TABLE IF NOT EXISTS decision_words (
                                            id integer primary key autoincrement not null,
                                            id_category int NOT NULL,
                                            decision_word text NOT NULL,
                                            value int NOT NULL,
                                            FOREIGN KEY (id_category) REFERENCES categories (id)
                                            );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create categories table
        create_table(conn, sql_create_categories_table)

        # create keywords table
        create_table(conn, sql_create_keywords_table)

        # create requests table
        create_table(conn, sql_create_requests_table)

        # create results table
        create_table(conn, sql_create_results_table)

        # create results linkage
        create_table(conn, sql_create_category_to_request)

        # create methods table
        create_table(conn, sql_create_methods_table)

        # create subjects table
        create_table(conn, sql_create_subjects_table)

        # create decision words table
        create_table(conn, sql_create_decision_words_table)

        conn.close()

        add_all_categories()

        add_all_decision_words()

        add_all_keywords()

        add_all_methods()

        add_all_subjects()

    else:
        print("Error! cannot create the database connection.")
