'''
* This program is free software; you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation; either version 2 of the License, or
* (at your option) any later version.
*  
*   awscli.py
*   Author: Charan Nareddula  (charan9331@gmail.com)
*
'''
import boto3
import time
import pprint


dict ={}


def printallvms():
    print(dict )
    
def printvm(id):
    print("dict value... :",dict[id])
    
'''


TODO-3: vm create 
TODO-4: Getting CLear status info of instances : how long its been running, when it is created etc, 
TODO-5: get the billing information

'''

def mylist(awsdict): 
   
    count=10
    for each_in in awsdict['Reservations']:
        print(count,":  ",each_in['Instances'][0]['InstanceId'],";;",each_in['Instances'][0]['State'])
        dict[str(count)]= each_in['Instances'][0]['InstanceId']
        count=count+1
def startvm():
    print("start")
   
    
def main():

    session = boto3.Session( region_name='us-east-2')
    ec2_con = boto3.resource('ec2', region_name='us-east-2')

    ec2 =session.client(service_name="ec2")
    
    awsdict = ec2.describe_instances();
   
    while True:
        input1 = input(">>") 
        if input1=='l':
            mylist(awsdict)
            continue
            
        if input1=='r':
            awsdict = ec2.describe_instances();
            mylist(awsdict)
            continue
        
        if input1=='s':
            input2 = input("Enter the instance id: ") 
            
            print("starting this instance: ",dict[input2])
            for each in ec2_con.instances.filter(Filters=[{'Name': 'instance-id', "Values": [dict[input2]]}]):
                each.start()
            continue
            
        if input1=='h':
            print("s - start\n l- list \n e- exit \n t - Terminate \n r- Refresh ")
            continue
            
        if input1=='e':
            print("exiting ")
            break
            
        if input1=='t':
            input2 = input("Enter the instance id: ") 
            
            print("terminating this instance: ",dict.get(input2))
            if dict.get(input2)==None:
                print("ERROR: Instance doesnt exist ")
                continue
            for each in ec2_con.instances.filter(Filters=[{'Name': 'instance-id', "Values": [dict.get(input2)]}]):
                ret=each.stop()
                print("returning :",ret)
            continue
        
        try:  
            val = int(input1)
            instid = (dict.get(input1))
            print("mapping:  ",instid)
            for each_in in awsdict['Reservations']:
                if instid == each_in['Instances'][0]['InstanceId']:
                    print(count,":  ",each_in['Instances'][0])
            
        except ValueError: 
            print("ERROR: It is not a number")
                
            
        
   
        
        
if __name__ == '__main__':
    main()

