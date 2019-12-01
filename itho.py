#!/usr/bin/env python

from pycc1101.pycc1101 import TICC1101

ticc1101 = TICC1101()

deviceId = [101, 89, 154, 153, 170, 105, 154, 86]

ithoMessage1FullCommandBytes = [1,84,213,85,50,203,52]
ithoMessage1MediumCommandBytes = [1,84,213,85,74,213,52]
ithoMessage1LowCommandBytes = [1,84,213,85,83,83,84]	
ithoMessage1Timer1CommandBytes = [1,83,83,84,204,202,180]	
ithoMessage1Timer2CommandBytes = [1,83,83,83,53,52,180]		
ithoMessage1Timer3CommandBytes = [1,83,83,82,173,82,180]			
ithoMessage1JoinCommandBytes = [0,170,171,85,84,202,180]	
ithoMessage1LeaveCommandBytes = [0,170,173,85,83,43,84]	

ithoMessage2FullCommandBytes = [6,89,150,170,165,101,90,150,85,149,101,89,102,85,150]
ithoMessage2MediumCommandBytes = [6,89,150,170,165,101,90,150,85,149,101,90,150,85,150]
ithoMessage2LowCommandBytes = [6,89,150,170,165,101,90,150,85,149,101,89,150,85,150]
ithoMessage2Timer1CommandBytes = [6,89,150,170,169,101,90,150,85,149,101,89,86,85,153]
ithoMessage2Timer2CommandBytes = [6,89,150,170,169,101,90,150,85,149,101,89,86,149,150]
ithoMessage2Timer3CommandBytes = [6,89,150,170,169,101,90,150,85,149,101,89,86,149,154]
ithoMessage2JoinCommandBytes = [9,90,170,90,165,165,89,106,85,149,102,89,150,170,165]
ithoMessage2LeaveCommandBytes = [9,90,170,90,165,165,89,166,85,149,105,90,170,90,165]

counterBytes24a = [1,2]
counterBytes24b = [84,148,100,164,88,152,104,168]
counterBytes25 = [149,165,153,169,150,166,154,170]
counterBytes26 = [96,160]
counterBytes41 = [5, 10, 6, 9]
counterBytes42 = [90, 170, 106, 154]
counterBytes43 = [154, 90, 166, 102, 150, 86, 170, 106]

counterBytes64 = [154,90,166,102,150,86,169,105,153,89,165,101,149,85,170,106]
counterBytes65 = [150,169,153,165,149,170,154,166]
counterBytes66 = [170,106]

def initSendMessage1():
    ticc1101._strobe(ticc1101.SRES)
    ticc1101._usDelay(1)
    ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2E)        #High impedance (3-state)
    ticc1101._writeSingleByte(ticc1101.FREQ2 ,0x21)        #00100001    878MHz-927.8MHz
    ticc1101._writeSingleByte(ticc1101.FREQ1 ,0x65)        #01100101
    ticc1101._writeSingleByte(ticc1101.FREQ0 ,0x6A)        #01101010
    ticc1101._writeSingleByte(ticc1101.MDMCFG4 ,0x07)    #00000111
    ticc1101._writeSingleByte(ticc1101.MDMCFG3 ,0x43)    #01000011
    ticc1101._writeSingleByte(ticc1101.MDMCFG2 ,0x00)    #00000000    2-FSK, no manchester encoding/decoding, no preamble/sync
    ticc1101._writeSingleByte(ticc1101.MDMCFG1 ,0x22)    #00100010
    ticc1101._writeSingleByte(ticc1101.MDMCFG0 ,0xF8)    #11111000
    ticc1101._writeSingleByte(ticc1101.CHANNR ,0x00)        #00000000
    ticc1101._writeSingleByte(ticc1101.DEVIATN ,0x40)    #01000000
    ticc1101._writeSingleByte(ticc1101.FREND0 ,0x17)        #00010111    use index 7 in PA table
    ticc1101._writeSingleByte(ticc1101.MCSM0 ,0x18)        #00011000    PO timeout Approx. 146us - 171us, Auto calibrate When going from IDLE to RX or TX (or FSTXON)
    ticc1101._writeSingleByte(ticc1101.FSCAL3 ,0xA9)        #10101001
    ticc1101._writeSingleByte(ticc1101.FSCAL2 ,0x2A)        #00101010
    ticc1101._writeSingleByte(ticc1101.FSCAL1 ,0x00)        #00000000
    ticc1101._writeSingleByte(ticc1101.FSCAL0 ,0x11)        #00010001
    ticc1101._writeSingleByte(ticc1101.FSTEST ,0x59)        #01011001    For test only. Do not write to this register.
    ticc1101._writeSingleByte(ticc1101.TEST2 ,0x81)        #10000001    For test only. Do not write to this register.
    ticc1101._writeSingleByte(ticc1101.TEST1 ,0x35)        #00110101    For test only. Do not write to this register.
    ticc1101._writeSingleByte(ticc1101.TEST0 ,0x0B)        #00001011    For test only. Do not write to this register.
    ticc1101._writeSingleByte(ticc1101.PKTCTRL0 ,0x12)    #00010010    Enable infinite length packets, CRC disabled, Turn data whitening off, Serial Synchronous mode
    ticc1101._writeSingleByte(ticc1101.ADDR ,0x00)        #00000000
    ticc1101._writeSingleByte(ticc1101.PKTLEN ,0xFF)        #11111111    #Not used, no hardware packet handling

    pa_table_send = [0x6F, 0x26, 0x2E, 0x8C, 0x87, 0xCD, 0xC7, 0xC0]
    ticc1101._writeBurst(ticc1101.PATABLE, pa_table_send)

    ticc1101._strobe(ticc1101.SIDLE)
    ticc1101._strobe(ticc1101.SIDLE)
    ticc1101._strobe(ticc1101.SIDLE)

    ticc1101._writeSingleByte(ticc1101.MDMCFG4 ,0x08)    #00001000
    ticc1101._writeSingleByte(ticc1101.MDMCFG3 ,0x43)    #01000011
    ticc1101._writeSingleByte(ticc1101.DEVIATN ,0x40)    #01000000
    ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2D)        #GDO0_Z_EN_N. When this output is 0, GDO0 is configured as input (for serial TX data).
    ticc1101._writeSingleByte(ticc1101.IOCFG1 ,0x0B)        #Serial Clock. Synchronous to the data in synchronous serial mode.

    ticc1101._strobe(ticc1101.STX)
    ticc1101._strobe(ticc1101.SIDLE)
    ticc1101._usDelay(1)
    ticc1101._strobe(ticc1101.SIDLE)

    ticc1101._writeSingleByte(ticc1101.MDMCFG4 ,0x08)    #00001000
    ticc1101._writeSingleByte(ticc1101.MDMCFG3 ,0x43)    #01000011
    ticc1101._writeSingleByte(ticc1101.DEVIATN ,0x40)    #01000000
    #ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2D)        #GDO0_Z_EN_N. When this output is 0, GDO0 is configured as input (for serial TX data).
    #ticc1101._writeSingleByte(ticc1101.IOCFG1 ,0x0B)        #Serial Clock. Synchronous to the data in synchronous serial mode.

    #Itho is using serial mode for transmit. We want to use the TX FIFO with fixed packet length for simplicity.
    ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2E)
    ticc1101._writeSingleByte(ticc1101.IOCFG1 ,0x2E)    
    ticc1101._writeSingleByte(ticc1101.PKTLEN , 19)
    ticc1101._writeSingleByte(ticc1101.PKTCTRL0 ,0x00)
    ticc1101._writeSingleByte(ticc1101.PKTCTRL1 ,0x00)

def initSendMessage2(command):
    finishTransfer()
        
    ticc1101._strobe(ticc1101.SRES)
    ticc1101._usDelay(1)
    ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2E)        #High impedance (3-state)
    ticc1101._writeSingleByte(ticc1101.FREQ2 ,0x21)        #00100001    878MHz-927.8MHz
    ticc1101._writeSingleByte(ticc1101.FREQ1 ,0x65)        #01100101
    ticc1101._writeSingleByte(ticc1101.FREQ0 ,0x6A)        #01101010    
    ticc1101._writeSingleByte(ticc1101.MDMCFG4 ,0x5A)    #difference compared to message1
    ticc1101._writeSingleByte(ticc1101.MDMCFG3 ,0x83)    #difference compared to message1
    ticc1101._writeSingleByte(ticc1101.MDMCFG2 ,0x00)    #00000000    2-FSK, no manchester encoding/decoding, no preamble/sync
    ticc1101._writeSingleByte(ticc1101.MDMCFG1 ,0x22)    #00100010
    ticc1101._writeSingleByte(ticc1101.MDMCFG0 ,0xF8)    #11111000
    ticc1101._writeSingleByte(ticc1101.CHANNR ,0x00)        #00000000
    ticc1101._writeSingleByte(ticc1101.DEVIATN ,0x50)    #difference compared to message1
    ticc1101._writeSingleByte(ticc1101.FREND0 ,0x17)        #00010111    use index 7 in PA table
    ticc1101._writeSingleByte(ticc1101.MCSM0 ,0x18)        #00011000    PO timeout Approx. 146us - 171us, Auto calibrate When going from IDLE to RX or TX (or FSTXON)
    ticc1101._writeSingleByte(ticc1101.FSCAL3 ,0xA9)        #10101001
    ticc1101._writeSingleByte(ticc1101.FSCAL2 ,0x2A)        #00101010
    ticc1101._writeSingleByte(ticc1101.FSCAL1 ,0x00)        #00000000
    ticc1101._writeSingleByte(ticc1101.FSCAL0 ,0x11)        #00010001
    ticc1101._writeSingleByte(ticc1101.FSTEST ,0x59)        #01011001    For test only. Do not write to this register.
    ticc1101._writeSingleByte(ticc1101.TEST2 ,0x81)        #10000001    For test only. Do not write to this register.
    ticc1101._writeSingleByte(ticc1101.TEST1 ,0x35)        #00110101    For test only. Do not write to this register.
    ticc1101._writeSingleByte(ticc1101.TEST0 ,0x0B)        #00001011    For test only. Do not write to this register.
    ticc1101._writeSingleByte(ticc1101.PKTCTRL0 ,0x12)    #00010010    Enable infinite length packets, CRC disabled, Turn data whitening off, Serial Synchronous mode
    ticc1101._writeSingleByte(ticc1101.ADDR ,0x00)        #00000000
    ticc1101._writeSingleByte(ticc1101.PKTLEN ,0xFF)        #11111111    #Not used, no hardware packet handling

    pa_table_send = [0x6F, 0x26, 0x2E, 0x8C, 0x87, 0xCD, 0xC7, 0xC0]
    ticc1101._writeBurst(ticc1101.PATABLE, pa_table_send)

    #difference, message1 sends a STX here
    ticc1101._strobe(ticc1101.SIDLE)
    ticc1101._strobe(ticc1101.SIDLE)

    ticc1101._writeSingleByte(ticc1101.MDMCFG4 ,0x5A)    #difference compared to message1
    ticc1101._writeSingleByte(ticc1101.MDMCFG3 ,0x83)    #difference compared to message1
    ticc1101._writeSingleByte(ticc1101.DEVIATN ,0x50)    #difference compared to message1
    ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2D)        #GDO0_Z_EN_N. When this output is 0, GDO0 is configured as input (for serial TX data).
    ticc1101._writeSingleByte(ticc1101.IOCFG1 ,0x0B)        #Serial Clock. Synchronous to the data in synchronous serial mode.

    ticc1101._strobe(ticc1101.STX)
    ticc1101._strobe(ticc1101.SIDLE)

    ticc1101._writeSingleByte(ticc1101.MDMCFG4 ,0x5A)    #difference compared to message1
    ticc1101._writeSingleByte(ticc1101.MDMCFG3 ,0x83)    #difference compared to message1
    ticc1101._writeSingleByte(ticc1101.DEVIATN ,0x50)    #difference compared to message1
    #ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2D)        #GDO0_Z_EN_N. When this output is 0, GDO0 is configured as input (for serial TX data).
    #ticc1101._writeSingleByte(ticc1101.IOCFG1 ,0x0B)        #Serial Clock. Synchronous to the data in synchronous serial mode.

    #Itho is using serial mode for transmit. We want to use the TX FIFO with fixed packet length for simplicity.
    ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2E)
    ticc1101._writeSingleByte(ticc1101.IOCFG1 ,0x2E)
    ticc1101._writeSingleByte(ticc1101.PKTCTRL0 ,0x00)
    ticc1101._writeSingleByte(ticc1101.PKTCTRL1 ,0x00)
    
    if command == 'IthoJoin':
        ticc1101._writeSingleByte(ticc1101.PKTLEN , 72)
    elif command == 'IthoLeave':
        ticc1101._writeSingleByte(ticc1101.PKTLEN , 57)
    else:
        ticc1101._writeSingleByte(ticc1101.PKTLEN , 50)

def finishTransfer():
    ticc1101._strobe(ticc1101.SIDLE)
    ticc1101._usDelay(1)
    ticc1101._writeSingleByte(ticc1101.IOCFG0 ,0x2E)
    ticc1101._usDelay(1)
    ticc1101._writeSingleByte(ticc1101.IOCFG1 ,0x2E)
    ticc1101._usDelay(1)
    ticc1101._strobe(ticc1101.SIDLE)
    ticc1101._strobe(ticc1101.SPWD)
    ticc1101._usDelay(1)

def createMessageStart(command, prev_command):
    msg = [170, 170, 170, 173, 51, 83, 51, 43, 84, 204]

    if command == 'IthoJoin':
        command_msg = ithoMessage1JoinCommandBytes
    elif command == 'IthoLeave':
        command_msg = ithoMessage1LeaveCommandBytes
    elif command == 'IthoFull':
        command_msg = ithoMessage1FullCommandBytes
    elif command == 'IthoMedium':
        command_msg = ithoMessage1MediumCommandBytes
    elif command == 'IthoLow':
        command_msg = ithoMessage1LowCommandBytes
    
    msg[-1] |= command_msg[0]
    msg += command_msg[1:]

    msg += [170, 171]

    if prev_command == 'IthoJoin':
        msg += [77]
    elif prev_command == 'IthoLeave':
        msg += [82]
    else:
        msg += [85]

    assert len(msg) == 19

    return msg

def counterToArray1(counter):
    return [
        counterBytes24a[(counter / 128)] | counterBytes24b[(counter % 128) / 16],
        counterBytes25[(counter % 16) % 8],
        counterBytes26[(counter % 16) / 8]
    ]

def commandToInt(command):
    return {
        'IthoFull': 37,
        'IthoMedium': 36,
        'IthoLow': 35
    }[command]

def calcByte41(counter, command):
    var = 0
    hi = 0
    if command == 'IthoJoin':
        hi = 96
        counter = 0
    elif command == 'IthoLeave':
        hi = 160
        counter = 0
    else:
        hi = 96
        var = 48 - commandToInt(command)
        if counter < var:
            counter = 74 - counter
    return (hi | counterBytes41[((counter - var) % 64) / 16])

def calcByte42(counter, command):
    if (command == 'IthoJoin') or (command == 'IthoLeave'):
        counter = 1
    else:
        counter += commandToInt(command)
    result = counterBytes42[counter / 64]
    if counter % 2 == 1:
        result -= 1
    return result

def calcByte43(counter, command):
    if (command == 'IthoJoin') or (command == 'IthoLeave'):
        counter = 0
    elif command == 'IthoFull':
        counter += 2
        if counter % 2 == 0:
            counter -= 1
    elif command == 'IthoMedium':
        pass
    elif command == 'IthoLow':
        if counter % 2 == 0:
            counter -= 1
    return counterBytes43[(counter % 16) / 2]

def counterToArray2(counter, command):
    return [
        calcByte41(counter, command),
        calcByte42(counter, command),
        calcByte43(counter, command)
    ]

def createMessageCommand(command, prev_command, counter):
    msg = [170, 170, 170, 170, 170, 170, 170, 171, 254, 0, 179, 42, 171, 42, 149, 154]
    msg += deviceId
    msg += counterToArray1(counter)

    if command == 'IthoJoin':
        command_msg = ithoMessage2JoinCommandBytes
    elif command == 'IthoLeave':
        command_msg = ithoMessage2LeaveCommandBytes
    elif command == 'IthoFull':
        command_msg = ithoMessage2FullCommandBytes
    elif command == 'IthoMedium':
        command_msg = ithoMessage2MediumCommandBytes
    elif command == 'IthoLow':
        command_msg = ithoMessage2LowCommandBytes

    msg[-1] |= command_msg[0]
    msg += command_msg[1:]

    msg += counterToArray2(counter, command)
    msg += [172, 170, 170, 170, 170, 170]

    assert len(msg) == 50

    return msg

def counterToArray3(counter):
    return [
        counterBytes64[(counter + 3) / 16],
        counterBytes65[counter % 8],
        counterBytes66[((counter - 13) % 16) / 8]
    ]

def createMessageJoin(command, prev_command, counter):
    msg = createMessageCommand(command, prev_command, counter)[0:-6]
    msg += deviceId[3:]
    msg += [85]
    msg += [165, 105, 89, 86, 106, 149]
    msg += deviceId
    msg += counterToArray3(counter)
    msg += [202, 170, 170, 170, 170]

    assert len(msg) == 72

    return msg

def sendCommand(command, prev_command, counter):
    msg1 = createMessageStart(command, prev_command)

    if command == 'IthoJoin':
        msg2 = createMessageJoin(command, prev_command, counter)
    else:
        msg2 = createMessageCommand(command, prev_command, counter)

    # Send messages
    for _ in range(0, 3):
        
        ticc1101.reset()

        initSendMessage1()
        ticc1101.sendData(msg1)

        ticc1101._usDelay(5)

        initSendMessage2(command)
        ticc1101.sendData(msg2)

        finishTransfer()
        ticc1101._usDelay(50)


if __name__ == '__main__':
    ticc1101.reset()
    ticc1101.selfTest()

    prev_command = 'IthoLow'
    counter = 0

    while True:
        print('\n1) IthoJoin')
        print('2) IthoFull')
        print('3) IthoMedium')
        print('4) IthoLow')
        print('q) Quit')
        choice = raw_input('? ')
        if choice == 'q':
            break
        command = {
            '1': 'IthoJoin',
            '2': 'IthoFull',
            '3': 'IthoMedium',
            '4': 'IthoLow'
        }[choice]

        sendCommand(command, prev_command, counter)
        prev_command = command
        counter += 1
