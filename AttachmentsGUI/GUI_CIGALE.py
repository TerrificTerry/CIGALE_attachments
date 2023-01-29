import tkinter
import tkinter.messagebox
import customtkinter
import io
# import webbrowser
from customtkinter import filedialog
from Execution import AttachmentsG
from Execution import AttachmentsR

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

anaconda_adr = "C:/Users/WorkingTRY/anaconda3/Scripts/activate.bat C:/Users/WorkingTRY/anaconda3/envs/py3"
diradr = "C:/Users/Terry Yin/Desktop/Computing/CIGALE/Data/M84x"
inilines = ""

SFHsel = ""
STPsel = ""
NEsel = ""
ATLsel = ""
DEsel = ""
AGNsel = ""

sfhdelayed = ["10.0, 100.0, 1000.0, 3000.0, 10000.0", "4000, 7000, 10000, 13000", "30.0, 50.0, 100.0", "100, 300, 500", "0.001, 0.005, 0.01, 0.05, 0.1"]
sfh2exp = ["10.0, 100.0, 1000.0, 3000.0, 10000.0", "10.0, 30.0, 50.0", "0.001, 0.005, 0.01, 0.05, 0.1", "5000", "20"]
sfhperiodic = ["1", "50", "20.0", "1000"]
bc03 = ["1", "0.008, 0.02, 0.05", "10"]
m2005 = ["0", "0.008, 0.02, 0.05", "10"]
nebular = ["-2.0", "0.014", "100.0", "0.0", "0.0"]
# stellar = []
dustatt = ["0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1", "0.44"]
dustattCF = ["1.0", "0.44"]
dale2014 = ["0.0", "2.0"]
dl2014 = ["2.5", "1.0", "2.0", "0.1"]
casey2012 = ["35.0", "1.6", "2.0"]
fritz2006 = ["60.0", "1.0", "-0.5", "4.0", "100.0", "30.1", "1", "0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9"]
skirtor2016 = ["5, 7, 9", "0.5, 1.0, 1.5", "1.0", "30, 40, 50", "20", "30", "1", "0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9"]

sfhdelayedtar = ["    tau_main ", "    age_main ", "    tau_burst ", "    age_burst ", "    f_burst "]
sfh2exptar = ["    tau_main ", "    tau_burst ", "    f_burst ", "    age ", "    burst_age "]
sfhperiodictar = ["   type_bursts ", "   delta_bursts ", "   tau_bursts ", "   age "]
bc03tar = ["    imf ", "    metallicity ", "    seperation_age "]
m2005tar = ["    imf ", "    metallicity ", "    seperation_age "]
nebulartar = ["    logU ", "    zgas ", "    ne ", "    f_esc ", "    f_dust "]
# stellartar = []
dustatttar = ["    E_BV_lines ", "    E_BV_factor "]
dustattCFtar = ["    Av_ISM ", "    mu "]
dale2014tar = ["    fracAGN ", "    alpha "]
dl2014tar = ["    qpah ", "    umin ", "    alpha ", "    gamma "]
casey2012tar = ["     temperature ", "    beta ", "    alpha "]
fritz2006tar = ["    r_ratio ", "    tau ", "    beta ", "    gamma ", "    opening_angle ", "    psy ", "    disk_type ", "    fracAGN "]
skirtor2016tar = ["    t ", "    pl ", "    q ", "    oa ", "    R ", "    i ", "    disk_type ", "    fracAGN "]

def select_folder():
    folder_path = filedialog.askdirectory()
    global diradr
    diradr = folder_path

def modify_ini(diradr, targetvar, pvalues):
    global inilines
    with io.open(diradr + "/pcigale.ini", "r", encoding='utf-8') as file:
        inilines = file.readlines()
    with io.open(diradr + "/pcigale.ini", "w", encoding='utf-8') as file:
        for line in inilines:
            if targetvar in line:
                line = pvalues + "\n"
            file.write(line)
            
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        def savepara(model):
            print("save parameters of " + model)
            global sfhdelayed, sfh2exp, sfhperiodic, bc03, m2005, nebular, dustatt, dustattCF, dale2014, dl2014, casey2012, fritz2006, skirtor2016;
            
            if model == "sfhdelayed":
                sfhdelayed = [self.entrysfh1.get(), self.entrysfh2.get(), self.entrysfh3.get(), self.entrysfh4.get(), self.entrysfh5.get()]
            elif model == "sfh2exp":
                sfh2exp = [self.entrysfhexp1.get(), self.entrysfhexp2.get(), self.entrysfhexp3.get(), self.entrysfhexp4.get(), self.entrysfhexp5.get(),]
            elif model == "sfhperiodic":
                sfhperiodic = [self.entrysfhper1.get(), self.entrysfhper2.get(), self.entrysfhper3.get(), self.entrysfhper4.get()]
            elif model == "bc03":
                bc03 = [self.entrybc031.get(), self.entrybc032.get(), self.entrybc033.get()]
            elif model == "m2005":
                m2005 = [self.entrym20051.get(), self.entrym20052.get(), self.entrym20053.get()]
            elif model == "nebular":
                nebular = [self.entryneb1.get(), self.entryneb2.get(), self.entryneb3.get(), self.entryneb4.get(), self.entryneb5.get()]
            elif model == "dustatt":
                dustatt = [self.entrydustatt1.get(), self.entrydustatt2.get()]
            elif model == "dustattCF":
                dustattCF = [self.entrydustattCF1.get(), self.entrydustattCF2.get()]
            elif model == "dale2014":
                dale2014 = [self.entrydale1.get(), self.entrydale2.get()]
            elif model == "dl2014":
                dl2014 = [self.entrydl1.get(), self.entrydl2.get(), self.entrydl3.get(), self.entrydl4.get()]
            elif model == "casey2012":
                casey2012 = [self.entrycasey1.get(), self.entrycasey2.get(), self.entrycasey3.get()]
            elif model == "fritz2006":
                fritz2006 = [self.entryFritz1.get(), self.entryFritz2.get(), self.entryFritz3.get(), self.entryFritz4.get(), self.entryFritz5.get(), self.entryFritz6.get(), self.entryFritz7.get(), self.entryFritz8.get()]
            elif model == "skirtor2016":
                skirtor2016 = [self.entrySkirtor1.get(), self.entrySkirtor2.get(), self.entrySkirtor3.get(), self.entrySkirtor4.get(), self.entrySkirtor5.get(), self.entrySkirtor6.get(), self.entrySkirtor7.get(), self.entrySkirtor8.get()]
            
              
        def mkini(diradr):
            global SFHsel, STPsel, NEsel, ATLsel, DEsel, AGNsel
            inifile = io.open(diradr + "/pcigale.ini", "w")
            inifiletxt = "data_file = cigale_input_corr.txt\nparameters_file = \nsed_modules =" + SFHsel + ', ' + STPsel + ', ' + NEsel + ', ' + ATLsel + ', ' + DEsel + ', redshifting, ' + AGNsel + "\nanalysis_method = pdf_analysis\ncores = 4\n"
            inifile.write(inifiletxt)
            
        def mkinispec(diradr):
            inifile = io.open(diradr + "/pcigale.ini.spec", "w")
            inifiletxt = "data_file = string()\nparameters_file = string()\nsed_modules = cigale_string_list()\nanalysis_method = string()\ncores = integer(min=1)\n"
            inifile.write(inifiletxt)
              
        def showTerm():
            global sfhdelayed, sfh2exp, sfhperiodic, bc03, m2005, nebular, dustatt, dustattCF, dale2014, dl2014, casey2012, fritz2006, skirtor2016;
            global SFHsel, STPsel, NEsel, ATLsel, DEsel, AGNsel
            modellist = [SFHsel, STPsel, NEsel, ATLsel, DEsel, AGNsel]
            for model in modellist:
                print(model+":")
                for para in vars(model):  #transfer string to variable here---->#
                    print(para)
        
        def modi(modeltar, model):
            i = 0
            for target in modeltar:
                modify_ini(diradr, target, target + "= " + model[i])
                i = i+1
         
        def configInput():
            global SFHsel, STPsel, NEsel, ATLsel, DEsel, AGNsel
            global diradr, anaconda_adr
            SFHsel = self.selection1.get()
            STPsel = self.selection2.get()
            NEsel = self.selection3.get()
            ATLsel = self.selection4.get()
            DEsel = self.selection5.get()
            AGNsel = self.selection6.get()
            
            mkini(diradr);
            mkinispec(diradr);
            
            AttachmentsG.pcigale_genconf(diradr, anaconda_adr)
           
        def applypara():
            global sfhdelayed, bc03, nebular, dustatt, dale2014, fritz2006;
            global sfhdelayedtar, bc03tar, nebulartar, dustatttar, dale2014tar, fritz2006tar;
            global diradr;
            global SFHsel, STPsel, NEsel, ATLsel, DEsel, AGNsel
            
            
            if SFHsel == "sfhdelayed":
                modi(sfhdelayedtar, sfhdelayed)
            elif SFHsel == "sfh2exp":
                modi(sfh2exptar, sfh2exp)
            elif SFHsel == "sfhperiodic":
                modi(sfhperiodictar, sfhperiodic)
                
            if STPsel == "bc03":
                modi(bc03tar, bc03)
            elif STPsel == "m2005":
                modi(m2005tar, m2005)
            
            if NEsel == "nebular":
                modi(nebulartar, nebular)
            
            if ATLsel == "dustatt_modified_starburst":
                modi(dustatttar, dustatt)
            elif ATLsel == "dustatt_modified_CF00":
                modi(dustattCFtar, dustattCF)
            
            if DEsel == "dale2014":
                modi(dale2014tar,dale2014)
            elif DEsel == "dl2014":
                modi(dl2014tar, dl2014)
            elif DEsel == "casey2012":
                modi(casey2012tar, casey2012)
                
            if AGNsel == "fritz2006":
                modi(fritz2006tar, fritz2006)
            elif AGNsel == "skirtor2016":
                modi(skirtor2016tar, skirtor2016)
    
        # configure window
        self.title("Attachments for CIGALE (version 22.10.1)")
        self.geometry(f"{1470}x{810}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(1, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CIGALE_ATT", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.linktoCIGALE = customtkinter.CTkLabel(self, text="More info about cigale, visit https://cigale.lam.fr/.", font=customtkinter.CTkFont(size=15))
        self.linktoCIGALE.grid(row=2, column=1, padx=20, pady=(20, 10))
        self.linktoGithub = customtkinter.CTkLabel(self, text="More info or tutorial about this GUI attachment, visit https://github.com/TerrificTerry/CIGALE_attachments.", font=customtkinter.CTkFont(size=15))
        self.linktoGithub.grid(row=3, column=1, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:select_folder())
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:configInput())
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=lambda:savepara("model"))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command = lambda:applypara())
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, command = lambda:AttachmentsR.pcigale_run(diradr, anaconda_adr))
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(100, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(0, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 0))

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        
        self.main_button_2 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text="Show In Terminal", text_color=("gray10", "#DCE4EE"), command = lambda:showTerm())
        self.main_button_2.grid(row=4, column=3, padx=(20, 20), pady=(5, 5), sticky="nsew")        

        # create textbox
        # self.textbox = customtkinter.CTkTextbox(self, width=250)
        # self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview for selection of models
        self.tabviews = customtkinter.CTkTabview(self, width=300, height=30)
        self.tabviews.grid(row=0, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")
        self.tabviews.add("SFH")
        self.tabviews.add("Stellar Population")
        self.tabviews.add("Nebular Emission")
        self.tabviews.add("Attenuation Laws")
        self.tabviews.add("Dust Emission")
        self.tabviews.add("AGN")
        
        # configure grid of individual tabs
        self.tabviews.tab("SFH").grid_columnconfigure(0, weight=1)
        self.tabviews.tab("Stellar Population").grid_columnconfigure(0, weight=1)
        self.tabviews.tab("Nebular Emission").grid_columnconfigure(0, weight=1)
        self.tabviews.tab("Attenuation Laws").grid_columnconfigure(0, weight=1)
        self.tabviews.tab("Dust Emission").grid_columnconfigure(0, weight=1)
        self.tabviews.tab("AGN").grid_columnconfigure(0, weight=1)
        
        # configure of model selection
        self.selection1 = customtkinter.CTkComboBox(self.tabviews.tab("SFH"),
                                                    values=["sfhdelayed", "sfh2exp", "sfhperiodic"])
        self.selection1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.selection2 = customtkinter.CTkComboBox(self.tabviews.tab("Stellar Population"),
                                                    values=["bc03", "m2005"])
        self.selection2.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.selection3 = customtkinter.CTkComboBox(self.tabviews.tab("Nebular Emission"),
                                                    values=["nebular"])
        self.selection3.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.selection4 = customtkinter.CTkComboBox(self.tabviews.tab("Attenuation Laws"),
                                                    values=["dustatt_modified_starburst", "dustatt_modified_CF00"])
        self.selection4.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.selection5 = customtkinter.CTkComboBox(self.tabviews.tab("Dust Emission"),
                                                    values=["dale2014", "dl2014", "casey2012"])
        self.selection5.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.selection6 = customtkinter.CTkComboBox(self.tabviews.tab("AGN"),
                                                    values=["fritz2006", "skirtor2016"])
        self.selection6.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        # create tabview for input
        self.tabview = customtkinter.CTkTabview(self, width=500, height=300)
        self.tabview.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("sfhdelayed")
        self.tabview.add("sfh2exp")
        self.tabview.add("sfhperiodic")
        self.tabview.add("bc03")
        self.tabview.add("m2005")
        self.tabview.add("nebular")
        # self.tabview.add("stellar")
        self.tabview.add("dustatt")
        self.tabview.add("dustattCF")
        self.tabview.add("dale2014")
        self.tabview.add("dl2014")
        self.tabview.add("casey2012")
        self.tabview.add("fritz2006")
        self.tabview.add("skirtor2016")
                
        # configure grid of individual tabs
        self.tabview.tab("sfhdelayed").grid_columnconfigure(0, weight=1)
        self.tabview.tab("sfh2exp").grid_columnconfigure(0, weight=1)
        self.tabview.tab("sfhperiodic").grid_columnconfigure(0, weight=1)
        self.tabview.tab("bc03").grid_columnconfigure(0, weight=1)
        self.tabview.tab("m2005").grid_columnconfigure(0, weight=1)
        self.tabview.tab("nebular").grid_columnconfigure(0, weight=1)
        # self.tabview.tab("stellar").grid_columnconfigure(0, weight=1)
        self.tabview.tab("dustatt").grid_columnconfigure(0, weight=1)
        self.tabview.tab("dustattCF").grid_columnconfigure(0, weight=1)
        self.tabview.tab("dale2014").grid_columnconfigure(0, weight=1)
        self.tabview.tab("dl2014").grid_columnconfigure(0, weight=1)
        self.tabview.tab("casey2012").grid_columnconfigure(0, weight=1)
        self.tabview.tab("fritz2006").grid_columnconfigure(0, weight=1)
        self.tabview.tab("skirtor2016").grid_columnconfigure(0, weight=1)        

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("sfhdelayed"), dynamic_resizing=False,
                                                        # values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("sfhdelayed"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("sfhdelayed"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("bc03"), text="CTkLabel on bc03")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        #The tab view for parameters on sfhdelayed
        self.entrysfh1 = customtkinter.CTkEntry(self.tabview.tab("sfhdelayed"), placeholder_text="tau_main (10.0, 100.0, 1000.0, 3000.0, 10000.0)")
        self.entrysfh1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfh2 = customtkinter.CTkEntry(self.tabview.tab("sfhdelayed"), placeholder_text="age_main (4000, 7000, 10000, 13000)")
        self.entrysfh2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfh3 = customtkinter.CTkEntry(self.tabview.tab("sfhdelayed"), placeholder_text="tau_burst (30.0, 50.0, 100.0)")
        self.entrysfh3.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfh4 = customtkinter.CTkEntry(self.tabview.tab("sfhdelayed"), placeholder_text="age_burst (100, 300, 500)")
        self.entrysfh4.grid(row=3, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfh5 = customtkinter.CTkEntry(self.tabview.tab("sfhdelayed"), placeholder_text="f_burst (0.001, 0.005, 0.01, 0.05, 0.1)")
        self.entrysfh5.grid(row=4, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentsfh = customtkinter.CTkButton(self.tabview.tab("sfhdelayed"), text="save parameters", command=lambda:savepara("sfhdelayed"))
        self.confentsfh.grid(row=5, column=0, padx=20, pady=10)
        
        #The tab view for parameters on sfh2exp
        self.entrysfhexp1 = customtkinter.CTkEntry(self.tabview.tab("sfh2exp"), placeholder_text="tau_main (10.0, 100.0, 1000.0, 3000.0, 10000.0)")
        self.entrysfhexp1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfhexp2 = customtkinter.CTkEntry(self.tabview.tab("sfh2exp"), placeholder_text="tau_burst (30.0, 50.0, 100.0)")
        self.entrysfhexp2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfhexp3 = customtkinter.CTkEntry(self.tabview.tab("sfh2exp"), placeholder_text="f_burst (0.001, 0.005, 0.01, 0.05, 0.1)")
        self.entrysfhexp3.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfhexp4 = customtkinter.CTkEntry(self.tabview.tab("sfh2exp"), placeholder_text="age (5000)")
        self.entrysfhexp4.grid(row=3, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfhexp5 = customtkinter.CTkEntry(self.tabview.tab("sfh2exp"), placeholder_text="burst_age (20)")
        self.entrysfhexp5.grid(row=4, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentsfhexp = customtkinter.CTkButton(self.tabview.tab("sfh2exp"), text="save parameters", command=lambda:savepara("sfh2exp"))
        self.confentsfhexp.grid(row=5, column=0, padx=20, pady=10)
        
        #The tab view for parameters on sfhperiodic
        self.entrysfhper1 = customtkinter.CTkEntry(self.tabview.tab("sfhperiodic"), placeholder_text="type_bursts (0)")
        self.entrysfhper1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfhper2 = customtkinter.CTkEntry(self.tabview.tab("sfhperiodic"), placeholder_text="delta_bursts (50)")
        self.entrysfhper2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfhper3 = customtkinter.CTkEntry(self.tabview.tab("sfhperiodic"), placeholder_text="tau_bursts (20.0)")
        self.entrysfhper3.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrysfhper4 = customtkinter.CTkEntry(self.tabview.tab("sfhperiodic"), placeholder_text="age (1000)")
        self.entrysfhper4.grid(row=3, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentsfhper = customtkinter.CTkButton(self.tabview.tab("sfhperiodic"), text="save parameters", command=lambda:savepara("sfhperiodic"))
        self.confentsfhper.grid(row=5, column=0, padx=20, pady=10)
        
        #The tab view for parameters on bc03
        self.entrybc031 = customtkinter.CTkEntry(self.tabview.tab("bc03"), placeholder_text="imf (0-Salpeter or 1-Chabrier)")
        self.entrybc031.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrybc032 = customtkinter.CTkEntry(self.tabview.tab("bc03"), placeholder_text="metallicity (0.008, 0.02, 0.05)")
        self.entrybc032.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrybc033 = customtkinter.CTkEntry(self.tabview.tab("bc03"), placeholder_text="seperation_age (10 Myr)")
        self.entrybc033.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentbc03 = customtkinter.CTkButton(self.tabview.tab("bc03"), text="save parameters", command=lambda:savepara("bc03"))
        self.confentbc03.grid(row=3, column=0, padx=20, pady=10)
        
        #The tab view for parameters on m2005
        self.entrym20051 = customtkinter.CTkEntry(self.tabview.tab("m2005"), placeholder_text="imf (0-Salpeter or 1-Chabrier)")
        self.entrym20051.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrym20052 = customtkinter.CTkEntry(self.tabview.tab("m2005"), placeholder_text="metallicity (0.008, 0.02, 0.05)")
        self.entrym20052.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrym20053 = customtkinter.CTkEntry(self.tabview.tab("m2005"), placeholder_text="seperation_age (10 Myr)")
        self.entrym20053.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentm2005 = customtkinter.CTkButton(self.tabview.tab("m2005"), text="save parameters", command=lambda:savepara("m2005"))
        self.confentm2005.grid(row=3, column=0, padx=20, pady=10)
        
        #The tab view for parameters on nebular
        self.entryneb1 = customtkinter.CTkEntry(self.tabview.tab("nebular"), placeholder_text="logU (-2.0)")
        self.entryneb1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryneb2 = customtkinter.CTkEntry(self.tabview.tab("nebular"), placeholder_text="zgas (0.014)")
        self.entryneb2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryneb3 = customtkinter.CTkEntry(self.tabview.tab("nebular"), placeholder_text="ne (100.0)")
        self.entryneb3.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryneb4 = customtkinter.CTkEntry(self.tabview.tab("nebular"), placeholder_text="f_esc (0.1)")
        self.entryneb4.grid(row=3, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryneb5 = customtkinter.CTkEntry(self.tabview.tab("nebular"), placeholder_text="f_dust (0.001, 0.005, 0.01)")
        self.entryneb5.grid(row=4, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentneb = customtkinter.CTkButton(self.tabview.tab("nebular"), text="save parameters", command=lambda:savepara("nebular"))
        self.confentneb.grid(row=5, column=0, padx=20, pady=10)
        
        # #The tab view for parameters on stellar
        # self.entryste1 = customtkinter.CTkEntry(self.tabview.tab("stellar"), placeholder_text="logU (-2.0)")
        # self.entryste1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        # self.entryste2 = customtkinter.CTkEntry(self.tabview.tab("stellar"), placeholder_text="zgas (0.014)")
        # self.entryste2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        # self.entryste3 = customtkinter.CTkEntry(self.tabview.tab("stellar"), placeholder_text="ne (100.0)")
        # self.entryste3.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        # self.entryste4 = customtkinter.CTkEntry(self.tabview.tab("stellar"), placeholder_text="f_esc (0.1)")
        # self.entryste4.grid(row=3, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        # self.entryste5 = customtkinter.CTkEntry(self.tabview.tab("stellar"), placeholder_text="f_dust (0.001, 0.005, 0.01)")
        # self.entryste5.grid(row=4, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        # self.confentste = customtkinter.CTkButton(self.tabview.tab("stellar"), text="save parameters", command=lambda:savepara("stellar"))
        # self.confentste.grid(row=5, column=0, padx=20, pady=10)
        
        #The tab view for parameters on dustatt
        self.entrydustatt1 = customtkinter.CTkEntry(self.tabview.tab("dustatt"), placeholder_text="E_BV_lines (0.001, 0.01, 0.1)")
        self.entrydustatt1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrydustatt2 = customtkinter.CTkEntry(self.tabview.tab("dustatt"), placeholder_text="E_BV_factor (0.44)")
        self.entrydustatt2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentdustatt = customtkinter.CTkButton(self.tabview.tab("dustatt"), text="save parameters", command=lambda:savepara("dustatt"))
        self.confentdustatt.grid(row=2, column=0, padx=20, pady=10)
        
        #The tab view for parameters on dustattCF
        self.entrydustattCF1 = customtkinter.CTkEntry(self.tabview.tab("dustattCF"), placeholder_text="Av_ISM (1.0)")
        self.entrydustattCF1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrydustattCF2 = customtkinter.CTkEntry(self.tabview.tab("dustattCF"), placeholder_text="mu (0.44)")
        self.entrydustattCF2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentdustattCF = customtkinter.CTkButton(self.tabview.tab("dustattCF"), text="save parameters", command=lambda:savepara("dustattCF"))
        self.confentdustattCF.grid(row=2, column=0, padx=20, pady=10)
        
        #The tab view for parameters on dale2014
        self.entrydale1 = customtkinter.CTkEntry(self.tabview.tab("dale2014"), placeholder_text="fracAGN (0.0 *preferred)")
        self.entrydale1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrydale2 = customtkinter.CTkEntry(self.tabview.tab("dale2014"), placeholder_text="alpha (2.0)")
        self.entrydale2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentdale = customtkinter.CTkButton(self.tabview.tab("dale2014"), text="save parameters", command=lambda:savepara("dale2014"))
        self.confentdale.grid(row=2, column=0, padx=20, pady=10)
        
        #The tab view for parameters on dl2014
        self.entrydl1 = customtkinter.CTkEntry(self.tabview.tab("dl2014"), placeholder_text="qpah (2.5)")
        self.entrydl1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrydl2 = customtkinter.CTkEntry(self.tabview.tab("dl2014"), placeholder_text="umin (1.0)")
        self.entrydl2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrydl3 = customtkinter.CTkEntry(self.tabview.tab("dl2014"), placeholder_text="alpha (2.0)")
        self.entrydl3.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrydl4 = customtkinter.CTkEntry(self.tabview.tab("dl2014"), placeholder_text="gamma (0.1)")
        self.entrydl4.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentdl = customtkinter.CTkButton(self.tabview.tab("dl2014"), text="save parameters", command=lambda:savepara("dl2014"))
        self.confentdl.grid(row=2, column=0, padx=20, pady=10)
        
        #The tab view for parameters on casey2012
        self.entrycasey1 = customtkinter.CTkEntry(self.tabview.tab("casey2012"), placeholder_text="temperature (35.0K)")
        self.entrycasey1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrycasey2 = customtkinter.CTkEntry(self.tabview.tab("casey2012"), placeholder_text="beta (1.6)")
        self.entrycasey2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrycasey3 = customtkinter.CTkEntry(self.tabview.tab("casey2012"), placeholder_text="alpha (2.0)")
        self.entrycasey3.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentcasey = customtkinter.CTkButton(self.tabview.tab("casey2012"), text="save parameters", command=lambda:savepara("casey2012"))
        self.confentcasey.grid(row=2, column=0, padx=20, pady=10)
        
        #The tab view for parameters on fritz2006
        self.entryFritz1 = customtkinter.CTkEntry(self.tabview.tab("fritz2006"), placeholder_text="r_ratio (60.0)")
        self.entryFritz1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryFritz2 = customtkinter.CTkEntry(self.tabview.tab("fritz2006"), placeholder_text="tau (1.0)")
        self.entryFritz2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryFritz3 = customtkinter.CTkEntry(self.tabview.tab("fritz2006"), placeholder_text="beta (-0.5)")
        self.entryFritz3.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryFritz4 = customtkinter.CTkEntry(self.tabview.tab("fritz2006"), placeholder_text="gamma (4.0)")
        self.entryFritz4.grid(row=3, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryFritz5 = customtkinter.CTkEntry(self.tabview.tab("fritz2006"), placeholder_text="opening_angle (100.0)")
        self.entryFritz5.grid(row=4, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryFritz6 = customtkinter.CTkEntry(self.tabview.tab("fritz2006"), placeholder_text="psy (30.1)")
        self.entryFritz6.grid(row=5, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryFritz7 = customtkinter.CTkEntry(self.tabview.tab("fritz2006"), placeholder_text="disk_type (0-Skirtor or 1-Schartmann)")
        self.entryFritz7.grid(row=6, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entryFritz8 = customtkinter.CTkEntry(self.tabview.tab("fritz2006"), placeholder_text="fracAGN (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)")
        self.entryFritz8.grid(row=7, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentFritz = customtkinter.CTkButton(self.tabview.tab("fritz2006"), text="save parameters", command=lambda:savepara("fritz2006"))
        self.confentFritz.grid(row=8, column=0, padx=20, pady=10)
        
        #The tab view for parameters on skirtor2016
        self.entrySkirtor1 = customtkinter.CTkEntry(self.tabview.tab("skirtor2016"), placeholder_text="t (5, 7, 9)")
        self.entrySkirtor1.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrySkirtor2 = customtkinter.CTkEntry(self.tabview.tab("skirtor2016"), placeholder_text="pl (0.5, 1.0, 1.5)")
        self.entrySkirtor2.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrySkirtor3 = customtkinter.CTkEntry(self.tabview.tab("skirtor2016"), placeholder_text="q (1.0)")
        self.entrySkirtor3.grid(row=2, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrySkirtor4 = customtkinter.CTkEntry(self.tabview.tab("skirtor2016"), placeholder_text="oa (30, 40, 50)")
        self.entrySkirtor4.grid(row=3, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrySkirtor5 = customtkinter.CTkEntry(self.tabview.tab("skirtor2016"), placeholder_text="R (20)")
        self.entrySkirtor5.grid(row=4, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrySkirtor6 = customtkinter.CTkEntry(self.tabview.tab("skirtor2016"), placeholder_text="i (30)")
        self.entrySkirtor6.grid(row=5, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrySkirtor7 = customtkinter.CTkEntry(self.tabview.tab("skirtor2016"), placeholder_text="disk_type (0-Skirtor or 1-Schartmann)")
        self.entrySkirtor7.grid(row=6, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.entrySkirtor8 = customtkinter.CTkEntry(self.tabview.tab("skirtor2016"), placeholder_text="fracAGN (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)")
        self.entrySkirtor8.grid(row=7, column=0, columnspan=1, padx=(0, 0), pady=(5, 5), sticky="nsew")
        self.confentSkirtor = customtkinter.CTkButton(self.tabview.tab("skirtor2016"), text="save parameters", command=lambda:savepara("skirtor2016"))
        self.confentSkirtor.grid(row=8, column=0, padx=20, pady=10)

          
                
        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.switch_1 = customtkinter.CTkSwitch(master=self.checkbox_slider_frame, command=lambda: print("switch 1 toggle"))
        self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        self.switch_2 = customtkinter.CTkSwitch(master=self.checkbox_slider_frame)
        self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")

        # create slider and progressbar frame
        # self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # # self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        # self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        # self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        # self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # set default values
        self.sidebar_button_1.configure(text="Add Folder...")
        self.sidebar_button_2.configure(text="Configure Input")
        self.sidebar_button_3.configure(state="disabled", text="Mock Mode")
        self.sidebar_button_4.configure(text="Apply Values")
        self.sidebar_button_5.configure(text="Confirm and RUN")
    
        self.checkbox_2.configure(state="disabled")
        self.switch_2.configure(state="disabled")
        self.checkbox_1.select()
        self.switch_1.select()
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Light")
        self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        # # self.textbox.insert("0.0", "CTkTextbox\n\n" + "This is a sample.\n\n" * 20)
        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
        
        
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
