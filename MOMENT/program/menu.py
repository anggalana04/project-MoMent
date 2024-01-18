from rich import print
from autentikasi import Akun, Cashflow
from time import sleep as delay
from rich.prompt import Prompt
from report import Laporan
from BEP_Prototype import Breakevenpoint
import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from dashboard import Dashboard
import Alat


prompt = Prompt()
console = Console()
akun = Akun()
instance_akun = Cashflow()
WHITE_SPACE_VERTICAL = '\t'
WHITE_SPACE_HORIZONTAL = '\n'
user_id = 0


def create_menu_detail(title, subtitle, kategori):
    while True:
        console.clear()
        Alat.mencetak_rule('C A S H  F L O W')
        print(WHITE_SPACE_HORIZONTAL * 3)
        Alat.mencetak_header()
        print(WHITE_SPACE_HORIZONTAL * 2)

        halaman_menu_detail = Panel(f'''
[bold chartreuse1] {kategori} : [/][dim grey7] -[/]
                                        
[bold ] NOMINAL : [/][dim grey7] -[/]
                                        
[bold ] DETAIL : [/][dim grey7] -[/]
                                        
            ''', padding=2, subtitle=f'{subtitle} DETAIL', title=title)

        console.print(halaman_menu_detail, style='bold bright_white',
                      justify='center')
        console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}>> ',
                      style='bold chartreuse1', end=' ')
        data_input = input('')
        print(' ', end=" ")

        console.clear()
        Alat.mencetak_rule('C A S H  F L O W')
        print(WHITE_SPACE_HORIZONTAL * 3)
        Alat.mencetak_header()
        print(WHITE_SPACE_HORIZONTAL * 2)

        halaman_menu_detail = Panel(f'''
[bold ] {kategori} :[/][bold bright_white] {data_input} [/][dim grey7] -[/]
                                        
[bold chartreuse1] NOMINAL : [/][dim grey7] -[/]
                                        
[bold ] DETAIL : [/][dim grey7] -[/]
                                        
            ''', padding=2, subtitle=f'{subtitle} DETAIL', title=title)

        console.print(halaman_menu_detail, style='bold bright_white',
                      justify='center')
        console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}>> ',
                      style='bold chartreuse1', end=' ')
        jumlah = input('')
        print(' ', end=" ")

        console.clear()
        Alat.mencetak_rule('C A S H  F L O W')
        print(WHITE_SPACE_HORIZONTAL * 3)
        Alat.mencetak_header()
        print(WHITE_SPACE_HORIZONTAL * 2)

        halaman_menu_detail = Panel(f'''
[bold ] {kategori} : [/][bold bright_white] {data_input} [/][dim grey7] -[/]
                                        
[bold ] NOMINAL :  [/][bold bright_white] {jumlah} [/][dim grey7] -[/]
                                        
[bold chartreuse1] DETAIL : [/][dim grey7]  -[/]
                                        
            ''', padding=2, subtitle=f'{subtitle} DETAIL', title=title)

        console.print(halaman_menu_detail, style='bold bright_white',
                      justify='center')
        console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}>> ',
                      style='bold chartreuse1', end=' ')
        detail = input('')
        print(' ', end=" ")

        console.clear()
        Alat.mencetak_rule('C A S H  F L O W')
        print(WHITE_SPACE_HORIZONTAL * 3)
        Alat.mencetak_header()
        print(WHITE_SPACE_HORIZONTAL * 2)

        halaman_menu_detail = Panel(f'''
[bold ] {kategori} : [/][bold bright_white] {data_input} [/][dim grey7] -[/]
                                        
[bold ] NOMINAL : [/][bold bright_white] {jumlah} [/][dim grey7]  -[/]
                                        
[bold ] DETAIL : [/][bold bright_white] {detail} [/][dim grey7] -[/]
                                        
            ''', padding=2, subtitle=f'{subtitle} DETAIL', title=title)

        console.print(halaman_menu_detail, style='bold bright_white',
                      justify='center')
        console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 4}APAKAH DATA DIATAS SUDAH BENAR ? [Y/N] >> ',
                      style='bold chartreuse1', end=' ')
        confirm = input('')
        print(' ', end=" ")

        if confirm.lower() == 'y':
            break
        elif confirm.lower() == 'n':
            continue
        else:
            Alat.kode_invalid()

    return data_input, jumlah, detail


def run_reporting_program():
    app = Laporan()
    app.run_sorting()


def run_ringkasan_saldo():
    app = Laporan()
    app.run_ringkasan_saldo()


class Menu:
    def menu_autentikasi():
        """
        Fungsi ini menampilkan halaman autentikasi dan meminta pengguna untuk memilih opsi login, registrasi, atau keluar.
        Returns:
            str: Pilihan yang dipilih oleh pengguna ('1', '2', atau '3').
        """
        while True:
            console.clear()
            Alat.mencetak_rule(' A U T E N T I K A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)

            halaman_autentikasi = Panel('''
[bold chartreuse1]🔐 1.[/] LOGIN [dim grey7]     -[/]

[bold chartreuse1]🆕 2.[/] REGISTRASI [dim grey7]-[/]    

[bold chartreuse1]🚪 3.[/] EXIT[dim grey7]       -[/]
            ''', padding=2, subtitle='PILIH 1 - 3')

            console.print(halaman_autentikasi, style='bold bright_white',
                          justify='center')
            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}>> ',
                          style='bold chartreuse1', end=' ')
            pilihan = input('')

            if pilihan in {'1', '2', '3'}:
                break
            else:
                console.print(
                    f'\n\n{WHITE_SPACE_VERTICAL * 9}   ⚠️ [bold red] KODE INVALID [/]⚠️')
                delay(1)
                console.clear()

        return pilihan

    @staticmethod
    def create_menu_detail_bep():
        console.clear()
        Alat.mencetak_rule('BREAK EVEN POINT')
        print(WHITE_SPACE_HORIZONTAL * 10)

        halaman_unit = Panel(f'''
Berapa banyak unit yang 
dapat diproduksi perusahaan 
dalam 1 bulan? 
''', padding=3)

        console.print(halaman_unit, style='bold bright_white',
                      justify='center')

        console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 8}   UNIT >> ',
                      style='bold chartreuse1', end=' ')
        unit = prompt.ask(' ')
        console.clear()

        Alat.mencetak_rule('BREAK EVEN POINT')
        print(WHITE_SPACE_HORIZONTAL * 10)

        halaman_price_per_unit = Panel(f'''
Berapa harga per unit produk?
''', padding=3)

        console.print(halaman_price_per_unit, style='bold bright_white',
                      justify='center')

        console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 8}   HARGA >> ',
                      style='bold chartreuse1', end=' ')
        harga_per_unit = prompt.ask(' ')
        console.clear()

        Alat.mencetak_rule('BREAK EVEN POINT')
        print(WHITE_SPACE_HORIZONTAL * 10)

        halaman_fixed_cost = Panel(f'''
Masukkan biaya tetap 
(contoh: tagihan wifi, tagihan air, gaji karyawan)
''', padding=3)

        console.print(halaman_fixed_cost, style='bold bright_white',
                      justify='center')

        console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 7}   FIXED COST >> ',
                      style='bold chartreuse1', end=' ')
        fixed_cost = prompt.ask(' ')
        console.clear()

        Alat.mencetak_rule('BREAK EVEN POINT')
        print(WHITE_SPACE_HORIZONTAL * 10)

        variable_cost = Panel(f'''
Masukkan biaya variabel 
(contoh: biaya produksi yang berubah seiring penjualan)
''', padding=3)

        console.print(variable_cost, style='bold bright_white',
                      justify='center')

        console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 8}   VARIABLE COST >> ',
                      style='bold chartreuse1', end=' ')
        variable_cost = prompt.ask(' ')
        console.clear()

        return int(unit), int(harga_per_unit), int(fixed_cost), int(variable_cost)

    def load_user_data():
        try:
            with open("data/bep.json", "r") as file:
                user_data = json.load(file)
            return user_data
        except FileNotFoundError:
            # If the file doesn't exist, raise an exception or log a message
            return []

    def save_user_data(user_data):
        with open("data/bep.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def menu_BEP():
        global user_id
        user_data = Menu.load_user_data()


        user_profile = next(
            (user for user in user_data if user["ID"] == str(user_id)), None)

        if user_profile:
            unit, harga_per_unit, fixed_cost, variable_cost = Menu.create_menu_detail_bep()

            vc_unit = Breakevenpoint.variabel_per_unit(unit, variable_cost)
            bep_unit_hasil = Breakevenpoint.bep_unit(
                harga_per_unit, fixed_cost, vc_unit)
            bep_rupiah_hasil = Breakevenpoint.bep_rupiah(
                harga_per_unit, fixed_cost, vc_unit)

            print(WHITE_SPACE_HORIZONTAL * 12)
            display_text = Text()
            display_text.append(
                f"Break-even Point (in units): {int(bep_unit_hasil):,} units")
            display_text.append(" - ")
            display_text.append(
                f"Break-even Point (in Rupiah): Rp. {float(bep_rupiah_hasil):,.2f}")
            display_text.append(" - ")

            display = Panel(
                display_text, style='bold bright_white', expand=False)
            console.print(display, justify='center')

            save = input('Save data? [y/n] > ')
            if save.lower() == "y":
                # Update or add the user's data in the user_data list
                user_profile["ID"] = str(user_id)
                user_profile["BEP_UNIT"] = bep_unit_hasil
                user_profile["BEP_RP"] = bep_rupiah_hasil
                Menu.save_user_data(user_data)
            elif save.lower() == "n":
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print(f"User with ID {user_id} not found.")
            delay(2)

    def menu_login():
        global user_id
        """
        Fungsi ini menangani proses login pengguna.
        """
        while True:
            Alat.mencetak_rule(' H A L A M A N  L O G I N ')
            print(WHITE_SPACE_HORIZONTAL * 10)

            halaman_login = Panel('''
[bold chartreuse1]ID       :[/][dim grey7] -[/]

[bold chartreuse1]PASSWORD :[/][dim grey7] -[/]    
    
            ''', padding=2, subtitle='Masukan ID')

            console.print(halaman_login, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}   ID >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            InID = input(' ')
            console.clear()
            Alat.mencetak_rule(' H A L A M A N  L O G I N ')
            print(WHITE_SPACE_HORIZONTAL * 10)

            halaman_login = Panel(f'''
[bold chartreuse1]ID       :[/][bold bright_white] {InID}[/][dim grey7] -[/]

[bold chartreuse1]PASSWORD :[/][dim grey7] -[/]    
    
            ''', padding=3, subtitle='Masukan password')

            console.print(halaman_login, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}   PASSWORD >> ',      # INPUT PASSWORD
                          style='bold chartreuse1', end=' ')
            InPW = prompt.ask(' ', password=True)

            console.clear()
            Alat.mencetak_rule(' H A L A M A N  L O G I N ')
            print(WHITE_SPACE_HORIZONTAL * 10)

            halaman_login = Panel(f'''
[bold chartreuse1]ID       :[/][bold bright_white] {InID}[/][dim grey7] -[/]

[bold chartreuse1]PASSWORD :[/] { '*' * len(InPW)}[dim grey7] -[/]    
    
            ''', padding=3, subtitle='Masukan password')

            console.print(halaman_login, style='bold bright_white',
                          justify='center')

            if akun.login(InID, InPW)[0]:
                user_id = str(InID)

                console.print(
                    f'\n\n{WHITE_SPACE_VERTICAL * 8}          ✅[bold green]  LOGIN BERHASIL  [/]✅')
                break
            else:
                console.print(
                    f'\n\n{WHITE_SPACE_VERTICAL * 8}      ⚠️[bold red]  ID ATAU PASSWORD SALAH [/]⚠️')
                delay(2)
                console.clear()

    def menu_registrasi():
        """
        Fungsi ini menangani proses registrasi pengguna.
        """
        while True:
            console.clear()
            Alat.mencetak_rule(' R E G I S T R A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)

            halaman_registrasi = Panel('''
[bold chartreuse1]ID       :[/][dim grey7] -[/]

[bold chartreuse1]PASSWORD :[/][dim grey7] -[/]    
    
            ''', padding=2, subtitle='ID')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 7}   MASUKAN ID BARU >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            InID = input(' ')

            console.clear()
            Alat.mencetak_rule(' R E G I S T R A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)

            halaman_registrasi = Panel(f'''
[bold chartreuse1]ID       :[/][bold bright_white] {InID}[/][dim grey7] -[/]

[bold chartreuse1]PASSWORD :[/][dim grey7] -[/]     
    
            ''', padding=3, subtitle='password')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 6}   Masukan PASSWORD Baru >> ',      # INPUT PASSWORD
                          style='bold chartreuse1', end=' ')
            InPW = input(' ')

            console.clear()

            Alat.mencetak_rule(' R E G I S T R A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold chartreuse1]ID       :[/][bold bright_white] {InID}[/][dim grey7] -[/]

[bold chartreuse1]PASSWORD :[/] {InPW}[dim grey7] -[/]     
    
            ''', padding=3, subtitle='Masukan password')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            if akun.registrasi_ID(InID, InPW):
                console.print(
                    f'\n\n{WHITE_SPACE_VERTICAL * 8}       ✅[bold green]  ID DAPAT DIGUNAKAN  [/]✅')
                delay(2)
                break
            else:
                console.print(
                    f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  ID SUDAH TERDAFTAR [/]⚠️')
                delay(2)

        while True:
            console.clear()
            Alat.mencetak_rule(' R E G I S T R A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold chartreuse1]NAMA     :[/][bold bright_white] [/][dim grey7] -[/]
[bold ]PERUSAHAAN:[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO KAS :[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO BANK:[/][bold bright_white] [/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 7}   MASUKAN NAMA BARU >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            InNAMA = input(' ')

            console.clear()
            Alat.mencetak_rule(' R E G I S T R A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold ]NAMA     :[/][bold bright_white] {InNAMA} [/][dim grey7] -[/]
[bold chartreuse1]PERUSAHAAN:[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO KAS :[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO BANK:[/][bold bright_white] [/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 6}   MASUKAN NAMA PERUSAHAAN BARU >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            In_nama_perusahaan = input(' ')

            console.clear()
            Alat.mencetak_rule(' R E G I S T R A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold ]NAMA     :[/][bold bright_white] {InNAMA} [/][dim grey7] -[/]
[bold ]PERUSAHAAN:[/][bold bright_white] {In_nama_perusahaan} [/][dim grey7] -[/]
[bold chartreuse1]SALDO KAS :[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO BANK:[/][bold bright_white] [/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 6}   MASUKAN SALDO KAS AWAL  >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            In_saldo_kas_awal = input(' ')

            console.clear()
            Alat.mencetak_rule(' R E G I S T R A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold ]NAMA    :[/][bold bright_white] {InNAMA} [/][dim grey7] -[/]
[bold ]PERUSAHAAN:[/][bold bright_white] {In_nama_perusahaan} [/][dim grey7] -[/]
[bold ]SALDO KAS :[/][bold bright_white] {In_saldo_kas_awal} [/][dim grey7] -[/]
[bold chartreuse1]SALDO BANK:[/][bold bright_white] [/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 6}   MASUKAN SALDO REKENING BANK AWAL  >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            In_saldo_bank_awal = input(' ')

            console.clear()
            Alat.mencetak_rule(' R E G I S T R A S I ')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold ]NAMA     :[/][bold bright_white] {InNAMA} [/][dim grey7] -[/]
[bold ]PERUSAHAAN:[/][bold bright_white] {In_nama_perusahaan} [/][dim grey7] -[/]
[bold ]SALDO KAS :[/][bold bright_white] {In_saldo_kas_awal} [/][dim grey7] -[/]
[bold ]SALDO BANK:[/][bold bright_white] {In_saldo_bank_awal}[/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 5}   APAKAH INI SUDAH BENAR?  [Y/N] >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            confirm = input(' ')

            if confirm == 'y' or confirm == 'Y':
                break
            elif confirm == 'n' or confirm == 'N':
                continue
            else:
                console.print(
                    f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  KODE INVALID [/]⚠️')
                delay(2)

        if akun.registrasi_profil(InID, InNAMA, In_nama_perusahaan, In_saldo_kas_awal, In_saldo_bank_awal):
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}       ✅[bold green]  REGISTRASI BERHASIL  [/]✅')
            delay(2)

        else:
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  ID SUDAH TERDAFTAR [/]⚠️')
            delay(2)

    def menu_utama():
        while True:
            console.clear()
            Alat.mencetak_rule('M E N U  U T A M A')
            print(WHITE_SPACE_HORIZONTAL * 3)
            Alat.mencetak_header()
            print(WHITE_SPACE_HORIZONTAL * 2)
            halaman_utama = Panel('''
[bold ]💰 1.[/] INPUT CASHFLOW [dim grey7]     -[/]

[bold ]📑 2.[/] LAPORAN [dim grey7]            -[/]

[bold ]📊 3.[/] Dashboard [dim grey7]          -[/]

[bold ]📈 4.[/] BEP [dim grey7]                -[/]    
                                        
[bold sky_blue1]↩  5.[/] KEMBALI [dim grey7]            -[/]
            ''', padding=2, subtitle='PILIH 1 - 5')

            console.print(halaman_utama, style='bold bright_white',
                          justify='center')
            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}>> ',
                          style='bold chartreuse1', end=' ')
            pilihan = input('')
            print(' ', end=" ")

            if pilihan in {'1', '2', '3', '4', '5', '6'}:
                break
            else:
                console.print(
                    f'\n\n{WHITE_SPACE_VERTICAL * 9}   ⚠️ [bold red] KODE INVALID [/]⚠️')
                delay(1)
                console.clear()

        return pilihan

    def menu_input_cashflow():
        while True:
            console.clear()
            Alat.mencetak_rule('C A S H  F L O W')
            print(WHITE_SPACE_HORIZONTAL * 3)
            Alat.mencetak_header()
            print(WHITE_SPACE_HORIZONTAL * 2)
            halaman_input_cashflow = Panel('''
[bold chartreuse1]💼 1.[/] KAS [dim grey7]     -[/]

[bold chartreuse1]🏦 2.[/] BANK [dim grey7]    -[/]    

[bold sky_blue1]↩  3.[/] KEMBALI [dim grey7] -[/]
        ''', padding=2, subtitle='PILIH 1 - 3', title='PILIH AKUN')
            console.print(halaman_input_cashflow, style='bold bright_white',
                          justify='center')
            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}>> ',
                          style='bold chartreuse1', end=' ')
            pilihan = input('')

            return pilihan

    def menu_pilihan_akun():
        while True:
            console.clear()
            Alat.mencetak_rule('C A S H  F L O W')
            print(WHITE_SPACE_HORIZONTAL * 3)
            Alat.mencetak_header()
            print(WHITE_SPACE_HORIZONTAL * 2)
            halaman_input_cashflow = Panel('''
[bold chartreuse1]⬇   1.[/] PEMASUKAN [dim grey7]       -[/]
                                        
[bold red1]⬆   2.[/] PENGELUARAN [dim grey7]     -[/]  
                                        
[bold sky_blue1]↩   3.[/] KEMBALI [dim grey7]         -[/]
    ''', padding=2, subtitle='pilih 1 - 3')

            console.print(halaman_input_cashflow, style='bold bright_white',
                          justify='center')
            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}>> ',
                          style='bold chartreuse1', end=' ')
            pilihan = input('')

            return pilihan

    def menu_pemasukan_kas():
        dari, jumlah, detail = create_menu_detail(
            'PEMASUKAN KAS', 'PENDAPATAN', 'DARI')
        untuk = None  # There is no "UNTUK" for expenses

        if instance_akun.transaksi(str(user_id), tipe_akun="KAS", kategori="PENDAPATAN", jumlah=int(jumlah), detail=detail, untuk=untuk, dari=dari):
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}       ✅[bold green]  BERHASIL  [/]✅')
            delay(2)
        else:
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  GAGAL [/]⚠️')
            delay(2)

    def menu_pengeluaran_kas():
        untuk, jumlah, detail = create_menu_detail(
            'PENGELUARAN KAS', 'PENGELUARAN', 'UNTUK')
        dari = None  # There is no "UNTUK" for expenses

        if instance_akun.transaksi(str(user_id), tipe_akun="KAS", kategori="PENGELUARAN", jumlah=int(jumlah), detail=detail, untuk=untuk, dari=dari):
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}       ✅[bold green]  BERHASIL  [/]✅')
            delay(2)
        else:
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  GAGAL [/]⚠️')
            delay(2)

    def menu_pemasukan_bank():
        dari, jumlah, detail = create_menu_detail(
            'PEMASUKAN BANK', 'PENDAPATAN', 'DARI')
        untuk = None  # There is no "DARI" for income

        if instance_akun.transaksi(str(user_id), tipe_akun="BANK", kategori="PENDAPATAN", jumlah=int(jumlah), detail=detail, untuk=untuk, dari=dari):
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}       ✅[bold green]  BERHASIL  [/]✅')
            delay(2)
        else:
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  GAGAL [/]⚠️')
            delay(2)

    def menu_pengeluaran_bank():
        untuk, jumlah, detail = create_menu_detail(
            'PENGELUARAN BANK', 'PENGELUARAN', 'UNTUK')
        dari = None  # There is no "UNTUK" for expenses

        if instance_akun.transaksi(str(user_id), tipe_akun="BANK", kategori="PENGELUARAN", jumlah=int(jumlah), detail=detail, untuk=untuk, dari=dari):
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}       ✅[bold green]  BERHASIL  [/]✅')
            delay(2)
        else:
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  GAGAL [/]⚠️')
            delay(2)

    def menu_laporan():

        while True:
            console.clear()
            Alat.mencetak_rule(' L A P O R A N ')
            print(WHITE_SPACE_HORIZONTAL * 3)
            Alat.mencetak_header()
            print(WHITE_SPACE_HORIZONTAL * 2)
            halaman_input_cashflow = Panel('''
[bold chartreuse1]⬇ [/][bold red1]⬆ [/]1. CASHFLOW [dim grey7]      -[/]
                                        
[bold ]💰 2. [/]Ringkasan Bank [dim grey7]-[/]  
                                        
[bold sky_blue1]↩   3.[/] KEMBALI [dim grey7]       -[/]
    ''', padding=2, subtitle='pilih 1 - 3')

            console.print(halaman_input_cashflow, style='bold bright_white',
                          justify='center')
            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 9}>> ',
                          style='bold chartreuse1', end=' ')
            pilihan = input('')

            Laporan.get_user_id(user_id)

            if pilihan == "1":
                run_reporting_program()
            if pilihan == "2":
                run_ringkasan_saldo()
            if pilihan == "3":
                break

    def menu_edit_profil(self):
        while True:
            console.clear()
            Alat.mencetak_rule('EDIT PROFIL')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold chartreuse1]NAMA     :[/][bold bright_white] [/][dim grey7] -[/]
[bold ]PERUSAHAAN:[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO KAS :[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO BANK:[/][bold bright_white] [/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 7}   MASUKAN NAMA BARU >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            InNAMA = input(' ')

            console.clear()
            Alat.mencetak_rule('EDIT PROFIL')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold ]NAMA     :[/][bold bright_white] {InNAMA} [/][dim grey7] -[/]
[bold chartreuse1]PERUSAHAAN:[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO KAS :[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO BANK:[/][bold bright_white] [/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 6}   MASUKAN NAMA PERUSAHAAN BARU >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            In_nama_perusahaan = input(' ')

            console.clear()
            Alat.mencetak_rule('EDIT PROFIL')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold ]NAMA     :[/][bold bright_white] {InNAMA} [/][dim grey7] -[/]
[bold ]PERUSAHAAN:[/][bold bright_white] {In_nama_perusahaan} [/][dim grey7] -[/]
[bold chartreuse1]SALDO KAS :[/][bold bright_white] [/][dim grey7] -[/]
[bold ]SALDO BANK:[/][bold bright_white] [/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 6}   MASUKAN SALDO KAS AWAL  >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            In_saldo_kas_awal = input(' ')

            console.clear()
            Alat.mencetak_rule('EDIT PROFIL')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold ]NAMA    :[/][bold bright_white] {InNAMA} [/][dim grey7] -[/]
[bold ]PERUSAHAAN:[/][bold bright_white] {In_nama_perusahaan} [/][dim grey7] -[/]
[bold ]SALDO KAS :[/][bold bright_white] {In_saldo_kas_awal} [/][dim grey7] -[/]
[bold chartreuse1]SALDO BANK:[/][bold bright_white] [/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 6}   MASUKAN SALDO REKENING BANK AWAL  >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            In_saldo_bank_awal = input(' ')

            console.clear()
            Alat.mencetak_rule('EDIT PROFIL')
            print(WHITE_SPACE_HORIZONTAL * 10)
            halaman_registrasi = Panel(f'''
[bold ]NAMA     :[/][bold bright_white] {InNAMA} [/][dim grey7] -[/]
[bold ]PERUSAHAAN:[/][bold bright_white] {In_nama_perusahaan} [/][dim grey7] -[/]
[bold ]SALDO KAS :[/][bold bright_white] {In_saldo_kas_awal} [/][dim grey7] -[/]
[bold ]SALDO BANK:[/][bold bright_white] {In_saldo_bank_awal}[/][dim grey7] -[/]
                ''', padding=3, subtitle='Profil Pengguna')

            console.print(halaman_registrasi, style='bold bright_white',
                          justify='center')

            console.print(f'{WHITE_SPACE_HORIZONTAL* 2}{WHITE_SPACE_VERTICAL * 5}   APAKAH INI SUDAH BENAR?  [Y/N] >> ',        # INPUT ID
                          style='bold chartreuse1', end=' ')
            confirm = input(' ')

            if confirm == 'y' or confirm == 'Y':
                break
            elif confirm == 'n' or confirm == 'N':
                continue
            else:
                console.print(
                    f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  KODE INVALID [/]⚠️')
                delay(2)

        if akun.edit_profil():
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}       ✅[bold green]  REGISTRASI BERHASIL  [/]✅')
            delay(2)

        else:
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}        ⚠️[bold red]  ID SUDAH TERDAFTAR [/]⚠️')
            delay(2)

    def menu_dashboard():
        with open("data/user.json", "r") as user_file:
            user_data = json.load(user_file)

        with open("data/bep.json", "r") as bep_file:
            bep_data = json.load(bep_file)

        with open("data/transaksi.json", "r") as transactions_file:
            transactions_data = json.load(transactions_file)

        dashboard = Dashboard(user_data, bep_data, transactions_data)


        console.clear()
        Alat.mencetak_rule('DASHBOARD')
        dashboard.display_user_profile(user_id)
        print("=" * 170)  # Add a separator between panels
        dashboard.display_bep_progress(user_id)
        input('')

