def admin_required(func):
   def wrapper(user,pin):
       if user!="admin":
           raise Exception("you are not allowed")
       else:
           return func(user,pin)
   return wrapper
# @admin_required
#     mypin=pin
#     return mypin

@admin_required
def delete_account(user,acno):
    return str(acno)+"deleted"

print(change_pin("user1",1000))