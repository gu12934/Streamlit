import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
import tempfile
import time
import os
from PIL import Image
#from yolor import *

#Note that this streamlit was developed from augmented startups, youtube channel is linked below

# mp_drawing= mp.solutions.drawing_utils
# mp_face_mesh= mp.solutions.face_mesh
# mp_pose = mp.solutions.pose
# mp_holistic = mp.solutions.holistic

def main():
	st.title('Object Tracking Dashboard YOLOR')
	
	st.sidebar.title('Settings')

	st.markdown(
	"""
	<style>
	[data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width: 400px;}
	[data-testid="stSidebar"][aria-expanded="false"] > div:first-child{width: 400px;margin-left: -488px}
	</style>
	""",
	unsafe_allow_html=True,
	)
	
	confidence=st.sidebar.slider('Confidence', min_value=0.0, max_value=1.0, value =0.25)
	st.sidebar.markdown('---')

	#checkboxes
	save_img=st.sidebar.checkbox('Save Video')
	enable_GPU=st.sidebar.checkbox('Enable GPU')
	custom_classes=st.sidebar.checkbox('Use Custom Classes')
	assigned_class_id=[]

	#custom classes
	if custom_classes:
		assigned_class = st.sidebar.multiselect('Select The Custom Classes', list(names), default='person')
		for each in assigned_class:
			assigned_class_id.append(names.index(each))

	#uploading out video
	video_file_buffer=st.sidebar.file_uploader("Upload a Video", type=["mp4", "mov", "avi", "asf", 'm4v'])
	DEMO_VIDEO= '1.mp4'
	tffile = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)

	## get input video here
	if not video_file_buffer:
		vid=cv2.VideoCapture(DEMO_VIDEO)
		tffile.name = DEMO_VIDEO
		dem_vid=open(tffile.name,'rb')
		demo_bytes=dem_vid.read()

		st.sidebar.text('Input Video')
		st.sidebar.video(demo_bytes)

	else:
		tffile.write(video_file_buffer.read())
		dem_vid=open(tffile.name,'rb')
		demo_bytes=dem_vid.read()

		st.sidebar.text('Input Video')
		st.sidebar.video(demo_bytes)
		
	print(tffile.name)

	stframe=st.empty()
	st.sidebar.markdown('---')

	kpi1, kpi2, kpi3= st.beta_columns(3)

	with kpi1:
		st.markdown("**Frame Rate**")
		kpi1_text= st.markdown("0")

	with kpi2:
		st.markdown("**Tracked Objects**")
		kpi2_text= st.markdown("0")

	with kpi3:
		st.markdown("**Width**")
		kpi3_text= st.markdown("0")

	load_yolor_and_process_each_frame()

if __name__ == '__main__':
	try:
		main()
	except SystemExit:
		pass
