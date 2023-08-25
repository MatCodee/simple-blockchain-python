from asyncio import run_coroutine_threadsafe
from urllib import response
from flask import Flask,jsonify

# global files
from blockchain import Blockchain

blockchain = Blockchain()

app = Flask(__name__)

@app.route('/mine_block',methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.get_hash(previous_block )
    block = blockchain.create_block(proof,previous_hash)
    response = {
        'message': "Nuevp bloque minado!",
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response,200)


@app.route('/get_chain',methods=['GET'])
def get_chain():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return jsonify(response)
    

@app.route('/is_valid',methods=['GET'])
def is_valid():
    if blockchain.is_chain_valid(blockchain.chain):
        return jsonify({"message": "Blockchain sin errores"})
    else:
        return jsonify({"message": "Error en la blockchain"})
