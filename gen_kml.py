import os
import sys

sys.path.append(os.path.abspath(os.path.curdir))

#located in Pre-processing/geoNet
from gen_stats_kml import *

ll_dir = "/nesi/projects/nesi00213/RunFolder/ykh22/2010Sept4_m7pt1_newtdelay_VMCant_v1p65_BULLDOZED-h0p100_EMODv3p0p4_170410_best_sim/fd_nz01-h0.100.ll"
out_name = "fd_nz01-h0.100.ll-NA_only.kml"
vs_dir = "/nesi/projects/nesi00213/StationInfo/non_uniform_with_real_stations_10042017.vs30"
ll_out = "fd_nz01-h0.100.ll-NA_only.ll"
def ll_to_stats_dict(file_dir):
    vs_na_list = []
    with open(vs_dir) as f2:
        for vs_line in f2:
            if "NA" in vs_line:
                #print vs_line.split()[0]
                vs_na_list.append(vs_line.split()[0])
    print len(vs_na_list)
    
    stat_dict = {}
    with open(file_dir) as f:
        for line in f:
            lon, lat, stat_code = line.split()
            stat_code = stat_code.strip(' ')
            if stat_code in vs_na_list:
                stat_dict.update({stat_code: [float(lon), float(lat)]})
    #print stat_dict
    return stat_dict

def gen_list():
    f_ll_out = open(os.path.join(os.path.curdir, ll_out),'w')
    vs_na_list = []
    with open(vs_dir) as f2:
        for vs_line in f2:
            if "NA" in vs_line:
                #print vs_line.split()[0]
                vs_na_list.append(vs_line.split()[0])
    with open(ll_dir) as f:
        for line in f:
            lon, lat, stat_code = line.split()
            stat_code = stat_code.strip(' ')
            if stat_code in vs_na_list:
               f_ll_out.write(line) 
    

if __name__ == '__main__':
    stat_dict = ll_to_stats_dict(ll_dir)
    #write_stats_kml(os.path.curdir, out_name, stat_dict)
    #gen_list()
