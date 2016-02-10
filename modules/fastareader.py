class FastaReader:
	def __init__(self, filename):
		self.filename = filename
	def read_fasta(self):
		f = open(self.filename)
		lines = f.readlines()
		
		fasta = []
		header = str()
		seq = str()
		for l in lines:
			if l[0] == '>':
				if len(header) != 0:
					fasta.append((header, seq))
					header = l.strip()[1:]
					header = header[0:header.index(' ')]
					seq = str()
				else:
					header = l.strip()[1:]
					header = header[0:header.index(' ')]
			elif len(header) != 0:
				seq += l.strip()
		fasta.append((header, seq))	

		return	fasta
