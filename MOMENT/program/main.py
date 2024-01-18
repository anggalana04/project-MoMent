from menu import Menu
from rich.console import Console
from autentikasi import Akun
from time import sleep as delay
from rich.prompt import Prompt
import Alat

"""
!!! NOTES 

Pastikan beberapa library dibawah ini terinstall 
1. rich
2. babel
3. locale
4. operator
5. json
6. os

"""

console = Console()
prompt = Prompt()
console = Console()
akun = Akun()
WHITE_SPACE_VERTICAL = '\t'
WHITE_SPACE_HORIZONTAL = '\n'


def main():
    while True:
        pilihan = Menu.menu_autentikasi()

        if pilihan == '1':
            console.clear()
            InID = Menu.menu_login()
            delay(1)
            while True:
                menu_utama_pilihan = Menu.menu_utama()
                if menu_utama_pilihan == '1':
                    while True:
                        menu_input_cashflow_pilihan = Menu.menu_input_cashflow()

                        if menu_input_cashflow_pilihan == '1':
                            while True:
                                menu_pilihan_akun_pilihan = Menu.menu_pilihan_akun()
                                if menu_pilihan_akun_pilihan == '1':
                                    Menu.menu_pemasukan_kas()

                                elif menu_pilihan_akun_pilihan == '2':
                                    Menu.menu_pengeluaran_kas()

                                elif menu_pilihan_akun_pilihan == '3':
                                    break

                                else:
                                    Alat.kode_invalid()

                        elif menu_input_cashflow_pilihan == '2':
                            while True:
                                menu_pilihan_akun_pilihan = Menu.menu_pilihan_akun()
                                if menu_pilihan_akun_pilihan == '1':
                                    Menu.menu_pemasukan_bank()

                                elif menu_pilihan_akun_pilihan == '2':
                                    Menu.menu_pengeluaran_bank()

                                elif menu_pilihan_akun_pilihan == '3':
                                    break

                                else:
                                    Alat.kode_invalid()
                        elif menu_input_cashflow_pilihan == '3':
                            break  # Exit sub-sub-menu

                        else:
                            Alat.kode_invalid()

                elif menu_utama_pilihan == '2':
                    Menu.menu_laporan()

                elif menu_utama_pilihan == '3':
                    Menu.menu_dashboard()

                elif menu_utama_pilihan == '4':
                    Menu.menu_BEP()

                    # Wait for user input

                elif menu_utama_pilihan == '5':
                    break

                else:
                    Alat.kode_invalid()

        elif pilihan == '2':
            Menu.menu_registrasi()
            delay(1)

        elif pilihan == '3':
            console.print('EXITING PROGRAM ...',
                          justify='center', style='bold red')
            delay(1)
            console.clear()
            exit()

        else:
            console.print(
                f'\n\n{WHITE_SPACE_VERTICAL * 8}      ⚠️[bold red]  ID ATAU PASSWORD SALAH [/]⚠️')
            delay(2)
            console.clear()


if __name__ == '__main__':
    main()
