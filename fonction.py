import serial.tools.list_ports
import serial



def test():
    print("test fonction")


def com_ouvrir(com,baudrate,bytesize,parity,stopbits,button):
    #  connection_COM = serial.Serial(port="COM1",baudrate=9600,bytesize=8,parity="PARITY_NONE",stopbits="STOPBITS_ONE")
    #  print(connection_COM)
    if bool_COM_open == False:
        port = serial.Serial()

        # parametre port
        port.port = com
        # parametre baudrate
        port.baudrate = int(baudrate)
        # parametre bytesize
        switch = {"5": serial.FIVEBITS,"6": serial.SIXBITS,"7": serial.SEVENBITS,"8": serial.EIGHTBITS}
        port.bytesize = switch.get(bytesize,"Erreur bytesize")
        # parametre parity
        switch = {"none": serial.PARITY_NONE,"even": serial.PARITY_EVEN,"odd": serial.PARITY_ODD,"mark": serial.PARITY_MARK,
                  "space": serial.PARITY_SPACE}
        port.parity = switch.get(parity,"Erreur parity")
        # parametre bit de stop
        switch = {"1": serial.STOPBITS_ONE,"1.5": serial.STOPBITS_ONE_POINT_FIVE,"2": serial.STOPBITS_TWO}
        port.stopbits = switch.get(stopbits,"Erreur stopbit")

        with port as s:
            s.write(b'com start\r')
            s.write()

        button['text'] = "Fermer COM"
        bool_COM_open = True

    else:
        button['text'] = "Ouvrir COM"
        bool_COM_open = False




def get_port_com():
    arr_port = serial.tools.list_ports.comports(include_links=False)
    print(len(arr_port))

    for i in range(0,len(arr_port)):  # formmattage pour ne gardé que COMx
        arr_port[i] = str(arr_port[i]).split()[0]

    return arr_port
