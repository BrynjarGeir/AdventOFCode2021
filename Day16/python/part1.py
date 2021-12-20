#hexvalue = open('input').readline()

#intValue = int(hexvalue, 16)
#binValue = bin(intValue)[2:]

binValue = bin(int('1'+open("input").read(),16))[3:]



def getVersion(binValue, pos=0): return int(binValue[pos:pos+3], 2)

def getTypeID(binValue, pos=3): return int(binValue[pos:pos+3], 2)

def getLengthID(binValue, pos=6): return int(binValue[pos])

def getEncodedNumber(binValue, pos=6):
    endcodedNumber = ''
    while(True):
        if binValue[pos+1] == '0': lstNum = True
        else: lstNum = False
        endcodedNumber += binValue[pos+1:pos+5]
        pos += 6
        if lstNum:
            pos += 3
            break
    return endcodedNumber, binValue[pos:]

def getNumberOfSubPackets(binValue, pos=7): return int(binValue[pos:pos+11], 2)

def getLengthOfSubPackets(binValue, pos=7): return int(binValue[pos:pos+15], 2)

def findSubPacketsByLength(binValue, length):
    typeIDs = []; versions = []; encodedNumbers = []
    tmpBinValue = binValue
    while(True):
        try:
            typeIDs.append(getTypeID(tmpBinValue))
            versions.append(getVersion(tmpBinValue))
            encodedNumber, tmpBinValue = getEncodedNumber(tmpBinValue)
            encodedNumbers.append(encodedNumber)
            if len(binValue) - len(tmpBinValue) >= length or int(tmpBinValue) == 0: break
        except: break
    binValue = tmpBinValue
    return binValue, typeIDs, versions, encodedNumbers

def findSubPacketsByNumber(binValue, number): 
    typeIDs = []; versions =  []; encodedNumbers = []
    for _ in range(number):
        try:
            typeIDs.append(getTypeID(binValue))
            versions.append(getVersion(binValue))
            encodedNumber, binValue = getEncodedNumber(binValue)
            encodedNumbers.append(encodedNumber)
        except: break
    return binValue, typeIDs, versions, encodedNumbers



def getDecodedValues(binValue):
    decodedValues = []
    while(len(binValue) > 3):
        typeID = getTypeID(binValue)
        version = getVersion(binValue)
        if typeID == 4:
            decodedNumber, binValue = getEncodedNumber(binValue)
            currDict = {'version':version, 'typeID':typeID, 'decodedNumber':int(decodedNumber,2)}
            decodedValues.append(currDict)
        else:
            if getLengthID(binValue) == 0: 
                packetLength = getLengthOfSubPackets(binValue)
                binValue, typeIDs, versions, encodedNumbers = findSubPacketsByLength(binValue, packetLength)
            else:
                numberOfPackets = getNumberOfSubPackets(binValue)
                binValue, typeIDs, version, encodedNumbers = findSubPacketsByNumber(binValue, numberOfPackets)
            currDict = {'versions':versions, 'typeIDs':typeIDs, 'decodedNumber':[int(encodedNumber, 2) for encodedNumber in encodedNumbers]}
            decodedValues.append(currDict)
    return decodedValues

def getVersionSum(decodedValues):
    return sum(decodedValues[0]['versions'])

decodedValues = getDecodedValues(binValue)

print(getVersionSum(decodedValues))
