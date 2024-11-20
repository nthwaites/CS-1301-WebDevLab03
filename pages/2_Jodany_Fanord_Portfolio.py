import streamlit as st
import info
import pandas as pd

#About Me

def about_me_section():
    st.header("About Me🌀")
    #st.image(info.profile_picture_1, width = 200)
    st.write(info.about_me_1)
    st.write("---")
about_me_section()

#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on Linkedin🔗")
    linkedin_link = f'<a href="{info.my_linkedin_url_1}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Check Out My Work")
    github_link = f'<a href="{info.my_github_url_1}"><img src="{info.github_image_url}" alt="Github" width = "65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Email Me!")
    email_html = f'<a href="mailto:{info.my_email_address_1}"><img src="{info.email_image_url}" alt="Email" width = "75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()
#Education
def education_section(education_data_1,course_data_1):
    st.header("Education📖")
    st.subheader(f"**{education_data_1['Institution']}**")
    st.write(f"**Degree:**{education_data_1['Degree']}")
    st.write(f"**Graduation Date:**{education_data_1['Graduation Date']}")
    st.write(f"**GPA:**{education_data_1['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data_1)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names" : "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True,
     )
    st.write("---")
education_section(info.education_data_1, info.course_data_1)

#Professional Experience

def experience_section(experience_data):
    st.header("Professional Experience🔌")
    for job_title, (job_description, image) in experience_data.items():
        expander= st.expander(f"{job_title}")
        expander.image(image,width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience_section(info.experience_data_1)

#Projects

def project_section(projects_data):
    st.header("Projects🤖")
    for project_name, project_description in projects_data.items():
        expander=st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project_section(info.projects_data_1)



#Activities

def activities_section(leadership_data, activity_data):
    st.header("Activities🧰")
    tab1,tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership🎤")
        for title, (details,image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Activities👐")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    st.write("---")
activities_section(info.leadership_data_1, info.activity_data_1)

#Skills
def skills_section(programming_data, spoken_data):
    st.header("Skills☝️")
    st.subheader("Programming Languages💻")
    for skill,percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons_1.get(skill,'')}")
        st.progress(percentage)
    st.subheader("Spoken Languages🧐")
    for spoken,proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons_1.get(spoken, '')}:{proficiency}")
    st.write("---")

skills_section(info.programming_data_1, info.spoken_data_1)












