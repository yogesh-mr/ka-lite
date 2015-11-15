import sys
import os

# print("elielieli: " + os.path)

# KALITE_DIR set, so probably called from bin/kalite
if 'KALITE_DIR' in os.environ:
    sys.path = [
        os.path.join(os.environ['KALITE_DIR'], 'python-packages'),
        os.path.join(os.environ['KALITE_DIR'], 'dist-packages'),
        os.path.join(os.environ['KALITE_DIR'], 'kalite')
    ] + sys.path
# KALITE_DIR not set, so called from some other source
else:
    filedir = os.path.dirname(__file__)
    sys.path = [os.path.join(filedir, 'python-packages'), os.path.join(filedir, 'kalite')] + sys.path

if __name__ == "__main__":
    arguments = sys.argv[1]
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    pidfile = "pidfile="+cur_dir+"/kalite/runcherrypyserver.pid"

    if arguments == 'start':
        sys.argv = ["manage.py", "kaserve", "host=0.0.0.0", "daemonize=true", "production=true", pidfile]
        sys.exit(execfile(cur_dir+'/kalite/manage.py'))
        sys.argv = ["manage.py", "cronserver", "&"]
        sys.exit(execfile(cur_dir+'/kalite/manage.py'))
    elif arguments == 'stop':
        sys.argv = ["manage.py", "runcherrypyserver", "stop", pidfile]
        sys.exit(execfile(cur_dir+'/kalite/manage.py'))
