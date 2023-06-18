import streamlit as st
from send_email import send_email
st.header("Contact Me")

with st.form(key="email_forms"):#key is necessary by syntax
    user_email = st.text_input("Your email address")
    message_Subject = st.text_input("Subject")
    raw_message = st.text_area("Your message")
    message=f"""\
Subject: {message_Subject} from {user_email}

From: {user_email}
{raw_message}"""

    # note the above indentation and format should be copy to copy maashi to masshi for it to work
    button = st.form_submit_button("Send")
    if button:
        send_email(message)
        st.info("Your Email was sent successfully")

