import requests
import time, datetime



class whatchdog:
	def __init__(self, filename):
		self.filename = filename

	def watch(self, sleeptime):
		while(True):
			respose = requests.get('https://git.uibk.ac.at')



			code = respose.status_code
			nowDate = datetime.datetime.now().strftime("%d-%m-%y")
			nowTime = datetime.datetime.now().strftime("%H-%M-%S")

			csvEntry = ', '.join([nowDate, nowTime, str(code)])

			print(csvEntry)

			with open(self.filename, "a") as myfile:
				myfile.write(csvEntry)
				myfile.write("\n")

			time.sleep(sleeptime)



if __name__ == '__main__':
	wd = whatchdog("gitlab_log.csv")
	wd.watch(10)
