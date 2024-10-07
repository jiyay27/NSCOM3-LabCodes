import math

def latency(proptime, tratime, quetime, procdelay):
    latency = proptime + tratime + quetime + procdelay
    return latency

def propagation_time(distance, propspeed):
    proptime = distance / (propspeed)
    return proptime

def transmission_time(msgsize, bandwidth):
    tratime = (msgsize) / bandwidth
    return tratime

def convert_s_to_ms(time):
    x = 0
    while x != 3:
        time *= 10
        x += 1
    return time

msgsize = 2500 * 8 # 2.5KB in Bits
bandwidth = math.pow(10, 9) # 1 Gbps in Bits
distance = 12000 * 1000 # Assume 12,000 km -- km to m
propspeed = 2.4 * math.pow(10, 8) # light travels 2.4 x 10^8 m/s

p_time = convert_s_to_ms(propagation_time(distance, propspeed))
print(f"Propagation Time: {p_time:.3f} ms")
t_time = convert_s_to_ms(transmission_time(msgsize, bandwidth))
print(f"Transmission Time: {t_time:.3f} ms")


