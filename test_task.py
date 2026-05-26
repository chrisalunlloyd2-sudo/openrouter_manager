import os

def test_hello_txt_exists():
    assert os.path.exists('hello.txt') == True

def test_hello_txt_content():
    with open('hello.txt', 'r') as file:
        content = file.read()
    assert content.strip() == 'Hello Danube'

def main():
    test_hello_txt_exists()
    test_hello_txt_content()
    exit(0)

if __name__ == "__main__":
    main()