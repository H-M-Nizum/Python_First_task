def access_value(key):
    if key in my_dict:
        value = my_dict[key]
        print(f"The value corresponding to the key '{key}' is: {value}")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")

if __name__ == "__main__":
    my_dict = {'name':'H.M. Nizum', 'age':23, 'address':'Mymensingh, Bangladesh', 'email':'hmnizum1714032@gmail.com', 'phone':'+8801981251861', 'education':'Computer Science and Engineering at Islamic Universit'}
    key = input("Enter a key for access a value from a dictionary : ")
    access_value(key.lower())


