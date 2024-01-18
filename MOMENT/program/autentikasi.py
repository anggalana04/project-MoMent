import os
import json
from datetime import datetime, timezone, timedelta


# Adjust this offset based on your location
local_timezone = timezone(timedelta(hours=7))
current_local_time = datetime.now(local_timezone)

# Format the timestamp as a string
formatted_timestamp = current_local_time.strftime("%Y/%m/%d %H:%M")


class Akun:
    '''class untuk mengatur akun user'''
    data_akun = {}
    data_transaksi = {}

    def __init__(self, data_akun=None, data_transaksi=None):
        self.data_akun = data_akun if data_akun is not None else self.cek_data_user_database()
        self.data_transaksi = data_transaksi if data_transaksi is not None else self.cek_data_transaksi_database()

    def cek_data_user_database(self):
        '''method untuk mengecek file data, jika tidak ada akan terbuat otomatis'''
        data_akun = [{"ID": 0, "NAMA": "", "NAMA_PERUSAHAAN": "",
                      "SALDO_KAS": 0, "SALDO_BANK": 0}]
        if os.path.exists('data/user.json'):
            with open('data/user.json', 'r') as file:
                data_akun = json.load(file)
        else:
            print('Data doesn\'t exist, creating a new folder...')
            os.makedirs('data')
            with open('data/user.json', 'w') as file:
                json.dump(data_akun, file, indent=4)
            print('Folder created!')

        return data_akun

    def cek_data_transaksi_database(self):
        '''method untuk mengecek file data, jika tidak ada akan terbuat otomatis'''
        data_transaksi = {} 
        data_directory = 'data'

        if not os.path.exists(data_directory) or not os.path.isdir(data_directory):
            print(f'{data_directory} doesn\'t exist, creating a new folder...')
            os.makedirs(data_directory)

        transaksi_file_path = os.path.join(data_directory, 'transaksi.json')

        if os.path.exists(transaksi_file_path):
            with open(transaksi_file_path, 'r') as file:
                data_transaksi = json.load(file)
        else:
            print(f'{transaksi_file_path} doesn\'t exist, creating...')
            with open(transaksi_file_path, 'w') as file:
                json.dump({}, file)

        return data_transaksi

    def login(self, InID, InPW):
        access = False
        for user in self.data_akun:
            if user["ID"] == InID and user["PW"] == InPW:
                access = True
                self.InID = InID  # Assuming you want to store the logged-in user ID
                break

        return access, InID

    def registrasi_profil(self, new_id, nama, nama_perusahaan, saldo_kas, saldo_bank):
        # Check if the user ID already exists
        user_exists = any(user["ID"] == new_id for user in self.data_akun)

        if user_exists:
            # Update the profile of an existing user
            for user in self.data_akun:
                if user["ID"] == new_id:
                    user["NAMA"] = nama
                    user["NAMA_PERUSAHAAN"] = nama_perusahaan
                    user["SALDO_KAS"] = int(saldo_kas)
                    user["SALDO_BANK"] = int(saldo_bank)

                    with open('data/user.json', 'w') as file:
                        json.dump(self.data_akun, file, indent=4)

                    return True
        else:
            # Create a new user profile and ID
            new_user = {
                "ID": new_id,
                "NAMA": nama,
                "NAMA_PERUSAHAAN": nama_perusahaan,
                "SALDO_KAS": int(saldo_kas),
                "SALDO_BANK": int(saldo_bank)
            }

            self.data_akun.append(new_user)

            with open('data/user.json', 'w') as file:
                json.dump(self.data_akun, file, indent=4)

            return True

    def registrasi_ID(self, new_id, new_pw):
        # Check if the user ID already exists
        if any(user["ID"] == new_id for user in self.data_akun):
            return False
        else:
            # Register a new user ID
            new_user = {
                "ID": new_id,
                "PW": new_pw,
                "NAMA": "",
                "NAMA_PERUSAHAAN": "",
                "SALDO_KAS": 0,
                "SALDO_BANK": 0
            }

            self.data_akun.append(new_user)

            with open('data/user.json', 'w') as file:
                json.dump(self.data_akun, file, indent=4)

            return True

    def registrasi_profil(self, new_id, nama, nama_perusahaan, saldo_kas, saldo_bank):
        user_exists = any(user["ID"] == new_id for user in self.data_akun)
        if user_exists:
            # Update the profile of an existing user
            for user in self.data_akun:
                if user["ID"] == new_id:
                    user["NAMA"] = nama
                    user["NAMA_PERUSAHAAN"] = nama_perusahaan
                    user["SALDO_KAS"] = int(saldo_kas)
                    user["SALDO_BANK"] = int(saldo_bank)

                    # Save the data immediately after modification
                    self.save_data_to_files()

                    return True
        else:
            # Create a new user profile and ID
            new_user = {
                "ID": new_id,
                "NAMA": nama,
                "NAMA_PERUSAHAAN": nama_perusahaan,
                "SALDO_KAS": int(saldo_kas),
                "SALDO_BANK": int(saldo_bank)
            }

            self.data_akun.append(new_user)

            # Save the data immediately after modification
            self.save_data_to_files()

            return True

    def edit_profil(self, id, new_pw=None, new_nama=None, new_name_company=None):
        for user in self.data_akun:
            if user["ID"] == str(id):
                user["NAMA"] = new_nama
                user["PW"] = new_pw
                user["NAMA_PERUSAHAAN"] = new_name_company

        self.save_data_to_files()

        return True  # Move this line outside the for loop

    def save_data_to_files(self):
        # Saving the updated user data
        with open('data/user.json', 'w') as file:
            json.dump(self.data_akun, file, indent=4)

        # Saving the transaction data
        with open('data/transaksi.json', 'w') as file:
            json.dump(self.data_transaksi, file, indent=2)


class Cashflow(Akun):
    def __init__(self, data_akun=None, data_transaksi=None):
        if data_akun is None:
            data_akun = self.cek_data_user_database()

        if data_transaksi is None:
            data_transaksi = self.cek_data_transaksi_database()

        # Additional initialization for transaction numbers for BANK accounts
        self.data_nomor_transaksi_bank = {}

        super().__init__(data_akun, data_transaksi)

    def get_user_index_by_id(self, user_id):
        for i, user_data in enumerate(self.data_akun):
            if user_data["ID"] == user_id:
                return i
        return -1  # User not found

    def create_transaction_entry(self, user_id, tipe_akun, kategori, jumlah, detail, untuk, dari):
        formatted_timestamp = datetime.now().strftime("%Y/%m/%d %H:%M")

        # Check if the list is not empty before accessing its elements
        transaksi = self.data_transaksi.setdefault(str(user_id), [])

        if transaksi:
            last_transaction = transaksi[-1]
            if isinstance(last_transaction.get("NOMOR"), list):
                # Increment the transaction number based on account type
                nomor_transaksi_terakhir = last_transaction["NOMOR"][1] + 1
            else:
                nomor_transaksi_terakhir = last_transaction.get("NOMOR", 0) + 1
        else:
            # If the list is empty, set the initial value
            nomor_transaksi_terakhir = 1

        # Generating the unique code based on account type
        if tipe_akun == 'BANK':
            nomor_transaksi_terakhir = self.data_nomor_transaksi_bank.setdefault(
                user_id, 1)
            kode_unik = f"{tipe_akun}/{nomor_transaksi_terakhir}"
            # Increment the transaction number for "BANK" account
            self.data_nomor_transaksi_bank[user_id] += 1
        else:
            kode_unik = f"{tipe_akun}/{nomor_transaksi_terakhir}"

        # Update the transaction number in the existing data
        transaksi.append({
            "NOMOR": [kode_unik, nomor_transaksi_terakhir],
            "KATEGORI": kategori,
            "JUMLAH": jumlah,
            "WAKTU": formatted_timestamp,
            "TIPE_AKUN": tipe_akun,
            "DETAIL": detail,
            "UNTUK": untuk,  # Initialize with None
            "DARI": dari    # Initialize with None
        })

        return kode_unik

    def transaksi(self, user_id, tipe_akun, kategori, jumlah, detail, untuk=None, dari=None):
        # Ensure the amount is positive
        if int(jumlah) <= 0:
            print("Invalid transaction amount. Amount must be a positive number.")
            return False

        # Get the user index by ID
        user_index = self.get_user_index_by_id(user_id)

        # If user exists, proceed with the transaction
        if user_index != -1:
            # Incrementing the transaction number and creating a new transaction entry
            kode_unik = self.create_transaction_entry(
                user_id, tipe_akun, kategori, jumlah, detail, untuk, dari)

            # Update the balance data
            if "PENDAPATAN" in kategori:
                # Add the amount for income (PENDAPATAN)
                if tipe_akun == 'KAS':
                    self.data_akun[user_index]["SALDO_KAS"] += int(jumlah)
                elif tipe_akun == 'BANK':
                    self.data_akun[user_index]["SALDO_BANK"] += int(jumlah)
            elif "PENGELUARAN" in kategori:
                # Deduct the amount for expenses (PENGELUARAN)
                if tipe_akun == 'KAS':
                    self.data_akun[user_index]["SALDO_KAS"] -= int(jumlah)
                elif tipe_akun == 'BANK':
                    self.data_akun[user_index]["SALDO_BANK"] -= int(jumlah)

            # Printing the result
            print(kode_unik)

            # Save the updated data to files
            self.save_data_to_files()

            return True

        else:
            print(f"User with ID {user_id} not found.")
            return False