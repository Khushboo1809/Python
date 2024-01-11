# class test :
#     a = 20
#     def disp():
#         print ("value of a =",test.a)
#     def check (a,b):
#         if a>b:
#             print("highest:",a)
#         else :
#             print("highest",b)
# x=test
# x.disp()   
# x.check(15,120)     

class test :
    a = 20
    def disp(self):
        print ("value of a =",test.a)
    def check (self,a,b):
        if a>b:
            print("highest:",a)
        else :
            print("highest",b)
x=test()
x.disp()   
x.check(15,120)  