def serial_scanner():
    import serial.tools.list_ports

    list_of_serial_ports = serial.tools.list_ports.comports()
    connected = []
    str(connected)
    for element in list_of_serial_ports:
        connected.append(element.device)
    # connected = str(connected)
    print(connected)
    for element in connected:
        print(element)


if __name__ == '__main__':
    serial_scanner()