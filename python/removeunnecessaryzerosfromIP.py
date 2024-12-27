def remove_leading_zeros(ip):
    parts = ip.split('.')
    print("parts",parts)
    cleaned_parts = [str(int(part)) for part in parts]
    print(cleaned_parts)
    cleaned_ip = '.'.join(cleaned_parts)
    print("clean id",cleaned_ip)
    # return cleaned_ip

ip_address = "192.168.010.01"
remove_leading_zeros(ip_address)
# print("IS ",cleaned_ip)
