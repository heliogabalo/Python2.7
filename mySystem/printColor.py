class PrintIntColor():

	def __init__(self, msg):
		self.msg = msg

	def enable(abc):
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKCYAN = '\033[96m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
		ENDC = '\033[0m'

	def disable():
		HEADER = ''
		OKBLUE = ''
		OKCYAN = ''
		OKGREEN = ''
		WARNING = ''
		FAIL = ''
		BOLD = ''
		UNDERLINE = ''
		ENDC = ''
	
	enable(abc.msg)
		
	def infog():
		print(OKGREEN + self.msg + ENDC)
		
	def info(msg):
		print(OKBLUE + self.msg + ENDC)
		
	def warn(msg):
		print(WARNING + self.msg + ENDC)
		
	def err():
		print(FAIL + self.msg + ENDC)

	

