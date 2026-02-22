import streamlit as st
from main import Bank  # This imports your class

# Initialize the bank object
obj = Bank()

st.title("🏦 Shimla Bank Management System")

menu = ["Create Account", "Deposit Money", "Withdraw Money", "View Details", "Delete Account"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create Account":
    st.subheader("Open New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    email = st.text_input("Email")
    pin = st.number_input("4-Digit PIN", min_value=0, max_value=9999)
    phone = st.text_input("Phone Number")

    if st.button("Register"):
        # Note: We simulate the logic here because your main.py uses input()
        info = {
            'name': name, 'age': int(age), 'email': email,
            'pin': int(pin), 'account': Bank.generate(),
            'balance': 0, 'phoneno.': int(phone)
        }
        Bank.data.append(info)
        Bank.update()
        st.success(f"Account Created! Your Account No: {info['account']}")

elif choice == "Deposit Money":
    st.subheader("Deposit")
    acc_no = st.text_input("Account Number")
    pin_no = st.number_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)
    
    if st.button("Deposit"):
        user = [i for i in Bank.data if i['account'] == acc_no and i['pin'] == pin_no]
        if user:
            user[0]['balance'] += amount
            Bank.update()
            st.success(f"Deposited ${amount}. New Balance: ${user[0]['balance']}")
        else:
            st.error("Invalid Account or PIN")

elif choice == "View Details":
    st.subheader("User Details")
    acc_no = st.text_input("Account Number")
    pin_no = st.number_input("PIN", type="password")
    
    if st.button("Show"):
        user = [i for i in Bank.data if i['account'] == acc_no and i['pin'] == pin_no]
        if user:
            st.write(user[0])
        else:
            st.error("User not found")