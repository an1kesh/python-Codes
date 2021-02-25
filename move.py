from ctypes import windll, Structure, c_long, byref
import time
import pyautogui
import random


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}



def run_code():
	pos = queryMousePosition()
	data = pos
	idl_time = 0
	max_idl_time = random.randint(20,60)
	print("max_idl_time = {}".format(max_idl_time))
	t_end = time.time() + 60 * 60
	while time.time() < t_end:
		time.sleep(1)
		pos = queryMousePosition()
		if(data == pos):
			#print("true")
			idl_time = idl_time + 1
			print(idl_time)
			if(idl_time > max_idl_time):
				pyautogui.moveTo(random.randint(0,1200), random.randint(0,700), duration = 0.2)
				idl_time = 0
				max_idl_time = random.randint(20,60)
				print("max_idl_time = {}".format(max_idl_time))
		else:
			max_idl_time = random.randint(20,60)
			print("max_idl_time = {}".format(max_idl_time))
			idl_time = 0		
		data = pos
		#print(pos)

if __name__ == '__main__':
	run_code()

#print (pos)



