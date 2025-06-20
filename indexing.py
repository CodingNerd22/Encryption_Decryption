password=input("Enter the Data= ")
convert_in_form='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
key=5
encrypt=''
decrypt=''
for i in password:
    initial_password=convert_in_form.find(i)
    final_password=(initial_password+5)%62
    encrypt+=convert_in_form[final_password]
print("Encrypted String = ",encrypt)
for i in encrypt:
    initial_pass=convert_in_form.find(i)
    final_pass=(initial_pass-5)%62
    decrypt+=convert_in_form[final_pass]
print("Decrypted String =",decrypt)