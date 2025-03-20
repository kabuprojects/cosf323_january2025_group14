import pywifi
import time
from util import get_security_type, detect_vulnerability

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    time.sleep(2)  # Waits for scan results
    results = iface.scan_results()

    networks = []
    scan_time = time.strftime('%Y-%m-%d %H:%M:%S')

    with open("wifi_scan_results.txt", "a", encoding="utf-8") as file:
        file.write(f"\nScan Time: {scan_time}\n" + "=" * 50 + "\n")

        for network in results:
            security = get_security_type(network)
            risk = detect_vulnerability(security, network.signal)
            networks.append({"ssid": network.ssid, "signal": network.signal, "security": security, "risk": risk})
            file.write(f"SSID: {network.ssid}, Signal: {network.signal}, Security: {security}, Risk: {risk}\n")
        
        file.write("=" * 50 + "\n")

    return networks
