import winpcapy

# Open the default adapter
adapter = winpcapy.open_live("\\Device\\NPF_{1C49D9C6-C479-4075-B474-2F905A69F475}", 65536, 1, 0)

# Set the BPF filter to capture only packets to or from the specified IP address
bpf_filter = "host  47.244.249.151"
winpcapy.setfilter(adapter, bpf_filter)

# Start sniffing
winpcapy.dispatch(adapter, 0, callback)

# Define the callback function
def callback(header, packet):
  # Print the packet data
  print(packet)

# Close the adapter
winpcapy.close(adapter)
