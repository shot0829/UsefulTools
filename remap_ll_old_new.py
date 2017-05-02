dict_dir = "dict.txt"
fd_dir = "GM/Sim/Data/AlpineFault_Rupture_VMSI_v1p65_200m-h0p200_EMODv3p0p4_170412_s2n/fd_sinz01-h0.200.ll"
fd_out = "fd_sinz01-h0.200.ll_new"


#def find_replace(file_dir, old, new):
    

f_fd_out = open(fd_out, 'w')

code_dict = {}
with open(dict_dir) as f_dict:
    for line in f_dict:
        new_code, old_code = line.replace("\n",'').split('\t',1)
        code_dict.update({old_code:new_code })


with open(fd_dir) as f_fd:
    for line in f_fd:
        lon, lat, stat_code = line.split()
        f_fd_out.write( "  %s   %s %s\n"%(lon, lat, code_dict[stat_code]) )


'''
with open(dict_dir) as f_dict:
    for line in f_dict:
        new_code, old_code = line.replace("\n",'').split('\t',1)
        with open(fd_dir) as f_fd:
            for line in f_fd:
                lon, lat, stat_code = line.split()
                if stat_code == old_code:
                    f_fd_out.write("  %s   %s %s\n"%(lon, lat, new_code) )
                    #print "lon:%s lat:%s code:%s."%(lon,lat, stat_code)
        #f_fd = open(fd_dir)
        #fd_line = f_fd.readline()
'''
        
