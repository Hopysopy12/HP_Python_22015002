try: 
   userIn = int(input("Enter : "))

   if n%2!=0:
      for i in range(userIn):
          for j in range(i):
              print(" ", end="")
          for j in range(userIn-i):
              print("*", end=" ")
          print()
   else:
       print("Should be an odd number")
except:
    print("Enter number only")
