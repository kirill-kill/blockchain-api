from fastapi import FastAPI
from app.blockchain import Blockchain
import hashlib

app = FastAPI()
blockchain = Blockchain()

@app.get("/")
def root():
    return {"status": "OK"}

@app.get("/chain")
def get_chain():
    return blockchain.chain

@app.post("/document")
def add_document(doc: dict):
    doc_hash = hashlib.sha256(str(doc).encode()).hexdigest()
    block = blockchain.add_block({
        "type": "document",
        "hash": doc_hash,
        "meta": doc
    })
    return {"tx_hash": block["hash"], "doc_hash": doc_hash}
