import random
import time

def Generate_OTP():
	return random.randint(111111,999999)
	
if __name__ == "__main__":
	for i in range(10):
		print(f"Your OTP Is : {Generate_OTP()}\n")
		time.sleep(1)
