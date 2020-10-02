import bluetooth
addr = "74:E5:43:D5:7B:4D"
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((addr,2))
sock.setblocking(False)