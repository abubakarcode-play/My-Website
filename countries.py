class Pakistan():
    def capital(self):
        print("lslamabad is the capital of Pakistan.")
    def language(self):
            print("Urdu is the most widely sopken language in Pakistan.")   
    def type(self):
         print('Pakistan is a developing country.')

class Palestine():
    def capital(self):
          print("Jerusalem is the capital of Palestine.")

    def language(self):
         print("Arabic is widely spoken in Palestine.")

    def type(self):
         print("Palestine is a developed country")

obj_pak = Pakistan()
obj_pal = Palestine()

for country in(obj_pak, obj_pal):
     country.capital()
     country.language()
     country.type()