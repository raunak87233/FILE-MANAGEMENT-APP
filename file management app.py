import os


def create_file(filename):
    try:
        with open('filename', 'x') as f:
            print(f"File Name:{filename}: Created Successfully!")
    except FileExistsError:
        print(f"File Name:{filename} Already Exists!")
    except Exception as E:
        print('An error Occured!')
        
def view_all_files():
    files = os.listdir()
    if not files:
        print('No Files Found!')
    else:
        print('Files in Directory!')
        for file in files:
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully')
    except FileNotFoundError:
        print('File Not Found')
    except Exception as e:
        print('An Occured Error')
            
def read_file(filename):
    try:
        with open('sample.txt', 'r') as f:
            content = f.read()
            print(f"Content of '{filename}' :\n(content)")
    except FileNotFoundError:
        print('File Not Found!')
    except Exception as e:
        print('An error Occurred!')
            
def edit_file(filename):
    try:
        with open('sample.txt', 'a') as f:
            content = input("Enter data to add = ")
            f.write(content +"\n")
            print('Content added to {filename} Successfully')
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
    except Exception as e:
        print('An error Occurred!')
            
            
def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: Create a file')
        print('2: View all files')
        print('3: Delete a file')
        print('4: Read a file')
        print('5: Edit a file')
        print('6: Exit')
        
        choice = input('Enter Your Choice :')
        if choice == '1':
            filename = input("Enter the File-Name to Create = ")
            create_file(filename)
        elif choice == 2:
            view_all_files()
        elif choice == '3':
            filename = input("Enter the File-Name to Delete = ")
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter the File-Name to Read = ")
            read_file(filename)
        elif choice == '5':
            filename = input("Enter the File-Name to Edit = ")
            edit_file(filename)
        elif choice == '6':
            print('Closing the App...........')
        else:
            print('Invalid Syntax!')
            
            
if __name__ == "__main__":
    main()
            
            
        
            
             
