from student_address_task_import_file import *

adr_list=[]
stu_list=[]

while True:
    while True:
        option=input('---------Options----------\n'
              '1.Address \n'
              '2.Student \n'
              '3.Exit \n'
              'Choose your Option: ')
        try:
            option_check(option)
            option=int(option)
            break
        except OptionError as msg:
            print(msg)
   
    if option==1:
        while True:
            while True:
                address_option=input('-------Address Options---------\n'
                      '1.Create Address \n'
                      '2.Update Address \n'
                      '3.Delete Address \n'
                      '4.Show Address \n'
                      '5.Back to Options :')
               
                try:
                    address_option_check(address_option)
                    address_option=int(address_option)
                    break
                except AddressOptionError as msg:
                    print(msg)


            if address_option==1:
                while True:
                    n=input('How many addresses you want to add: ')
                    try:
                        integer_check(n)
                        n=int(n)
                        break
                    except IntegerError as msg:
                        print(msg)
                i=1
                for x in range(n):
                    print(f'Address {i}:')
                    a=Address()
                    a.setCity(input('enter city: '))
                    while True:
                        p=input('enter pincode:  ')
    
                        try:
                            pincode_check(p)
                            p=int(p)
                            break
                        except PincodeError as msg:
                            print(msg)
                            
                    a.setPin(p)
                    adr_list.append(a)
                    i+=1
                    
                    

            elif address_option==2:
                if adr_list:
                    while True:
                        while True:
                            update_option=input('-------Address Update Options---------\n'
                                                  '1.Update by City \n'
                                                  '2.Update by Pincode \n'
                                                  '3.Back to Address Option :  ')
                        
                            try:
                                option_check(update_option)
                                update_option=int(update_option)
                                break
                            except OptionError as msg:
                                print(msg)

                        if update_option==1:
                            while True:
                                old_address=input('Enter old City to Update: ')
                                try:
                                    Name_check(old_address)
                                    break
                                except Name_Error as msg:
                                    print(msg)

                            for x in adr_list:
                                if x.getCity()==old_address:
                                    new_address=input('Enter new address: ')
                                    x.setCity(new_address)
                                    z=adr_list.index(x)
                                    adr_list.remove(x)
                                    adr_list.insert(z,x)
                                    print(f'Successfully updated address {old_address} to {new_address}')
                                    break
                                    
                            else:
                                print(f' Address {old_address} does not exist')
                                    
                        elif update_option==2:
                            old_pincode=int(input('Enter old Pincode to Update: '))
                            for x in adr_list:
                                if x.getPin()==old_pincode:
                                    new_pincode=int(input('Enter new pincode: '))
                                    x.setPin(new_pincode)
                                    z=adr_list.index(x)
                                    adr_list.remove(x)
                                    adr_list.insert(z,x)
                                    print(f'Successfully updated address {old_pincode} to {new_pincode}')
                                    break
                            else:
                                print(f'Pincode {old_pincode} does not exist')
                                
                        elif update_option==3:
                            break
                              
                else:
                    print('Please add address  first')
                

            elif address_option==3:
                if adr_list:
                    while True:
                        while True:
                            delete_option=input('-------Address Delete Options---------\n'
                                                  '1.Delete by City \n'
                                                  '2.Delete by Pincode \n'
                                                  '3.Back to Address Option :')

                            try:
                                option_check(delete_option)
                                delete_option=int(delete_option)
                                break
                            except OptionError as msg:
                                print(msg)

                        if delete_option==1:
                            print('Which of the following city you want to delete?')
                            i=1
                            for city in adr_list:
                                print(f'city {i}:{city.getCity()}')
                                i+=1
                            city=input('Enter City to Delete: ')

                            for x in adr_list:
                                if x.getCity()==city:
                                    adr_list.remove(x)
                                    print(f'Address with city {city} has been deleted Successfully')
                                    break
                                    
                            else:
                                print(f' Address with city {city} does not exist')
                                    
                        elif delete_option==2:
                            print('Which of the following Address with given Pincode you want to delete?')
                            i=1
                            for pincode in adr_list:
                                print(f'Pincode {i}:{pincode.getPin()}')
                                i+=1
                            pincode=int(input('Enter Pincode of Address to Delete: '))
                            for x in adr_list:
                                if x.getPin()==pincode:
                                    adr_list.remove(x)
                                    print(f'Address with pincode {pincode} has been deleted Successfully')
                                    break
                            else:
                                print(f'Addresss with Pincode {pincode} does not exist')
                                
                        elif delete_option==3:
                            break
                        
                        else:
                            print('choose from above options only')

                else:
                    print('Please add address  first')
                

            elif address_option==4:
                if adr_list:
                    i=1
                    for x in adr_list:
                        print(f' Address {i}-> City:{x.getCity()} , Pincode:{x.getPin()}')
                        i+=1
                else:
                    print('Please add address  first')
                    

            elif address_option==5:
                break
            else:
                print('Choose option from above')  
            
    elif option==2:
        while True:
            while True:
                student_option=input('----------Student Option-------------\n'
                                          '1.Create Student \n'
                                          '2.Update Student \n'
                                          '3.Delete Student \n'
                                          '4.Show Student \n'
                                          '5.Show Student by marks(descending)\n'
                                          '6.Back to Options: ')
                try:
                    student_option_check(student_option)
                    student_option=int(student_option)
                    break
                except StudentOptionError as msg:
                    print(msg)

            if student_option==1:
                if adr_list:
                    n=int(input('How many students you wish to add: '))
                    for x in range(n):
                        s=Student()
                        s.setRn(int(input('Enter Roll NO: ')))
                        s.setName(input('Enter Name: '))
                        s.setMarks(float(input('Enter Marks: ')))
                        print('plese add anyone city of the following: \n')
                        i=1
                        for x in adr_list:
                            print(f'city {i}: {x.getCity()}')
                            i+=1
                        
                        while True:
                            city=input('Enter city: ')
                            try:
                                city_check(city,adr_list)
                                break
                            except City_Not_Found_Error as msg:
                                print(msg)

                        for x in adr_list: 
                            if x.getCity()==city:
                                s.setAddress(x)
                                stu_list.append(s)
                                print('Student has been added Successfully')  
                else:
                    print('please add address first')

            elif student_option==2:
                if stu_list: 
                    while True:
                        n=input('Enter RollNo of student you want to update: ')
                        try:
                            Rn_check(n,stu_list)
                            n=int(n)
                            break
                        except Rn_Not_Found_Error as msg:
                            print(msg)

                    for x in stu_list:   
                        if x.getRn()==n:
                            print(f'this is the student details you want to update: ,RollNo:{x.getRn()},Name:{x.getName()},Marks:{x.getMarks()},Address:{x.getAddress()}')
                            x.setName(input('Enter Updated Name: '))
                            x.setMarks(float(input('Enter Updated Marks: ')))
                            while True:
                                city=input('Enter city: ')
                                try:
                                    city_check(city,adr_list)
                                    break
                                except City_Not_Found_Error as msg:
                                    print(msg)
                            for a in adr_list:
                                if a.getCity()==city:
                                    x.setAddress(a)
                                    print('student details updated Successfully')        
                            
                else:
                    print('please add student first')
                
            elif student_option==3:
                if stu_list:
                    stu_rn=int(input('Enter RN to Delete: '))
                    for x in stu_list:
                        if x.getRn()==stu_rn:
                            stu_list.remove(x)
                            print(f'Student with RollNo {stu_rn} has been deleted Successfully')
                            break
                    else:
                        print(f'Student with RollNo {stu_rn} does not exist')
                else:
                    print('Please add student first')
                


            elif student_option==4:
                if stu_list:
                    i=1
                    for x in stu_list:
                         print(f' Student {i}-> Rn:{x.getRn()} , Name:{x.getName()} ,Marks:{x.getMarks()},Address:{x.getAddress()}')
                         i+=1    
                    
                else:
                    print('Please add Students first')

            elif student_option==5:
                if stu_list:
                    mark_list=[]
                    for x in stu_list:
                        mark_list.append(x.getMarks())
                    mark_list.sort(reverse=True)
                    i=1
                    for y in mark_list:
                        for x in stu_list:
                            if x.getMarks()==y:
                                print(f' Student {i}-> Rn:{x.getRn()} , Name:{x.getName()} ,Marks:{x.getMarks()},Address:{x.getAddress()}')
                                i+=1
                        
                        
                        
                    
                else:
                    print('Please add Students first')
                    

            elif student_option==6:
                break


    elif option==3:
         break
            
     
       
        

    

    
          
    
              
    
