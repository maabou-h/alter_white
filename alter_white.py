from netfilterqueue import NetfilterQueue
from scapy.all import IP

def pkt_callback(pkt):
    payload = pkt.get_payload()
    data = IP(payload)
    print("source: " + data.src + "\ndest: " + data.dst)
    print("-------------")
    print(payload)
    print("-------------")
    print(data)
    pkt.accept()

if __name__ == "__main__":
    nfq = NetfilterQueue()
    nfq.bind(1, pkt_callback) # 1 for queue num
    try:
        nfq.run()
    except KeyboardInterrupt:
        print("\rInterruption was requested by user...")
    nfq.unbind()
    print("Exiting now...")
