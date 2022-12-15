# Import de deux bibliothéque ; hashlib pour crypter les données et datetime pour enregistrer la date et l'heure de chaque transaction.
import hashlib
import datetime


# Création d'une classe ; Block qui prend en entrée les données de la transaction, l'horodatage de la transaction et le hash du bloc précédent.
# Cette classe contient une méthode pour crypter les données de la transaction utilisant l'algorithme de hachage SHA-256 



class Block:
    def __init__(self, data, timestamp, previous_hash):
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.get_hash()

    @staticmethod
    def get_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8') + self.timestamp.encode('utf-8') + self.previous_hash.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()



# Création d'une classe ; Blockchain qui contiendra la chaîne de blocs. 
# Cette classe contient une méthode pour ajouter des blocs à la chaîne et une méthode pour retourner la dernière entrée de la chaîne.


class Blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(Block("Genesis Block", datetime.datetime.now(), "0"))

    def add_block(self, data):
        self.chain.append(Block(data, datetime.datetime.now(), self.chain[-1].hash))

    def get_latest_block(self):
        return self.chain[-1]




# Création d'une instance de blockchain pour ajouter des blocs de données en utilisant les lignes de code suivantes.

blockchain = Blockchain()
blockchain.add_block("Premier bloc")
blockchain.add_block("Deuxième bloc")
blockchain.add_block("Troisième bloc")

print("Dernier bloc de la chaîne :")
print(blockchain.get_latest_block().data)