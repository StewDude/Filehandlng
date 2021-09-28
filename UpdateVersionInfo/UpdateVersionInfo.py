
import os

RootPath = os.path.dirname(os.path.abspath(__file__))
Versionfileloc = RootPath + "\BG96\inc\VersionInfo.h"

def ReadAllLines( filename ):
    lines = None
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def replaceline( lines, orignalline, replacewith ):
    if orignalline in lines:
        lines[lines.index(orignalline)] = replacewith
        print("\nLine: \"{}\" replaced with \"{}\" in file \"{}\"".format(orignalline, replacewith, Conffileloc))
        return lines
    else:
        return None

def WriteAllLines( filename, lines ):
    with open(filename, 'w') as f:
        return f.writelines(lines)

def UpdateVersionNumber(line, version):
    import re
    p = re.compile(r'(\d+)')  # a pattern for a number
    number = int(re.search(r'\d+', line).group(0))
    number = number + 1
    re.sub(r'\d+', line, str(number) )
    print("{} has been updated to version {}".format(version, number))




def update_lines( lines, ProtocolVersion, FirmwareVersion ):
    for line in lines:
        line = line.rstrip()  # remove '\n' at end of line
        if line.find( ProtocolVersion ):
            UpdateVersionNumber(line, ProtocolVersion)
        if line.find( FirmwareVersion ):
            UpdateVersionNumber(line, FirmwareVersion



versionfilelines = ReadAllLines( Versionfileloc )
ProtocolVersion ="#define PROTOCOL_REVISION_NUMBER"
FirmwareVersion = "#define FIRMWARE_REVISION_NUMBER"
update_lines( ProtocolVersion, FirmwareVersion )
WriteAllLines( Versionfileloc, versionfilelines )
