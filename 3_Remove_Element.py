def remove_element(l):
    while True:
        print('\nIf you want remove element base on index, press : 1 ')
        print('If you want remove element base on element, press : 2 ')
        print('If you want stop this process, press : 3\n')
        chose = int(input('Enter your Number : '))
        if chose == 1:
            index = int(input('Enter a index number : '))
            if index < len(l):
                l.pop(index)
                print(f"Successfully {index}th element is removed.")
            else:
                print('This index is out of range')
        elif chose == 2:
            element = int(input('Enter a element : '))
            if element in l:
                l.remove(element)
                print(f"Successfully removed : {element}.")
            else:
                print('This element is not found')
        elif chose == 3:
            print("After remove element this list is : ", l)
            break
        else:
            print('Please Enter a correct number!')



if __name__ == "__main__":
    l = list(map(int, input('Enter your list : ').split()))
    remove_element(l)