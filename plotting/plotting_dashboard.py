#data visualization app - https://www.youtube.com/watch?v=w2PwerViVbA 

#importing libraries
import streamlit as st
import plotly_express as px
import pandas as pd
from PIL import Image
import seaborn as sns
import plotly.figure_factory as ff

#title of the app
st.title("Data Visualization App")

#add a sidebar
st.sidebar.subheader("Visualization Settings")


# Setup file upload
uploaded_file= st.sidebar.file_uploader(label="Upload your CSV or Excel file.", type=['csv','xlsx'])

#uploading files to the streamlit app
global df
if uploaded_file is not None:
    print(uploaded_file)
    print('hello')
    try:
        df= pd.read_csv(uploaded_file)
    
    except Exception as e:
        print(e)
        df= pd.read_excel(uploaded_file)

global numeric_columns
try:
    st.write(df)
    numeric_columns=list(df.select_dtypes(['float', 'int']).columns)

except Exception as e:
    print(e)
    st.write("Please upload file to the application.")

global categoric_columns
try:
    st.write(df)
    categoric_columns=list(df.select_dtypes(["bool","object"]).columns)
    
except Exception as e:
    print(e)
    st.write("Please upload file to the application.")



#add a select widget to the side bar
chart_select = st.sidebar.selectbox(
    label= "Select the chart type",
    options=['Scatterplots', 'Lineplots', 'Barplots', 'LinePlot', 'Histogram']
)

#main code where it lets you select x and y values
if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot Settings")
    try:
        x_values=st.sidebar.selectbox('X axis', options=numeric_columns)
        y_values=st.sidebar.selectbox('Y axis', options=numeric_columns)
        plot=px.scatter(data_frame=df, x=x_values, y=y_values)
        #display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)


# csv file to opem

#################################################################################another table
# import pandas as pd
# import json
# # Load JSON data
# with open('/home/ubuntu/cbs/test/streamlit_db/9-14-2022-12_8_15_output.json', 'r') as f:
#     data = json.load(f)
# # Extract relevant data into a list of dictionaries
# rows = []
# for batch in data:
#     for obj in batch['batches'][0]['objects']:
#         row = {
#             'object_id': obj['object_id'],
#             'frame_num': batch['batches'][0]['frame_num'],
#             'pose3d': obj['pose3d'],
#             'pose25d': obj['pose25d'],
#             'timestamp':batch['batches'][0]['ntp_timestamp']
#         }
#         rows.append(row)
# # Convert list of dictionaries to a pandas DataFrame
# df = pd.DataFrame(rows)
# id_filter=st.selectbox("Select the id", pd.unique(df['object_id']))

# st.write(df)
# #take id number and certain points

# take pose 3d data and plot function of plot

# display plot

# interactive menu to choose other ids

######################
#code that Huyue and i worked on together

# import numpy as np
# import plotly.graph_objs as go
# def plot_skeleton(raw_data):
#     # Reshape the raw data into an array with shape (34, 4)
#     data_with_confidence = raw_data.reshape(-1, 4)
#     # Extract the 3D coordinates (ignoring the confidence values)
#     coords = data_with_confidence[:, :3]
#     # Define the connections and joint names (as in the previous response)
#     connections = [
#     ("pelvis", "left_hip"),
#     ("pelvis", "right_hip"),
#     ("pelvis", "torso"),
#     ("left_hip", "left_knee"),
#     ("right_hip", "right_knee"),
#     ("torso", "neck"),
#     ("left_knee", "left_ankle"),
#     ("right_knee", "right_ankle"),
#     ("left_ankle", "left_big_toe"),
#     ("right_ankle", "right_big_toe"),
#     ("left_ankle", "left_small_toe"),
#     ("right_ankle", "right_small_toe"),
#     ("left_ankle", "left_heel"),
#     ("right_ankle", "right_heel"),
#     ("neck", "nose"),
#     ("nose", "left_eye"),
#     ("nose", "right_eye"),
#     ("left_eye", "left_ear"),
#     ("right_eye", "right_ear"),
#     ("neck", "left_shoulder"),
#     ("neck", "right_shoulder"),
#     ("left_shoulder", "left_elbow"),
#     ("right_shoulder", "right_elbow"),
#     ("left_elbow", "left_wrist"),
#     ("right_elbow", "right_wrist"),
#     ("left_wrist", "left_pinky_knuckle"),
#     ("right_wrist", "right_pinky_knuckle"),
#     ("left_wrist", "left_middle_tip"),
#     ("right_wrist", "right_middle_tip"),
#     ("left_wrist", "left_index_knuckle"),
#     ("right_wrist", "right_index_knuckle"),
#     ("left_wrist", "left_thumb_tip"),
#     ("right_wrist", "right_thumb_tip"),
# ]
# # Define the joint names
#     joint_names = [
#     "pelvis", "left_hip", "right_hip", "torso", "left_knee", "right_knee", "neck",
#     "left_ankle", "right_ankle", "left_big_toe", "right_big_toe", "left_small_toe",
#     "right_small_toe", "left_heel", "right_heel", "nose", "left_eye", "right_eye",
#     "left_ear", "right_ear", "left_shoulder", "right_shoulder", "left_elbow",
#     "right_elbow", "left_wrist", "right_wrist", "left_pinky_knuckle",
#     "right_pinky_knuckle", "left_middle_tip", "right_middle_tip", "left_index_knuckle",
#     "right_index_knuckle", "left_thumb_tip", "right_thumb_tip",
# ]
#     joint_idx = {name: i for i, name in enumerate(joint_names)}
#     scatter = go.Scatter3d(
#         x=coords[:, 0], y=coords[:, 1], z=coords[:, 2],
#         mode="markers",
#         marker=dict(size=4, color="red"),
#         text=joint_names,
#         hoverinfo="text",
#     )
#     lines = [
#         go.Scatter3d(
#             x=[coords[joint_idx[a], 0], coords[joint_idx[b], 0]],
#             y=[coords[joint_idx[a], 1], coords[joint_idx[b], 1]],
#             z=[coords[joint_idx[a], 2], coords[joint_idx[b], 2]],
#             mode="lines",
#             line=dict(color="blue", width=4),
#             hoverinfo="none",
#         )
#         for a, b in connections
#     ]
#     data = [scatter] + lines
#     layout = go.Layout(
#         scene=dict(
#             xaxis=dict(title="X"),
#             yaxis=dict(title="Y"),
#             zaxis=dict(title="Z"),
#         ),
#         margin=dict(l=0, r=0, t=0, b=0),
#         showlegend=False,
#     )
#     fig = go.Figure(data=data, layout=layout)
#     fig.show()

# #puts in a seperate tab
# raw_data = np.array([191.603210, 265.205933, 3153.333984, 0.731934, 230.486237, 277.560089, 3108.027344, 0.676270, 133.807739, 268.066620, 3192.440918, 0.699219, 187.246750, -3.937817, 3112.998291, 0.835449, 237.136551, 507.366608, 3202.865967, 0.578125, 125.456978, 516.513367, 3263.148193, 0.790039, 184.355011, -281.874695, 3081.331787, 0.815918, 258.972626, 520.126953, 3300.819824, 0.700684, 149.763992, 540.506348, 3383.201660, 0.840332, 271.128113, 532.641296, 3294.507080, 0.743652, 152.609528, 548.237183, 3392.881104, 0.679688, 282.496155, 532.877747, 3293.842041, 0.703125, 149.100189, 549.752258, 3402.257568, 0.666016, 268.461029, 529.713501, 3328.909912, 0.764648, 162.968338, 548.356506, 3399.827637, 0.793457, 101.871178, -391.050812, 2998.252197, 0.930176, 163.101364, -434.765930, 2993.321533, 0.865723, 81.823166, -438.722717, 3026.144043, 0.943848, 233.926941, -424.069153, 3029.631836, 0.941406, 112.651436, -425.534393, 3084.423828, 0.786621, 306.142517, -217.735275, 3015.613281, 0.740234, 147.284149, -246.433868, 3191.779297, 0.742676, 351.638397, 106.466621, 2993.807617, 0.782715, 149.133316, 45.981018, 3248.995850, 0.672363, 327.813568, 371.529388, 2995.560791, 0.701172, 119.731201, 262.061523, 3318.486572, 0.666992, 338.453247, 421.623260, 2984.965820, 0.753906, 120.396957, 321.690826, 3350.444092, 0.700195, 321.071808, 443.661652, 2963.965820, 0.718750, 120.151443, 349.829651, 3338.312744, 0.739746, 311.520111, 418.243011, 2973.464111, 0.736816, 108.414734, 319.069763, 3331.515137, 0.695801, 300.618347, 429.052643, 2971.887207, 0.722168, 111.805054, 329.794159, 3325.039062, 0.748535])
# plot_skeleton(raw_data)
#this code above graphs the image in 3d pose into a seperate tab

##################################################

#opening the image

# image = Image.open('imagefile')

# #displaying the image on streamlit app

# st.image(image, caption='Enter any caption here')


###########################################################################################
#code for pose estimation of joints
# import matplotlib.pyplot as plt

# y_axis=[327.337483727811, 322.324652774347, 331.087523824162, 345.582746154012, 366.906167536302, 291.059026808947, 383.444894921119, 239.974225110361, 321.630512423123, 304.111645697879, 335.760527177563, 323.179670200598, 352.498042928019, 265.187319290173, 330.030564548107, 364.216422463677, 374.523797034937, 395.097944323988, 365.7120246096, 406.429743720313, 389.930674812547, 366.023728240626, 364.880153046231, 331.634965635666, 450.127680664648, 300.767410955174, 438.699138086055, 313.362002790122, 415.700368774871, 276.282775707828, 441.191767348025, 279.77266773424, 410.964189258654, 257.807180374123]

# x_axis= ["pelvis", "left_hip", "right_hip", "torso", "left_knee", "right_knee", "neck",
#     "left_ankle", "right_ankle", "left_big_toe", "right_big_toe", "left_small_toe",
#     "right_small_toe", "left_heel", "right_heel", "nose", "left_eye", "right_eye",
#     "left_ear", "right_ear", "left_shoulder", "right_shoulder", "left_elbow",
#     "right_elbow", "left_wrist", "right_wrist", "left_pinky_knuckle",
#     "right_pinky_knuckle", "left_middle_tip", "right_middle_tip", "left_index_knuckle",
#     "right_index_knuckle", "left_thumb_tip", "right_thumb_tip"]

# plt.plot(x_axis, y_axis)
# plt.xticks(rotation=90)
# plt.xlabel("Joint Names")
# plt.ylabel("Data Points")
# plt.title("Line Graph of Data Points by Joint Names")
# plt.show()

# if chart_select == 'Scatterplot':
#     st.sidebar.subheader("Scatterplot Settings")
#     try:
#         # x_values=x_axis
#         # y_values=y_axis
#         x_values=st.sidebar.selectbox(x_axis, options=numeric_columns)
#         y_values=st.sidebar.selectbox(y_axis, options=numeric_columns)
#         plot=px.scatter(data_frame=df, x=x_values, y=y_values)
#         #display the chart
#         st.plotly_chart(plot)
#     except Exception as e:
#         print(e)
#bar plot code for streamlit
if chart_select == 'Barplots':
    st.sidebar.subheader("Barplot Settings")
    try:
        # x_values=x_axis
        # y_values=y_axis
        x_values=st.sidebar.selectbox("X_axis", options=numeric_columns)
        y_values=st.sidebar.selectbox("Y_axis", options=categoric_columns)
        plot=px.bar(data_frame=df, x=x_values, y=y_values)
        #display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)

# import pandas as pd
# import matplotlib.pyplot as plt
# data = {'y_axis': [327.337483727811, 322.324652774347, 331.087523824162, 345.582746154012, 366.906167536302, 291.059026808947, 383.444894921119, 239.974225110361, 321.630512423123, 304.111645697879, 335.760527177563, 323.179670200598, 352.498042928019, 265.187319290173, 330.030564548107, 364.216422463677, 374.523797034937, 395.097944323988, 365.7120246096, 406.429743720313, 389.930674812547, 366.023728240626, 364.880153046231, 331.634965635666, 450.127680664648, 300.767410955174, 438.699138086055, 313.362002790122, 415.700368774871, 276.282775707828, 441.191767348025, 279.77266773424, 410.964189258654, 257.807180374123]}

# df = pd.DataFrame(data)
#chart_data = pd.DataFrame(data)

#line plot code
if chart_select == 'Lineplots':
    st.sidebar.subheader("Lineplots Settings")
    try:
        data = {'y_axis': [327.337483727811, 322.324652774347, 331.087523824162, 345.582746154012, 366.906167536302, 291.059026808947, 383.444894921119, 239.974225110361, 321.630512423123, 304.111645697879, 335.760527177563, 323.179670200598, 352.498042928019, 265.187319290173, 330.030564548107, 364.216422463677, 374.523797034937, 395.097944323988, 365.7120246096, 406.429743720313, 389.930674812547, 366.023728240626, 364.880153046231, 331.634965635666, 450.127680664648, 300.767410955174, 438.699138086055, 313.362002790122, 415.700368774871, 276.282775707828, 441.191767348025, 279.77266773424, 410.964189258654, 257.807180374123]}
        x_axis = ["pelvis", "left_hip", "right_hip", "torso", "left_knee", "right_knee", "neck", "left_ankle", "right_ankle", "left_big_toe", "right_big_toe", "left_small_toe", "right_small_toe", "left_heel", "right_heel", "nose", "left_eye", "right_eye", "left_ear", "right_ear", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow", "left_wrist", "right_wrist", "left_pinky_knuckle", "right_pinky_knuckle", "left_middle_tip", "right_middle_tip", "left_index_knuckle", "right_index_knuckle", "left_thumb_tip", "right_thumb_tip"]
        df = pd.DataFrame(data, index=x_axis)
        st.line_chart(df)
        
    except Exception as e:
        print(e)

if chart_select == 'LinePlot':
    st.sidebar.subheader("Lineplot Settings")
    try:
        x_values=st.sidebar.selectbox("X_axis", options=numeric_columns)
        y_values=st.sidebar.selectbox("Y_axis", options=categoric_columns)
        plot=px.line(data_frame=df, x=x_values, y=y_values)
        # df=pd.DataFrame(y_values,index=x_values)
        #display the chart
        st.plotly_chart(plot)
    except Exception as e:
        print(e)
