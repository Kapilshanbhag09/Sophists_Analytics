from csv import reader
from fpdf import FPDF
pdf = FPDF()
pdf.set_font("Arial", size = 15) 
#https://towardsdatascience.com/creating-pdf-files-with-python-ad3ccadfae0f link to know about pdf making
teammemlist={"Abhyuday":[['U01AND9S3EK','Dhanaraj Prabhu'],['U011SJUV2RK','Kavita Prabhu'],['U01B7RJTBBQ','Prajwal Purushotham Varekar'],['U011SJSTLAH','Prakash Pai'],['U01BM4QUG85','Shridhar J P'],['U011SJTD48M','Suraj Nayak'],['U011SJTABT7','Suraj Pai K'],['UUG3PS2PN','Vineet Nayak S']],
        "Achintya":[['U011SJTBNR3','Ajay Kini'],['U011SJTPWDT','Apeksha M Prabhu'],['U01ANK416Q7','Jevisha Sweety Fernandes'],['U011SJU6VB7','Vishal Kharvi'],['U01BSJJ6332','Laxminarayan Shenoy'],['UU4EW4N90','Niranjan Kamath'],['U011SJRRE2Z','Sameeksha Bhat'],['U01BFUSKN7K','Srilakshmi  Kamath'],['U011SJV2LE9','Sumanth K'],['U01ANJ730KZ','Vaidik S Prabhu']],
        "Ankuram":[['U011SJUERAR','Ananth G Prabhu'],['U01AW0GAGVC','Damodar Prabhu'],['U01B8UH7M5J','Jagrathi J Nayak'],['U011SJTJDFX','Karthik Shenoy'],['U011SJTFRGD','Kavita Satish Kamath'],['U012A078DQU','Keerthi Kamath'],['U011ZAWDETF','Prajwal B Kamath'],['U01B31TEY1Z','Sandesha Dsouza'],['U011SJTRB2R','Soumya Shenoy'],['U011SJTEFS9','Sucheta Shanbhag'],['U017C274RJ7','Vaishnavi S Salvankar']],
        "Atulya":[['U01AW6MFTFY','Adithya Naik'],['U011SJVASFP','Prathveesh Hulekal'],['U01BFHEEARF','Prinson Joel Pereira'],['U012JKFF858','Rakesh Shanbhag'],['U011ZAW9WTF','Raksha Baliga'],['U011SJSJV6Z','Samarth Kamath'],['U011SJT7B0D','Santhosh Patkar'],['U0149NLCVPD','Sarwesh Shenvi'],['U011SJSQQBX','Sukanya Shet S']],
        "Avishkar":[['U012GE0D6KT','Aishwarya A'],['U011SJSEB9T','Apoorva Prabhu R'],['U011SJVBYH3','Bhargavi Nayak'],['U01B0F73H3Q','Hrithika Pai'],['U011SJVEQCD','Namratha Nayak'],['U01AW4FB4BG','Raksha Shenoy'],['U011SJU5B6H','Svadhi Shenoy'],['U01B8GUH4US','Swathi Nagekar'],['U01AZNNC5PX','Vinutha Shenoy']],
        "Ayusheer":[['U011SJU25LM','Deviprasad'],['U012QHE211N','Gagan S Shenoy'],['U011SJSHDTP','Nanda Kishor M Pai'],['U01AZPY50VB','Prateeksha K Ankolekar'],['U011SJV41E1','Rajath Prabhu'],['U012A87H92Q','Sahana'],['U011SJU89JR','Srinidhi V Prabhu'],['U011SJSCTBP','Sudarshan N Kamat'],['U01467XM7DF','Sudeeksha Nayak'],['U0120N27V42','Vinayaka N Shenoy'],['U01AWB83E8N','Yash S Prabhudesai']],
        "Ekyam":[['U011SJRGP0D','Alisha Mesta'],['U017KE7MSJ2','Ameesha A Patel'],['U01BFRYBHK3','Amruta Kamat'],['U01B9LL4WEQ','Arpita S Vernekar'],['U01BSU6K5DE','Chaitanya K R'],['U017SG20U3C','Dhanushree S'],['U01AWAYUFN2','Nagesh R Shanbhag'],['U018G415YTS','Rakhi Shet'],['U017S8RDRUJ','Sriraksha'],['U011SJV14QM','Yashaswini']],
        "Lakshak":[['U01B0DEN52S','Akshay V Nayak'],['U011SJVJW7P','Kapil Shanbhag'],['U012ZGB3FQB','Megha Shet'],['U01BDQHUQUU','Mukund P Nayak'],['U012N7MHRFZ','Poorva Naik'],['U011TQQMCKF','Prathiksha PH'],['U011SJULLMB','Shashidhar Pai B'],['U01BAH47FDZ','Srishtik Bhandarkar'],['U01BNTZ0S0H','Sumanth Prabhu']],
        "Samanvay":[['U0152PC7C12','Anjani Prabhu'],['U0122DFTL13','Prahalya Mathias'],['U01AQLDB6TZ','Selen Preethi Pinto'],['U011SJVFZKP','Priyanka Kudva'],['U011SJTNCN9','Rakshitha Nayak'],['U011SJS092R','Rithika Pai T'],['U011SJS86CV','Sahana V'],['U0120N24M6E','Shravya S Mallya'],['U011SJSV7LM','Vasundhara Shenoy'],['U0124344JSF','Vinaya Pai']],
        "Sankalp":[['U01BFCCJQC9','Adarsh. S. Pal'],['U011SJUS1NH','Apoorva'],['U011SJU9X6Z','K Venkatesh Bhat'],['U011SJS9NBX','Chaithra Baliga'],['U011SJT60BX','M Jesta Kamath'],['U011SJV6L4D','Raghavendra Pai'],['U011SJUG7QD','Swasthik C Nayak'],['U011SJT1BFF','Swathi Prabhu'],['U011SJRNJKX','Tulsi'],['U011SJUHPCM','Vaibhav Nayak']],
        "Sarvathr":[['U012X8DF049','Amith Kini'],['U011ZAWAU5B','Anup U Vernekar'],['U011SJRTG93','Deeksha G Mesta'],['U011WFDMT0V','Disha Shanbhag'],['U011SJSMP37','Karthik'],['U011SJUPBJ9','Ramadas Kamat'],['U011SJUN0AH','D S Sharath Shenoy'],['U015XQH5B4M','Shravan R Tandel'],['U011SJTSN5B','Siddharth Anvekar']],
        "Sudhaksha":[['U01ASH9D4GP','Akshatha N K'],['U01B4941H0V','Anand Ajith'],['U011U0GRJ0N','Khushi Raikar'],['U01AW1H5C30','Khyati Rajesh Amballi'],['U011SJV9HNH','Prateeksha Vasant Pai'],['U01B0HQQSCE','Pratiksha Krishna Jadhav'],['U012ARUK92Q','Sakshi Desai'],['U01B5D72AHK','Sindu Sarang'],['U01BB1H8LRJ','Vishwanatha']],
        "Tejas":[['U012MTKBJU8','Abhishek Bhaktha'],['U01223FQDUM','Ananya R Prabhu'],['U01AW13K8MU','Ashwin A Shanbhag'],['U016X3S3J95','Edric Oscar Dsilva'],['U012DB28FFB','Joel Nazareth'],['U011TLPN4HK','K Avinash Nayak'],['U01BFR9TL4R','Mayur M Shet'],['U011SJUK3PF','Pavan Kumar M S'],['U011SJS61JR','Shreyas Kamath'],['UUH8LDQKS','Srinidhi Bhat'],['U012GDRM6FK','Vittal']],
        "Udayagiri":[['U01BSJF3UP2','AJAY G NAYAK'],['U01B2QUUTDG','Gautham Bhat'],['U011SJT4H53','Nima'],['U011SJV5FJ9','Nithesh Pai'],['U011ZAW5ULV','Parthiv Kamath CS'],['U011SJTLYRK','Prajaktha P Prabhu'],['U011SJVDE2H','Praneeth'],['U011SJU0ABF','Pranita Shenoy'],['U011X31BM46','Prathviraj Prabhu'],['U01AW0FS08N','Shreeram Bhat']],
        "Urja":[['U011P4E8ER5','Aaditya D Pai'],['U011P3CALLX','Ajay H Hegde'],['U011ZAW92S1','M Karthik Krishna'],['UUJCZBCJK','Deeksha Sanu'],['U01BFDKHJQH','B Hrishikesh Kamath'],['U014JC5LRJ5','Krishna'],['U011WML3LHK','Mayur Shet'],['U0131A0PY8Y','Prateek Nayak'],['U0120N270H0','Rishabh Naik'],['U01AWA1TT4N','Subramanya L Mahale'],['U011SJVHDMK','Vaishnavi Hegde']],
        "Vajra":[['U01AWF13VJA','Aishwarya Kudatarkar'],['U01BSRECG9W','ANKITHA MESTHA'],['U011SJT8PNH','Navya Shanbhag'],['U01AVV40W8N','Roja Ishwar Tandel'],['U011SJTH24V','Sujith Kharvi'],['U011SJVLE77','Vaishnavi Shet'],['U011SJVN7A9','N Venkatesh Kamath'],['U011SJUTD9B','Vidya Kharvi']],
        #"Mentors":[['U011SJSP3NZ','Chaitra Kamath G'],['U011SJT2TK7','Gaurav Prabhu K'],['U012HRBP01W','Gopika Kini'],['U012ECB9KS9','Gurudath Bantwalkar'],['U014CHDH3MJ','Karan Kini K'],['U013RL46BF1','Movin Sequeira'],['U01205N97EY','Nabha Kamath'],['U019R5Y8CGL','Navami Kini'],['U011D8NTJUF','Niriksha Shenoy'],['U01BLEFGH4P','Pragathi P Nayak'],['U019480VA2K','Premitha'],['U01AN69A9AT','Raamnath Mallya'],['U01C52CAB6X','Rishikesh Pai'],['UU537F459','Royal'],['U012ECG0Y77','Sahana Kini'],['U011D8A8E79','Samyuktha Prabhu'],['U0126K0RD2M','Sneha Shenoy'],['U011D8A8NCF','Sukanya Pai'],['U01BJTQKHQQ','Sulochana'],['U0149CRNH52','Sushma Kini'],['U01205NLM4L','Venkatesh Prabhu']],
    }
a=int(0)
teamnameslist=[]
datafetchedfromcsvfile=[]
#fetch data from csv file
with open('analytics.csv', 'r',encoding='utf8') as csvfile:
    csvlist=reader(csvfile)
    for row in csvlist:
        #print(row)
        datafetchedfromcsvfile.append(row)
print("Data fetched from analytics.csv file")
for i in teammemlist.keys():
    teamnameslist.append(i)

teamnocounter=int(0)
n=int(0)
totalteamstatisticslist=[]#to store all teamscore.
for i in teammemlist.values():
    totalteamstatisticslist.append([])
    teammesspostedinchannel=int(0)
    teammessposted=int(0)
    teamreactions=int(0)
    inditeamtotalscoreslist=[]#to store total points or messages number
    inditeamindiscoreslist=[]#to store points or score of each and everymember of team
    
    for j in i:
        
       for a in datafetchedfromcsvfile:
           if j[0]==str(a[2]):
                indipersonscoreslist=[]#to store individual scores
                indipersonscoreslist.append(j[1])#name from csv file
                indipersonscoreslist.append(a[2])#User ID from CSV file
                indipersonscoreslist.append(a[3])#Email Id from csv file
                indipersonscoreslist.append(a[4])#Days active from csv file
                indipersonscoreslist.append(a[5])#Message posted from csv file
                indipersonscoreslist.append(a[6])#Message posted in channel from csv file
                indipersonscoreslist.append(a[7])#Reactions added from csv file
                indipersonscoreslist.append(a[8])#last active date
                inditeamindiscoreslist.append(indipersonscoreslist)
                teammessposted=teammessposted+int(a[5])
                teammesspostedinchannel=teammesspostedinchannel+int(a[6])
                teamreactions=teamreactions+int(a[7])
                #print(indipersonscoreslist)
                break

    inditeamtotalscoreslist.append(teamnameslist[teamnocounter])
    inditeamtotalscoreslist.append(teammessposted)
    inditeamtotalscoreslist.append(teammesspostedinchannel)
    inditeamtotalscoreslist.append(teamreactions)
    #print("inditeamtotalscores added")
    #print(inditeamtotalscoreslist)
    #print(teamnameslist[teamnocounter])
    totalteamstatisticslist[teamnocounter].append(inditeamtotalscoreslist)
    totalteamstatisticslist[teamnocounter].append(inditeamindiscoreslist)
    #print("Added for" +str(teamnameslist[teamnocounter]))
    teamnocounter=teamnocounter+1
'''
for i in totalteamstatisticslist:
    print(i[0])
    #for j in i:
        #print(j)
    print("********************************************************************")
    for j in i[1]:
        print(j)
        print(n)
        n=n+1
    print("========================================================================")
print("Started with pdf creation")
'''






#note only have "name","what I do", "User Id"."Email adress","Days Active","Message posted", "Message posted in channels", "Reactions given","Last active" as column in .csv file or else the order will change and result in wrong answers.
