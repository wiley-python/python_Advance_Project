# python_Jr_project_Solution
## Problem Statement

The StarLine groups are into different business sectors. Their growth in business is well known and is one of the most popular business groups. It all started with a conversation where one of the board members commented that soon this business group will touch the sky. Thus, the StarLine Groups started its operations in the year 2008 January. They initially started with a single aircraft operating between New York and Chicago. As they have been into business for years, they decided to concentrate on the customer satisfaction as the key area to improve their business. Very soon StarLine Airways earned the prestigious Service Excellence award for customer satisfaction. They earned a profit of $1 million in the first year of its operation. Substantially increased customer base over the past five years.

## Current System

StarLine Airways has several reservation offices in each city where the flights operate. Each reservation office has multiple reservation counters to handle reservations and cancellations. Each counter has a counter assistant who is responsible for making reservations or cancellations. Reservations for a flight commence 30 days before the date of the flight.

## Project Scope/Functionalities

**The Project should include the below functionality:**

 customers module - Book, Print and Cancel Tickets online
 
      _customer Module should include register information to book the ticket, Print ticket should have the scope to retrieve the passenger details from the database. Cancel Ticket should have the scope to cancel booked ticket by specifying a proper reason for cancellation. Cancelled details of passenger should be removed from the database too._
  
  
Admin module - Add & view Customers, Add & view flights, Add and view bookings

      _Admin Module should enable admin to add and view customer details, Add and View Flight details, add and view bookings._ 
   

### Files to be Edited:

In this project you need to implement:

**step-1**: setup database in class - **databasesetup**  with different methods - 
   
   1. **create_database** -  
     
           (Includes connecting to db with credentials 
                  host="localhost", 
                  user="root", 
                  passwd="root",
                  database="stock")
            create a db of name airline
            
            
    2. **create_flight_table** - functionality - create table flight with given structure
    
            CREATE TABLE if not exists flight (
                   flightNo int(4) PRIMARY KEY,
                   data DATE,
                   source char(30) NOT NULL ,
                   destination char(30) NOT NULL, 
                   capacity int, 
                   cost float(8,2))
                   
   3. **insert_flight_table** -  
     
         functionality - insert data into flight table based on structure and return rowcount 
                   
   4. **create_customer_table** - 
   
        functionality - create table customer with given Structure 
            CREATE TABLE if not exists customer (
                 custid int(4) PRIMARY KEY,
                 custname varchar(30) NOT NULL,
                 custage int(4))
                 
   5. **insert_customer_table** - 
              
            functionality - insert data into customer table based on structure and return rowcount 
              
   6. **create_bookings_table** -
              
          functionality - create table bookings with given structure
                 CREATE TABLE if not exists bookings (
                        bid int primary key,
                        flightNo int(4) NOT NULL,
                        bdate DATE,
                        custid int(4) NOT NULL)
                       
    7. **drop_tables** - 
    
          functionality - drop tables of flight customer and bookings
           
**step-2**: implement customer module in class **customer** with different methods
           
   1. **customer_register** - _functionality - register  customer details to the database if customer age > 20 _
   
   2. **customer_views_All_flights** - 
          _functionality - list all the flights from the database for the customer and return using fetchall()_
   
   3. **customer_booking_flight_ticket** - _functionality - record the data of bookings from the customer_
   
   4.  **customer_cancel_booked_flight** -  _functionality - cancelling booked tickets which update in database_
   
**step-3**: implement admin module in class **admin** with following methods
            
   1. **add_flight_detailst** - _functionality - add flight details to the database_
   
   2. **add_customers** - _functionality - add customers details to the database_
   
   3. **add_bookings** - _functionality - add booking details from admin which should update database_ 
   
   4. **view_bookings** - _functionality - view booking from database _
   
   
   
**step - 4**: go to models.py file and add model for flight database
             
                     
# --------Steps to Solve the Problem---------

## Step1: Make sure you have Required Tools:

           Python latest version

           VS Code IDE with Required Plugins for Java, GIT.

           Git

## Step2: Accessing GITHUB Classroom and submiting Assignment:

       Get the Link for GITHUB Classroom.

       Click and Authorize from your GITHUB account.

       Clone the Repository / open through VSCODE IDE.

       Open stockmanagement.py File to complete code.

       Solve the Problem Statements through code as detailed in Step 3 below.

       Commit the changes to the repositories, 
       labelling each commit numerically (Commit1, Commit2, etc.).

       Each commit will be tested automatically against the relevant testcases, 
       so you may need to submit several commits as you refine your solution.

        Once you are finished with the assignment (either all test cases passed or not),
        make sure to lable this commit as "final commit" 
        (this may mean a previous commit passing and 
        you making a slight edit to the latter in order to mark 
        the next commit as being final).

## Step3: Solving the Problem:

      Read the Problem Statement carefully

      Go to respective files to complete assignment
      
      AS TEST CASES ARE EXECUTED USING AUTOMATION TECHNIQUE, REQUEST TO
      
      STRICTLY FOLLOW BELOW MENTIONED RULES
      
      1. THE REST OF THE CODE PROVIDED TO YOU SHOULD BE KEPT STRICTLY UNTOUCHED.
      
      2. YOUR OWN CODE WOULD COME ONLY INSIDE CLASSES AND METHODS WHICH ARE MENTIONED.
      
      3. THE CLASS NAMES, INTERFACE NAMES, METHOD SIGNATURES AND ATTRIBUTE NAMES SHOULD
      
        NOT BE ALTERED OR MODIFIED AND KEPT STRICTLY UNTOUCHED.
          
    
Note: Every Assignment is being tested with Automation Technique. So Please do follow the points mentioned.

