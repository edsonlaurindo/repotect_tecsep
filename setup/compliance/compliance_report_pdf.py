from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image, Paragraph, Table
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import CMYKColor
import sys,os,locale
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QLineEdit, QWidget 

# Classe Para Geração dos Reports
class GerarReport:
    def gerar_pdf(self,filename,report_cabecalho,fluid_information,drilling_information,average,solids_control,audi):

        def caminho_absoluto_desktop():
            idioma_sistema = locale.getdefaultlocale()[0].lower()

            if "pt" in idioma_sistema:
                return os.path.join(os.path.expanduser("~"), "Desktop")
            else:
                return os.path.join(os.path.expanduser("~"), "Desktop")

        caminho_desktop = caminho_absoluto_desktop()

        c = canvas.Canvas(caminho_desktop+"/"+filename, pagesize=A4,bottomup=False)  # alternatively use bottomup=False
        width, height = A4

        value_info = report_cabecalho
        value_fluid_information = fluid_information
        
        value_drilling_information = drilling_information
        value_average = average

        value_solids_control = solids_control

        value_audit = audi

        
        
        data = [
                        ["Shift (Day/NIgth):", value_info[5], "Approved By:",value_info[10]],
                        ["Job Type:",value_info[4], "Prepared By:",value_info[9]],
                        ["Filed/Location:", value_info[3], "Well NUmber:",value_info[8]],
                        ["Rig Name:", value_info[2], "Customer Name:",value_info[7]],
                        ["Job Ref. Number:",value_info[1], "Report Date:",value_info[6]],
        ]

        data_drilling_information =   [
                    [value_info[11], value_info[12], value_info[13],value_info[14],value_info[15]],
                    ["Hole Size", "Total Depth (ft)", "Feets Drilling","Average ROP","Time at Depth"]
                    
                ]

        data_fluid_information =  [
                   
                    [value_fluid_information[31], value_fluid_information[5], value_fluid_information[6],value_fluid_information[7],value_fluid_information[8],value_fluid_information[9]],
                    ["Mud type / Base Oil type", "Rig total volume", "Density","Viscosity (PV)","Viscosity (YP)"," Hole Volume"]
                    
                ]


        data_drilling_fluid_properties =  value_drilling_information + [
                    
                ]

        data_average_occ =   [
                    ["","S/N: " + value_average[14]],
                    ["","Model: " + value_average[13]],
                    ["Number of Shakers online",value_average[13]],
                    ["Number of Cutting Dryers",value_average[12]],
                    ["Mass of Dry cuttings (Md)",value_average[11]],
                    ["Mass of NAF base Fluids (MBF)",value_average[10]],
                    ["Mass Balance Requirement (MBR)",value_average[9]],
                    ["Mass of Wet Cuttings (Mw)",value_average[8]],
                    ["Average wet cuttings gms/Kg",value_average[7]],
                    ["Average Dry cuttings gms/kg",value_average[6]],
                    ["Time of test",value_average[5]],
                    ["Date of test",value_average[4]],
                    ["Sample Number (frequency)",value_average[3]],
                    ["Sample Location",value_average[2]],
                    ["Depth at Location",value_average[1]]
                    
                ]
        data_solid_control_equipament = [
                    [" ",value_solids_control[7]],
                    ["Dryer Screen size (mm)",value_solids_control[6]],
                    [" ",value_solids_control[5]],
                    ["Hours run",value_solids_control[4]],
                    ["Front",value_solids_control[3]],
                    ["Middle",value_solids_control[2]],
                    ["Back",value_solids_control[1]],
                    ["Scalper",value_solids_control[0]],
                    ["Shaker (Screen-API mesh)"]
        ]

        data_solid_control_sample = [
                    ["Well Section Average % OOC ",""],
                    [" Average % OOC",value_solids_control[11]],
                    ["Daily % OOC ( % BFi) ",value_solids_control[11]],
                    ["Weight in (ppg)",value_solids_control[10]],
                    ["Flow (gpm)",value_solids_control[9]],
                    ["Hours run",value_solids_control[4]],
                    ["Bowl Speed (rpm )",value_solids_control[8]],
                    ["Location of Sample"]
        ]

        data_auditQuestionary = value_audit + [
            ["Equipment Breakdown","Yes/No","Time","Contractor"]
        ]

        data_ongoing_rig_activity = [
                    [value_info[16]]
                    
                ]
        
        data_monitoring = [
                    [value_info[17]]
                    
                ]



        data_compliance_enginer = [
            ["teste","teste","teste"],
            ["teste","teste","teste"],
            ["Drilling Fluids Complience Engineer","Shift",""]
        ]


        #TBaela Well Infomration
        table_drilling_information = Table(data_drilling_information, colWidths=[40*mm,35*mm,35*mm,50*mm,40*mm])

        #Tabela REport Information
        table = Table(data, colWidths= [40*mm,72*mm,38*mm,49.7*mm])
        #table.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        #                ("ALIGN", (0,0), (-1,-1), "LEFT"),
        #                ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black)])

        table_fluid_information = Table(data_fluid_information,colWidths=[40*mm,33*mm,35*mm,23*mm,29*mm,40*mm])

        table_drilling_fluid_properties = Table(data_drilling_fluid_properties,colWidths=[40*mm,160*mm])

        table_average_occ = Table(data_average_occ,colWidths=[40*mm,160*mm])

        table_solid_control_equipament = Table(data_solid_control_equipament,colWidths=[40*mm,160*mm])

        table_solid_control_sample = Table(data_solid_control_sample,colWidths=[40*mm,160*mm])

        table_ongoing_activity = Table(data_ongoing_rig_activity,colWidths=200*mm)

        table_monitoring_comments = Table(data_monitoring,colWidths=200*mm)

        table_auditQuestionary = Table(data_auditQuestionary,colWidths=[70*mm,30*mm,50*mm,50*mm,])

        table_compliance_enginer = Table(data_compliance_enginer,colWidths=[70*mm,30*mm,100*mm])

        padding = 3
        table.setStyle([
                    
                    #('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                    ('FONTSIZE', (0, 0), (-1, -1), 7),
                    ('TOPPADDING', (0, 0), (-1, -1), -4),  # Espaçamento superior das células
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 3),  # Espaçamento inferior das células
                    ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                    ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                    ('VALIGN',(0,0),(0,-1),'MIDDLE'),
                    ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                    ('LINEABOVE', (0,1), (-1,-1), 0.3, colors.black),
                    ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                    ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,4,alpha=85)),
                    ("BACKGROUND", (3,5),(1,-6),colors.PCMYKColor(0,1,1,4,alpha=85)),
                    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black)
                ])

        table_drilling_information.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), -4),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEABOVE', (0,1), (-1,-1), 0.3, colors.black),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ('BACKGROUND',(0,1),(4,1),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ('BACKGROUND',(0,0),(0,0),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])

        table_fluid_information.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), -3),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "CENTER"),
                        ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])


        table_drilling_fluid_properties.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), -5),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEABOVE', (0,1), (-1,-1), 0.3, colors.black),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])

        table_average_occ.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                        ("LINEABOVE", (0,14), (1,14), 0.9, colors.black),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), -5),  # Espaçamento superior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                        ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ("BACKGROUND", (0,14),(1,14),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])
        
        table_solid_control_equipament.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                        ("LINEABOVE", (0,14), (1,14), 0.9, colors.black),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), -5),  # Espaçamento superior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("BACKGROUND", (0,1),(0,-1),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ("BACKGROUND", (0,8),(1,8),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])
        
        table_solid_control_sample.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                        ("LINEABOVE", (0,14), (1,14), 0.9, colors.black),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), -5),  # Espaçamento superior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("BACKGROUND", (0,0),(0,-1),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])

        table_ongoing_activity.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ('LINEABOVE', (0,0), (-1,-1), 0.9, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), 27),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])
        
        table_monitoring_comments.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ('LINEABOVE', (0,0), (-1,-1), 0.9, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), 27),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])
        

        table_auditQuestionary.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                        ("LINEABOVE", (0,14), (1,14), 0.9, colors.black),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), -4),  # Espaçamento superior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("BACKGROUND", (0,1),(3,1),colors.PCMYKColor(0,1,1,4,alpha=85)),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])


        table_compliance_enginer.setStyle([("VALIGN", (0,0), (-1,-1), "MIDDLE"),
                        ("LINEABOVE", (0,0), (-1,0), 0.9, colors.black),
                        ('LINEABOVE', (0,1), (-1,-1), 0.25, colors.black),
                        ('FONTSIZE', (0, 0), (-1, -1), 7),
                        ('TOPPADDING', (0, 0), (-1, -1), -4),  # Espaçamento superior das células
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),  # Espaçamento inferior das células
                        ('LEFTPADDING', (0, 0), (-1, -1), padding),  # Espaçamento esquerdo das células
                        ('RIGHTPADDING', (0, 0), (-1, -1), padding),
                        ('LINEBELOW', (0,-1), (-1,-1), 0.9, colors.black),
                        ("ALIGN", (0,0), (-1,-1), "LEFT"),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),])

        

        table.wrapOn(c, width, height)
        table.drawOn(c, 5*mm, 26*mm)

        

        table_drilling_information.wrapOn(c, width,height)
        table_drilling_information.drawOn(c,5*mm,49.5*mm)

        table_fluid_information.wrapOn(c,width,height)
        table_fluid_information.drawOn(c,5*mm,61.9*mm)

        altura_wbco_primary = table_fluid_information._height
        print(altura_wbco_primary)

        table_drilling_fluid_properties.wrapOn(c,width,height)
        table_drilling_fluid_properties.drawOn(c,5*mm,( (53.8*mm) + (altura_wbco_primary) + 35))

        altura_wbco_back_up = table_drilling_fluid_properties._height
        print(altura_wbco_back_up)

        table_average_occ.wrapOn(c,width,height)
        table_average_occ.drawOn(c,5*mm,((51.5*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 20)

        
        altura_on_going_activity = table_average_occ._height

        table_solid_control_equipament.wrapOn(c,width,height)
        table_solid_control_equipament.drawOn(c,5*mm,((51.5*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 34.5 + altura_on_going_activity)

        altura_solid_equipament = table_solid_control_equipament._height

        table_solid_control_sample.wrapOn(c,width,height)
        table_solid_control_sample.drawOn(c,5*mm,((51.5*mm) + (altura_wbco_primary) + 37) + altura_wbco_back_up + 34.5 + altura_on_going_activity + altura_solid_equipament)

        valor_heigth_total = ((51.5*mm) + (altura_wbco_primary) + 37) + altura_wbco_back_up + 34.5 + altura_on_going_activity + altura_solid_equipament

        altura_solid_sample = table_solid_control_sample._height

        table_ongoing_activity.wrapOn(c,width,height)
        table_ongoing_activity.drawOn(c,5*mm,valor_heigth_total + altura_solid_sample + 13)

        total_table_with_ongoing_value = valor_heigth_total + altura_solid_sample + 13

        table_ongoing_heigth = table_ongoing_activity._height

        table_monitoring_comments.wrapOn(c,width,height)

        table_monitoring_comments.drawOn(c,5*mm,table_ongoing_heigth + total_table_with_ongoing_value + 13 )

        table_monitoring_heigth = table_monitoring_comments._height

        total_table_with_monitoring = table_ongoing_heigth + total_table_with_ongoing_value + 13 + table_monitoring_heigth



        table_auditQuestionary.wrapOn(c,width,height)
        table_auditQuestionary.drawOn(c,5*mm,total_table_with_monitoring + 13)
        
        table_audi_heigth = table_auditQuestionary._height
        
        total_height_with_audit = table_ongoing_heigth + total_table_with_ongoing_value + 13 + table_monitoring_heigth + table_audi_heigth

        table_compliance_enginer.wrapOn(c,width,height)
        table_compliance_enginer.drawOn(c,5*mm,total_height_with_audit + 13)

        styles = getSampleStyleSheet()   


        width = 2.2 * inch  # largura da imagem
        height = 0.8 * inch  # altura da imagem




        #Borda Para a Pagina
        c.setFillColorRGB(1,0,0)
        c.rect(12,12,571,800)

        styles = {
            'Normal': ParagraphStyle(
                'normal',
                fontSize=10,
                textColor='black',
                spaceAfter=12,
            ),
            'Estilo_texto_titulo': ParagraphStyle(
                'estilo_texto_titulo',
                fontSize=11,
                textColor='#0018F9',
                spaceAfter=5,
                underline = True
            ),
            'Estilo_texto_url': ParagraphStyle(
                'estilo_texto_url',
                fontSize=12,
                textColor='#0018F9',
                spaceAfter=12,
            ),

            'Estilo_titulo_tabela': ParagraphStyle(
                'estilo_titulo_tabela',
                fontSize=7.5,
                textColor='#0018F9',
                spaceAfter=5,
                #backColor = colors.PCMYKColor(0,1,1,4,alpha=85),
                alignment=0,
            ),
        }

        img = ImageReader("img/img.png",styles["Estilo_texto_titulo"])
        c.drawImage(img, 5*mm, 5*mm, width, height, mask='auto')


        width = 7.5 * inch  # largura da imagem
        height = 2 * inch  # altura da imagem

        #img_certificate = ImageReader("img/arrendoda.png",styles["Estilo_texto_titulo"])
        #c.drawImage(img_certificate,5*mm,230*mm,width,height,mask='auto')

        

        
        ptext = "Daily Report #"+str(value_info[0])+" Drilling Fluids Compliance "
        pdrilling_information = "Drilling Information"
        p_fluid_information = " Fluid Information"
        p_drilling_fluid_properties = "Drilling Fluid Proprties"
        p_average_ooc_cuttings = "Average OOC Cuttings Discharged Overboard from Drying Equipment"
        p_ongoing_activity = "Ongoing Rig Activity:"
        p_monitoring_comments = "Monitoring Comments:"
        p_text_lema = '"Proudly Tecsep, Proudly African"'
        p_audit_questionary = "Audit Questionnaire"
        



        p = Paragraph(ptext, style=styles["Estilo_texto_titulo"])
        pdrilling = Paragraph(pdrilling_information, style= styles["Estilo_titulo_tabela"])
        p_fluid = Paragraph(p_fluid_information, style= styles["Estilo_titulo_tabela"])
        p_fluid_properties = Paragraph(p_drilling_fluid_properties, style= styles["Estilo_titulo_tabela"])
        p_averange_ooc = Paragraph(p_average_ooc_cuttings,style=styles["Estilo_titulo_tabela"])
        p_solids_control_equipament = Paragraph("Solids Control equipment information",style=styles["Estilo_titulo_tabela"])
        p_activity = Paragraph(p_ongoing_activity, style=styles["Estilo_titulo_tabela"])
        p_comments = Paragraph(p_monitoring_comments, style=styles["Estilo_titulo_tabela"])
        p_audit = Paragraph(p_audit_questionary,style=styles["Estilo_titulo_tabela"])

        p_lema = Paragraph(p_text_lema,style = styles["Normal"])


        #color = CMYKColor(0.035, 0.043, 0.047, 0.035)

        #c.setFillColor(color)

        #c.rect(5*mm,45.7*mm,200*mm,10,fill=1, stroke=0)

        p.wrapOn(c, 80*mm, 70*mm)  # size of 'textbox' for linebreaks etc.
        p.drawOn(c, 65*mm, 18*mm)    # position of text / where to draw

        pdrilling.wrapOn(c,200*mm,10*mm)
        pdrilling.drawOn(c,5*mm,46.5*mm)

        p_fluid.wrapOn(c,70*mm,50*mm)
        p_fluid.drawOn(c,5*mm,59*mm)

        p_fluid_properties.wrapOn(c,70*mm,50*mm)
        p_fluid_properties.drawOn(c,5*mm,(54.5*mm) + (altura_wbco_primary) + 25)

        p_averange_ooc.wrapOn(c,140*mm,50*mm)
        p_averange_ooc.drawOn(c,5*mm,((51.3*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 12 )

        p_solids_control_equipament.wrapOn(c,70*mm,50*mm)
        p_solids_control_equipament.drawOn(c,5*mm,((40.5*mm) + (altura_wbco_primary) + 35) + altura_wbco_back_up + 33 + altura_on_going_activity + 25)

        p_activity.wrapOn(c,40*mm,50*mm)
        p_activity.drawOn(c,5*mm,altura_solid_equipament + valor_heigth_total - 4)

        p_comments.wrapOn(c,70*mm,60*mm)
        p_comments.drawOn(c,5*mm,altura_on_going_activity + total_table_with_ongoing_value - 85)

        p_audit.wrapOn(c,40*mm,50*mm)
        p_audit.drawOn(c,5*mm,total_table_with_monitoring + 6 )

        p_lema.wrapOn(c,70*mm,60*mm)
        p_lema.drawOn(c,7*mm,283*mm)


        c.save()
