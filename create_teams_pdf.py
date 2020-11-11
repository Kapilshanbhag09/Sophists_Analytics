from teamanalysis import totalteamstatisticslist
from fpdf import FPDF
pdf = FPDF()
pdf.set_font("Arial", size = 15) 
for i in totalteamstatisticslist:
    photoname=i[0][0]
    photodir="logos/"+photoname+".png"
    pdf.add_page()
    pdf.set_font("Arial",'B',size=20)
    pdf.image(photodir, 10, 10,25,25)
    pdf.cell(0, 25, txt = photoname.upper(), ln = 1, align = 'C') 
    pdf.image("logos/Sushiksha.png",175,10,25,25)
    pdf.line(10, 40, 200, 40)
    #firsttable
    pdf.set_font("Arial",'B',size=15)
    #pdf.cell(100, 5, txt = 'kapil')
    top=pdf.y+10 
    pdf.y=top
    offset=pdf.x+63
    pdf.multi_cell(63,7,"Total Messages Posted",1,0,)
    pdf.y=top
    pdf.x=offset
    pdf.multi_cell(63,7,"Messages in channel",1,0)
    pdf.y=top 
    pdf.x=offset+63
    pdf.multi_cell(64,7,"Total Reactions",1,0)

    #2nd table
    top=pdf.y 
    pdf.y=top
    offset=pdf.x+63
    pdf.multi_cell(63,7,str(i[0][1]),1,0)
    pdf.y=top
    pdf.x=offset
    pdf.multi_cell(63,7,str(i[0][2]),1,0)
    pdf.y=top 
    pdf.x=offset+63
    pdf.multi_cell(64,7,str(i[0][3]),1,0)
    #teamtabledescription
    pdf.set_font("Arial",'B',size=12)
    top=pdf.y+10
    pdf.y=top
    offset=pdf.x+135
    pdf.multi_cell(135,7,'Name',1,0)
    pdf.y=top
    pdf.x=offset
    pdf.multi_cell(55,7,"Member ID",1,0)
    #2nd row
    pdf.set_font("Arial",'B',size=10)
    top=pdf.y 
    pdf.y=top
    offset=pdf.x+25
    pdf.multi_cell(25,7,"Days Active",1,0)
    pdf.y=top
    pdf.x=offset
    pdf.multi_cell(35,7,"Messages posted",1,0)
    pdf.y=top 
    pdf.x=offset+35
    pdf.multi_cell(54,7,"Messages posted in channel",1,0)
    pdf.y=top 
    pdf.x=offset+35+54
    pdf.multi_cell(41,7,"Reactions added",1,0)
    pdf.y=top 
    pdf.x=offset+35+54+41
    pdf.multi_cell(35,7,"Last Active",1,0)

    '''
    pdf.cell(0,10,txt=str(i[0][1]),ln=1,align='L')
    pdf.cell(0,10,txt=str(i[0][2]),ln=1,align="L")
    pdf.cell(0,10,txt=str(i[0][3]),ln=1,align="L")
    '''
    #for the individual member:
    for mem in i[1]:
        
        #first row
        pdf.set_font("Arial",'B',size=11)
        top=pdf.y+3
        pdf.y=top
        offset=pdf.x+135
        pdf.multi_cell(135,7,mem[0],1,0)
        pdf.y=top
        pdf.x=offset
        pdf.multi_cell(55,7,mem[1],1,0)
        #second row
        pdf.set_font("Arial",'B',size=10)
        top=pdf.y 
        pdf.y=top
        offset=pdf.x+25
        pdf.multi_cell(25,7,mem[3],1,0)
        pdf.y=top
        pdf.x=offset
        pdf.multi_cell(35,7,mem[4],1,0)
        pdf.y=top 
        pdf.x=offset+35
        pdf.multi_cell(54,7,mem[5],1,0)
        pdf.y=top 
        pdf.x=offset+35+54
        pdf.multi_cell(41,7,mem[6],1,0)
        pdf.y=top 
        pdf.x=offset+35+54+41
        pdf.multi_cell(35,7,mem[7],1,0)


    print("completed "+str(photoname))
pdf.output("Sophists_team_analysis.pdf")