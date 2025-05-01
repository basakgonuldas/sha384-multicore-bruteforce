# SHA-384 Brute Force Cracker

This project is a simple Python script designed to brute-force a given SHA-384 hash by trying every possible 5-character combination using lowercase letters and digits. It leverages Python's `multiprocessing` module to speed up the cracking process by utilizing multiple CPU cores.

## Features

- **Parallel Processing:** Uses `multiprocessing.Pool` for efficient multi-core utilization.
- **Character Set:** Lowercase letters (`a-z`) and digits (`0-9`).
- **Hash Algorithm:** SHA-384
- **5-Character Combinations:** Tries every possible 5-character string.

## Requirements

- Python 3.x (version 3.7 or higher recommended)

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/sha384-bruteforce.git
    cd sha384-bruteforce
    ```

2. **Run the script:**
    ```bash
    python3 brute_force.py
    ```

### Output

If the correct message is found, the script will print something like: abc12



## How It Works

- The script generates all possible 5-character combinations from the defined `alphabet`.
- It computes the SHA-384 hash of each combination.
- It compares the computed hash with the target hash.
- When a match is found, it prints the matching string.

## Important Notes

- This script currently brute-forces 5-character strings, resulting in **36^5 (60,466,176)** combinations.
- Increasing the character set or string length will **exponentially** increase the runtime.
- This script is intended for **educational and ethical** use only.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you'd like to improve this project.



