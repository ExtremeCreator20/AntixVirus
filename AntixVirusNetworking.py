import psutil, requests, json, threading

def analyze(result):
    undetected = 0
    malicious = 0
    suspicious = 0
    harmless = 0
    for i in result:
        if i.lower() == "undetected":
            undetected += 1
        elif i.lower() == "suspicious":
            suspicious += 1
        elif i.lower() == "harmless":
            harmless += 1
        elif i.lower() == "malicious":
            malicious += 1
    
    return undetected, suspicious, harmless, malicious


def ipcheck(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

    headers = {
        "accept": "application/json",
        "x-apikey": json.load(open("config.json", "r"))["apikey"]
    }

    return requests.get(url, headers=headers)

def active_connections():
    connections = psutil.net_connections(kind='inet')
    active_urls = set()

    for conn in connections:
        if conn.status == 'ESTABLISHED':
            remote_address = conn.raddr
            if remote_address:
                active_urls.add(remote_address.ip)

    return active_urls

def connections():
    actives = active_connections()
    for ip in actives:
        analyze(ipcheck(ip))


def run_function():
    connections()
    threading.Timer(30.0, run_function).start()

run_function()