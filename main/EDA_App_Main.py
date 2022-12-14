
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from email.mime import image
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
# library for front-end
import tkinter as tk
from tkinter import Image, Label, Tk, Canvas, Entry, Text, Button, PhotoImage

#library for backend
import webbrowser 
import time
import subprocess
import getpass

# Get the file path of this python file
OUTPUT_PATH = Path(__file__).parent

#Append the ./assets into python file path
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# change if chrome is different for users
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'       

# Open Files
username = getpass.getuser()
GlobalEDARef = r"/Emerson/GLOBAL EDA - General/References/"
FLMCECADxcl = r"C:/Users/" + username + "/Emerson/GLOBAL EDA - General/FLMC ECAD Components Monitoring.xlsx"
AltLib = r"C:/Users/" + username + GlobalEDARef + "Altium Concord Pro Library Management References.xlsx"
IPCFp = r"C:/Users/" + username + GlobalEDARef + "IPC Footprint Data and References.xlsx"
Pnumb = r"C:/Users/" + username + GlobalEDARef + "Part Numbering Process Flow and Guidelines_rev9.xlsx"
CompRev = r"C:/Users/" + username + "/Emerson/ANME Component Team - EDA/09 Monitorings/Component Review.xlsx"

PwrApps = "https://apps.powerapps.com/play/e/default-eb06985d-06ca-4a17-81da-629ab99f6505/a/469e64ad-7edc-4674-8a51-c45ed4c4001e?tenantId=eb06985d-06ca-4a17-81da-629ab99f6505&source=portal&screenColor=rgba(255%2C%20255%2C%20255%2C%201)"

ECADBi = "https://app.powerbi.com/groups/688015c0-edf8-40a8-ae64-0338ece6d218/reports/b0797279-d148-4d14-93f5-97b75f09cc2e/ReportSection3f8ac91b104b34dd6747"

ECADRiskBi = "https://app.powerbi.com/groups/688015c0-edf8-40a8-ae64-0338ece6d218/reports/86186d18-6d9d-450d-83ff-28dda9991c7d/ReportSection77ddb1e26e11e8b0c705"



def OpenLinks(linkstr):
    webbrowser.open(linkstr)

def OpenFiles(filestr):
    subprocess.run(('cmd', '/C', 'start', '', filestr))

# Function for returning path of Assets folder
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    

class EDAApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.title("EDA App")
        self.geometry("862x519")
        self.resizable("False","False")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, SiliconExpert, DPXE, EDAFiles):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")
        # self.iconbitmap("Icon.ico")
        self.iconbitmap(relative_to_assets("Icon.ico"))

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

# include self in image to avoid not showing the images

class HomePage (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            587.0,
            519.0,
            fill="#00A4D2",
            outline="")

        canvas.create_text(
            17.0,
            179.0,
            anchor="nw",
            text="Choose functionalities from buttons at the right",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )
        
        self.DPXE_Home_button_image = PhotoImage(
            file=relative_to_assets("DPXE_button.png"))
        DPXE_Home_button = Button(
            self,
            image=self.DPXE_Home_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("DPXE"),
            relief="flat"
        )
        DPXE_Home_button.place(
            x=642.0,
            y=294.0,
            width=168.0,
            height=42.46942138671875
        )
        
        canvas.create_text(
            606.0,
            85.0,
            anchor="nw",
            text="Choose from below",
            fill="#000000",
            font=("Inter Bold", 25 * -1,'bold')
        )
        self.SE_Home_button_image = PhotoImage(
            file=relative_to_assets("SE_button.png"))
        SE_Home_button = Button(
            self,
            image=self.SE_Home_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("SiliconExpert"),
            relief="flat"
        )
        SE_Home_button.place(
            x=642.0,
            y=235.0,
            width=168.0,
            height=44.0
        )
  
        self.Files_Home_button_image = PhotoImage(
            file=relative_to_assets("Files_button.png"))
        Files_Home_button = Button(
            self,
            image=self.Files_Home_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("EDAFiles"),
            relief="flat"
        )
        Files_Home_button.place(
            x=642.0,
            y=176.0,
            width=168.0,
            height=44.0
        )

        canvas.create_text(
            17.0,
            56.0,
            anchor="nw",
            text="Welcome to the Electronic Design ",
            fill="#FFFFFF",
            font=("Inter", 30 * -1,'bold')
        )

        canvas.create_rectangle(
            0.0,
            428.0,
            862.0,
            519.0,
            fill="#D6DFDF",
            outline="")

        self.Emerson_footer = PhotoImage(
            file=relative_to_assets("Emerson.png"))
        
        self.Emerson_footer_canvas = canvas.create_image(
            431.0,
            474.0,
            image=self.Emerson_footer
        )
        
        canvas.create_text(
            17.0,
            103.0,
            anchor="nw",
            text="Automation App!",
            fill="#FFFFFF",
            font=("Inter", 30 * -1,'bold')
        )

        canvas.create_text(
            560.0,
            501.0,
            anchor="nw",
            text="For Technical support, contact Ceejay.Lapuz@emerson.com\n",
            fill="#000000",
            font=("Inter Regular", 10 * -1)
        )
class SiliconExpert (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller        

        def SELinks():
            SEurl = SE_textarea.get('1.0','end-1c') # get input from drawing numbers
            SEurl1 = list(SEurl.split()) #make the input as list
            SE_link = 'https://my.siliconexpert.com/search?text='
            URLs = [SE_link + x for x in SEurl1] # for loop to append SE_link string in elements of url1 list
            for links in URLs: # create a for loop to open links
                webbrowser.get(chrome_path).open_new_tab(links)
                time.sleep(1)

        def clear_textSE():
            SE_textarea.delete('1.0','end-1c')

        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            587.0,
            519.0,
            fill="#00A4D2",
            outline="")

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("DPXE_Page.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("DPXE"),
            relief="flat"
        )
        button_3.place(
            x=135.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("Home_Page.png"))
        button_4 = Button(
            self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("HomePage"),
            relief="flat"
        )
        button_4.place(
            x=17.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        self.Files_tab = PhotoImage(
            file=relative_to_assets("Files_Page.png"))
        button_4 = Button(
            self,
            image=self.Files_tab,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("EDAFiles"),
            relief="flat"
        )
        button_4.place(
            x=253.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        canvas.create_text(
            17.0,
            305.0,
            anchor="nw",
            text="Important: For this to work, a Chrome browser must be open,",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            18.0,
            329.0,
            anchor="nw",
            text="and you must be logged-in to Silicon Expert",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            17.0,
            179.0,
            anchor="nw",
            text=" 1. Input the MPNs at the box at the right",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        canvas.create_text(
            17.0,
            216.0,
            anchor="nw",
            text=" 2. Click Go",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        canvas.create_text(
            17.0,
            56.0,
            anchor="nw",
            text="Open Multiple Silicon Expert MPNs",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_rectangle(
            0.0,
            428.0,
            862.0,
            519.0,
            fill="#D6DFDF",
            outline="")

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("SE_Go.png"))
        button_5 = Button(
            self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: SELinks(),
            relief="flat"
        )
        button_5.place(
            x=617.0,
            y=395.0,
            width=99.0,
            height=24.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("SE_Clear.png"))
        button_6 = Button(
            self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=clear_textSE,
            relief="flat"
        )
        button_6.place(
            x=734.0,
            y=395.0,
            width=99.0,
            height=24.0
        )

        canvas.create_rectangle(
            0.0,
            428.0,
            862.0,
            519.0,
            fill="#D6DFDF",
            outline="")

        self.image_image_0 = PhotoImage(
            file=relative_to_assets("Emerson.png"))
        image_1 = canvas.create_image(
            726.0,
            474.0,
            image=self.image_image_0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("SE_Entry.png"))
        entry_bg_1 = canvas.create_image(
            724.0,
            225.5,
            image=self.entry_image_1
        )
        SE_textarea = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        SE_textarea.place(
            x=602.0,
            y=68.0,
            width=244.0,
            height=313.0
        )
        self.image_image_2 = PhotoImage(
            file=relative_to_assets("SE_Header.png"))
        image_2 = canvas.create_image(
            724.0,
            42.0,
            image=self.image_image_2
        )

class DPXE (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def DPXELinks():
            DPXEurl = DPXE_textarea.get('1.0','end-1c') # get input from drawing numbers
            DPXEurl1 = list(DPXEurl.split()) #make the input as list
            DPXE_link = 'https://printroom.ascovalve.com/search.jsp?DWGNO='
            URLs = [DPXE_link + x for x in DPXEurl1] # for loop to append SE_link string in elements of url1 list
            for links in URLs: # create a for loop to open links
                webbrowser.get(chrome_path).open_new_tab(links)
                time.sleep(1)
        def clear_textDPXE():
            DPXE_textarea.delete('1.0','end-1c')
        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
                )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            587.0,
            519.0,
            fill="#00A4D2",
            outline="")

        self.Files_tab = PhotoImage(
            file=relative_to_assets("Files_Page.png"))
        button_4 = Button(
            self,
            image=self.Files_tab,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("EDAFiles"),
            relief="flat"
        )
        button_4.place(
            x=253.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("SE_Page.png"))
        button_1 = Button(
            self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("SiliconExpert"),
            relief="flat"
        )
        button_1.place(
            x=135.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("Home_Page.png"))
        button_2 = Button(
            self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("HomePage"),
            relief="flat"
        )
        button_2.place(
            x=17.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        canvas.create_text(
            17.0,
            305.0,
            anchor="nw",
            text="Important: For this to work, a Chrome browser must be open,",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            18.0,
            329.0,
            anchor="nw",
            text="and you must be logged-in to Digital Printroom",
            fill="#FFFFFF",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            17.0,
            179.0,
            anchor="nw",
            text=" 1. Input the Drawings at the box at the right",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        canvas.create_text(
            17.0,
            216.0,
            anchor="nw",
            text=" 2. Click Go",
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.button_image_9 = PhotoImage(
        file=relative_to_assets("DPXE_Go.png"))
        button_3 = Button(
            self,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: DPXELinks(),
            relief="flat"
        )
        button_3.place(
            x=617.0,
            y=395.0,
            width=99.0,
            height=24.0
        )

        self.button_image_10 = PhotoImage(
            file=relative_to_assets("DPXE_Clear.png"))
        button_4 = Button(
            self,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=clear_textDPXE,
            relief="flat"
        )
        button_4.place(
            x=734.0,
            y=395.0,
            width=99.0,
            height=24.0
        )

        canvas.create_text(
            17.0,
            56.0,
            anchor="nw",
            text="Open Multiple DPXE Drawings",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_rectangle(
            0.0,
            428.0,
            862.0,
            519.0,
            fill="#D6DFDF",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("Emerson.png"))
        image_1 = canvas.create_image(
            726.0,
            474.0,
            image=self.image_image_1
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("DPXE_Entry.png"))
        entry_bg_1 = canvas.create_image(
            724.0,
            225.5,
            image=self.entry_image_2
        )
        DPXE_textarea = Text(
            self,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0
        )
        DPXE_textarea.place(
            x=602.0,
            y=68.0,
            width=244.0,
            height=313.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("DPXE_Header.png"))
        image_2 = canvas.create_image(
            724.0,
            42.0,
            image=self.image_image_2
        )
class EDAFiles (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        canvas = Canvas(
        self,
        bg = "#FFFFFF",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            862.0,
            519.0,
            fill="#00A4D2",
            outline="")

        canvas.create_text(
            256.0,
            33.0,
            anchor="nw",
            text="Open EDA-Related Files",
            fill="#FFFFFF",
            font=("Inter", 30 * -1)
        )

        canvas.create_rectangle(
            0.0,
            428.0,
            862.0,
            519.0,
            fill="#D6DFDF",
            outline="")

        self.buttonimage_1 = PhotoImage(
            file=relative_to_assets("SE_Page.png"))
        self.button1 = Button(
            self,
            image=self.buttonimage_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("SiliconExpert"),
            relief="flat"
        )
        self.button1.place(
            x=138.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        self.buttonimage_2 = PhotoImage(
            file=relative_to_assets("DPXE_Page.png"))
        self.button2 = Button(
            self,
            image=self.buttonimage_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("DPXE"),
            relief="flat"
        )
        self.button2.place(
            x=259.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("Emerson.png"))
        image_1 = canvas.create_image(
            784.0,
            474.0,
            image=self.image_image_1
        )

        self.buttonimage_3 = PhotoImage(
            file=relative_to_assets("Home_Page.png"))
        self.button3 = Button(
            self,
            image=self.buttonimage_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("HomePage"),
            relief="flat"
        )
        self.button3.place(
            x=17.0,
            y=464.0,
            width=99.0,
            height=24.0
        )

        self.buttonimage_4 = PhotoImage(
            file=relative_to_assets("FLMC_ECAD_excel.png"))
        self.button4 = Button(
            self,
            image=self.buttonimage_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: OpenFiles(FLMCECADxcl),
            relief="flat"
        )
        self.button4.place(
            x=67.0,
            y=105.0,
            width=252.0,
            height=50.15138244628906
        )

        self.buttonimage_5 = PhotoImage(
            file=relative_to_assets("FLMC_ECAD_BI.png"))
        self.button5 = Button(
            self,
            image=self.buttonimage_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: OpenFiles(ECADBi),
            relief="flat"
        )
        self.button5.place(
            x=543.0,
            y=245.0,
            width=252.0,
            height=50.1513671875
        )

        self.buttonimage_6 = PhotoImage(
            file=relative_to_assets("Comp_Rev.png"))
        self.button6 = Button(
            self,
            image=self.buttonimage_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: OpenFiles(CompRev),
            relief="flat"
        )
        self.button6.place(
            x=543.0,
            y=105.0,
            width=252.0,
            height=50.15138244628906
        )

        self.buttonimage_7 = PhotoImage(
            file=relative_to_assets("IPC.png"))
        self.button7 = Button(
            self,
            image=self.buttonimage_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: OpenFiles(IPCFp),
            relief="flat"
        )
        self.button7.place(
            x=67.0,
            y=245.0,
            width=252.0,
            height=50.1513671875
        )

        self.buttonimage_8 = PhotoImage(
            file=relative_to_assets("Altium_reference.png"))
        self.button8 = Button(
            self,
            image=self.buttonimage_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: OpenLinks(AltLib),
            relief="flat"
        )
        self.button8.place(
            x=67.0,
            y=175.0,
            width=252.0,
            height=50.15138244628906
        )

        self.buttonimage_9 = PhotoImage(
            file=relative_to_assets("Part_Num.png"))
        self.button9 = Button(
            self,
            image=self.buttonimage_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: OpenFiles(Pnumb),
            relief="flat"
        )
        self.button9.place(
            x=67.0,
            y=315.0,
            width=252.0,
            height=50.1513671875
        )

        self.buttonimage_10 = PhotoImage(
            file=relative_to_assets("PowerApp.png"))
        self.button10 = Button(
            self,
            image=self.buttonimage_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: OpenLinks(PwrApps),
            relief="flat"
        )
        self.button10.place(
            x=543.0,
            y=175.0,
            width=252.0,
            height=50.15138244628906
        )

        self.buttonimage_11 = PhotoImage(
            file=relative_to_assets("RiskBI.png"))
        self.button11 = Button(
            self,
            image=self.buttonimage_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: OpenLinks(ECADRiskBi),
            relief="flat"
        )
        self.button11.place(
            x=543.0,
            y=315.0,
            width=252.0,
            height=50.1513671875
        )

app = EDAApp()
app.mainloop()