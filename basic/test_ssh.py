import subprocess
#cmd=' '.join(['ssh', 'regression1@$T82', 'ls', '/h/home/regression1/sqa/Nightly_Full_Flow/Regression/Release_v1.0.2_v2/TC4.5*/'])
#subprocess.call(cmd, shell=True)

cmd=' '.join(['scp', '-r', 'regression1@$T82:'+'/h/home/regression1/sqa/Nightly_Full_Flow/Regression/Release_v1.0.2_v2/TC4.5*/\{setup,gui,mdp_session.xml,session_manager/jobinfo/crms*xml\}', 'test'])
subprocess.call(cmd, shell=True)
