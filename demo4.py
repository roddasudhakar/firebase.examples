from firebase.firebase import FirebaseApplication
fb=FirebaseApplication("https://chotu-56c8c.firebaseio.com/")
uname=input("enter user name:")
upass=input("enter password:")
d1={"username":uname,"password":upass}
res=fb.put("merchant","admin",d1)
print("successfully admin name pass saved")
