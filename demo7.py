from firebase.firebase import FirebaseApplication
fb=FirebaseApplication("https://chotu-56c8c.firebaseio.com/")
type=input("enter type of mobiles:")
res=fb.get("merchant/mobiles/"+type,None)
for x,y in res.items():
    print(x,y)

