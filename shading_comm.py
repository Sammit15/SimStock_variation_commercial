import sys
import random as rd
from eppy import modeleditor
from eppy.modeleditor import IDF

iddfile = "C:/Users/Anmol/Desktop/UEM__6_amd_comm/EnergyPlus/ep8.9_windows/Energy+.idd"

# fname1 = "C:/Users/Home/Desktop/session_9_downloads/idf_files/bi_1.idf"

IDF.setiddname(iddfile)
#idf1 = IDF(fname1)


shaded = [ "36_00295_0001","37_00075_0003","37_00075_0004","37_00075_0010","37_00075_0011","37_00293_0001","37_00293_0005","37_00293_0008","37_00294_0001","37_00294_0006","37_00294_0018","37_00295_0001","37_00296_0001","37_00296_0004","37_00296_0005","37_00296_0011","37_00296_0012","38_00075_0010","38_00295_0001","39_00295_0001","37_00074_0002","37_00075_0011","37_00294_0001","37_00296_0001","37_00296_0005","37_00051_0479","37_00074_0004","37_00075_0001","37_00075_0002","37_00075_0003","37_00075_0004","37_00075_0005","37_00075_0006","37_00075_0007","37_00075_0008","37_00075_0009","37_00075_0013","37_00075_0014","37_00075_0016","37_00293_0002","37_00293_0003","37_00293_0004","37_00293_0006","37_00293_0007","37_00294_0002","37_00294_0003","37_00294_0004","37_00294_0005","37_00294_0007","37_00294_0008","37_00294_0009","37_00294_0010","37_00294_0011","37_00294_0012","37_00294_0013","37_00294_0014","37_00294_0015","37_00294_0016","37_00296_0002","37_00296_0003","37_00296_0006","37_00296_0007","37_00296_0008","37_00296_0010","37_00296_0011","37_00296_0012","38_00294_0011","38_00296_0003"]


for i in range(0,68):
    fname1 = "C:/Users/Anmol/Desktop/UEM__6_amd_comm/idf_files/bi_{}.idf".format(i+1)
    #print(fname1)
    idf1 = IDF(fname1)
    window_list = idf1.idfobjects['WINDOW']
    window_names = list()
    for item in window_list:
        window_names.append(item.Name)
    
    #print(window_names)

    shaded_win = list()
    for item in window_names:
        if item[0:13] in shaded:
            shaded_win.append(item)
    #print(residential_win)
    
    for win in shaded_win:
        idf1.newidfobject(
        "Shading:Overhang".upper(),
        Name = "Overhang_{}".format(win),
        Window_or_Door_Name = win, 
        Height_above_Window_or_Door = 0,
        Tilt_Angle_from_WindowDoor = 90,
        Left_extension_from_WindowDoor_Width = 0,
        Right_extension_from_WindowDoor_Width = 0,
        Depth = 0.1 * rd.randint(3,6))		

		
		
    idf1.saveas("C:/Users/Anmol/Desktop/UEM__6_amd_comm/idf_files_overhang/bi_{}_overhang.idf".format(i+1))
