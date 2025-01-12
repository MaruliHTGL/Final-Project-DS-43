import streamlit as st
from ml_app import run_ml_app

def main():
    menu = ['Home', 'Fake News Prediction']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.markdown(
            """
            <h1 style='text-align: center;'>Beware of Fake News: Stay Informed, Stay Safe</h1>
            <p>
                In this digital era, the rapid spread of information is both a blessing and a challenge.
                While it allows us to stay connected and informed, it also opens the door for the dissemination of 
                <strong>fake news</strong>—false or misleading information presented as fact.
            </p>
            <p>We urge you to stay vigilant and take these precautions to combat the spread of fake news:</p>
            <ul>
                <li><strong>Verify Sources:</strong> Always ensure the information comes from a credible and reliable source. Look for established news organizations and official statements.</li>
                <li><strong>Cross-Check Facts:</strong> Compare information with multiple trusted sources to confirm its accuracy.</li>
                <li><strong>Beware of Sensational Headlines:</strong> Fake news often uses shocking or exaggerated headlines to grab attention. Be skeptical of such content.</li>
                <li><strong>Think Before Sharing:</strong> Sharing unverified news can contribute to misinformation. Always check the validity of the information before forwarding it.</li>
                <li><strong>Educate Yourself and Others:</strong> Encourage friends and family to be critical of the news they consume and share.</li>
            </ul>
            <p>
                Fake news can cause unnecessary panic, harm reputations, and divide communities. Together, we can stop its spread 
                by being more discerning and responsible with the information we consume and share.
            </p>
            <p style='text-align: center;'><strong>Stay informed. Stay safe.</strong></p>
            """, 
            unsafe_allow_html=True
        )

    elif choice == "Fake News Prediction":
        run_ml_app()

if __name__ == '__main__':
    main()
