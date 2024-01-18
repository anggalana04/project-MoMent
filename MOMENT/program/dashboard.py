import json
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from babel.numbers import format_currency
from rich.layout import Layout
from rich.console import Console

console = Console()


class Dashboard:
    def __init__(self, user_data, bep_data, transactions_data):
        self.user_data = user_data
        self.bep_data = bep_data
        self.transactions_data = transactions_data
        self.layout = Layout()
        self.console = Console()

    def calculate_total_sales(self, user_id):
        transactions = self.transactions_data.get(user_id, [])
        total_sales = sum(
            transaction["JUMLAH"]
            for transaction in transactions
            if transaction["KATEGORI"] == "PENDAPATAN" and transaction.get("DETAIL") == "PENJUALAN"
        )
        return total_sales

    def handle_file(self, filename, data=None):
        try:
            with open(filename, "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, create an empty list for data
            existing_data = []

        if data is not None:
            existing_data.append(data)

        with open(filename, "w") as file:
            json.dump(existing_data, file, indent=4)

    def display_user_profile(self, user_id):
        user_profile = next(
            (user for user in self.user_data if user["ID"] == user_id), None
        )

        if user_profile:
            formatted_kas_balance = format_currency(
                user_profile["SALDO_KAS"], "IDR", locale="id_ID"
            )
            formatted_bank_balance = format_currency(
                user_profile["SALDO_BANK"], "IDR", locale="id_ID"
            )

            # Format and style balances
            kas_balance_text = Text(
                f"Kas Balance: {formatted_kas_balance}"
            )
            bank_balance_text = Text(
                f"Bank Balance: {formatted_bank_balance}"
            )

            # Apply color to balances
            kas_balance_text.stylize(
                "green" if user_profile["SALDO_KAS"] > 0 else "red"
            )
            bank_balance_text.stylize(
                "green" if user_profile["SALDO_BANK"] > 0 else "red"
            )

            # Create a navbar-like display
            navbar_text = Text()
            navbar_text.append(f"ID:", style="bold")
            navbar_text.append(f" {user_profile['ID']}  ", style="bold blue")
            navbar_text.append(f"Name:", style="bold")
            navbar_text.append(f" {user_profile['NAMA']}  ", style="bold blue")
            navbar_text.append(f"Company:", style="bold")
            navbar_text.append(
                f" {user_profile['NAMA_PERUSAHAAN']}  ", style="bold blue"
            )
            navbar_text.append(
                f"\t\t\t\t\t{kas_balance_text}", style="bold green"
            )
            navbar_text.append(f"\t\t{bank_balance_text}", style="bold green")

            self.console.print(
                Panel(navbar_text, title="", expand=True)
            )
        else:
            self.console.print(
                Panel(f"User with ID {user_id} not found.", expand=False)
            )

    def display_bep_progress(self, user_id):
        user_profile = next(
            (user for user in self.user_data if user["ID"] == user_id), None
        )

        if user_profile:
            user_bep = next(
                (bep for bep in self.bep_data if bep["ID"]
                 == user_profile["ID"]), None
            )

            if user_bep:
                total_sales = self.calculate_total_sales(user_profile["ID"])
                bep_target = user_bep["BEP_RP"]

                progress_percentage = min(
                    100, (total_sales / bep_target) * 100
                )

                # Determine the color and emoji based on the progress percentage
                if progress_percentage <= 20:
                    color = "red"
                    emoji = "😢"  # Sad emoji
                    description = "Uh-oh, still a long way to go! Keep pushing."
                    advice = "Don't worry, every sale brings you closer to your goal. Keep hustling!"
                elif progress_percentage <= 50:
                    color = "dark_orange3"
                    emoji = "😐"  # Neutral emoji
                    description = "Making progress, but there's room for improvement!"
                    advice = "Explore new sales channels or promotions to boost your sales."
                elif progress_percentage <= 99:
                    color = "yellow"
                    emoji = "😊"  # Happy emoji
                    description = "Great job! You're getting close to reaching your Break-Even Point."
                    advice = "Keep up the good work! Consider upselling or cross-selling to increase sales."
                else:
                    color = "green"
                    emoji = "🎉"  # Excited emoji
                    description = "Congratulations! You've surpassed your Break-Even Point."
                    advice = "Fantastic achievement! Consider expanding your product range or celebrating with your team."

                formatted_bep_rp = format_currency(
                    bep_target, "IDR", locale="id_ID"
                )
                formatted_total_sales = format_currency(
                    total_sales, "IDR", locale="id_ID"
                )

                progress_text = f"BEP Progress: {progress_percentage:.2f}%"
                progress_bar = "━" * int(progress_percentage)
                remaining_space = " " * (100 - len(progress_bar))

                colored_progress_text = Text(progress_text, style=color)
                panel_title = f"Break-Even Point Progress {emoji}"

                panel_content = f"""
[bold]{panel_title}[/bold]
{colored_progress_text}
[{progress_bar}{remaining_space}]
{description}

[bold]Sales Progress:[/bold]
{formatted_total_sales} / {formatted_bep_rp}

[bold]Sales Advice:[/bold]
{advice}
                """

                self.console.print(
                    Panel(
                        panel_content,
                        title=panel_title,
                        style=color,
                        expand=False,
                    )
                )
            else:
                self.console.print(
                    Panel(
                        f"BEP data not found for user with ID {user_id}.", expand=False)
                )
        else:
            self.console.print(
                Panel(f"User with ID {user_id} not found.", expand=False)
            )
