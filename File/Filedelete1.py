import os

def DeleteFile(FileName):
    if(os.path.exists(FileName)):
        size=os.path.getsize(FileName)
        if (size==0):
            os.remove(FileName)
        else:
            print("Are you sure to delete the file ? Y/N")
            option=input()
            if(option=="Y"or option=="Y"):
                os.remove(FileName)
            else:
                print("File deletion process stoped . ")        
    
    else:
        print("File is not existing")
        return

def main():
    print("Enter the file name to create")
    Name = input()

    DeleteFile(Name)

if __name__ == "__main__":
    main()