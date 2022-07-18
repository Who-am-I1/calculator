#Qoidalar

print("""\nUshbu dastur Nodirbek tomonidan ishlab chiqildi.

Qoidalar:

   1.Raqam so'ralgan joyiga faqat butun sonlarni kiriting.

   2.Amal so'ralgan joyiga esa faqat belgilangan amallarni kiriting.

   

Belgilangan amallar:Qo'shish'+',  ayirish'-',  ko'paytirish'*',  bo'lish':' amallari.""")

#Dasturni takrorlanishi

takror=int(input("\nSiz Calculatorimizdan necha martda foydalanmoqchisiz:"))

scor=0  #Dasturni hissobi

while scor!=takror:   #Dasturni necha martda takrorlanganini hisoblovchi

        r=str(input("Raqam:"))

        ra=str(input("Raqam:"))

        b=str(input("Amalni tanglang:"))

        s=float(r)

        ss=float(ra)

        a=str(b)

        if a=="+":

                print(f"Javob:",s+ss)

        elif a=="-":

                print(f"Javob:",s-ss)

        elif a=="*":

                print(f"Javob:",s*ss)

        elif a==":":

                print(f"Javob:",s/ss)

        elif a!="+" and a!="-" and a!="*" and a!=":":   #Agar amalda +  -  *  :  belgilari bo'lmasam foydalanuvchiga ogohlantirish berish

                print("Siz noto'g'ri amal tanladingiz")

 

             

        scor+=1  #Agar dastur 0martadan ko'p takrorlanmoqchi bo'lsa bu unga bir martda takrorlandi uni hisobiga 1qo'sh deydi

       

        if scor==takror:  #Dasturni takrorlanish miqdori necha martda bo'lsa usha miqdorga yetib kelding to'xta deydi

            print("""

Bizning xizmatlarimizdan

foydalanganingiz uchun raxmat""")   #Dastur ohirida foydalanuvchiga tashshakkur
