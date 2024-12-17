def remove_leading_zeros(ip):
    parts = ip.split('.')
    print(parts)
    cleaned_parts = [str(int(part)) for part in parts]
    print(cleaned_parts)
    cleaned_ip = '.'.join(cleaned_parts)
    print(cleaned_ip)
    return cleaned_ip

ip_address = "192.168.001.010"
cleaned_ip = remove_leading_zeros(ip_address)
print(cleaned_ip)
