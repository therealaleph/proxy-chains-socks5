list = "socks5_proxies.txt"
import socks
import time
def download_proxies():
    import requests
    url = "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt"
    r = requests.get(url)
    with open("socks5_proxies.txt", "w") as f:
        f.write(r.text)
    print("Downloaded proxies")
download_proxies()
def test_proxy(proxy):
    try:
        start = time.time()
        s = socks.socksocket()
        s.settimeout(1)
        ip = proxy.split(" ")[0]
        port = int(proxy.split(" ")[1])
        s.set_proxy(socks.SOCKS5, ip, port)
        s.connect(("www.google.com", 80))
        end = time.time()
        list = ip,port,end-start
        return list
    except Exception as e:
        print(e)
plist = []
with open(list, "r") as f:
    proxies = f.read().splitlines()
    for proxy in proxies:
        test_result = test_proxy(proxy)
        if test_result == None:
            continue
        ip = test_result[0]
        port = test_result[1]
        delay = test_result[2]
        if int(delay) < 1:
            plist.append([ip,port,delay])
            print(f"Proxy {ip}:{port} is working with delay {delay}")
text = ""
for proxy in plist:
    print(proxy[0])
    print(proxy[1])
    text = text  + f"socks5 {proxy[0]} {proxy[1]}\n"
towrite = f"""
random_chain
quiet_mode
proxy_dns
tcp_read_time_out 3000
tcp_connect_time_out 2000
[ProxyList]
{text}
""" #change params accordingly! -aleph
#chmod this if you're not root
with open("/etc/proxychains.conf", "w") as f:
    f.write(towrite)
