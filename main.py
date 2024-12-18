import subprocess

def main():
    subprocess.run(['python', 'parser.py'])
    subprocess.run(['python', 'process.py'])
    subprocess.run(['python', 'buffer.py'])

if __name__ == "__main__":
    main()
