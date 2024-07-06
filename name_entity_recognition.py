import streamlit as st
import spacy
from spacy import displacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

def main():
    st.title("Named Entity Recognition (NER) App")

    st.write("Enter text to extract named entities:")

    # Text input from user
    user_input = st.text_area("Text input", height=200)

    if st.button("Analyze"):
        if user_input:
            # Process the input text with spaCy
            doc = nlp(user_input)

            # Extract entities and display them
            entities = [(ent.text, ent.label_) for ent in doc.ents]

            st.write("Entities found:")
            for entity in entities:
                st.write(f"{entity[0]} ({entity[1]})")

            # Visualize the entities
            html = displacy.render(doc, style="ent", jupyter=False)
            st.markdown(html, unsafe_allow_html=True)
        else:
            st.write("Please enter some text for analysis.")

if __name__ == "__main__":
    main()
