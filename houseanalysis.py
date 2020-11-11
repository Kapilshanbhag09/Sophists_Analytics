from teamanalysis import totalteamstatisticslist
houselist=[[['Mithila'],['Ankuram','Lakshak','Sarvathr','Urja']],[['Nalanda'],['Achintya','Ayusheer','Samanvay','Sankalp']],[['Takshashila'],['Abhyuday','Avishkar','Ekyam','Udayagiri']],[['Vikramshila'],['Atulya','Sudhaksha','Tejas','Vajra']]]
housestatisticslist=[]
#print(totalteamstatisticslist[0][0])
for house in houselist:
    houseandteamlist=[]
    houselist=[]
    teamlist=[]
    housemess=int(0)
    housemessincha=int(0)
    housereactions=int(0)
    for teams in house[1]:
        for i in totalteamstatisticslist:
            if teams==i[0][0]:
                housemess=housemess+int(i[0][1])
                housemessincha=housemessincha+int(i[0][2])
                housereactions=housereactions+int(i[0][3])
                teamlist.append(i[0])
    houselist.append(house[0][0])
    houselist.append(housemess)
    houselist.append(housemessincha)
    houselist.append(housereactions)
    houseandteamlist.append(houselist)
    houseandteamlist.append(teamlist)
    housestatisticslist.append(houseandteamlist)

