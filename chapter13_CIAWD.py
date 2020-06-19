# chapter13_CIAWD.py --Generate a Word document with custom invitation.
# Only run on windows.
# CIAWD_format.docx and blank.docx are needed.


import sys, os, docx

# Get guests file and will output file name via command line
if len(sys.argv) != 3:
	print('\n\tPlease make sure there are and only guests file and output Doc name given!')
	print('\t\tUsage: ./chapter13_CIAWD.py guests.txt Invitations.docx\n')
elif not os.path.exists(sys.argv[1]):
	print('\n\tPlease make sure %s exists!\n' %(sys.argv[1]))
else:
	#print('\nTest\n')
	guestTextFileName = sys.argv[1]
	outputDocName = sys.argv[2]

# Save guests' name in a list.
	with open(guestTextFileName) as f:
		data = f.read()
		#print(data)
	guestList = data.split('\n')
	print(guestList)
	
# Create Docx file obj
	template = docx.Document('CIAWD_format.docx')
	document = docx.Document('blank.docx')
	

# Add the text and page break
# Set the stype

        # The key is that, the original document is created inside Word Application, not right click.
	for i in range(len(guestList)):
                document.add_paragraph('It would be a pleasure to have the company of', style='Para_1')
                document.add_paragraph(guestList[i], style='Para_2')
        
                underLinePara = document.add_paragraph('at')
                underLinePara.runs[0].underline = True
                underLinePara.add_run(' 11010 memory Lane on the evening of')
                underLinePara.style = 'Para_1'
        
                document.add_paragraph('April 1st', style='Para_4')
                
                underLinePara2 = document.add_paragraph('at')
                underLinePara2.runs[0].underline = True
                underLinePara2.add_run(" 7 o'clock")
                underLinePara2.style = 'Para_1'
                
                if i != len(guestList) - 1:
                        document.add_page_break()



# Generate the Docx File
	document.save(outputDocName)
    
