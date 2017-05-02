
old_vel_dir="GM/Sim/Data/nesi/projects/nesi00213/RunFolder/baes/AlpineFault_Rupture_VMSI_v1p65_200m-h0p200_EMODv3p0p4_170412_s2n/BB/Cant1D_v2-midQ_hfnp2mm+_rvf0p8_sd50_k0p045/m7.90-411.0x17.3_s1129570_s2n/Vel_old/"
new_vel_dir="GM/Sim/Data/nesi/projects/nesi00213/RunFolder/baes/AlpineFault_Rupture_VMSI_v1p65_200m-h0p200_EMODv3p0p4_170412_s2n/BB/Cant1D_v2-midQ_hfnp2mm+_rvf0p8_sd50_k0p045/m7.90-411.0x17.3_s1129570_s2n/Vel/"
dict_dir = "dict.txt"
fd_dir = "GM/Sim/Data/AlpineFault_Rupture_VMSI_v1p65_200m-h0p200_EMODv3p0p4_170412_s2n/fd_sinz01-h0.200.ll"
from subprocess import call
import os
import sys


#cmd ="ls -l"
#call(cmd,shell=True)

v0 = ".000"
v9 = ".090"
vv = ".ver"

code_dict = {}
with open(dict_dir) as f_dict:
    for line in f_dict:
        new_code, old_code = line.replace("\n",'').split('\t',1)
        code_dict.update({old_code:new_code })

stat_list = []
with open(fd_dir) as f_fd:
    for line in f_fd:
        lon, lat, stat_code = line.split()
        stat_code = stat_code.strip(' ')
        stat_list.append(stat_code)


for code in stat_list:
    cmd = "cp %s %s"%(os.path.join(old_vel_dir,code+v0), os.path.join(new_vel_dir,code_dict[code]+v0) )
    print cmd
    #sys.exit()
    call(cmd,shell=True)
    cmd = "cp %s %s"%(os.path.join(old_vel_dir,code+v9), os.path.join(new_vel_dir,code_dict[code]+v9) )
    call(cmd,shell=True)
    cmd = "cp %s %s"%(os.path.join(old_vel_dir,code+vv), os.path.join(new_vel_dir,code_dict[code]+vv) )
    call(cmd,shell=True)
