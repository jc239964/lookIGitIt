def new(numBuckets=256):
	"""Initializes a Map with the given number of buckets."""
	aMap = []
	for i in range(0, numBuckets):
		aMap.append([])
	return aMap

def hashKey(aMap, key):
	"""Given a key this will create a number and then convert it to an index for the aMap's buckets"""
	return hash(key) % len(aMap)

def getBucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucketID = hashKey(aMap, key)
	return aMap[bucketID]

def getSlot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = getBucket(aMap, key)

	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v

	return -1, key, default

def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = getSlot(aMap, key, default=default)
	return v

def set(aMap, key, value): 
	"""Sets the key to the value, replacing any existing value"""
	bucket = getBucket(aMap, key)
	i, k, v = getSlot(aMap, key)
	
	if i >= 0:
		# the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not exist, append to create it
		bucket.append((key, value))

def delete(aMap, key): 
	"""Deletes the given key from the map"""
	bucket = getBucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break

def list(aMap):
	"""Prints out what is in map"""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
	
