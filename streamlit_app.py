import streamlit as st

# Wedding details
bride_name = "Alice"
groom_name = "Bob"
invitation_text = "You're invited to our wedding!"
photo_bride = "bride.jpg"  # Path to bride's photo
photo_groom = "groom.jpg"  # Path to groom's photo

# Display content
st.title(f"{bride_name} & {groom_name}'s Wedding")
st.markdown(invitation_text)
st.image(photo_bride, caption=f"{bride_name}", use_column_width=True)
st.image(photo_groom, caption=f"{groom_name}", use_column_width=True)
