#KBPS
kbps = 1
bps_sent = kbps * 1000 
bps_received = bps_sent + (bps_sent/1000)
extra_bps = bps_received - bps_sent

print ("KBPS")
print (f"{bps_sent} bits sent")
print (f"{bps_received:.4g} bits received")
print (f"{extra_bps:.4g} extra bit/s")

#MBPS
mbps = 1
mbps_sent = mbps * 1000000 
mbps_received = mbps_sent + (mbps_sent/1000)
extra_mbps = mbps_received - mbps_sent

print(" ")
print ("MBPS")
print (f"{mbps_sent} bits sent")
print (f"{mbps_received:.8g} bits received")
print (f"{extra_mbps:.8g} extra bits")


