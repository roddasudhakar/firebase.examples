from firebase.firebase import FirebaseApplication
fb=FirebaseApplication("https://chotu-56c8c.firebaseio.com/")
re=fb.get("admin",None)
print(re)