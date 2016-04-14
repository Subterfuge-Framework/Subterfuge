class sslstrip:
    def __init__(self):
        import os
        import sys
        sys.path.append("../")

    def proxy(self, PROXY_PORT):
        import os
        import sys
        sys.path.append("../")
        import subprocess

        print "Starting SSLStrip on " + PROXY_PORT

        package_dir = os.path.dirname(os.path.dirname(__file__)) + '/packages/'
        print package_dir

        process = subprocess.Popen(
            'python ' + package_dir + 'sslstrip.py -w ' + package_dir + '/sslstrip.log -l ' + str(PROXY_PORT) + ' -f &',
            shell=True)

        return process.pid

        # os.system('python packages/sslstrip.py -w packages/sslstrip.log -l ' + str(PROXY_PORT) + ' -f &')
