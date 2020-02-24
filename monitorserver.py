'''
* This program is free software; you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation; either version 2 of the License, or
* (at your option) any later version.
* monitorserver.py
*   Author: Charan Nareddula  (charan9331@gmail.com)
*
'''

import boto3
import time

dict ={}
def printallvms():
    print(dict )
    
def printvm(id):
    print("dict value... :",dict[id])
    
    
def main():
    session = boto3.Session()
    
    ec2 = session.resource('ec2', region_name='us-east-2')
    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running','stopped']}])
    #for instance in instances:
            #dict[instance.id] = {'name': 'test', 'id':instance.id, 'state':instance.state}     
    printallvms()
    print ("running inifinity loop")
 
    while True:
        printallvms()
        
    
        for instance in instances:
            vm = dict.get(instance.id)
           # print("inside for loop")
            #print ('AWS', vm)
            if vm==None:
                dict[instance.id] = {'name': 'test', 'id':instance.id, 'state': instance.state}
                print("adding new vm to dictionary")
                continue
    
            #print("while from dict .aaa...: ",vm['state']['Name'])
            #print(instance.state['Name'])
            if vm['state'] != instance.state:
                #print('both are same')
                printvm(instance.id)
                vm['state']= instance.state
            
        time.sleep(5)
        
        
 
        
        
if __name__ == '__main__':
    main()

