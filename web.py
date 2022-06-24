import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('D:\House\price_model', 'rb'))
#
def main():

    st.title("House Price Prediction")

    AreaIncome = st.number_input('Avg Area Income')
    AreaHouseAge=st.number_input('Avg Area House Age')
    Numberofrooms=st.number_input(' Number of Rooms')
    Numberofbedrooms=st.number_input('Number of Bedrooms')
    AreaPopulation=st.number_input('Area Population')

    features = [AreaIncome,AreaHouseAge,Numberofrooms,Numberofbedrooms,AreaPopulation]
# convert user inputs into an array fr the model
    int_features = [int(x) for x in features]
    final_features = [np.array(int_features)]

    if st.button('predict'):
         # when the submit button is
         prediction = loaded_model.predict(final_features)
         st.write(prediction)
                

if __name__ == '__main__':
    main()
    

