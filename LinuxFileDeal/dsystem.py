import os
from subprocess import check_output

# kill progress succeed return true
# no progress return false


def kill_progress(progress_name):
    cmd = 'ps aux | grep {} | grep -v grep '.format(progress_name)
    progress_num = len(os.popen(cmd).readline())
    if progress_num >= 1:
        get_progress_id = check_output(['pidof', progress_name])
        kill_progress_id_cmd = 'kill -9 {}'.format(get_progress_id)
        os.system(kill_progress_id_cmd)
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
            return name
    return False



