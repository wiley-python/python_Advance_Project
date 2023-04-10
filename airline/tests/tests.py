import pytest
import mysql.connector
from airlineReservationSystem.airline.airlineImplimentation import databasesetup, customer, cus, admin, db

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="airline")
mycursor = mydb.cursor()

# Create your tests here.
@pytest.fixture(scope='module')
def setup():
    print('----------setup----------------')
    db = databasesetup()
    db.create_database()
    yield db
    print('----------teardown----------------')
    db.drop_tables()


def test_customer_before_registration():
    act = cus.customer_register(111,'test-11',22)
    exp = 1
    assert act == exp



def test_customer_views_all_flights():
    print("details of all the flights")
    sql = "select * from flight"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    exp = cus.customer_views_All_flights()
    assert result == exp

def test_customer_booking_flight_ticket():
    act = cus.customer_booking_flight_ticket(11,2,1)
    exp = 1
    assert act == exp
    db.drop_tables()

def test_add_flight_details():
    act = admin.add_flight_details(10,'2022-10-10','test','test',20,200.45)
    exp = 1
    assert act == exp
    db.drop_tables()
