
import streamlit as st # Streamlit for deployment
import pandas as pd # Pandas for data processing and manipulation
import numpy as np # Numpy for data preprocessing and manipulation
import pypickle # To download and manage machine learning model
from sklearn import preprocessing

loaded_model = pypickle.load('model.pkl') # Load model using pickle

def prediction(data):

     df = pd.DataFrame(data)
     df.iloc[2].replace({"D 3-6 month": 3, "E 6-9 month": 6, "K > 24 month": 24,
                        "I 18-21 month": 18, "H 15-18 month": 15, "G 12-15 month": 12,
                        "J 21-24 month": 21, "F 9-12 month": 9}, inplace=True)



     label = preprocessing.LabelEncoder()

     df.iloc[1] = label.fit_transform(df.iloc[1])
     df.iloc[16] = label.fit_transform(df.iloc[16])

     num_data = df.drop([0, 14]).values.reshape(1, -1)

     pred = loaded_model.predict(num_data)

     if pred[0] == 0 :
          return "Customer is not going, but staying with Expresso"
     else:
          return "The Customer will leave Expresso"
     

def main():
     
     st.title("Expresso Telecommunication Predictive Model")
     user_id = st.text_input("User Identification")
     REGION = st.text_input("What is the location of the client")
     TENURE = st.text_input("What is the duration in the network")
     MONTANT = st.number_input("What is the top-up amount spent by the client")
     FREQUENCE_RECH = st.number_input("What is the  number of times the customer refilled")
     REVENUE = st.number_input("What is the monthly income of each client")
     ARPU_SEGMENT = st.number_input("What is the income over 90 days / 3")
     FREQUENCE = st.number_input("What is the number of times the client has made an income")
     DATA_VOLUME = st.number_input("What is the number of connections")
     ON_NET = st.number_input("What is the inter expresso call")
     ORANGE = st.number_input("What is the call to orange")
     TIGO = st.number_input("What is the call to tigo")
     ZONE1 = st.number_input("What is the call to zone 1")
     ZONE2 = st.number_input("What is the call to call to zone 2")
     MRG = st.text_input("What is the client going")
     REGULARITY = st.number_input("What is the number of times the client is active for 90 days")
     TOP_PACK = st.text_input("What is the most active packs")
     FREQ_TOP_PACK = st.number_input("What is the number of times the client has activated the top pack packages")

     Churn = " "


     if st.button("Result"):
          Churn = prediction([user_id, REGION, TENURE, MONTANT, FREQUENCE_RECH, REVENUE,
       ARPU_SEGMENT, FREQUENCE, DATA_VOLUME, ON_NET, ORANGE, TIGO,
       ZONE1, ZONE2, MRG, REGULARITY, TOP_PACK, FREQ_TOP_PACK])
          

     st.success(Churn)


if __name__ == "__main__":
     main()




