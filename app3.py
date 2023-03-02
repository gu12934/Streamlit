# Core Pkgs
import streamlit as st 
import pandas as pd
from datetime import datetime

# DB Mgmt
import sqlite3 
conn = sqlite3.connect('database.sqlite')
c = conn.cursor()


# Fxn Make Execution
def sql_executor(raw_code):
	c.execute(raw_code)
	data = c.fetchall()
	return data 


Country=['id,','name']
League=['id','country_id','name']
Player=['id', 'player_name', 'birthday','height','weight']




#city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
#country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
#countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']




def main():
	st.title("SQLPlayground")

	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("HomePage")

		# Columns/Layout
		col1,col2 = st.columns(2)

		with col1:
			with st.form(key='query_form'):
				raw_code = st.text_area("SQL Code Here")
				submit_code = st.form_submit_button("Execute")

			# Table of Info

			with st.expander("Table Info"):
				table_info={'League':League,'Country':Country,'Player':Player}
				#table_info = {'city':city,'country':country,'countrylanguage':countrylanguage}
				st.json(table_info)
			
		# Results Layouts
		with col2:
			if submit_code:
				st.info("Query Submitted")
				st.code(raw_code)

				# Results 
				query_results = sql_executor(raw_code)
				with st.expander("Results"):
					st.write(query_results)

				with st.expander("Pretty Table"):
					query_df = pd.DataFrame(query_results)
					st.dataframe(query_df)


	else:
		st.subheader("About")


filters = {"time_bucket": "Daily",
           "start_date": datetime(2021, 9, 1),
           "end_date": datetime(2021, 10, 12),
           "collection_one": "",
           "collection_two": ""}

collections_info = None

with st.sidebar:
    # display filters
    min_date = datetime(2021, 1, 1)
    max_date = datetime(2021, 10, 12)
    filters["time_bucket"] = st.selectbox("Time bucket:", ["Daily", "Weekly"], 0)
    filters["start_date"] = st.date_input("Start date: ", value=filters["start_date"], min_value=min_date, max_value=max_date)
    filters["end_date"] = st.date_input("End date: ", value=filters["end_date"], min_value=min_date, max_value=max_date)
    #collections_options = db.list_popular_collections(filters=filters)
    #filters["collection_one"] = st.selectbox("Collection:", collections_options, 0)
    #filters["collection_two"] = st.selectbox("compare to", collections_options, 1)
    
    # display collection images in the correct order
    #collections_info = db.collection_info(filters=filters)
    swap = None
    # if collections_info[0][7] != filters["collection_one"]:
    #     swap = collections_info[0]
    #     collections_info[0] = collections_info[1]
    #     collections_info[1] = swap
    
    # st.image(collections_info[0][2])
    # if len(collections_info) > 1:
    #     st.image(collections_info[1][2])


if __name__ == '__main__':
	main()