import json
import locale
import time
from rich.console import Console
from rich.table import Table
from rich import box
from datetime import datetime
from operator import itemgetter
from time import sleep as delay
from Alat import mencetak_rule
console = Console()
user_ID = 0


class SortingMethods:
    @staticmethod
    def sort_by_date(entries, sort_option):
        return sorted(entries, key=itemgetter("WAKTU"), reverse=(sort_option == "terbaru"))

    @staticmethod
    def sort_by_kategori(entries, sort_option):
        return sorted(entries, key=itemgetter("KATEGORI"), reverse=(sort_option == "pengeluaran"))

    @staticmethod
    def sort_by_jumlah(entries, sort_option):
        return sorted(entries, key=itemgetter("JUMLAH"), reverse=(sort_option == "terbesar"))

    @staticmethod
    def sort_by_tipe(entries, tipe_option):
        return [entry for entry in entries if entry["TIPE_AKUN"].upper() == tipe_option.upper()]

    @staticmethod
    def sort_by_tanggal_periode(entries, periode_option):
        now = datetime.now()
        if periode_option == 'hari ini':
            return [entry for entry in entries if datetime.strptime(entry["WAKTU"], "%Y/%m/%d %H:%M").date() == now.date()]
        elif periode_option == 'bulan ini':
            return [entry for entry in entries if datetime.strptime(entry["WAKTU"], "%Y/%m/%d %H:%M").month == now.month]
        elif periode_option == 'tahun ini':
            return [entry for entry in entries if datetime.strptime(entry["WAKTU"], "%Y/%m/%d %H:%M").year == now.year]
        else:
            return entries


class Laporan():
    def __init__(self, data_file='data/transaksi.json'):
        self.data_file = data_file
        self.load_data()
        self.console = Console()

    def load_data(self):
        with open(self.data_file, 'r') as file:
            self.data = json.load(file)

    def calculate_saldo_kas(self, entries):
        saldo_awal_kas, total_diterima_kas, total_dibelanjakan_kas, saldo_akhir_kas = self.calculate_saldo(
            entries, "KAS")
        return saldo_awal_kas, total_diterima_kas, total_dibelanjakan_kas, saldo_akhir_kas

    def calculate_saldo_bank(self, entries):
        saldo_awal_bank, total_diterima_bank, total_dibelanjakan_bank, saldo_akhir_bank = self.calculate_saldo(
            entries, "BANK")
        return saldo_awal_bank, total_diterima_bank, total_dibelanjakan_bank, saldo_akhir_bank

    def calculate_saldo(self, entries, account_type):
        saldo_awal = 0
        total_diterima = 0
        total_dibelanjakan = 0

        for entry in entries:
            if entry["TIPE_AKUN"].upper() == account_type:
                if entry["KATEGORI"] == "PENDAPATAN":
                    total_diterima += entry["JUMLAH"]
                elif entry["KATEGORI"] == "PENGELUARAN":
                    total_dibelanjakan += entry["JUMLAH"]

        saldo_akhir = saldo_awal + total_diterima - total_dibelanjakan

        return saldo_awal, total_diterima, total_dibelanjakan, saldo_akhir

    def ringkasan_saldo_menu(self, entries):
        while True:
            # Move the cursor to the beginning of the line
            locale.setlocale(locale.LC_ALL, 'id_ID.utf-8')

            self.console.print("\r", end="")

            # Clear the current line
            self.console.print(" " * self.console.width, end="")

            # Move the cursor back to the beginning of the line
            self.console.print("\r", end="")
            console.clear()
            mencetak_rule(' SALDO KAS ')
            saldo_kas = self.calculate_saldo_kas(entries)
            saldo_bank = self.calculate_saldo_bank(entries)


            # Set the locale for currency formatting to 'id_ID.utf-8' for IDR
            locale.setlocale(locale.LC_ALL, 'id_ID.utf-8')

            # Display "SALDO KAS" section
            tabel_kas = Table(show_header=True, header_style="bold bright_white",
                              box=box.MINIMAL_DOUBLE_HEAD)
            tabel_kas.add_column("Nama", style="bright_white", width=40)
            tabel_kas.add_column("Saldo", style="bright_white", width=20)

            # Add rows for "KAS"
            tabel_kas.add_row("SALDO AWAL KAS", locale.currency(
                saldo_kas[0], grouping=True))
            tabel_kas.add_row("UANG DITERIMA KAS", locale.currency(
                saldo_kas[1], grouping=True))
            tabel_kas.add_row("UANG DIBELANJAKAN KAS", locale.currency(
                saldo_kas[2], grouping=True))
            tabel_kas.add_row("SALDO AKHIR KAS", locale.currency(
                saldo_kas[3], grouping=True))

            self.console.print(tabel_kas, justify='center')

            mencetak_rule(' SALDO BANK ')
            # Display "SALDO BANK" section
            tabel_bank = Table(show_header=True, header_style="bold bright_white",
                               box=box.MINIMAL_DOUBLE_HEAD)
            tabel_bank.add_column("Nama", style="bright_white", width=40)
            tabel_bank.add_column("Saldo", style="bright_white", width=20)

            # Add rows for "BANK"
            tabel_bank.add_row("SALDO AWAL BANK", locale.currency(
                saldo_bank[0], grouping=True))
            tabel_bank.add_row("UANG DITERIMA BANK", locale.currency(
                saldo_bank[1], grouping=True))
            tabel_bank.add_row("UANG DIBELANJAKAN BANK", locale.currency(
                saldo_bank[2], grouping=True))
            tabel_bank.add_row("SALDO AKHIR BANK", locale.currency(
                saldo_bank[3], grouping=True))

            self.console.print(tabel_bank, justify='center')

            # Add a rule for the "TOTAL" section
            mencetak_rule(' TOTAL ')

            # Calculate total saldo
            total_saldo_awal = saldo_kas[0] + saldo_bank[0]
            total_diterima = saldo_kas[1] + saldo_bank[1]
            total_dibelanjakan = saldo_kas[2] + saldo_bank[2]
            total_saldo_akhir = saldo_kas[3] + saldo_bank[3]

            tabel_total = Table(show_header=True, header_style="bold bright_white",
                                box=box.MINIMAL_DOUBLE_HEAD)
            tabel_total.add_column("Nama", style="bright_white", width=40)
            tabel_total.add_column("Saldo", style="bright_white", width=20)

            # Add rows for "TOTAL"
            tabel_total.add_row("SALDO AWAL TOTAL", locale.currency(
                total_saldo_awal, grouping=True))
            tabel_total.add_row("UANG DITERIMA TOTAL", locale.currency(
                total_diterima, grouping=True))
            tabel_total.add_row("UANG DIBELANJAKAN TOTAL", locale.currency(
                total_dibelanjakan, grouping=True))
            tabel_total.add_row("SALDO AKHIR TOTAL", locale.currency(
                total_saldo_akhir, grouping=True))

            self.console.print(tabel_total, justify='center')
            # Reset the locale
            locale.setlocale(locale.LC_ALL, '')

            self.console.print("\nMENU:")
            self.console.print("1. Back")

            option = input("Choose an option: ")

            if option == "1":
                break
            else:
                print("Invalid option. Please choose 1.")
                delay(2)

    def get_user_id(user_id):
        global user_ID
        user_ID = user_id

    def extract_entries(self):
        return self.data.get(user_ID, [])

    def tampilkan_ringkasan_arus_kas(self, entries):
        # Set the locale for currency formatting
        locale.setlocale(locale.LC_ALL, 'id_ID.utf-8')

        total_pendapatan = sum(
            entry["JUMLAH"] for entry in entries if entry["KATEGORI"] == "PENDAPATAN")
        total_pengeluaran = sum(
            entry["JUMLAH"] for entry in entries if entry["KATEGORI"] == "PENGELUARAN")
        total_arus_kas = total_pendapatan - total_pengeluaran

        self.console.clear()
        self.console.rule("Ringkasan Arus Kas")
        self.console.print(
            f"Total Pendapatan: [green]{locale.currency(total_pendapatan, grouping=True)}[/green]")
        self.console.print(
            f"Total Pengeluaran: [red]{locale.currency(total_pengeluaran, grouping=True)}[/red]")
        if total_arus_kas > 0:
            self.console.print(
                f"Total Arus Kas: [bold green]{locale.currency(total_arus_kas, grouping=True)}[/]")
        else:
            self.console.print(
                f"Total Arus Kas: [bold red]{locale.currency(total_arus_kas, grouping=True)}[/]")

    def tampilkan_rincian_transaksi(self, entries):
        tabel = Table(show_header=True, header_style="bold bright_white",
                      box=box.MINIMAL_DOUBLE_HEAD)
        tabel.add_column("Tanggal", style="bright_white", width=20)
        tabel.add_column("Kategori", style="bright_white", width=15)
        tabel.add_column("Jumlah", style="bright_white", width=15)
        tabel.add_column("Tipe", style="bright_white", width=15)
        tabel.add_column("Detail", style="bright_white", width=30)
        tabel.add_column("Untuk", style="bright_white", width=20)
        tabel.add_column("Dari", style="bright_white", width=20)

        for entry in entries:
            jumlah_formatted = locale.currency(
                entry['JUMLAH'], grouping=True)
            kategori_style = "green" if entry["KATEGORI"] == "PENDAPATAN" else "red"
            tabel.add_row(
                entry["WAKTU"],
                f"[{kategori_style}]{entry['KATEGORI']}[/{kategori_style}]",
                f"[{kategori_style}]{jumlah_formatted}[/{kategori_style}]",
                entry["TIPE_AKUN"],
                entry["DETAIL"],
                entry["UNTUK"],
                entry["DARI"]
            )

        self.console.print("\nRincian Transaksi", style="bold bright_white ")
        self.console.print(tabel)

    def sort_menu(self, entries):
        while True:
            # Move the cursor to the beginning of the line
            self.console.print("\r", end="")

            # Clear the current line
            self.console.print(" " * self.console.width, end="")

            # Move the cursor back to the beginning of the line
            self.console.print("\r", end="")

            self.console.print("\nOptions:")
            self.console.print("1. Sort")
            self.console.print("2. Back")

            option = input("Choose an option: ")

            if option == "1":
                self.sort_entries(entries)
            elif option == "2":
                break
            else:
                print("Invalid option. Please choose 1 or 2.")
                delay(2)

    def sort_entries(self, entries):
        sort_options = []  # To store the current sort options

        while True:
            try:
                self.console.print("\nSort by:")
                self.console.print("1. Tanggal")
                self.console.print("2. Kategori")
                self.console.print("3. Jumlah")
                self.console.print("4. Tipe")
                self.console.print("5. Reset")
                
                option = input("Choose an option (1-6): ").strip()

                if option == '5':
                    entries = self.extract_entries()
                    sort_options = []  # Reset sorting options
                else:
                    valid_options = ['1', '2', '3', '4']
                    if option not in valid_options:
                        raise ValueError(
                            "Invalid option. Please choose a valid option.")

                    if option == '2':
                        kategori_option = self.choose_option(
                            "Sort by category (pendapatan, pengeluaran), 'Default' for default",
                            ['pendapatan', 'pengeluaran'])
                        entries = [
                            entry for entry in entries if entry["KATEGORI"] == kategori_option.upper()]
                        sort_options.append(('kategori', kategori_option))
                    elif option == '1':
                        date_sort_option = self.choose_option(
                            "Sort by date (Oldest, Newest, Period), 'Default' for default",
                            ['terlama', 'terbaru', 'periode']
                        )
                        if date_sort_option == 'periode':
                            periode_option = self.choose_option(
                                "Sort by period (today, this month, this year)",
                                ['hari ini', 'bulan ini', 'tahun ini']
                            )
                            entries = SortingMethods.sort_by_tanggal_periode(
                                entries, periode_option
                            )
                            sort_options.append(
                                ('tanggal', f'period - {periode_option}'))
                        else:
                            entries = SortingMethods.sort_by_date(
                                entries, date_sort_option
                            )
                            sort_options.append(('tanggal', date_sort_option))

                    elif option == '3':
                        jumlah_sort_option = self.choose_option(
                            "Sort by amount (Largest, Smallest), 'Default' for default",
                            ['terbesar', 'terkecil'])
                        entries = SortingMethods.sort_by_jumlah(
                            entries, jumlah_sort_option)
                        sort_options.append(('jumlah', jumlah_sort_option))
                    elif option == '4':
                        tipe_option = self.choose_option(
                            "Filter by type (Bank, Cash), 'Default' for default",
                            ['bank', 'kas'])
                        entries = SortingMethods.sort_by_tipe(
                            entries, tipe_option)
                        sort_options.append(('tipe', tipe_option))

            except ValueError as e:
                print(str(e))
                delay(2)
                continue

            # Clear only the prompt area
            self.console.print("\n" + " " * (self.console.width - 1), end='\r')

            self.tampilkan_ringkasan_arus_kas(entries)
            self.tampilkan_rincian_transaksi(entries)

            print("\nCurrent Sort Options:", sort_options)

            if not self.choose_yes_no("Do you want to continue sorting?"):
                break

        # Apply sorting based on sort_options
        for key, option in sort_options:
            if key == 'kategori':
                entries = SortingMethods.sort_by_kategori(entries, option)
            elif key == 'tanggal':
                if 'period' in option:
                    entries = SortingMethods.sort_by_tanggal_periode(
                        entries, option.split(' - ')[1])
                else:
                    entries = SortingMethods.sort_by_date(entries, option)
            elif key == 'jumlah':
                entries = SortingMethods.sort_by_jumlah(entries, option)
            elif key == 'tipe':
                entries = SortingMethods.sort_by_tipe(entries, option)

        return entries

    def choose_option(self, prompt, options):
        self.console.print(prompt)
        for i, option in enumerate(options, 1):
            self.console.print(f"{i}. {option}")
        selected_option = input(
            f"Choose an option (1-{len(options)}): ").strip()
        if selected_option.isnumeric() and 1 <= int(selected_option) <= len(options):
            return options[int(selected_option) - 1]
        else:
            raise ValueError("Invalid option. Please choose a valid option.")

    def choose_yes_no(self, prompt):
        while True:
            response = input(f"{prompt} (y/n): ").strip().lower()
            if response == 'y':
                return True
            elif response == 'n':
                return False
            else:
                print("Invalid response. Please enter 'y' or 'n'.")

    def run_sorting(self):
        entries = self.extract_entries()
        entries = SortingMethods.sort_by_date(
            entries, 'terbaru')  # Default sorting by date
        self.tampilkan_ringkasan_arus_kas(entries)
        self.tampilkan_rincian_transaksi(entries)
        self.sort_entries(entries)

    def run_ringkasan_saldo(self):
        entries = self.extract_entries()
        self.ringkasan_saldo_menu(entries)

    def tampilan_langsung(self):
        entries = self.extract_entries()

        self.tampilkan_ringkasan_arus_kas(entries)
        self.tampilkan_rincian_transaksi(entries)
        self.tampilkan_menu_sort(entries)

        time.sleep(5)  # Update every 5 seconds

    def run(self):
        self.tampilan_langsung()


if __name__ == "__main__":
    app = Laporan()
    app.run_sorting()
