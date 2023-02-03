import os

def DeleteFile(FileName):
    if(os.path.exists(FileName)):
        os.remove(FileName)
    
    else:
        print("File is not existing")
        return

def main():
    print("Enter the file name to create")
    Name = input()

    DeleteFile(Name)

if __name__ == "__main__":
    main()