import os
import sys

def test_hello_txt_exists():
    assert os.path.exists('hello.txt'), "hello.txt does not exist"

def test_hello_txt_content():
    with open('hello.txt', 'r') as f:
        content = f.read()
        assert content.strip() == 'Hello Danube', "hello.txt content is incorrect"

def main():
    try:
        test_hello_txt_exists()
        test_hello_txt_content()
        sys.exit(0)
    except AssertionError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()