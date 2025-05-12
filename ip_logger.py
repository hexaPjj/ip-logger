import requests
import os
import platform
from pystyle import Write, Colors, Colorate

def clear_terminal():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def get_ip_info():
    try:
        # IP Al
        ip_data = requests.get("https://api.ipify.org?format=json").json()
        ip = ip_data['ip']
        Write.Print(f"\n     [+] IP Address Detected: {ip}\n", Colors.cyan_to_blue, 0.001)

        # Lokasyon datası
        location_data = requests.get(f"http://ip-api.com/json/{ip}").json()

        if location_data['status'] == 'success':
            Write.Print("\n" + "     ------------------------------------------------",Colors.green_to_cyan ,0.0001)
            print("")
            Write.Print(f"     🌍 Country     : {location_data['country']}\n", Colors.red_to_blue, 0.001)
            Write.Print(f"     🏙️  City       : {location_data['city']}\n", Colors.green_to_red, 0.001)
            Write.Print(f"     🌐 ISP         : {location_data['isp']}\n", Colors.blue_to_red, 0.001)
            Write.Print(f"     📍 Coordinates : {location_data['lat']}, {location_data['lon']}\n", Colors.cyan_to_green, 0.001)
            Write.Print(f"     📮 Zip Code    : {location_data['zip']}\n", Colors.red_to_blue, 0.001)
            Write.Print(f"     🕓 Timezone    : {location_data['timezone']}\n", Colors.blue_to_cyan, 0.001)
            Write.Print("     ------------------------------------------------" + "\n",Colors.green_to_cyan,0.0001, "\n")
        else:
            Write.Print("\n[!] Cant find location info.\n", Colors.red_to_blue, 0.001)

    except Exception as e:
        Write.Print(f"\n[!] Error: {e}\n", Colors.red_to_blue, 0.001)

def banner():
    clear_terminal()
    print(Colorate.Vertical(Colors.red_to_purple, """
    ╔══════════════════════════════════════════════════════════════════════╗
    ║  ██╗██████╗     ██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗   ║
    ║  ██║██╔══██╗    ██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗  ║
    ║  ██║██████╔╝    ██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝  ║
    ║  ██║██╔═══╝     ██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗  ║
    ║  ██║██║         ███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║  ║
    ║  ╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝  ║
    ╚══════════════════════════════════════════════════════════════════════╝
                           IP LOGGER | Basic Version
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """, 1))

if __name__ == "__main__":
    banner()
    Write.Print("\n     [?] Do you wanna run the IP logger? (ye/no): ", Colors.cyan_to_blue, 0.01)
    ipcevap = input()

    if ipcevap.strip().lower() == "ye":
        Write.Print("     Ur a lucky guy nigu✔️",Colors.green_to_cyan)
        print("")
        get_ip_info()
    else:
        Write.Print("\n     [!] Operation cancelled. Stay safe, nerd and nigu😭.\n", Colors.red_to_blue, 0.01)
