'''
* This program is free software; you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation; either version 2 of the License, or
* (at your option) any later version.
* awscli.py
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
    
    
def main():

    session = boto3.Session( region_name='us-east-2')
    
    #ec2 = session.resource('ec2', region_name='us-east-2')
    #ec2_re=session.resource(service_name= "ec2")  
    ec2 =session.client(service_name="ec2")
    
    awsdict = ec2.describe_instances();
    while True:
        print(">>")
        input1 = input() 
        if input1=='l':
            count=1
            for each_in in awsdict['Reservations']:
                print(count,":  ",each_in['Instances'][0]['InstanceId'],";;",each_in['Instances'][0]['State'])
                dict[str(count)]= each_in['Instances'][0]['InstanceId']
                count=count+1
                
        if input1 >='1' and input1 <='9':
            instid = (dict.get(input1))
            print("mapping:  ",instid)
            for each_in in awsdict['Reservations']:
                if instid == each_in['Instances'][0]['InstanceId']:
                    print(count,":  ",each_in['Instances'][0])
            
            
                
            
        
   
        
        
if __name__ == '__main__':
    main()

