import pywifi

def get_security_type(network):
    if network.akm and network.akm[0] == pywifi.const.AKM_TYPE_WPA2:
        return "WPA2"
    elif network.akm and network.akm[0] == pywifi.const.AKM_TYPE_WPA:
        return "WPA"
    elif network.akm and network.akm[0] == pywifi.const.AKM_TYPE_WPA2PSK:
        return "WPA2-Personal"
    elif network.akm and network.akm[0] == pywifi.const.AKM_TYPE_WPAPSK:
        return "WPA-Personal"
    elif network.akm and network.akm[0] == pywifi.const.AKM_TYPE_NONE:
        return "Open (Unsecured)"
    else:
        return "Unknown"

def detect_vulnerability(security, signal):
    if security == "Open (Unsecured)":
        return "HIGH RISK: No encryption!"
    elif security == "WEP":
        return "WEAK SECURITY: Easy to crack!"
    elif signal < -80:
        return "UNSTABLE SIGNAL"
    else:
        return "Secure"
