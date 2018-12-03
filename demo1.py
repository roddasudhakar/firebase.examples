from firebase.firebase import FirebaseApplication
fb=FirebaseApplication("https://chotu-56c8c.firebaseio.com/")
d1={"username":"sudha@4242","password":"chotu@4242"}
fb.put("admin","login",d1)

