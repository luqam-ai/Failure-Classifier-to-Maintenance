import pickle
import streamlit as st
import pandas as pd
import analysis

def main():
        
    # Page title
    st.title('Pognozowanie awarii w maszynach')
    st.image('images/maintenance.jpg')
    st.write("\n\n")

    st.markdown(
        """
        Ta aplikacja ma na celu pomóc w klasyfikowaniu awarii, zmniejszając tym samym czas potrzebny na analizę problemów maszynowych. Umożliwia analizę danych z czujników w celu szybkiej klasyfikacji awarii i przyspieszenia procesu rozwiązywania problemów. Źródło aplikacji demo: [Failure-Classifier-to-Maintenance](https://github.com/thales-vignoli/Failure-Classifier-to-Maintenance).   
        """
    )

    # Load the model
    with open('model/model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Streamlit interface to input data
    col1, col2 = st.columns(2)

    with col1:
        air = st.number_input(label='Temperatura powietrza')
        process = st.number_input(label='Temperatura procesu')
        rpm = st.number_input(label='Prędkość obrotowa')

    with col2:
        torque = st.number_input(label='Moment obrotowy')
        tool_wear = st.number_input(label='Zużycie narzędzia')
        type = st.selectbox(label='Typ', options=['Low', 'Medium', 'High'])

# Function to predict the input
    def prediction(air, process, rpm, torque, tool_wear, type):
        # Create a df with input data
        df_input = pd.DataFrame({
            'Air_temperature': [air],
            'Process_temperature': [process],
            'Rotational_speed': [rpm],
            'Torque': [torque],
            'Tool_wear': [tool_wear],
            'Type': [type]
        })
    
        prediction = model.predict(df_input)
        return prediction

    # Botton to predict
    if st.button('Predict'):
        predict = prediction(air, process, rpm, torque, tool_wear, type)
        st.success(predict)


# Sidebar navigation
def sidebar_navigation():
    
    # Add options for subpages
    selected_page = st.sidebar.radio("Wybierz zakres:", ("Analiza danych", "Prognoza awarii"))
    
    # Display selected page content
    if selected_page == "Analiza danych":
        analysis.main()
    elif selected_page == "Prognoza awarii":
        main()

# Run the app
if __name__ == "__main__":
    st.set_page_config(
        page_title="Failure Classifier",
        page_icon="images/icone.png",
    )

    with st.sidebar:
        st.markdown("## Platforma do wizualizacji analizy danych i prognozy awarii")
        
    sidebar_navigation()
