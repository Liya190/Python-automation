import os
import time
import sys
import shutil
sys.path.insert(0,r"C:\Users\HP\PycharmProjects\5G Automation\VariableFiles")
import config_file

class attach:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        pass
    def ABC(self):

        pw = config_file.pw
        pw1 = config_file.pw1
        if pw1 == pw:
            os.chdir('D:/Automation')
            if not os.path.exists("D:/Automation/Locker"):
                if not os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}"):
                    os.mkdir("Locker")
                    print("Locker Folder Successfully created")
                else:
                    os.popen('attrib -h -s -r Locker')
                    os.rename("Locker.{645ff040-5081-101b-9f08-00aa002f954e}", "Locker")
                    print("Locker Folder has been Successfully Unlocked")
            else:
                print("Locker folder is not locked")
                #sys.exit()
        else:
            print("Wrong password! ,Please Enter right password")
    #q=unlock()
# Attach
# Testcase 1.2
    #moving source file to destination folder

    def move_ue_gnb(self):
        source1 = 'D:/Automation/Locker/UE/request.txt'
        source2 = 'D:/Automation/Locker/gnb/response.txt'
        destination1 = 'D:/Automation/Locker/gnb'
        destination2 = 'D:/Automation/Locker/UE'
        dest1 = shutil.move(source1, destination1)
        dest2 = shutil.move(source2, destination2)
        print('messages  moved')
    #x = move_ue_gnb()

    # Validating messages
    def rach_request_val(self):
        req_msg1 = config_file.message_1
        req_msg2 = config_file.message_3
        req_file = open('D:/Automation/Locker/gnb/request.txt')
        read_req = req_file.read()
        if req_msg1 in read_req and req_msg2 in read_req:
            print('req messages are present in req file')
        else:
            print('req message not found')
        req_file.close()
    #k = rach_req_val()

    def rach_respone_val(self):
        resp_msg1 = config_file.message_2
        resp_msg2 = config_file.message_4
        print(resp_msg1, resp_msg2)
        resp_file = open('D:/Automation/Locker/UE/response.txt','r')
        read_resp = resp_file.read()
        print(read_resp)

        if resp_msg1 in read_resp and resp_msg2 in read_resp:
            print('resp messages are present in resp file')
        else:
            print('resp message not found')
        resp_file.close()
    #s = rach_resp_val()
# testcase 1.12
    def move_sour_des(self):
        source=[config_file.source1,config_file.source2,config_file.source3,config_file.source4,config_file.source5,config_file.source6,config_file.source7,config_file.source8,config_file.source9,config_file.source10,config_file.source11,config_file.source12,config_file.source13,config_file.source14,config_file.source15,config_file.source16,config_file.source17,config_file.source18,config_file.source19,config_file.source20,config_file.source21,config_file.source22]
        destination=[config_file.destination1,config_file.destination2,config_file.destination3,config_file.destination4,config_file.destination5,config_file.destination6,config_file.destination7,config_file.destination8,config_file.destination9,config_file.destination10,config_file.destination11,config_file.destination12,config_file.destination13,config_file.destination14,config_file.destination15,config_file.destination16,config_file.destination17,config_file.destination18,config_file.destination19,config_file.destination20,config_file.destination21,config_file.destination22]
        for i in range(0,len(source)):
            shutil.move(source[i],destination[i])
        print('Messages moved')

    def reset(self):
        file=open('D:/Automation/Locker/amf/gnb_to_amf.txt','r')
        #file.truncate()
        a= [config_file.message_34, config_file.message_35]
        l=[]
        for line in file:
            for i in a:
                if i in line:
                    d= open('D:/Automation/Locker/amf/oamf_to_amf.txt','w')
                    d.truncate()
                    d.write('new ue context')
        d.close()
        file.close()
#validating
    def val(self):
        file=[config_file.file1,config_file.file2,config_file.file3,config_file.file4,config_file.file5,config_file.file6,config_file.file7,config_file.file8,config_file.file9,config_file.file10,config_file.file11,config_file.file12,config_file.file13,config_file.file14,config_file.file15,config_file.file16,config_file.file17,config_file.file18,config_file.file19,config_file.file20,config_file.file21,config_file.file22,config_file.file23,config_file.file24,config_file.file25,config_file.file26,config_file.file27,config_file.file28]
        msg=[config_file.message_5,config_file.message_6,config_file.message_7,config_file.message_8,config_file.message_9,config_file.message_10,config_file.message_11,config_file.message_12,config_file.message_13,config_file.message_14,config_file.message_15,config_file.message_16,config_file.message_17,config_file.message_18,config_file.message_19,config_file.message_20,config_file.message_21,config_file.message_22,config_file.message_23,config_file.message_24,config_file.message_25,config_file.message_26,config_file.message_27,config_file.message_28,config_file.message_29,config_file.message_30,config_file.message_31,config_file.message_32]
        for i in range(0,len(file)):
            f=open(file[i])
            read=f.read()
            if msg[i] in read:
                print('All Messages are present')
            else:
                print('All Messages are not present')
            f.close()
# testcase_1.30
    def move_gnb_dut(self):
        source23 = 'D:/Automation/Locker/gnb/gnb_to_dut.txt'
        source24 = 'D:/Automation/Locker/dut/dut_to_gnb.txt'
        destination23 = 'D:/Automation/Locker/dut'
        destination24 = 'D:/Automation/Locker/gnb'
        dest1 = shutil.move(source23, destination23)
        dest2 = shutil.move(source24, destination24)
        print('messages  moved')
    #validating
    def gnb_request_val(self):
        req_msg55 = config_file.message_38
        dugn_file = open('D:/Automation/Locker/gnb/dut_to_gnb.txt')
        read_dugn = dugn_file.read()
        if req_msg55 in read_dugn:
            print('req messages are present in req file')
        else:
            print('req message not found')
        dugn_file.close()
    def dut_resp_val(self):
        req_msg56 = config_file.message_37
        dut_file = open('D:/Automation/Locker/dut/gnb_to_dut.txt')
        read_dut = dut_file.read()
        if req_msg56 in read_dut:
            print('req messages are present in req file')
        else:
            print('req message not found')
        dut_file.close()
# testcase_1.23
    def move_cell_ue(self):
        source25 = 'D:/Automation/Locker/neighbouring_cells/neigh_cell1.txt'
        source26 = 'D:/Automation/Locker/neighbouring_cells/neigh_cell2.txt'
        destination25 = 'D:/Automation/Locker/UE'
        destination26 = 'D:/Automation/Locker/UE'
        dest25 = shutil.move(source25, destination25)
        dest26 = shutil.move(source26, destination26)
        print('messages  moved')

    def sel_criteria(self):
        sel_msg= config_file.message_39
        sel_file1= open('D:/Automation/Locker/UE/neigh_cell1.txt')
        sel_file2= open('D:/Automation/Locker/UE/neigh_cell2.txt')
        read_sel1= sel_file1.read()
        read_sel2=sel_file2.read()
        if sel_msg in read_sel1 and sel_msg in read_sel2:
            print('Neighbouring cells fulfil the selection criteria')
        else:
            print('Neighbouring cells doesnot fulfil selection criteria')
    def resel_criteria(self):
        resel_msg1= config_file.message_40
        resel_msg2= config_file.message_41
        resel_file= open('D:/Automation/Locker/UE/ue_rank_cal.txt')
        resel_read= resel_file.read()
        if resel_msg1 in resel_read and resel_msg2 in resel_read:
            print('ue may reselect cell1 and cell2 using r criteria ')
        elif resel_msg1 in resel_read:
            print('ue may reselect cell1 using r criteria')
        elif resel_msg2 in resel_read:
            print('ue may reselect cell2 using r criteria')
        else:
            print('ue maynot reselect cell1 and cell2 using r criteria')

    def best_cell(self):
        best_msg=config_file.message_42
        best_file= open('D:/Automation/Locker/UE/ue_rank_cal.txt')
        best_read= best_file.read()
        if best_msg in best_read:
            print('Cell1 is the best cell')
        else:
            print('Cell2 is the best cell')
    def lock(self):  # lock the folder
        p_w = config_file.pw
        pw1 = config_file.pw1
        if p_w == pw1:
            os.chdir('D:/Automation')
            # print("Your path Successfully Changed")
            # If Locker folder or Recycle bin does not exist then we will be create Locker Folder
            if os.path.exists('D:/Automation/Locker'):
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # sys.exit()
                # break
            else:
                os.path.exists("Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.mkdir("Locker")
                print("Locker Folder Successfully created")
                os.rename("Locker", "Locker.{645ff040-5081-101b-9f08-00aa002f954e}")
                os.popen('attrib +h +s +r Locker.{645ff040-5081-101b-9f08-00aa002f954e}')
                print("Locker folder has been successfully locked")
                # break
        else:
            print("wrong password! Try again later")
            # break
#handover
# Testcase 1.20
    def handover_sour_des(self):
        source=[config_file.source_30,config_file.source_31,config_file.source_32,config_file.source_33,config_file.source_34,config_file.source_35,config_file.source_36,config_file.source_37,config_file.source_38,config_file.source_39,config_file.source_01]
        destination=[config_file.des_30,config_file.des_31,config_file.des_32,config_file.des_33,config_file.des_34,config_file.des_35,config_file.des_36,config_file.des_37,config_file.des_38,config_file.des_39,config_file.des_39]
        for i in range(0,len(source)):
            shutil.move(source[i],destination[i])
        print('Messages moved')
    def hand_val(self):
        file=[config_file.file31,config_file.file32,config_file.file33,config_file.file34,config_file.file35,config_file.file36,config_file.file37,config_file.file38,config_file.file39,config_file.file40,config_file.file41,config_file.file42,config_file.file43,config_file.file44,config_file.file45]
        msg=[config_file.msg31,config_file.msg32,config_file.msg33,config_file.msg34,config_file.msg35,config_file.msg36,config_file.msg37,config_file.msg38,config_file.msg39,config_file.msg40,config_file.msg41,config_file.msg42,config_file.msg43,config_file.msg44,config_file.msg45]
        for i in range(0,len(file)):
            f=open(file[i])
            read=f.read()
            if msg[i] in read:
                print('All Messages are present')
            else:
                print('All Messages are not present')
            f.close()
    def hand_veri(self):
        mssg=[config_file.msg38,config_file.msg46]
        files=[config_file.file47,config_file.file46]
        for j in range(0,len(files)):
            fs=open(files[j])
            rs=fs.read()
            if mssg[j] in rs:
                print('Verified')
            else:
                print('Not Verified')
            fs.close()
# Testcase 1.21
    def handover_multi_gnb(self):
        gnb=[config_file.gnb1,config_file.gnb2,config_file.gnb3]
        tamf=[config_file.tamf1,config_file.tamf2,config_file.tamf3]
        sognb=[config_file.sognb1,config_file.sognb2,config_file.sognb3]
        amfso=[config_file.amfso1,config_file.amfso2,config_file.amfso3]
        amfta=[config_file.amfta1,config_file.amfta2,config_file.amfta3]
        soamf=[config_file.soamf1,config_file.soamf2,config_file.soamf3]
        sogta=[config_file.sogta1,config_file.sogta2,config_file.sogta3]
        ugnb=[config_file.ugnb1,config_file.ugnb2,config_file.ugnb3]
        sue=[config_file.sue1,config_file.sue2,config_file.sue3]
        ugnbb=[config_file.ugnb11,config_file.ugnb22,config_file.ugnb33]
        for j in range(0,len(gnb)):
            source=[sue[j],ugnb[j],soamf[j],sogta[j],sognb[j],tamf[j],amfta[j],amfso[j],ugnbb[j]]
            destination=[config_file.des_30,config_file.des_31,config_file.des_32,gnb[j],config_file.des_34,config_file.des_35,gnb[j],config_file.des_37,config_file.des_39]
            for i in range(0,len(source)):
                shutil.move(source[i],destination[i])
        print('Messages moved')
    def multi_gnb_val(self):
        file=[config_file.file50,config_file.file51,config_file.file52,config_file.file53,config_file.file54,config_file.file55,config_file.file56,config_file.file57,config_file.file58,config_file.file59,config_file.file60,config_file.file61,config_file.file59,config_file.file60,config_file.file61,config_file.file62,config_file.file63,config_file.file64,config_file.file65,config_file.file66,config_file.file67,config_file.file68,config_file.file69,config_file.file70,config_file.file68,config_file.file69,config_file.file70,config_file.file71,config_file.file72,config_file.file73,config_file.file71,config_file.file72,config_file.file73]
        msg=[config_file.msg32,config_file.msg32,config_file.msg32,config_file.msg32,config_file.msg32,config_file.msg32,config_file.msg37,config_file.msg37,config_file.msg37,config_file.msg40,config_file.msg40,config_file.msg40,config_file.msg41,config_file.msg41,config_file.msg41,config_file.msg35,config_file.msg35,config_file.msg35,config_file.msg35,config_file.msg35,config_file.msg35,config_file.msg33,config_file.msg33,config_file.msg33,config_file.msg34,config_file.msg34,config_file.msg34,config_file.msg44,config_file.msg44,config_file.msg44,config_file.msg45,config_file.msg45,config_file.msg45]
        for i in range(0,len(file)):
            f=open(file[i])
            read=f.read()
            if msg[i] in read:
                print('All Messages are present')
            else:
                print('All Messages are not present')
            f.close()
    def multi_gnb_veri(self):
        filee=[config_file.sourc1,config_file.sourc2,config_file.sourc3]
        mssge=config_file.msg38
        for k in range(0,len(filee)):
            fe=open(filee[k])
            ra=fe.read()
            if mssge in ra:
                print('Verified')
            else:
                print('Not Verified')
            fe.close()
#Testcase 1.23
    def move_mul(self):
        uta=[config_file.se110,config_file.se210,config_file.se310,config_file.se41,config_file.se51,config_file.se61,config_file.se71,config_file.se81,config_file.se91,config_file.se101,config_file.se111,config_file.se121,config_file.se131,config_file.se141,config_file.se151,config_file.se161]
        uetgnb=[config_file.source301,config_file.source302,config_file.source303,config_file.source304,config_file.source305,config_file.source306,config_file.source307,config_file.source308,config_file.source309,config_file.source310,config_file.source311,config_file.source312,config_file.source313,config_file.source314,config_file.source315,config_file.source316]
        gtue=[config_file.source414,config_file.source415,config_file.source416,config_file.source417,config_file.source418,config_file.source419,config_file.source420,config_file.source421,config_file.source422,config_file.source423,config_file.source424,config_file.source425,config_file.source426,config_file.source427,config_file.source428,config_file.source429]
        user=[config_file.user119,config_file.user212,config_file.user312,config_file.user41,config_file.user51,config_file.user61,config_file.user71,config_file.user81,config_file.user91,config_file.user101,config_file.user111,config_file.user121,config_file.user131,config_file.user141,config_file.user151,config_file.user161]
        sou=[config_file.s1,config_file.s2,config_file.s3,config_file.s4,config_file.s5,config_file.s6]
        des=[config_file.des_32,config_file.des_36,config_file.des_32,config_file.des_31,config_file.des_36,config_file.des_31]
        for j in range(0,len(uetgnb)):
            source=[uetgnb[j],gtue[j],uta[j]]
            destination=[config_file.des_188,user[j],config_file.des_399]
            for i in range(0,len(source)):
                shutil.move(source[i],destination[i])
        for x in range(0,len(sou)):
            shutil.move(sou[x],des[x])

        print('Messages moved')
    def mul_val(self):
        message1=config_file.msg44
        message2=config_file.msg45
        message3=config_file.msg288

        file1=[config_file.source500,config_file.source501,config_file.source502,config_file.source503,config_file.source504,config_file.source505,config_file.source506,config_file.source507,config_file.source508,config_file.source509,config_file.source510,config_file.source511,config_file.source512,config_file.source513,config_file.source514,config_file.source515]
        file2=[config_file.source516,config_file.source517,config_file.source518,config_file.source519,config_file.source520,config_file.source521,config_file.source522,config_file.source523,config_file.source524,config_file.source525,config_file.source526,config_file.source527,config_file.source528,config_file.source529,config_file.source530,config_file.source531]
        file3=[config_file.fi1,config_file.fi2,config_file.fi3,config_file.fi3,config_file.fi4,config_file.fi5,config_file.fi5,config_file.fi6]
        msg1=[config_file.mg1,config_file.mg2,config_file.mg3,config_file.mg4,config_file.mg5,config_file.mg6,config_file.mg7,config_file.mg8]
        for j in range(0,len(msg1)):
            ff=open(file3[j])
            r=ff.read()
            if msg1[j] in r:
                print('All msgs are there')
            else:
                print('No messages')
        for i in range(0,len(file1)):
            f=open(file1[i])
            f1=open(file2[i])
            read=f.read()
            read1=f1.read()
            if message1 in read and message2 and message3 in read1:
                print('All Messages are present')
            else:
                print('All Messages are not present')
            f.close()
            f1.close()
            ff.close()
    def mul_veri(self):
        d=[config_file.de1,config_file.de2,config_file.de3,config_file.de4,config_file.de5,config_file.de6,config_file.de7,config_file.de8,config_file.de9,config_file.de10,config_file.de11,config_file.de12,config_file.de13,config_file.de14,config_file.de15,config_file.de16]
        message4=config_file.mg101
        for t in range(0,len(d)):
            fr=open(d[t])
            rr=fr.read()
            if message4 in rr:
                print('Verified')
            else:
                print('Not Verified')
            fr.close()
# Testcase 1.24
    def move_multiuser(self):
        utaa=[config_file.se1,config_file.se2,config_file.se3,config_file.se4,config_file.se5,config_file.se6,config_file.se7,config_file.se8,config_file.se9,config_file.se10,config_file.se11,config_file.se12,config_file.se13,config_file.se14,config_file.se15,config_file.se16,config_file.se17,config_file.se18,config_file.se19,config_file.se20,config_file.se21,config_file.se22,config_file.se23,config_file.se24,config_file.se25,config_file.se26,config_file.se27,config_file.se28,config_file.se29,config_file.se30,config_file.se31,config_file.se32]
        utg=[config_file.source600,config_file.source601,config_file.source602,config_file.source603,config_file.source604,config_file.source605,config_file.source606,config_file.source607,config_file.source608,config_file.source609,config_file.source610,config_file.source611,config_file.source612,config_file.source613,config_file.source614,config_file.source615,config_file.source616,config_file.source617,config_file.source618,config_file.source619,config_file.source620,config_file.source621,config_file.source622,config_file.source623,config_file.source624,config_file.source625,config_file.source626,config_file.source627,config_file.source628,config_file.source629,config_file.source630,config_file.source631]
        gtu=[config_file.source632,config_file.source633,config_file.source634,config_file.source635,config_file.source636,config_file.source637,config_file.source638,config_file.source639,config_file.source640,config_file.source641,config_file.source642,config_file.source643,config_file.source644,config_file.source645,config_file.source646,config_file.source647,config_file.source648,config_file.source649,config_file.source650,config_file.source651,config_file.source652,config_file.source653,config_file.source654,config_file.source655,config_file.source656,config_file.source657,config_file.source658,config_file.source659,config_file.source660,config_file.source661,config_file.source662,config_file.source663]
        user1=[config_file.user1,config_file.user2,config_file.user3,config_file.user4,config_file.user5,config_file.user6,config_file.user7,config_file.user8,config_file.user9,config_file.user10,config_file.user11,config_file.user12,config_file.user13,config_file.user14,config_file.user15,config_file.user16,config_file.user17,config_file.user18,config_file.user19,config_file.user20,config_file.user21,config_file.user22,config_file.user23,config_file.user24,config_file.user25,config_file.user26,config_file.user27,config_file.user28,config_file.user29,config_file.user30,config_file.user31,config_file.user32]
        sou=[config_file.s11,config_file.s22,config_file.s33,config_file.s44,config_file.s55,config_file.s66]
        des=[config_file.des_32,config_file.des_36,config_file.des_32,config_file.des_31,config_file.des_36,config_file.des_31]
        for j in range(0,len(utg)):
            source=[utg[j],gtu[j],utaa[j]]
            destination=[config_file.des_189,user1[j],config_file.des_395]
            for i in range(0,len(source)):
                shutil.move(source[i],destination[i])
        for x in range(0,len(sou)):
            shutil.move(sou[x],des[x])

        print('Messages moved')

    def multi_val(self):
        message1=config_file.msg44
        message2=config_file.msg45
        message3=config_file.msg288
        #message4=config_file.mg101
        file11=[config_file.sour1,config_file.sour2,config_file.sour3,config_file.sour4,config_file.sour5,config_file.sour6,config_file.sour7,config_file.sour8,config_file.sour9,config_file.sour10,config_file.sour11,config_file.sour12,config_file.sour13,config_file.sour14,config_file.sour15,config_file.sour16,config_file.sour17,config_file.sour18,config_file.sour19,config_file.sour20,config_file.sour21,config_file.sour22,config_file.sour23,config_file.sour24,config_file.sour25,config_file.sour26,config_file.sour27,config_file.sour28,config_file.sour29,config_file.sour30,config_file.sour31,config_file.sour32]
        file22=[config_file.sour33,config_file.sour34,config_file.sour35,config_file.sour36,config_file.sour37,config_file.sour38,config_file.sour39,config_file.sour40,config_file.sour41,config_file.sour42,config_file.sour43,config_file.sour44,config_file.sour45,config_file.sour46,config_file.sour47,config_file.sour48,config_file.sour49,config_file.sour50,config_file.sour51,config_file.sour52,config_file.sour53,config_file.sour54,config_file.sour55,config_file.sour56,config_file.sour57,config_file.sour58,config_file.sour59,config_file.sour60,config_file.sour61,config_file.sour62,config_file.sour63,config_file.sour64]
        file33=[config_file.fi11,config_file.fi22,config_file.fi33,config_file.fi33,config_file.fi44,config_file.fi55,config_file.fi55,config_file.fi66]
        msg1=[config_file.mg1,config_file.mg2,config_file.mg3,config_file.mg4,config_file.mg5,config_file.mg6,config_file.mg7,config_file.mg8]
        for j in range(0,len(msg1)):
            ff1=open(file33[j])
            r=ff1.read()
            if msg1[j] in r:
                print('All msgs are there')
            else:
                print('No messages')
        for i in range(0,len(file11)):
            f1=open(file11[i])
            f11=open(file22[i])
            read11=f1.read()
            read12=f11.read()
            if message1 in read11 and message2 and message3 in read12:
                print('All Messages are present')
            else:
                print('All Messages are not present')
            f1.close()
            f11.close()
            ff1.close()
    def multiuser_veri(self):
        di=[config_file.de1110,config_file.de21,config_file.de31,config_file.de41,config_file.de51,config_file.de61,config_file.de71,config_file.de81,config_file.de91,config_file.de101,config_file.de111,config_file.de121,config_file.de131,config_file.de141,config_file.de151,config_file.de161,config_file.de1112,config_file.de211,config_file.de311,config_file.de411,config_file.de511,config_file.de611,config_file.de711,config_file.de811,config_file.de911,config_file.de1011,config_file.de1211,config_file.de1311,config_file.de1411,config_file.de1511,config_file.de1611]
        message4=config_file.mg101
        for y in range(0,len(di)):
            frr=open(di[y])
            rrr=frr.read()
            if message4 in rrr:
                print('Verified')
            else:
                print('Not Verified')
            frr.close()

#c=attach()
#d=c.multiuser_veri()
