import streamlit as st
import cohere

# Initialisation du client Cohere avec la clé API
cohere_api_key = st.secrets["COHERE_API_KEY"]
if not cohere_api_key:
    st.error("La clé API Cohere n'est pas définie dans les secrets.")
    st.stop()

co = cohere.Client(cohere_api_key)

# Fonction pour transformer une phrase méchante en une version gentille et fun
def transformer_phrase_mechante(phrase):
    prompt = (
        "Tu es un assistant créatif et drôle dont la mission est de transformer les phrases méchantes en versions gentilles, "
        "positives et amusantes. Tu reformules les phrases de manière bienveillante, avec humour léger et empathie. "
        "Voici un exemple :\n\n"
        "Phrase méchante : Tu es trop nul, tu n’arriveras jamais à rien !\n"
        "Phrase gentille et fun : Tu es encore en chemin vers ton succès, et chaque pas te rend plus fort ! 🚀😄\n\n"
        f"Phrase méchante : {phrase}\n"
        "Phrase gentille et fun :"
    )

    try:
        response = co.chat(
            model="command-r-plus",
            message=prompt,
            max_tokens=150,
            temperature=0.9
        )
        return response.text.strip()
    except Exception as e:
        return f"Erreur lors de la transformation : {e}"

# Interface Streamlit
st.markdown("<h3 style='text-align: right; font-size: 14px;'>Hadrien Poinseaux</h3>", unsafe_allow_html=True)

# Couleur de fond
page_bg_img = '''
<style>
[data-testid="stMain"] {
background-color: #d63384;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Titre et introduction
st.title("Transformateur de phrases méchantes 😈➡️😇")

st.markdown("""
Bienvenue ! Tape une phrase méchante ou désagréable, et je vais la transformer en une version gentille, fun et bienveillante ✨  
Parfait pour détendre l’atmosphère ou s’entraîner à la communication positive ! 🧡
""")


# Entrée utilisateur
phrase_mechante = st.text_input("Entre une phrase méchante :")

if st.button("Transformer 💫"):
    if phrase_mechante:
        phrase_transformee = transformer_phrase_mechante(phrase_mechante)
        st.write(f"😈 **Phrase méchante :** {phrase_mechante}")
        st.write(f"😇 **Phrase transformée :** {phrase_transformee}")


