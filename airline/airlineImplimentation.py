import mysql.connector
import datetime


class databasesetup:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="airline")
    mycursor = mydb.cursor()

    def create_database(self):
        print("Creating database")
        sql = "create database if not exists airline"
        db.mycursor.execute(sql)
        print("airline database created successfully")

    def create_flight_table(self):
        print(" Creating flight table")
        sql = ''' CREATE TABLE if not exists flight (
                              flightNo int(4) PRIMARY KEY,
                              data DATE,
                              source char(30) NOT NULL ,
                              destination char(30) NOT NULL, 
                               capacity int, 
                                cost float(8,2)); '''

        db.mycursor.execute(sql)
        print("flight table created successfully")

    def insert_flight_table(self):
        print("Inserting 5 records")
        sql = "INSERT INTO flight values (%s,%s,%s,%s,%s,%s)"
        val = [
            (1, '11/14/2020', 'San Francisco', 'New York', 30, 300.00),
            (2, '11/14/2020', 'San Diego', 'San Jose', 20, 200.00),
            (3, '11/14/2020', 'Dallas', 'Boston', 35, 144.45),
            (4, '11/14/2020', 'Denver', 'Chicago', 25, 350.56),
            (5, '11/14/2020', 'San Francisco', 'Sacramento', 40, 480.59),
            (6, '11/14/2020', 'San Luis Obispo', 'Portland', 30, 250.50)
        ]
        db.mycursor.executemany(sql, val)
        db.mydb.commit()
        print("\t\t flight details updated")
        res = db.mycursor.rowcount
        print(res, "rows inserted")
        return res

    def create_customer_table(self):
        print(" Creating customer table")
        sql = '''CREATE TABLE if not exists customer (
                                      custid int(4) PRIMARY KEY,
                                      custname varchar(30) NOT NULL,
                                      custage int(4)
                                      );'''
        db.mycursor.execute(sql)
        print(" customer table created successfully")

    def insert_customer_table(self):
        print("Inserting 5 records")
        sql = "INSERT INTO customer values (%s,%s,%s)"
        val = [(1, 'Neha', 30),
               (2, 'Sahil', 45),
               (3, 'Rohan', 35),
               (4, 'Ankita', 54),
               (5, 'Rahul', 25)]
        db.mycursor.executemany(sql, val)
        db.mydb.commit()
        print("\t\t customer details updated")
        res = db.mycursor.rowcount
        print(res, "rows inserted")
        return res

    def create_bookings_table(self):
        print("creating bookings table")
        sql = '''CREATE TABLE if not exists bookings (
                                      bid int primary key,
                                      flightNo int(4) NOT NULL,
                                      bdate DATE,
                                      custid int(4) NOT NULL
                                      ); '''
        db.mycursor.execute(sql)
        print(" bookings table created successfully")

    def drop_tables(self):
        print("dropping tables")
        sql = "drop table flight"
        db.mycursor.execute(sql)
        print(" drop flight table successfully")
        sql = "drop table customer"
        db.mycursor.execute(sql)
        print(" drop customer table successfully")
        sql = "drop table bookings"
        db.mycursor.execute(sql)
        print(" drop bookings table successfully")


db = databasesetup()

db.create_database()
db.create_flight_table()
db.create_customer_table()
db.create_bookings_table()
db.insert_customer_table()
db.insert_flight_table()


class customer:
    def customer_register(self, cust_id, cust_name, cust_age):
        print("registering customer details")
        if cust_age > 20:
            sql = "INSERT INTO customer values (%s,%s,%s)"
            val = (cust_id, cust_name, cust_age)
            db.mycursor.execute(sql, val)
            db.mydb.commit()
            res = db.mycursor.rowcount
            return res
        else:
            print("you are not eligible for booking air ticket!! ")
            return 0

    def customer_views_All_flights(self):
        print("details of all the flights")
        sql = "select * from flight"
        db.mycursor.execute(sql)
        res = db.mycursor.rowcount
        result = db.mycursor.fetchall()
        print(res)
        return result

    def customer_booking_flight_ticket(self, bid, flightNo, custid):
        now = datetime.datetime.now()
        sql = "insert into bookings values(%s,%s,%s,%s)"
        now = datetime.datetime(2009, 5, 5)
        bdate = now.date().isoformat()
        val = (bid, flightNo, bdate, custid)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        res = db.mycursor.rowcount
        return res

    def customer_cancel_booked_flight(self, bid):
        sql = "delete from bookings where bid = %s"
        val = bid
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        res = db.mycursor.rowcount
        return res


cus = customer()


class admin:
    def add_flight_details(self, flightNo, date, source, destination, capacity, cost):
        sql = "INSERT INTO flight values (%s,%s,%s,%s,%s,%s)"
        val = (flightNo, date, source, destination, capacity, cost)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        print("\t\t flight details added")
        res = db.mycursor.rowcount
        print(res, "rows inserted")
        return res

    def add_customers(self, cust_id, cust_name, cust_age):
        cus.customer_register(cust_id, cust_name, cust_age)

    def add_bookings(self, bid, flightNo, custid):
        cus.customer_booking_flight_ticket(bid, flightNo, custid)

    def view_bookings(self):
        cus.customer_views_All_flights()


admin = admin()

# db.drop_tables()
