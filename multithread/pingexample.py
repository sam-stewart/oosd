# Tom Clark example
import os, re, threading

class PingCheck(threading.Thread):
    received_packages = re.compile(r"(\d) packets received")

    def __init__(self, ip):
        threading.Thread.__init__(self)
        self.ip = ip
        self._successful_pings = 0

    def run(self):
        ping_out = os.popen("ping -q -c2 "+self.ip, "r")
        while True:
            line = ping_out.readline()
            if not line:
                break
            n_received = re.findall(self.received_packages, line)
            print n_received
            #print n_received
            if n_received:
                self._successful_pings = int(n_received[0])

    def status(self):
        if self._successful_pings == 0:
            return "no response"
        elif self._successful_pings == 1:
            return "alive, but 50% package loss"
        elif self._successful_pings == 2:
            return "alive"
        else:
            return "shouldn't occur"

if __name__ == "__main__":
    check_results = []
    for suffix in range (1,100):
        ip = "10.25.1."+str(suffix)
        current = PingCheck(ip)
        check_results.append(current)
        current.start()

    for el in check_results:
        el.join()
        print "Status from ", el.ip, "is", el.status()
