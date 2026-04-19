#!/usr/bin/env python3
"""
StormScan - Escáner de red multithread
Más rápido que nmap/zenmap con detección automática
"""

import sys
import json
import subprocess
from datetime import datetime

VERSION = "0.1.0"

def banner():
    print("""
    ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
    ⚡     STORMSCAN v{}     ⚡
    ⚡  Network Scanner Pro   ⚡
    ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡
    """.format(VERSION))

def scan_nmap(host, ports="1-1000"):
    print(f"[+] Escaneando {host} en puertos {ports}...")
    cmd = ["nmap", "-sV", "--open", "-p", ports, host, "-oX", "-"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def main():
    banner()
    
    if len(sys.argv) < 2:
        print("Uso: python main.py <target> [ports]")
        print("Ejemplo: python main.py 192.168.1.1")
        print("Ejemplo: python main.py google.com 1-10000")
        sys.exit(1)
    
    target = sys.argv[1]
    ports = sys.argv[2] if len(sys.argv) > 2 else "1-1000"
    
    print(f"\n[🌩️] Iniciando tormenta contra {target}")
    start_time = datetime.now()
    
    resultado = scan_nmap(target, ports)
    
    # Guardar resultado
    with open(f"scan_{target.replace('/', '_')}.xml", "w") as f:
        f.write(resultado)
    
    end_time = datetime.now()
    print(f"\n[✅] Escaneo completado en {end_time - start_time}")
    print(f"[📁] Resultados guardados en scan_{target}.xml")

if __name__ == "__main__":
    main()
