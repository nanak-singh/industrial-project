import streamlit as st
import hashlib
import random
import re


def encrypt(a):
    result = ""
    s = 4
    for i in range(len(a)):
        char = a[i]
        #uppercase , lowercase , digits
        #uppercase 
        # A -> 65 -> 69 -> E
        if char.isupper():
            result += chr((ord(char)+ s -65) %26 +65)
        #lowercase
        elif char.islower():
            result += chr((ord(char)+ s -97) %26 +97)
        elif char.isdigit():
            x = int(char)
            y = x + s
            result += str(y)
        else:
            result += char
    return result

def main():

    title_html = """
    
        <style>

            .title h1 {
                text-align: center;
                font-size: 50px;
                color: blue;
            }

        </style>

        <div class="title">
            <h1><i>Industrial Training Project</i></h1>
        </div>

    """

    st.markdown(title_html, unsafe_allow_html=True) 
    #st.title("Industrial Training Project")

    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                content:'NANAK SINGH KHURANA | CSE-2 | 06613202718'; 
                visibility: visible;
                display: block;
                text-align: center;
                position: relative;
                color: black;
                #background-color: red;
                font-size: 20px;
                padding: 5px;
                padding-tip: -50px;
                top: 2px;
            }

            </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


    FiveLayerHashing = """
    
        <style>

            .title h3 {
                text-align: center;
                font-size: 35px;
                color: red;

            }

        </style>

        <div class="title">
            <h3><i>5 Layer Hashing</i></h3>
        </div>

    """
    st.markdown(FiveLayerHashing, unsafe_allow_html=True) 
    #st.title("5 Layer Hashing")
    mystring = st.text_input("Enter Text to Hash")
    if st.button("HASH"):
        mystring = mystring + '@akj51A$'
        hash_obj = hashlib.md5(mystring.encode())
        a = hash_obj.hexdigest()
        a = a[::-1]
        a = encrypt(a)        
        hash_obj1 = hashlib.sha1(a.encode())
        b = hash_obj1.hexdigest()
        hash_obj2 = hashlib.md5(b.encode())
        b = hash_obj2.hexdigest()
        st.success(b)
    
    PassGen = """
        <div class="title">
            <h3><i>Password Generator</i></h3>
        </div>
    """
    st.markdown(PassGen, unsafe_allow_html=True) 
    #st.title("Password Generator")

    #st.markdown("HOW MANY LETTERS WOULD YOU LIKE IN YOUR PASSWORD?")
    nr_letters = st.number_input("HOW MANY LETTERS WOULD YOU LIKE IN YOUR PASSWORD?", min_value=4, step=1)
    #st.markdown("HOW MANY SYMBOLS WOULD YOU LIKE?")
    nr_symbols = st.number_input("HOW MANY SYMBOLS WOULD YOU LIKE?", min_value=1, step=1)
    #st.markdown("HOW MANY NUMBERS WOULD YOU LIKE?")
    nr_numbers = st.number_input("HOW MANY NUMBERS WOULD YOU LIKE?", min_value=3, step=1)

    if st.button("GENERATE"):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        
        #total = nr_letters + nr_symbols + nr_numbers

        password_list = []
        password = ''
        for number in range (0,nr_letters):
            password_list.append(random.choice(letters))
        for number in range (0,nr_symbols):
            password_list.append(random.choice(symbols))
        for number in range (0,nr_numbers):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)

        for item in password_list:
            password += item
        
        st.success(f'Your new lucky password is {password}')
        


    PassChecker = """
        <div class="title">
            <h3><i>Check Your Password Strength</i></h3>
        </div>
    """
    st.markdown(PassChecker, unsafe_allow_html=True) 

    #st.title("Check Your Password Strength")

    a = st.text_input("Enter your password")
    if st.button("CHECK"):

        # the password should not be a 
        # newline or space 
        if a == "\n" or a == " ": 
            st.markdown("Password cannot be a newline or space!")

        elif 9 <= len(a) <= 20: 
   
            # checks for occurrence of a character  
            # three or more times in a row 
            if re.search(r'(.)\1\1', a): 
                st.error("Weak Password: Same character repeats three or more times in a row")
            
            # checks for occurrence of same string  
            # pattern( minimum of two character length) 
            # repeating 
            elif re.search(r'(..)(.*?)\1', a): 
                st.error("Weak password: Same string pattern repetition")
    
            else: 
                st.success("Strong Password!")
    
        else: 
            st.error("Password length must be 9-20 characters!")

    #st.markdown("Nanak Singh Khurana")
    #st.markdown("CSE-2")
    #st.markdown("06613202718")
    




if __name__ == '__main__':
    main()
