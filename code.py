import sqlite3
import os



 #conncetion
conn = sqlite3.connect('data.db')

#data insertation and deletion variable call data 
data= conn.cursor()

opt = int(input("Show Data press 1 Or Insert Data Press 2 Or Delete All Press 3 : "))


if opt == 1:
    os.system("CLS")
    print("\t Data Displayed Sucess Fully")
    data.execute("Select * From Login")
    print("\t" ,data.fetchall())
      
elif(opt == 2):

  
        os.system("CLS")
        print("\tInsert The Data")
        item1 = int(input("\tEnter An Id: ")) 
        item2 = str(input("\tEnter the Username: "))
        item3 = str(input("\tEnter Password: "))
        
  
        

        # inserting data
        data.execute("Insert into Login (id ,username,password) values(?,?,?)",(item1,item2,item3))
        print("Inserted Sucessfully")
        conn.commit()

        option = input("Show Data : ")
        if option == "yes":
            os.system("CLS")
            print("\tData DisplayedSucessfully")
            #printing the data
            print("\t", data.fetchall())
        else:
            os.system("CLS")
            print("\tData Saved")


#deleting the data
else:
    os.system("CLS")
    print("\tData Deleted Sucess Fully")
    data.execute("delete  from Login")
    conn.commit()
    print("\t", data.fetchall())



    
