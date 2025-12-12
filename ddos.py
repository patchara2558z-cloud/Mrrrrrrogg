import os
import sys
import time
import getpass
import webbrowser
import subprocess
import requests

def launch_gui(): 
    app = ctk.CTk()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app.title("Osint-kit Gui - By Hyper")
    app.geometry("900x750")

    def whhois():
        link = entry.get()
        try:
            whhois_res = whois.whois(link)
            result_textbox.delete(1.0, ctk.END)
            result_textbox.insert(1.0, str(whhois_res))
        except Exception as e:
            result_textbox.delete(1.0, ctk.END)
            result_textbox.insert(1.0, f"Errore: {e}")

    whois_label = ctk.CTkLabel(
        app,
        text="Whois Lookup",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    whois_label.pack(pady=10)

    labeel = ctk.CTkLabel(master=app, text="Link of the Website to scan with WHOIS : ")
    labeel.pack()

    entry = ctk.CTkEntry(master=app, width=400, height=30)
    entry.pack(pady=5)

    button = ctk.CTkButton(master=app, text="Scan Url", command=whhois)
    button.pack(pady=10)

    label_info = ctk.CTkLabel(master=app, text="Output of whois scan : ")
    label_info.pack()

    result_textbox = ctk.CTkTextbox(app, height=150, width=800)
    result_textbox.pack(pady=10)

    def ipinfo():
        ip = entry_ip.get()
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            if data['status'] == 'success':
                ip_lookup_result = (
                    f"[*] Country     : {data.get('country')}\n"
                    f"[*] CountryCode : {data.get('countryCode')}\n"
                    f"[*] City        : {data.get('city')}\n"
                    f"[*] Zip Code    : {data.get('zip')}\n"
                    f"[*] Timezone    : {data.get('timezone')}\n"
                    f"[*] Org         : {data.get('org')}\n"
                    f"[*] Region      : {data.get('region')}\n"
                    f"[*] RegionName  : {data.get('regionName')}\n"
                    f"[*] AS          : {data.get('as')}\n"
                    f"[*] Latitude    : {data.get('lat')}\n"
                    f"[*] Longitude   : {data.get('lon')}"
                )
            else:
                ip_lookup_result = f"Errore: {data.get('message', 'IP non trovato')}"
        except Exception as e:
            ip_lookup_result = f"Errore durante la richiesta: {e}"

        result_textbox_ip.delete(1.0, ctk.END)
        result_textbox_ip.insert(1.0, ip_lookup_result)

    ipinfo_label = ctk.CTkLabel(
        app,
        text="IP Lookup",
        font=ctk.CTkFont(size=28, weight="bold"),
        text_color="red"
    )
    ipinfo_label.pack(pady=10)

    label_ip = ctk.CTkLabel(master=app, text="IP address : ")
    label_ip.pack()

    entry_ip = ctk.CTkEntry(master=app, width=400, height=30)
    entry_ip.pack(pady=5)

    button_ip = ctk.CTkButton(master=app, text="Get IP Info", command=ipinfo)
    button_ip.pack(pady=10)

    label_ip2 = ctk.CTkLabel(master=app, text="IP Info Output : ")
    label_ip2.pack()

    result_textbox_ip = ctk.CTkTextbox(app, height=150, width=800)
    result_textbox_ip.pack(pady=10)

    app.mainloop()


if __name__ == "__main__":
    launch_gui()
