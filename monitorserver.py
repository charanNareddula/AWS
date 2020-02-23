import boto3
import time

AWS_ACCESS_KEY_ID = "AKIA3HNPFT27M5BCNN5N"
AWS_SECRET_ACCESS_KEY = "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"
dict ={}
def printallvms():
    print(dict )
    
def printvm(id):
    print("dict value... :",dict[id])
    
    
def main():
    session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    
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

