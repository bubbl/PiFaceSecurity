import piface.pfio as pf
import time
import sys
import syslog

''' Script that uses PiFace Digital inputs/outputs 
    to inform about security breeches in your home.
    Uses reed switches and magnets placed at doors/windows/etc.
    to indicate if they're opened/closed.
    Logs the information into /var/log/security.log file.
'''

class SecurityReeds:
    def __init__(self, pin_pair, label):
        self.pin_pair = pin_pair
        self.label = label
        self.laststatus = ""
        self.inform()

    def inform(self):
        if pf.digital_read(self.pin_pair) == 1:
            if self.laststatus != 'closed':
                pf.digital_write(self.pin_pair, 1)
                self.loginfo(self.label + ' is CLOSED')
                self.laststatus = 'closed'
        else:
            if self.laststatus != 'open':
                pf.digital_write(self.pin_pair, 0)
                self.loginfo(self.label + ' is OPENED')
                self.laststatus = 'open'

    def loginfo(self, message):
        # Echo message
        print(message + ' at ' + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime()))
        # Log entry to auth log
        syslog.syslog(syslog.LOG_LOCAL0 | syslog.LOG_INFO, message)

def main(argv):
    pf.init()

    # Initialise reed switches
    gauges = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    gauge_obj = [];
    cnt = 0
    for switch in gauges:
        gauge_obj.append(SecurityReeds(cnt, switch))
        cnt = cnt + 1

    # Loop and check reeds state
    while True:
        for gauge in gauge_obj:
            gauge.inform()
        time.sleep(0.05)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
