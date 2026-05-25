import hashlib

def double_consent(input_data):
    # Validate and authorize input data
    hashed_data = hashlib.sha256(input_data.encode()).hexdigest()
    return hashed_data

def main():
    input_data = "example_input"
    output_data = double_consent(input_data)
    print("Double Consent Output:", output_data)

if __name__ == "__main__":
    main()
