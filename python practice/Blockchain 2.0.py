zeros = 4
class votechoice:
    def __init__(self,voterId,candidate):
        self.voterId = voterId
        self.candidate = candidate
        self.time = time.strftime('%d/%m/%Y - %H:%M:%S')
        self.voteobject = {'Voter_ID':self.voterId,'Candidate_Name':self.candidate,'Time':self.time}
        Blockchain.votepool.append(self.voteobject)

class Blockchain:
    votepool = []
    chain = []

class Block:
    def __init__(self):
        self.merkleRoot = calculateMerkleRoot()
        self.difficulty = zeros
        self.timestamp = time.strftime('%d/%m/%Y - %H:%M:%S')
        self.nonce = pow()
        self.prevhash = Blockchain.chain[len(Blockchain.chain)-1].hash
        self.hash = calchash()



