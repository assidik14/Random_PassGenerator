'''Module untuk mengambil karakter dan mengacaknya'''
import random
import string

def gen_password(lenght):
    '''Fungsi Generate Password'''
    letters = string.ascii_letters
    number = string.digits
    symbol = string.punctuation
    str_data = letters+number+symbol
    random_str = "".join(random.choices(str_data, k=lenght))
    return random_str

if __name__ == "__main__":

    while(True):
        try:
            PanjangPassword = int(input("Masukkan Panjang Password = "))
            break
        except ValueError:
            print("Panjang Password Harus Angka!!")
            
    YOUR_PASSWORD = gen_password(PanjangPassword)
    print(f"Your Password Is = {YOUR_PASSWORD}")