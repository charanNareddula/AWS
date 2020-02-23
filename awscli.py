import boto3
import time
import pprint

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
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name='us-east-2')
    
    #ec2 = session.resource('ec2', region_name='us-east-2')
    #ec2_re=session.resource(service_name= "ec2")  
    ec2 =session.client(service_name="ec2")
    
    awsdict = ec2.describe_instances();
    
    for each_in in awsdict['Reservations']:
        print("AWS instance : ",each_in)
        pprint.pprint(each_in)
        #print(each_in.id,each_in.state['Name'])
        
    '''' 
    printallvms()
    print ("running inifinity loop")
 
    while True:
        printallvms()
        
    
        for instance in instances:
            print ("AWS instance)
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
        
        
''' 
        
        
if __name__ == '__main__':
    main()

