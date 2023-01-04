import argparse
import os
import sys

def embed(input_js_file, payload_file):
    """Embed the payload file in the input JavaScript file using XOR encryption.

    Args:
        input_js_file (str): The path to the input JavaScript file.
        payload_file (str): The path to the payload file.
    """
    try:
        # read the input JavaScript file
        with open(input_js_file, "r") as f:
            input_js = f.read()

        # read the payload file
        with open(payload_file, "rb") as f:
            payload = f.read()

        # generate a random key for the XOR encryption
        key = os.urandom(len(payload))

        # XOR the payload with the key
        encoded_payload = bytes([p ^ k for p, k in zip(payload, key)])

        # encode the key and encoded payload as hexadecimal strings
        key_hex = key.hex()
        encoded_payload_hex = encoded_payload.hex()
        
        # modify the input JavaScript to include the encoded payload and key
        output_js = input_js + "\n" + f"const k = '{key_hex}'; const encoded_payload = '{encoded_payload_hex}';"

        # write the modified JavaScript to the input file
        with open(input_js_file, "w") as f:
            f.write(output_js)

        print("Embedding successful!")
    except Exception as e:
    	print(f"Error: {e}")
		
if __name__ == "__main__":
	# parse the command-line arguments
	parser = argparse.ArgumentParser(description="Embed a payload file in a JavaScript file using XOR encryption.")
	parser.add_argument("input_js_file", help="The path to the input JavaScript file.")
	parser.add_argument("payload_file", help="The path to the payload file.")
	args = parser.parse_args()
	
	# embed the payload in the input JavaScript file
	embed(args.input_js_file, args.payload_file)
