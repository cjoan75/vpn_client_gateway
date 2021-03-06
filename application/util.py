import subprocess
import syslog

def host_os_type():
        cmd = "cat /etc/*release"
        p = subprocess.Popen(cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        releaseinfo, err = p.communicate()
	if 'osmc' in releaseinfo:
		host_os_type = 'osmc'
        else:
		if 'raspbian' in releaseinfo:
                        host_os_type = 'raspbian'
                else:
                	if 'alpine' in releaseinfo:
                                host_os_type = 'alpine'
			else:
				if 'debian' in releaseinfo:
                                        host_os_type = 'debian'
                                else:
                                        host_os_type = 'other'
        return host_os_type

def stop_service(service_name):
	cmd = 'sudo service %s stop' % service_name
        p = subprocess.Popen(cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        return output

def start_service(service_name):
	cmd = 'sudo service %s start' % service_name
        p = subprocess.Popen(cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        return output

def restart_service(service_name):
	cmd = 'sudo service %s restart' % service_name
        p = subprocess.Popen(cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        return output

def disable_service(service_name):
        os_type = host_os_type()
	if os_type == 'alpine':
		disable_service_cmd = 'sudo rc-update del %s' % service_name
	else:
		disable_service_cmd = 'sudo update-rc.d %s disable' % service_name
        p = subprocess.Popen(disable_service_cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        return output

def enable_service(service_name):
	os_type = host_os_type()
        if os_type == 'alpine':
        	enable_service_cmd = 'sudo rc-update add %s' % service_name
        else:
                enable_service_cmd = 'sudo update-rc.d %s enable' % service_name
        p = subprocess.Popen(enable_service_cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        return output

def service_active(service_name):
        cmd = 'sudo service %s status' % service_name
        p = subprocess.Popen(cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        if ('Active: active' in output) or ('is running' in output) or ('started' in output):
                result = True
        else:
                result = False
        return result

def reboot():
        cmd = "sudo shutdown -r now"
        p = subprocess.Popen(cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        return output

def shutdown():
        cmd = "sudo shutdown -h now"
        p = subprocess.Popen(cmd,shell=True,executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        return output

