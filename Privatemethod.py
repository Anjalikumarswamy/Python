class someClass:
    def public(self):
        print("This is a Public Function")

    def __private(self):   # __ for private method
        print("This is a Private Function")

obj = someClass()
obj.public() 
obj._someClass__private()  #calling private function.