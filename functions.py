def fn_name()->None:
   print("called")
   if 2%2==0:
       print("Even")


@fn_name
def msg(e):
    print("Called 2")


