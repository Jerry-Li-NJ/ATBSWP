# chapter13_CIAWD.py --Generate a Word document with custom invitation.
# Only run on windows.
# CIAWD_format.docx and blank.docx are needed.

import sys, os, docx

def add_At(docObj, content):
        thePara = docObj.add_paragraph('at')
        thePara.runs[0].underline = True
        thePara.add_run(content)
        thePara.style = 'Para_1'
                
# Get guests file and will-output file name via command line
if len(sys.argv) != 3:
	print('\n\tPlease make sure there are and only guests file and output Doc name given!')
	print('\t\tUsage: ./chapter13_CIAWD.py guests.txt Invitations.docx\n')
elif not os.path.exists(sys.argv[1]):
	print('\n\tPlease make sure %s exists!\n' %(sys.argv[1]))
else:
	guestTextFileName = sys.argv[1]
	outputDocName = sys.argv[2]

# Save guests' name in a list.
	with open(guestTextFileName) as f:
		data = f.read()

	guestList = data.split('\n')
	
# Create Docx file obj
	template = docx.Document('CIAWD_format.docx')   # This should be the docx file with custom styles
	document = docx.Document('blank.docx')          # This docx file should be created inside Word Application
	

# Add the text and page break
# Set the stype

        # --- Very Important---
        # The key is that, the original document is created inside Word Application, not right click.
        # --- Very Important---
        
	for i in range(len(guestList)):
                document.add_paragraph('It would be a pleasure to have the company of', style='Para_1')
                document.add_paragraph(guestList[i], style='Para_2')
                
                add_At(document, ' 11010 memory Lane on the evening of')
                
                document.add_paragraph('April 1st', style='Para_4')
                
                add_At(document, " 7 o'clock")
                
                if i != len(guestList) - 1:             # Skip the last page break
                        document.add_page_break()
                print('\n\tInvitation %i generated\n' %(i+1))


# Generate the Docx File
	document.save(outputDocName)


