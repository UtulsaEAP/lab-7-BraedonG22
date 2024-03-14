def fileNameChange():
    input_file = input()
    try:
        with open(input_file, 'r') as file:
            file_names = file.readlines()
            for name in file_names:
                modified_name = name.strip().replace('_photo.jpg', '_info.txt')
                print(modified_name)
    except FileNotFoundError:
        print("File not found.")
    return

if __name__ == '__main__':
    fileNameChange()