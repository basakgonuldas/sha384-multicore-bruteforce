import hashlib
import itertools
import multiprocessing

alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"
target_hash = "b3035c12c4741d6794d9e127d773fcd6e830cd4fe040dfa18657b1a4e2d3cb450790e34e54f2ee23374b47151bec4e7b"

def brute_force_worker(prefix):
    for combo in itertools.product(alphabet, repeat=5 - len(prefix)):
        guess = prefix + ''.join(combo)
        hashed = hashlib.sha384(guess.encode()).hexdigest()
        if hashed == target_hash:
            print(f"Found! Message {guess}")
            return True
    return False

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        prefixes = [c for c in alphabet]  
        results = pool.map(brute_force_worker, prefixes)
