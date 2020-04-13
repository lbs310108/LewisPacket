from os import popen, system
from sys import executable
from subprocess import check_output

# kill progress succeed return true
# no progress return false


def kill_progress(progress_name):
    install_path = executable
    cmd = 'ps aux | grep {} | grep -v grep | grep -v {}'.format(progress_name, install_path)
    progress_num = len(popen(cmd).readline())
    cmd_id = 'pidof {}'.format(progress_name)
    if progress_num >= 1:
        get_progress_id = popen(cmd_id).readline()
        kill_progress_id_cmd = 'kill -9 {}'.format(get_progress_id)
        system(kill_progress_id_cmd)
        return True
    else:
        return False


# keywords to search in current dir
# if find, return the full_name to the variable
# if not find, return false
def get_curdir_name(keywords):
    file_list = check_output(['ls']).split()
    for name in file_list:
        if keywords in name:
            print name
    return False



