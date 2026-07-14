#file=open('example.txt','r')
#data=file.read()
#print(data)
#file.close()

def read_file(filename):
    try:
        file=open(filename,'r')
        data=file.read()
        print(data)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'file' in locals():
            file.close()

readfilename=input("Enter the filename to read: ")
read_file(readfilename)


