__author__ = 'nestmilk'
__date__ = '2019/2/21 11:13'


from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm, Inches, Pt

doc = DocxTemplate("D:\Merge.docx")
doc.render({"name":"龚振华", "gong":InlineImage(doc,"D:\gong.jpg", width=Mm(30), height=Mm(30))})

doc.save("D:\龚振华.docx")