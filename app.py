import streamlit as st
import folium
import json
import pandas as pd
from streamlit_folium import folium_static
import requests
import branca
st.set_page_config(layout ="wide")
st.title('Visa policy of Turkey')
GEOJSON_URL='https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'
response=requests.get(GEOJSON_URL)
geojson=response.json()
with open('country.geojson') as json_file:
    geojson= json.load(json_file)
with open('my_dict.txt') as json_file:
    my_dict= json.load(json_file)

df=pd.read_csv('df_visa.csv')
list_countries=['World']
list_countries.extend(df['Country'].to_list())
print(list_countries)

selected_country = st.sidebar.selectbox("Select Country",list_countries )
try:
    st.sidebar.title(selected_country)
    for i in my_dict[selected_country]:
        st.sidebar.write(i)

except:
    st.write('''The visa policy of Turkey deals with the requirements which a foreign national wishing to enter Turkey must meet to be permitted to travel to, enter and remain in the country.

Visitors to Turkey must obtain a visa from one of the Turkish diplomatic missions unless they come from one of the 78 visa-exempt countries and territories or one of the 42 countries and territories whose citizens are eligible to apply for an e-Visa online. Turkish visas are documents issued by the Ministry of Foreign Affairs and its subsequent diplomatic missions abroad with the stated goal of regulating and facilitating migratory flows.

Visitors of most nationalities must hold a passport valid for no less than 150 days from the date of arrival. The passport validity requirement does not apply to citizens of Belgium, France, Luxembourg, Portugal, Spain and Switzerland who can enter with a passport expired for less than five years, citizens of Germany who can enter with a passport or an ID card expired for less than one year, citizens of Bulgaria who are only required to have a passport valid for their period of stay.[4] An identity card is accepted in lieu of a passport for citizens of Azerbaijan, Belgium, France, Georgia, Germany, Greece, Italy, Liechtenstein, Luxembourg, Malta, Moldova, Netherlands, Northern Cyprus, Portugal, Spain, Switzerland and Ukraine. The validity period requirement also does not apply to nationals of countries whose identity cards are accepted.

Even though Turkey is a candidate country for membership of the European Union, it has a more complex visa policy than the visa policy of the Schengen Area.[2] Turkey requires visas from citizens of one EU member state Cyprus, as well as Schengen Annex II countries and territories – Antigua and Barbuda, Australia, Bahamas, Barbados, Canada, Dominica, East Timor, Grenada, Kiribati, Marshall Islands, Mauritius, Mexico, Micronesia, Palau, Saint Lucia, Saint Vincent and the Grenadines, Samoa, Solomon Islands, Taiwan, Tonga, Tuvalu, United Arab Emirates, United States, and Vanuatu. On the other hand, Turkey grants visa-free access to citizens of other countries and territories – Azerbaijan, Belarus, Belize, Bolivia, Ecuador, Iran, Kosovo, Kyrgyzstan, Jordan, Lebanon, Mongolia, Morocco, Qatar, Russia, Tajikistan, Thailand, Tunisia, Turkmenistan and Uzbekistan.

The Turkish government announced that effective from 2 March 2020, visas are not required for passport holders from the following countries: Austria, Belgium, Croatia, Republic of Ireland, Malta, Netherlands, Norway, Poland, Portugal, Spain and the United Kingdom.''')





if selected_country=='World':
    m = folium.Map(location=[38.963745, 35.243322],
                   zoom_start=2)
else:
    countrys_cent=pd.read_csv('countrys_cent.csv')
    df_cent=countrys_cent[countrys_cent['name']==selected_country]
    latitude=df_cent['latitude'].to_list()[0]
    longitude=df_cent['longitude'].to_list()[0]
    m = folium.Map(location=[latitude,longitude],
                   zoom_start=6)


folium.Choropleth(
    geo_data=geojson,

    data=df,
    columns=['Country',"Visa_Free"],
    key_on="feature.properties.name",
    fill_color='RdYlGn',
    fill_opacity=0.5,
    #line_opacity=.2,
    legend_name=selected_country,

).add_to(m)





folium_static(m, width=800, height=450)
st.image('visa.png')
