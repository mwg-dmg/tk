import streamlit as st
import pandas as pd
#import numpy as np

    
st.set_page_config(page_title="MWG",page_icon="&",layout="centered",initial_sidebar_state="auto",menu_items=None)


url="tkphoto.csv"
df=pd.read_csv(url)
if "page" not in st.session_state:
    st.session_state.page = 0
if "j" not in st.session_state:
    st.session_state.j = 0
if "status" not in st.session_state:
    st.session_state.status ="Not Opened"
if (st.session_state.status =="Not Opened"):
    st.title(":blue[GPP TREKKERS]")
    

def nextpage():
    st.session_state.page += 1
    st.session_state.status ="Not Opened"
def restart():
    st.session_state.page = 0
    st.session_state.status ="Not Opened"
def prvpage():
    st.session_state.page -= 1
    st.session_state.status ="Not Opened"
def ij_next(i):
    i=i
    st.session_state.j +=1
    return(i,st.session_state.j)
def ij_pre(i):
    i=i
    st.session_state.j -=1
    return(i,st.session_state.j)
def get_ij_start(i):
    i=i
    st.session_state.j = 0
    return(i,st.session_state.j)
def read_data(i,j):
    df1=df[[df.columns[i]]]
    #print(df1)
    df1=df1.dropna()
    jmax=((len(df1[[df1.columns[0]]]))-1)
    if j>jmax:
        j=j-1
        st.session_state.j -=1
    if j<0:
        j=0
        st.session_state.j = 0
    #print(jmax)
    return(df1[df1.columns[0]][j],jmax)
def view_next_photo():
    placeholder = st.empty()
    with placeholder.container():
                i_in=st.session_state.page-1
                #st.write("1) Rajmachi-7th Feb 2016")
                list=[]
                list=ij_next(i_in)
                i=list[0]
                j=list[1]
                #st.write(i)
                #st.write(j)
                
                file,jmax=read_data(i,j)
                
                #st.write(file)
                col1, col2 = st.columns(2)
                with col2:
                    st.button("Next Photo/Video",on_click=view_next_photo,disabled=(j ==jmax ))
                with col1:
                    st.button("Prev Photo/Video",on_click=view_pre_photo,disabled=(j ==0))
                if file.endswith("mp4"):
                    video_file=open(file,"rb")
                    video_bytes=video_file.read()
                    st.video(video_bytes)                
                else:
                
                    st.image(file)
                
                
                
def view_pre_photo():
    placeholder = st.empty()
    with placeholder.container():
                i_in=st.session_state.page-1
                #st.write("1) Rajmachi-7th Feb 2016")
                list=[]
                list=ij_pre(i_in)
                i=list[0]
                j=list[1]
                #st.write(i)
                #st.write(j)
                
                file,jmax=read_data(i,j)
                #st.write(file)
                col1, col2 = st.columns(2)
                with col2:
                    st.button("Next Photo/Video",on_click=view_next_photo,disabled=(j ==jmax ))
                with col1:
                    st.button("Prev Photo/Video",on_click=view_pre_photo,disabled=(j ==0))
                if file.endswith("mp4"):
                    video_file=open(file,"rb")
                    video_bytes=video_file.read()
                    st.video(video_bytes)
                else:
                
                    st.image(file)
                
                
    
    
def view_photo():
    placeholder = st.empty()
    st.session_state.status ="Opened"
    with placeholder.container():
                i_in=st.session_state.page-1
                #st.write("1) Rajmachi-7th Feb 2016")
                list=[]
                list=get_ij_start(i_in)
                i=list[0]
                j=list[1]
                #st.write(i)
                #st.write(j)
                        
                file,jmax=read_data(i,j)
                #st.write(file)
                col1, col2 = st.columns(2)
                with col2:
                    st.button("Next Photo/Video",on_click=view_next_photo,disabled=(j ==jmax ))
                with col1:
                    st.button("Prev Photo/Video",on_click=view_pre_photo,disabled=(j ==0))
                
                if file.endswith("mp4"):
                    video_file=open(file,"rb")
                    video_bytes=video_file.read()
                    st.video(video_bytes)
                else:
                
                    st.image(file)
        
        

def lgin():
    if login=="gpptk" :
        if password=="gpptk123":
            st.session_state.one = ""
            st.session_state.two = ""
            #st.write("Login successful")
            st.session_state.page = 1         
            
    else:
            st.write("Wrong login name or password, Try again")
            st.session_state.one = ""
            st.session_state.two = ""

            
placeholder = st.empty()

if st.session_state.page == 0:
    with placeholder.container():            
        login=st.text_input('Login Name',key="one",placeholder="Login Name")
        password=st.text_input('Password',key="two",placeholder="Password")
        st.button("Submit",key=None,on_click=lgin)
        
elif st.session_state.page == 1:    
    with placeholder.container():
        
        #st.markdown("<h5 style='text-align: center; color: voilet;'>1) Rajmachi-25th Nov 2015</h1>", unsafe_allow_html=True)
        st.write("1) Rajmachi-25th Nov 2015")
        
        if (st.session_state.status =="Not Opened"):            
                
                st.text(
                    """
                        This is our first trek.
                        Rajmachi fort is near Lonavala.
                        There are two forts  Manoranjan and Shrivardhan.
                        
                    """
                    )

                st.button("View Photo/Video",key=None,on_click=view_photo)
                
elif st.session_state.page == 2:
   with placeholder.container():
        #st.markdown("<h5 style='text-align: center; color: voilet;'>2) Dharmvirgad -9th Sept 2017</h1>", unsafe_allow_html=True)
       
        st.write("2) Dharmvirgad -9th Sept 2017")
        if (st.session_state.status =="Not Opened"):            
                
                st.text(
                    """
                        Dharmvirgad is also known as Bahadurgad or Pemgad.
                        It is on the banks of Bhima river.
                        It is near Sidhdhatek Ganpati.
                        We visited Rashin Devi Temple and Rehakuri reserve forest on the same day.
                        
                    """
                    )
                st.button("View Photo/Video",key=None,on_click=view_photo)        
        
elif st.session_state.page == 3:
    with placeholder.container():
        #st.markdown("<h5 style='text-align: center; color: voilet;'>3)-video</h1>", unsafe_allow_html=True)
        st.write("3)Korigad")
        if (st.session_state.status =="Not Opened"):            
                
                st.text(
                    """
                       Korigad is near Amby Valley City.                        
                    """
                    )
                st.button("View Photo/Video",key=None,on_click=view_photo)

elif st.session_state.page == 4:
    with placeholder.container():
        #st.markdown("<h5 style='text-align: center; color: voilet;'>3)-video</h1>", unsafe_allow_html=True)
        st.write("4)Video")
        if (st.session_state.status =="Not Opened"):            
                
                st.text(
                    """
                       A video combining all treks.                        
                    """
                    )
                st.button("View Photo/Video",key=None,on_click=view_photo)  

else:
    with placeholder.container():
        st.write("This is the last Page")
        st.button("Previous Page",on_click=prvpage,disabled=(st.session_state.page ==1))
        st.button("Restart",key=None,on_click=restart)
       
if st.session_state.page != 0:
    col1, col2 = st.columns(2)
    with col2:
            st.button("Next Page",on_click=nextpage,disabled=(st.session_state.page > 3))
    with col1:
            st.button("Previous Page",on_click=prvpage,disabled=(st.session_state.page ==1))
    st.write("")
    #st.write("If you have an exlusive photo/video of our trek please send it to MWG or AAG")
    st.divider()
    st.write(":rainbow[Website developed and maintained by MWG and AAG.]")
        




