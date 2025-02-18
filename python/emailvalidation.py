def is_valid_mail(email):
    if "@" in email and '.' in email:
        local,domain = email.split("@",1)
        print('..........',local,domain)
        if local and domain and not domain.startswith(".") and len(domain.split(".")) > 1 :
                # '.' in domain and local and domain.split(".")[-1]):
            return True
    return False
print(is_valid_mail("test@gmail.com"))
print(is_valid_mail("kiran@gmail"))
print(is_valid_mail("kiran_kodi.com"))
print(is_valid_mail("kiran@.com"))
print(is_valid_mail("kiran.abc@@gmail.co.in"))