import random

# Database untuk menyimpan Akun untuk Sementara
database = {}

def generate_account_number():
    return str(random.randint(1000, 9999))

def register():
    print("====== Daftar akun ATM ======")
    first_name = input("Nama depan             : ")
    last_name = input("Nama belakang          : ")
    pin = input("Masukkan PIN (4 digit) : ")

    account_number = generate_account_number()
    database[account_number] = {
        'first_name': first_name,
        'last_name': last_name,
        'pin': pin,
        'balance': 0
    }

    print(f"Akun Anda telah terdaftar. Nomor akun Anda adalah {account_number}.")
    print("")

def login():
    print("====== Masuk ke akun ATM ======")
    account_number = input("Nomor akun  : ")
    pin = input("PIN         : ")

    if account_number in database and database[account_number]['pin'] == pin:
        print("Selamat datang", database[account_number]['first_name'],"",database[account_number]['last_name'])
        print("")
        atm_menu(account_number)
    else:
        print("Nomor akun atau PIN salah. Silakan coba lagi.")
        print("")

def atm_menu(account_number):
    while True:
        print("====== Menu ATM ======")
        print("1. Cek Saldo")
        print("2. Penarikan")
        print("3. Setoran")
        print("4. Transfer")
        print("5. Keluar")
        print("======================")
        choice = input("Pilih tindakan                : ")

        if choice == "1":
            check_balance(account_number)
        elif choice == "2":
            withdraw(account_number)
        elif choice == "3":
            deposit(account_number)
        elif choice == "4":
            transfer(account_number)
        elif choice == "5":
            print("Terima kasih. Selamat tinggal.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def check_balance(account_number):
    balance = database[account_number]['balance']
    print(f"Saldo Anda adalah   : Rp.{balance}")
    print("")

def withdraw(account_number):
    amount = float(input("Jumlah yang akan ditarik  : Rp."))
    if amount > 0 and amount <= database[account_number]['balance']:
        database[account_number]['balance'] -= amount
        print(f"Anda telah menarik Rp.{amount}. Saldo baru Anda adalah Rp.{database[account_number]['balance']}.")
        print("")
    else:
        print("Penarikan gagal. Pastikan saldo mencukupi dan jumlah valid.")
        print("")

def deposit(account_number):
    amount = float(input("Jumlah yang akan disetor      : Rp. "))
    if amount > 0:
        database[account_number]['balance'] += amount
        print(f"Anda telah melakukan setoran sebesar Rp.{amount}. Saldo baru Anda adalah Rp.{database[account_number]['balance']}.")
        print("")

def transfer(account_number):
    target_account = input("Nomor akun tujuan   : ")
    if target_account in database:
        amount = float(input("Jumlah yang akan ditransfer   : Rp."))
        if amount > 0 and amount <= database[account_number]['balance']:
            database[account_number]['balance'] -= amount
            database[target_account]['balance'] += amount
            print(f"Anda telah mentransfer Rp.{amount} ke akun {target_account}.")
            print("")
        else:
            print("Transfer gagal. Pastikan saldo mencukupi dan jumlah valid.")
            print("")
    else:
        print("Nomor akun tujuan tidak valid.")
        print("")

# Contoh penggunaan:
while True:
    print("====== Selamat datang di ATM Sederhana ======")
    print("1. Daftar Akun")
    print("2. Masuk ke Akun")
    print("3. Keluar")
    print("======================")
    choice = input("Pilih tindakan  : ")
    print("")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Terima kasih. Selamat tinggal.")
        print("")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
