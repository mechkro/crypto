from hashlib import sha256
import time

max_nonce = 100000000	#Setting range limit for guessing the hash
genesis_hash = "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048"  #First block satoshi - 5o btc award
block_number = 1

sample_transactions = """
Al --> Tony = Dixon Hatebreed shirt
Tony --> Al = Truball release
"""

report_string = ""

#---------------------------------------
def SHA256(text):
	""" 
	
	"""

	return sha256(text.encode("ascii")).hexdigest()

#---------------------------------------
def mine(block_number, transactions, previous_hash, prefix_zeros):
	"""

	"""

	prefix_string = '0'*prefix_zeros  #Difficulty level (how many zeros does hash need to start with)
	for nonce in range(max_nonce):
		text = str(block_number) + transactions + previous_hash + str(nonce)
		new_hash = SHA256(text)
		if new_hash.startswith(prefix_string):
			print(f"Correct Nonce Found: {nonce}")
			return new_hash

	raise BaseException(f"Couldn't find correct hash after: {max_nonce} nonces")


block_stats = { '1': [],
				'2': [],
				'3': [],
				'4': [],
				'5': [],
				'6': []
			  }

runs = 4
levels = 6
block_stats2 = {}

#---------------------------------------
if __name__ == "__main__":
	for trialrun in range(runs):
		for i in range(levels):
			difficulty = i+1
			start = time.time()
			print(f"\nStarted Mining - Difficulty stage: {i+1}")
			new_hash = mine(block_number, sample_transactions, genesis_hash, difficulty)
			total_time = str(round((time.time()-start),4))
			print(f"End Mining. Mining time: {total_time} seconds")
			block_stats[f"{difficulty}"].append(total_time)
			print(f"Hash Length: {len(new_hash)} Hexadecimal chars.")
			print(f"New Hash: {new_hash}\n")
			block_number += 1

	for k,v in block_stats.items():
		block_avg = sum([float(i) for i in v])/runs
		print(f"Avg solve time: {block_avg}, for Difficulty: {k}")
