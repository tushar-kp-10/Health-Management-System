from typing import List, Dict, Optional


def readPatientsFromFile(fileName):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    patients = {}                                   #to store dictonary of the patient data
    try:
        f=open(fileName,'r')                        #open file given in read mode
    except Exception as e:
        print(e)
        exit()                                      #exits program if file is not present
    try:
        file=(f.read()).split()                     #to make into file format
    except:
        print("An unexpected error occurred while reading the file")
    lst1=[]
    numFields=1
    for i in file:
        line=i.split(',')                           
        if len(line)!=8:                            #to check if number of details is as per data or not
            print(f"Invalid number of fields {numFields} in line: {line}")
            continue
        try:                                        #to check if given data are of required data types or not
            temp=float(line[2])                           
            hr=int(line[3])
            rr=int(line[4])
            sbp=int(line[5])
            dbp=int(line[6])
            spo2=int(line[7])
        except:
            print(f"Invalid data type in line: {line}")
            continue
        #Can check data type validation in this method too
        if (isinstance(line[1],str) and isinstance(temp,float) and isinstance(hr,int) and isinstance(rr,int) and isinstance(sbp,int) and isinstance(dbp,int) and isinstance(spo2,int)):
            pass
        else:
            print(f"Invalid data type in line: {line}")
            continue
        list2=[]
        list2.append(line[1])

        #Checking the optimal cases for all the data as per human limits
        
        if temp>=35 and temp<=42:                      
            list2.append(temp)
        else:
            print(f"Invalid temperature value {line[2]} in line: {line}")
            continue
        if hr>=30 and hr<=180:                      
            list2.append(hr)
        else:
            print(f"Invalid  heart rate value {line[3]} in line: {line}")
            continue
        if (rr>=5 and rr<=40):                      
            list2.append(rr)
        else:
            print(f"Invalid respiratory rate value {line[4]} in line: {line}")
            continue
        if sbp>=70 and sbp<=200:                     
            list2.append(sbp)
        else:
            print(f"Invalid systolic blood pressure value {line[5]} in line: {line}")
            continue
        if dbp>=40 and dbp<=120:                      
            list2.append(dbp)
        else:
            print(f"Invalid diastolic blood pressure value {line[6]} in line: {line}")
            continue
        if spo2>=70 and spo2<=100:                      
            list2.append(spo2)
        else:
            print(f"Invalid oxygen saturation value {line[7]} in line: {line}")
            continue
        lst1=patients.get(int(line[0]))             #Joining all the visits of a single patient into dictonary in list format
        if lst1==None:                             
            lst3=[]
            patients[int(line[0])]=lst3
        lst3.append(list2)                          #To make it into a list of lists format
        patients[int(line[0])]=lst3
        numFields+=1
    #print(patients)     
    return patients                                 





def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
   
    if patientId not in patients and patientId!=0:  #if patientId inputted by user is present in the dictonary or if it is 0 then valid
        print(f"Patient with ID {patientId} not found")
    else:
        if patientId==0:                            #0 refers printing all the data
            for i in patients:                     
                print(f"Patient Id : {i}\n")
                k=patients.get(i)                   
                for j in k:                         
                    print(f" Visit Date : {j[0]}\n  Temperature : {j[1]}\n  Heart Rate : {j[2]}\n  Respiratory Rate : {j[3]}\n  Systolic Blood Pressure : {j[4]}\n  Diastolic Blood Pressure : {j[5]}\n  Oxygen Saturation : {j[6]}\n")
                print("\n\n")
        else:                                       #Else part for particular patient
            print(f"Patient Id : {patientId}\n")
            k=patients.get(patientId)               
            for j in k:                             
                print(f" Visit Date : {j[0]}\n  Temperature : {j[1]}\n  Heart Rate : {j[2]}\n  Respiratory Rate : {j[3]}\n  Systolic Blood Pressure : {j[4]}\n  Diastolic Blood Pressure : {j[5]}\n  Oxygen Saturation : {j[6]}\n")
            print("\n\n")



              

def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.
    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """

    import math
    try:                                            #If patiendId can be converted to int code will run else error
        patientId=int(patientId)
    except:
        print("Error: 'patientId' should be an integer.")
        return
    if isinstance(patients,dict):                   #To check if patients is in dictonary foamt or not
        pass
    else:                                           
        print ("Error: 'patients' should be a dictionary.")
        return
    if patientId not in patients and patientId!=0:  #if patientId inputted by user is present in the dictonary or if it is 0 then valid
        print(f"Patient with ID {patientId} not found")
    else:
        if patientId==0:                            #if patientId is 0 display average of all patient's data
            temp=0                                  #Initializing all stats to 0 to take total  
            hr=0                                     
            rr=0                                     
            sbp=0                                     
            dbp=0                                     
            spo2=0                                     
            count=0                                 
            print("Vital Signs for all patients :")
            for i in patients:                                    
                k=patients.get(i)                  
                for j in k:                         
                    count+=1                       
                    temp+=j[1]                        #\
                    hr+=j[2]                           #\
                    rr+=j[3]                            #\-----> Sum all values in list j in their respective places to get total temp,hr,rr,sbp,dbp,spo2
                    sbp+=j[4]                           #/----/
                    dbp+=j[5]                          #/
                    spo2+=j[6]                        #/
            print(f"  Average Temperature : {round(temp/count,2)} C\n  Average Heart Rate : {round(hr/count,2)} bpm\n  Average Respiratory Rate : {round(rr/count,2)} bpm\n  Average Systolic Blood Pressure : {round(sbp/count,2)} mmHg\n  Average Diastolic Blood Pressure : {round(dbp/count,2)} mmHg\n  Average Oxygen Saturation : {round(spo2/count,2)} %")
        else:
            print(f"Vital Signs for patient {patientId} :")                               
            k=patients.get(patientId)               
            count=0                                   #To count number of iteration                   
            temp=0                                    #Initializing all stats to 0 to take total  
            hr=0                                     
            rr=0                                     
            sbp=0                                     
            dbp=0                                     
            spo2=0                                     
            for j in k:                             
                count+=1                           
                temp+=j[1]                            #\
                hr+=j[2]                               #\
                rr+=j[3]                                #\-----> Sum all values in list j in their respective places to get total temp,hr,rr,sbp,dbp,spo2
                sbp+=j[4]                               #/----/
                dbp+=j[5]                              #/
                spo2+=j[6]                            #/
            print(f"  Average Temperature : {temp/count} C\n  Average Heart Rate : {hr/count} bpm\n  Average Respiratory Rate : {rr/count} bpm\n  Average Systolic Blood Pressure : {sbp/count} mmHg\n  Average Diastolic Blood Pressure : {dbp/count} mmHg\n  Average Oxygen Saturation : {spo2/count} %")



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """
    import re                                      # \
    reg=re.compile(r"^\d{4}-\d{2}-\d{2}$")          # \
    if re.fullmatch(reg,date):                       # \
        pass                                          # |----> To validate if the format of date inputted is correct or not
    else:                                            # /
        print("Invalid date format")                # /
        return                                     # /
    j=date                                         
    ye=int(j[0]+j[1]+j[2]+j[3])                    #To take parts from date string and convert as integer
    mon=int(j[5]+j[6])                             
    day=int(j[8]+j[9])                             
    lst=[]
    
    #Checking the valid conditions for datas
    
    if ye>=1900 and mon>=1 and mon<=12 and day<=31 and day>=1 :
        lst.append(date)                           
    else:
        print("Invalid date. Please enter a valid date.")
        return
    if temp>=35.0 and temp<=42.0:
        lst.append(temp)                           
    else:
        print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        return
    if hr>=30 and hr<=180:
        lst.append(hr)                             
    else:
        print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        return
    if rr>=5 and rr<=40:
        lst.append(rr)                             
    else:
        print("Invalid respiration rate. Please enter a respiratory rate between 5 and 40 bpm.")
        return
    if sbp>=70 and sbp<=200:
        lst.append(sbp)                            
    else:
        print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg")
        return
    if dbp>=40 and dbp<=120:
        lst.append(dbp)                            
    else:
        print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        return
    if spo2>=70 and spo2<=100:
        lst.append(spo2)                           
    else:
        print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
        return
    try:                                           
        file=open(fileName,'w')                    
        ids=[]                                   
        if patientId in patients:                  
            ids=patients.get(patientId)           
        ids.append(lst)                            
        patients[patientId]=ids                    
        for i in patients:                         
            for j in patients.get(i):              
                k=str(i)                              # \
                date=str(j[0])                         # \
                temp=str(j[1])                          # \
                hr=str(j[2])                             # |---->To convert all values of the list j into string as we have to write into a file
                rr=str(j[3])                             # |---/
                sbp=str(j[4])                           # /
                dbp=str(j[5])                          # /
                spo2=str(j[6])                        # /
                st=""                              
                st=(k+","+j[0]+","+temp+","+hr+","+rr+","+sbp+","+dbp+","+spo2+"\n")
                file.write(st)                           #Write the string st into our file
        print(f"---->Visit saved for Patient # {patientId}")
    except:                                        
        print("An unexpected error occurred while adding new data.")
        
 
        



def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """
    visits = []
    if (patients=={} or (year==None and month !=None)):      #Error cases:- If patient dictonary is empty or month given without any year
        return visits
    else:
        if year==None and month ==None :                     #To print all data if no month and no year given
            for i in patients:                               
                lst=[]
                for j in patients.get(i):                    
                    ye=int(j[0][0]+j[0][1]+j[0][2]+j[0][3])  
                    mon=int(j[0][5]+j[0][6])                 
                    day=int(j[0][8]+j[0][9])                 
                    if mon<=12 and day<=31 :                 
                        lst=(i,j)
                        visits.append(lst)                   
        elif year!=None and month ==None :                   #All matched data of a year when no specific month given
            for i in patients:                               
                lst=[]
                for j in patients.get(i):                    
                    ye=int(j[0][0]+j[0][1]+j[0][2]+j[0][3])  
                    mon=int(j[0][5]+j[0][6])                 
                    day=int(j[0][8]+j[0][9])                 
                    if mon<=12 and day<=31 and year==ye:     
                        lst=(i,j)
                        visits.append(lst)                   
        elif year!=None and month != None :                  #All matched data of a specified year and month
            for i in patients:                               
                lst=[]
                for j in patients.get(i):                    
                    ye=int(j[0][0]+j[0][1]+j[0][2]+j[0][3])  
                    mon=int(j[0][5]+j[0][6])                 
                    day=int(j[0][8]+j[0][9])                 
                    if mon<=12 and day<=31 and year==ye and month==mon:
                        lst=(i,j)
                        visits.append(lst)                   #appends the list data to our main list visits
        else :
            pass
    return visits


def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """
    followup_patients = []                  #To store patient's id who needs follow up
    for i in patients:                           
        for j in patients.get(i):           
            if (j[2]>100 or j[2]<60 or j[4]>140 or j[5]>90 or j[6]<90):            #Check cases if patient needs followup
                followup_patients.append(i)         
                break
    return followup_patients


def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """
    if patientId not in patients:                #If patientId not present in database print error
        print (f"No data found for patient with ID {patientId}")
    else:
        file=open(filename,'w')                  #Open given file in write mode
        patients.pop(patientId)                  #Remove the patient details to be removed
        for i in patients:                       
            for j in patients.get(i):            
                k=str(i)                            # \
                date=str(j[0])                       # \
                temp=str(j[1])                        # \
                hr=str(j[2])                           # |----->To convert all values of the list j into string as we have to write into a file
                rr=str(j[3])                           # |----/
                sbp=str(j[4])                         # /
                dbp=str(j[5])                        # /
                spo2=str(j[6])                      # /
                st=""                            
                st=(k+","+j[0]+","+temp+","+hr+","+rr+","+sbp+","+dbp+","+spo2+"\n")
                file.write(st)                   #Write the string st into our file
        print(f"---->Data for Patient {patientId} has been deleted")



###########################################################################
###########################################################################
#                                                                         #
#   The following code is being provided to you. Please don't modify it.  #
#                                                                         #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
