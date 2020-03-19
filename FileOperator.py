import os.path

class FileOperator():
    """Performs read & write operations"""
    def __init__(self):
        """FileOperator constructor"""
        pass

    def readFromFile(self, fileName='default.dat'):
        """Returns all lines from selected file"""
        outputList = []
        with open(fileName) as dataFile:
            for line in dataFile:
                # Strip off endline symbol
                outputList.append(line.strip('\n'))
        return outputList

    def saveToFile(self, linesList, fileName='default_out.dat'):
        """Writes lines to a file"""
        with open(fileName, 'w') as outputFile:
            # Write every line from a linesList
            for line in linesList:
                outputFile.write(line+'\n')

if __name__ == '__main__':
    # File load/save test
    from MixturesEncoderDecoder import MixturesEncoderDecoder
    fileOperator = FileOperator()
    lineList = []
    lineList.append('1:9        Epoxy/D520')
    lineList.append('1:3:6      Epo/Des1/W500')
    fileOperator.saveToFile(lineList, 'default.dat')
    strList = fileOperator.readFromFile()

    # Line decoding test
    coder = MixturesEncoderDecoder()
    decoded1 = coder.decodeString(strList[1])
    print(decoded1)

    # Data encoding text
    codedString = coder.encodeData(decoded1[0], decoded1[1])
    print(codedString)

