

import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection



def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_table1 = """
create table Plane_Inventory(
Plane_ID int primary key,
Make_Model varchar(30) not null,
Max_Speed int not null, 
Max_Capacity int not null,
Start_Date varchar(20) not null);

"""

create_table2 = """
create table Routes(
Plane_ID int primary key,
Depart_From varchar(30) not null,
Depart_Time varchar(30) not null,
Arrival_Location varchar(30) not null,
Arrival_Time varchar(15) not null);
"""

create_table3 = """
create table Pilots(
Employee_ID int primary key,
Name varchar(30) not null,
Education varchar(15) not null,
Experience varchar(15) not null,
Salary varchar(25) not null,
Hired varchar(20) not null);
"""



#Callout section
connection = create_server_connection("localhost", "root", "student", "United_Air")
execute_query(connection, create_table3)


