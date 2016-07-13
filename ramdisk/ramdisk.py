import os



print ("Enter the folder name to be created :")
fName=raw_input()

fPath="/home/keyur/"+fName;

if os.path.exists(fPath):
    print ("Directory Exist !!")
else :
    os.system("mkdir "+fPath)
    
os.system("chmod 777 "+fPath)

os.system("mount -t tmpfs "+fPath+" -o size=12777 "+fPath)

os.system("cp /home/keyur/assgn4/calc/ip.txt "+fPath)
os.system("cp /home/keyur/assgn4/calc/op.txt "+fPath)
os.system("cp /home/keyur/assgn4/calc/calc.py "+fPath)

os.chdir(fPath)

os.system(" python "+fPath+"/calc.py")



