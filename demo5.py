from firebase.firebase import FirebaseApplication
fb=FirebaseApplication("https://chotu-56c8c.firebaseio.com/")
mid=input("enter mobile id:")
mname=input("enter mobile name:")
mprice=input("enter mobile price:")
d1={"mobilename":mname,"price":mprice}
fb.put("merchant/mobiles/normal",mid,d1)
print("normala mobile details saved")
