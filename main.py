

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

plane_info = """
insert into Plane_Inventory values
( 001, "Boeing 747", 650, 300, "2012" ),
( 002, "Boeing 777", 660 , 310 , "2014" ),
( 003, "Boeing 888", 700, 320, "2018" );
"""

route_info = """
insert into Routes values
(001, "Miami, Florida", "0600", "NYC, NY", "1200" ),
(002, "STL, MO", "1200", "Orlando, FL", "1400" ),
(003, "Indianapolis, Indiana", "1700", "Dallas, TX", "2000" );
"""

pilots_info = """
insert into Pilots values
( 0001, "Bob Blue", "BS", "3 years", "$80,000", "2019"),
( 0002, "George Purple", "BA", "6 years", "$100,000", "2016"),
( 0003, "Kathy Green", "MBA", "2 years", "$75,000", "2020");
"""



#Callout section
connection = create_server_connection("localhost", "root", "student", "United_Air")
execute_query(connection, pilots_info)


