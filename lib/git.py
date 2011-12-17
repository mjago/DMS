import os

def gitInitCmd(repoDir):
    if not isinstance(repoDir, str):
        raise Exception, 'gitInitCmd() expects a string'
    elif len(repoDir) < 1:
        raise Exception, 'gitInitCmd() does not expect an empty string'
    elif not os.path.isdir(repoDir):
        raise Exception, repoDir + ' does not exist!'
    else:    
        return('CD ' + repoDir  + '; git init')

#pipe = subprocess.Popen(cmd, shell=True, cwd=repoDir)
#pipe.wait()
#    cmd)
#
#def gitAdd(fileName, repoDir):
#    cmd = 'git add ' + fileName
#    pipe = subprocess.Popen(cmd, shell=True, cwd=repoDir)
#    pipe.wait()
#    return

