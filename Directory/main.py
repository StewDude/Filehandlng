
import os

dir = "\\\\QNAP-TS-219\Video\Films"

#for file in os.listdir( dir ):
#    name = file
#    pos1 = name.find(".-")
#    pos2 = name.find(" (")
#    if pos1 > 0 or pos2 > 0:
#        if pos1 > 0:
#            pos_neg = pos1 + 2
#            number = int(name[pos_neg:pos_neg + 3])
#            if number > 19:
#                num = '1' + name[pos_neg:pos_neg + 3]
#            else:
#                num = '2' + name[pos_neg:pos_neg + 3]
#            new_name = name[:pos1]
#            new_name = new_name + " (" + num + ")"
#            print("{}  {}".format(name, new_name))

#        if pos2 > 0:
#            pos_neg = pos2 + 4
#            try:
#                number = int(name[pos_neg:-5])
#            if number > 19:
#                num = '19' + name[pos_neg:pos_neg + 2]
#            else:
#                num = '20' + name[pos_neg:pos_neg + 2]
#            new_name = name[:pos2]
#            new_name = new_name + " (" + num + ")"
#            print("{}  {}".format(name, new_name))

#        os.rename(dir + "/" + file, dir + "/" + "".join(new_name))

for file in os.listdir( dir ):
    if file.find("-"):
        print(file)


