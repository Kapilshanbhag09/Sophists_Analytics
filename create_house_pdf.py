from houseanalysis import housestatisticslist
from fpdf import FPDF
pdf = FPDF()

for i in housestatisticslist:
    pdf.add_page()
    pdf.set_font("Arial", 'B',size = 20) 
    houselogoname="logos/"+i[0][0]+".png"
    print("Calculating for "+i[0][0] )
    pdf.image(houselogoname,10,10,35,35)
    pdf.cell(0, 30, txt = i[0][0].upper(), ln = 1, align = 'C')
    pdf.image("logos/Sushiksha.png",165,10,35,35)
    pdf.line(10, 50, 200, 50)
    #firsttable
    #row one
    pdf.set_font("Arial", 'B',size = 15) 
    top=pdf.y+15 
    pdf.y=top
    offset=pdf.x+63
    pdf.multi_cell(63,7,"Total Messages Posted",1,0,)
    pdf.y=top
    pdf.x=offset
    pdf.multi_cell(63,7,"Messages in channel",1,0)
    pdf.y=top 
    pdf.x=offset+63
    pdf.multi_cell(64,7,"Total Reactions",1,0)
    #second row
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
    #teamsinage
    teamimageheight=int(80)
    teamtableheight=int(0)
    for teams in i[1]:
        pdf.image("logos/"+teams[0]+".png",10,teamimageheight,30,30)
        teamimageheight=teamimageheight+45
        top=pdf.y +44-teamtableheight
        pdf.y=top
        offset=pdf.x+63
        pdf.multi_cell(63,7,str(teams[1]),1,0)
        pdf.y=top
        pdf.x=offset
        pdf.multi_cell(63,7,str(teams[2]),1,0)
        pdf.y=top 
        pdf.x=offset+63
        pdf.multi_cell(64,7,str(teams[3]),1,0)
        teamtableheight=teamtableheight+3











pdf.output("Sophists_house_analysis.pdf")
print("Pdf created in same directory file with name Sophists_house_analysis.pdf")