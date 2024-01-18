from rich.console import Console
from rich.panel import Panel
from time import sleep as delay

console = Console()
WHITE_SPACE_VERTICAL = '\t'


def mencetak_rule(header):
    console.rule(f" [bold medium_spring_green]{header}[/]")


def mencetak_header():
    console.print('''
     ooo        ooooo        .oooooo.        ooo        ooooo      oooooooooooo      ooooo      ooo      ooooooooooooo 
     `88.       .888'       d8P'  `Y8b       `88.       .888'      `888'     `8      `888b.     `8'      8'   888   `8 
 888b     d'888       888      888       888b     d'888        888               8 `88b.    8            888      
 8 Y88. .P  888       888      888       8 Y88. .P  888        888oooo8          8   `88b.  8            888      
 8  `888'   888       888      888       8  `888'   888        888    "          8     `88b.8            888      
 8    Y     888       `88b    d88'       8    Y     888        888       o       8       `888            888      
 o8o        o888o       `Y8bood8P'       o8o        o888o      o888ooooood8      o8o        `8           o888o     
''', style='green', justify='center')


def kode_invalid():
    console.print(
        f'\n\n{WHITE_SPACE_VERTICAL * 9}    ⚠️[bold red]  KODE INVALID [/]⚠️')
    delay(2)
    console.clear()






