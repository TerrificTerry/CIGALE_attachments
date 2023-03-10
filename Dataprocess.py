import tkinter
import tkinter.messagebox
import customtkinter
import io
# import webbrowser
from customtkinter import filedialog
from Execution import AttachmentsG
from Execution import AttachmentsR
from Execution import Preprocess
from Execution import Extinctioncorr

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("NED Data Preprocess")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=12, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(12, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="NED Prep", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,text="Select Init File", command=lambda:select_file())
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_entry_1 = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="redshift")
        self.sidebar_entry_1.grid(row=2, column=0, padx=20, pady=5)
        self.sidebar_entry_2 = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Target (e.g.NGC5813)")
        self.sidebar_entry_2.grid(row=3, column=0, padx=20, pady=5)
        self.sidebar_entry_3 = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="E-BV Extinction")
        self.sidebar_entry_3.grid(row=4, column=0, padx=20, pady=5)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Priority:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.Priority_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Aperture", "Time"],
                                                                       command=self.change_appearance_mode_event)
        self.Priority_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Start Preprocess", command=lambda:Process(), width= 40, height= 100, fg_color="red", hover = "false")
        self.sidebar_button_2.grid(row=7, column=0, padx=20, pady=20)
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(0, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:")
        self.appearance_mode_label.grid(row=10, column=0, padx=20, pady=(0, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(0, 10))

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        # self.textbox = customtkinter.CTkTextbox(self, width=250)
        # self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        # self.tabview = customtkinter.CTkTabview(self, width=250)
        # self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.tabview.add("CTkTabview")
        # self.tabview.add("Tab 2")
        # self.tabview.add("Tab 3")
        # self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create radiobutton frame
        # self.radiobutton_frame = customtkinter.CTkFrame(self)
        # self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.radio_var = tkinter.IntVar(value=0)
        # self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="FUV", command= lambda:check(1))
        self.checkbox_1.grid(row=1, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="NUV", command= lambda:check(2))
        self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")
        self.checkbox_3 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="u_sdss", command= lambda:check(3))
        self.checkbox_3.grid(row=3, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_4 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="g_sdss", command= lambda:check(4))
        self.checkbox_4.grid(row=4, column=0, pady=10, padx=20, sticky="n")
        self.checkbox_5 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="r_sdss", command= lambda:check(5))
        self.checkbox_5.grid(row=5, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_6 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="i_sdss", command= lambda:check(6))
        self.checkbox_6.grid(row=6, column=0, pady=10, padx=20, sticky="n")
        self.checkbox_7 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="z_sdss", command= lambda:check(7))
        self.checkbox_7.grid(row=7, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_8 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="g_DeCaLs", command= lambda:check(8))
        self.checkbox_8.grid(row=8, column=0, pady=10, padx=20, sticky="n")
        self.checkbox_9 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="r_DeCaLs", command= lambda:check(9))
        self.checkbox_9.grid(row=9, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_10 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="z_DeCaLs", command= lambda:check(10))
        self.checkbox_10.grid(row=10, column=0, pady=10, padx=20, sticky="n")
        self.checkbox_11 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="WISE1", command= lambda:check(11))
        self.checkbox_11.grid(row=1, column=1, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_12 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="WISE2", command= lambda:check(12))
        self.checkbox_12.grid(row=2, column=1, pady=10, padx=20, sticky="n")
        self.checkbox_13 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="WISE3", command= lambda:check(13))
        self.checkbox_13.grid(row=3, column=1, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_14 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="WISE4", command= lambda:check(14))
        self.checkbox_14.grid(row=4, column=1, pady=10, padx=20, sticky="n")
        self.checkbox_15 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="IRAC1", command= lambda:check(15))
        self.checkbox_15.grid(row=5, column=1, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_16 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="IRAC2", command= lambda:check(16))
        self.checkbox_16.grid(row=6, column=1, pady=10, padx=20, sticky="n")
        self.checkbox_17 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="IRAC3", command= lambda:check(17))
        self.checkbox_17.grid(row=7, column=1, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_18 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="IRAC4", command= lambda:check(18))
        self.checkbox_18.grid(row=8, column=1, pady=10, padx=20, sticky="n")
        self.checkbox_19 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="IRAS1", command= lambda:check(19))
        self.checkbox_19.grid(row=9, column=1, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_20 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="IRAS2", command= lambda:check(20))
        self.checkbox_20.grid(row=10, column=1, pady=10, padx=20, sticky="n")
        self.checkbox_21 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="IRAS3", command= lambda:check(21))
        self.checkbox_21.grid(row=1, column=2, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_22 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="IRAS4", command= lambda:check(22))
        self.checkbox_22.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.checkbox_23 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="MIPS1", command= lambda:check(23))
        self.checkbox_23.grid(row=3, column=2, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_24 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="MIPS2", command= lambda:check(24))
        self.checkbox_24.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        self.checkbox_25 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="MIPS3", command= lambda:check(25))
        self.checkbox_25.grid(row=5, column=2, pady=(20, 10), padx=20, sticky="n")
        # self.checkbox_26 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="MODEL")
        # self.checkbox_26.grid(row=6, column=2, pady=10, padx=20, sticky="n")
        # self.checkbox_27 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="MODEL")
        # self.checkbox_27.grid(row=7, column=2, pady=(20, 10), padx=20, sticky="n")
        # self.checkbox_28 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="MODEL")
        # self.checkbox_28.grid(row=8, column=2, pady=10, padx=20, sticky="n")
        # self.checkbox_29 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="MODEL")
        # self.checkbox_29.grid(row=9, column=2, pady=(20, 10), padx=20, sticky="n")
        # self.checkbox_30 = customtkinter.CTkButton(master=self.checkbox_slider_frame, text="MODEL")
        # self.checkbox_30.grid(row=10, column=2, pady=10, padx=20, sticky="n")
        chkbxs = ["", "FUV", "NUV", "sdss.up", "sdss.gp", "sdss.rp", "sdss.ip", "sdss.zp", "legacyG", "legacyR", "legacyZ", "WISE1", "WISE2", "WISE3", "WISE4", "IRAC1", "IRAC2", "IRAC3", "IRAC4", "IRAS1", "IRAS2", "IRAS3", "IRAS4", "MIPS1", "MIPS2", "MIPS3"]
        
        chkcolorsel = [self.checkbox_1, self.checkbox_1, self.checkbox_2, self.checkbox_3, self.checkbox_4, self.checkbox_5, self.checkbox_6, self.checkbox_7, self.checkbox_8, self.checkbox_9, self.checkbox_10, self.checkbox_11, self.checkbox_12, self.checkbox_13, self.checkbox_14, self.checkbox_15, self.checkbox_16, self.checkbox_17, self.checkbox_18, self.checkbox_19, self.checkbox_20, self.checkbox_21, self.checkbox_22, self.checkbox_23, self.checkbox_24, self.checkbox_25]
        
        checkboxes = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        def check(boxnum):
            checkboxes[boxnum] *= -1
            if checkboxes[boxnum] == 1:
                print(chkbxs[boxnum]+": Selected")
                # print(chkcolorsel[boxnum]._fg_color)
                chkcolorsel[boxnum].configure(fg_color = "blue", hover = "false")
            else:
                print(chkbxs[boxnum]+": Cancelled")
                chkcolorsel[boxnum].configure(fg_color = ['#3B8ED0', '#1F6AA5'], hover = "true")
        
        # create checkbox and switch frame
        
        # self.switch_1 = customtkinter.CTkSwitch(master=self.checkbox_slider_frame, command=lambda: print("switch 1 toggle"))
        # self.switch_1.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        # self.switch_2 = customtkinter.CTkSwitch(master=self.checkbox_slider_frame)
        # self.switch_2.grid(row=4, column=0, pady=(10, 20), padx=20, sticky="n")

        # create slider and progressbar frame
        # self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
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
        # self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        # self.checkbox_2.configure(state="disabled")
        # self.switch_2.configure(state="disabled")
        # self.checkbox_1.select()
        # self.switch_1.select()
        # self.radio_button_3.configure(state="disabled")
        self.Priority_optionemenu.set("Aperture")
        self.appearance_mode_optionemenu.set("Light")
        self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        # self.textbox.insert("0.0", "CTkTextbox\n\n" + "This is a sample.\n\n" * 20)
        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")
        
        # self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text="Start Preprocess", command=lambda:self.Process(self, checkboxes), width= 40, height= 100, fg_color="red")
        global diradr
        global dirfile
        global galaname
        global bandtocorr
        bandtocorr = []
        
        def bandcorr():
            global bandtocorr
            cnt = 1
            print(cnt)
            while(cnt<=14):
                if checkboxes[cnt] == 1:
                    bandtocorr.append(chkbxs[cnt])
                print(cnt)
                cnt+=1
        
        def select_file():
            folder_path = filedialog.askopenfilename()
            global diradr
            global dirfile
            dirfile = folder_path
            diradr = ""
            # Find the index of the last occurrence of "/" in s
            print(folder_path)
            index = folder_path.rfind("/")
            print(index)
            # If "/" is found in s, slice the string from the beginning to that index
            diradr = folder_path[:index+1]
            print(diradr)
                        # print(diradr)
        
        def add_model(model):
            file = open("./Execution/filters.txt", "a")
            file.write(model+"\n")
            file.close()
        
        def Process():
            global diradr
            global dirfile
            global galaname
            cnt = 0;
            file = open("./Execution/filters.txt", "w")
            file.write("#filter"+"\n")
            file.close()
            for model in checkboxes:
                if model == 1:
                    add_model(chkbxs[cnt])
                cnt+=1
            print("Preprocessed filter list!")
            galaname = self.sidebar_entry_2.get()
            # listfile = [dirfile]
            Preprocess.preprocess([dirfile], [self.sidebar_entry_1.get()], "./Execution/filters.txt", "./Execution/bands_to_filter_full_v1.csv", diradr, self.sidebar_entry_2.get())
            print("cigale_input Processed!")
            
            bandcorr()
            print("bandcorr")
            for filter in bandtocorr:
                print(filter)
                
            # Extinctioncorr.extinctioncorr(galaname, diradr, bandtocorr, self.sidebar_entry_3.get())
            EBV = float(self.sidebar_entry_3.get())
            Extinctioncorr.extinctioncorr(galaname, diradr, bandtocorr, EBV)
            print("cigale_input_corr Processed!")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
