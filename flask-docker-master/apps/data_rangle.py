import netaddr


def convert_ip(str_ip):
    res = int(netaddr.IPAddress(str(str_ip)))
    return(res)
