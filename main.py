import os
import sys
import ctypes

# This script targets windows machines. 

def main():
	ctypes.windll.kernel32.SetConsoleTitleW("Local DNS Poisoning | github.com/LocalsGitHub | Awaiting confirmation to spoof")
	os.system('cls')
	print("Press enter to start spoof")
	os.system('PAUSE')
	checkForAdmin()
	dnsSpoof()

def dnsSpoof():
	with open(r"C:\windows\System32\drivers\etc\hosts", "a") as hostFile:
		try:
			hostFile.write("\n" + ip + " " + host + "\n")
			hostFile.close()
			os.system('cls')
			print("Done!")
		except Exception as e:
			print(e)
		

def is_running_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def checkForAdmin():
	if not is_running_as_admin():
		print('[!] The script is NOT running with administrative privileges. Please run with admin.')
		os.system('PAUSE')
		exit()
	else:
		print('[+] The script is running with administrative privileges! - Continuing')

def checkForArgs():
	global ip
	global host
	try:
		ip = sys.argv[1]
		host = sys.argv[2]
	except Exception:
		os.system('cls')
		print("Please pass in the correct arguments.")
		print("Example: 'py main.py {ip} {domain}'")
		os.system('PAUSE')
		exit()
	if (ip == ' ' and host == ' '):
		os.system('cls')
		print("Please pass in the correct arguments.")
		print("Example: 'py main.py {ip} {domain}'")
		os.system('PAUSE')
		exit()
	else:
		pass

if __name__ == '__main__':
	ctypes.windll.kernel32.SetConsoleTitleW("Local DNS Poisoning | github.com/LocalsGitHub ")
	checkForArgs()
	main()

