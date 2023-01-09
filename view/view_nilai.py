
data = {}
class Data():
     def __init__(self,data1,data2,data3,data4,data5,data6):
        while True:

            print("\n")
            print('.'*50)
            print('             DATA "MAHASISWA"          ')
            print('.'*50)

            x = input("> Choose the menu : ")

            print("\n")

            if x == 'Enter':
                self.ADD()
            elif x == 'Show':
                self.SHOW()
            elif x == 'Change':
                self.CHANGE()
            elif x == 'Delete':
                self.DELETE()
            elif x == 'Exit':
                self.EXIT()
                break
            
            else:
                exit()
     def ADD(self):
        print("Add Data")
        self.nim    = input('NIM\t            : ')
        self.nama   = input('Name\t        : ')
        self.tugas  = int(input('Duty value\t    : '))
        self.uts    = int(input('UTS value\t    : '))
        self.uas    = int(input('UAS value\t    : '))
        self.akhir = (self.tugas * 30/100) + (self.uts * 35/100) + (self.uas * 35/100)
        data[self.nim] = self.nama, self.tugas, self.uts, self.uas, self.akhir


class rajahappyanto(Data):

     def SHOW(self):  
        if data.items():
            print(100*'=')
            print('|   NO  |    NIM         |     NAME      |  DUTY  |   UTS   |   UAS   |     ENDED    |')
            print(100*'=')
            i = 0
            for a in data.items():
                i += 1
                print("|    {no:2d} | {0:14s} | {1:11s} | {2:7d} | {3:7d} | {4:7d} |    {5:6.2f}    |".format (a[0][: 14],a[1][0],a[1][1],a[1][2],a[1][3],a[1][4], no = i))
                print(100*'=')
    
datarjhpp = rajahappyanto("data1", "data2", "data3", "data4", "data5", "data6") 