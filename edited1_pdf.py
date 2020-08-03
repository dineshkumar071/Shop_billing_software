import qrcode,webbrowser
from reportlab.pdfgen import canvas
def getTotal(list):
  total=0
  for data in list:
    total=total+data[5]
  return total

def getTotalTax(list):
  totalTax=0
  for data in list:
    totalTax=totalTax+data[6]
  return totalTax

def getTotalDis(list):
  totalDis=0
  for data in list:
    totalDis=totalDis+data[4]
  return totalDis

def rightalingn(pdf,string,left,right,ycoordinate):
  length=len(string)
  totalLength=(right-left)/7
  print(totalLength)
  spaces=int(totalLength-length)
  print(spaces)
  pdf.drawString(right,ycoordinate," "*spaces)
  left=left+(7*spaces)
  pdf.drawString(left,ycoordinate,string)

def header(header,pdf):
  pdf.setTitle(header.date+"Invoice")
  # logo="logo.jpeg"
  # pdf.drawInlineImage(logo,190,253)

  pdf.line(30,815,350,815)
  pdf.setFont("Courier-Bold",20)
  pdf.drawString(30,800,"THANGAM JEWELLERS")
  pdf.setFont("Courier-Bold",11)
  pdf.drawString(30,785,"27,Madhar khand tafethar lane,South Avani Moola Street")
  pdf.drawString(30,770,"Madurai-625001")
  pdf.drawString(30,755,"Contact Number:9976639550,9486230769")

  pdf.line(30,753,350,753)

  pdf.drawString(30,735,"Invoice Number: "+ str(int(header.InvoiceNumber)))
  pdf.drawString(30,720,"Customer Name: "+ str(header.CustomerName))
  pdf.drawString(30,705,"Contact Number: "+ str(header.CustomerContact))
  pdf.drawString(30,690,"Date: "+ str(header.date))
  
  qr = qrcode.QRCode(
    version=1,
    box_size=2,
    border=2
  )

  data = 'InvoiceNumber:'+str(int(header.InvoiceNumber))+'\nTime:'+(header.date+"--"+header.time)+"\nGoogle Map: https://maps.app.goo.gl/phW19nxcAH88eSnD7\nTerms & Conditions:\n1:Sold items will not be returned or changed.\nTHANK YOU"
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill='black', back_color='white')

  pdf.drawInlineImage(img,400,685)
  

def middle(pdf):
  pdf.line(30,677,550,677)
  
  pdf.drawString(30,668,"Sr.No.")
  pdf.drawString(75,668,"Product Name")
  pdf.drawString(168,668,"Quan")
  pdf.drawString(212,668,"Weight")
  pdf.drawString(260,668,"Rate")
  pdf.drawString(320,668,"Discount")
  pdf.drawString(400,668,"Total")
  pdf.drawString(490,668,"Tax")
  
  pdf.line(30,662,550,662)
  pdf.line(73,677,73,150)
  pdf.line(164,677,164,150)
  pdf.line(210,677,210,150)
  pdf.line(258,677,258,150)
  pdf.line(318,677,318,150)
  pdf.line(398,677,398,150)
  pdf.line(488,677,488,150)
  pdf.line(30,150,550,150)

def additem(product,pdf,ycoordinate):
  while(len(product.name)>18):
    pdf.drawString(75,ycoordinate,product.name[:18]+"-")
    product.name=product.name[18:]
    ycoordinate=ycoordinate-15
  
  pdf.drawString(75,ycoordinate,product.name)
  pdf.drawString(171,ycoordinate,product.quantity)
  pdf.drawString(215,ycoordinate,str(product.weight))
  rightalingn(pdf,"%.2f" %product.rate,260,316,ycoordinate)
  print(product.rate)
  rightalingn(pdf,"%.2f" %product.discount,320,398,ycoordinate)
  rightalingn(pdf,"%.2f" %product.total,400,488,ycoordinate)
  rightalingn(pdf,"%.2f" %product.tax,490,552,ycoordinate)
  return (ycoordinate-15)

def footer(pdf,list):
  pdf.drawString(30,135,"Total Discount:")
  rightalingn(pdf,"-"+"%.2f" %getTotalDis(list)+" INR",393,488,135)
  pdf.drawString(30,120,"Gross Total(Discount Included):")
  rightalingn(pdf,"%.2f" %getTotal(list)+" INR",400,488,120)
  pdf.drawString(30,105,"Tax:")
  rightalingn(pdf,"+"+"%.2f" %getTotalTax(list)+" INR",393,488,105)
  pdf.line(30,100,550,100)
  pdf.drawString(30,90,"Grand Total: ")
  rightalingn(pdf,"%.2f" %(getTotal(list)+getTotalTax(list))+" INR",400,488,90)
  pdf.drawString(400,50,"Authorized Signatory")
  pdf.setFont("Courier-Bold",7)
  pdf.drawString(15,15,"Scan QR code for Applied Terms & Conditions.")

def About():
  pdf=canvas.Canvas("G:\\bill\\about.pdf")
  pdf.setFont("Courier-Bold",20)
  pdf.drawString(40,700,"S.Dinesh Kumar")
  pdf.setFont("Courier-Bold",15)
  pdf.drawString(40,650,"Student, ")
  pdf.drawString(40,630,"Computer Science & Engineering,")
  pdf.drawString(40,610,"Sri Ramakrishna Institute of Technology,")
  pdf.drawString(40,590,"Coimbatore, 641010.")
  pdf.drawString(40,550,"Contact: 9525658478")
  pdf.save()
  webbrowser.open("G:\\bill\\receipt.pdf")
