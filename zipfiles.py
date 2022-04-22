def make_parts():

	with open("drive.zip", "rb") as f:
		zip = f.read()
		
		
	byte_count = 0
	for byte in zip:
		byte_count += 1
		
	section_size = int(byte_count / 4)


	prev_done = 0

	for x in range(4):
		with open("zip" + str(x+1) + ".thomsonzippart", "wb") as f:
			comb = section_size + prev_done
			f.write(zip[prev_done:comb])
			prev_done += section_size
			
def reconstruct():
	bytes = b''
	for x in range(4):
		with open("zip" + str(x+1) + ".thomsonzippart", "rb") as f:
			bytes += f.read()
			
	
	with open("reconstruct.zip", "wb") as f:
		f.write(bytes)
	
	
	
reconstruct()