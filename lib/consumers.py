class harvester:
    def __init__(self):
        import os
        import sys
        sys.path.append("../")

    def _clear_file(self, file):
        try:
            open(file, 'w').close()
        except:
            print("Unable to clear: {0}".format(file))

    def purgeLogs(self):
        # Purge Logs
        self._clear_file("/usr/share/subterfuge/sslstrip.log")
        self._clear_file("/usr/share/subterfuge/mitmproxy.log")
        os.remove("/usr/share/subterfuge/harvester.log")
        os.remove("touch /usr/share/subterfuge/harvester.log")

    def httpHarvester(self, feed):
        import os
        import sys
        sys.path.append("../")
        import subprocess

        package_dir = os.path.dirname(os.path.dirname(__file__)) + '/packages/'
        print "Starting Harvester"
        cmd = "python {0} "
        process = subprocess.Popen('python {0} harvester/http_cred_harvester.py {1} &'.format( package_dir, feed),
                                   shell=True)

        return process.pid
