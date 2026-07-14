import streamlit as st
import pandas as pd
import os
from datetime import datetime

from streamlit_autorefresh import (
    st_autorefresh
)



# ===============================
# AUTO REFRESH
# ===============================

st_autorefresh(
    interval=1000,
    key="refresh"
)



# ===============================
# PAGE SETUP
# ===============================


st.set_page_config(

    page_title=
    "AI Traffic System",

    layout="wide"

)



# ===============================
# HEADER
# ===============================


st.title(
    "🚦 AI Smart Traffic Management System"
)



st.caption(

    "SUMO + Unity Digital Twin + AI Vision"

)





# ===============================
# PERFORMANCE
# ===============================


st.subheader(
    "📊 AI Signal Performance"
)



if os.path.exists(
    "data/results.csv"
):


    data = pd.read_csv(
        "data/results.csv"
    )



    normal = data[
        data["Mode"]=="Normal"
    ]["Average Waiting"].values[0]



    ai = data[
        data["Mode"]=="AI"
    ]["Average Waiting"].values[0]



    improvement = (

        (normal-ai)

        /

        normal

        *

        100

    )



    a,b,c = st.columns(3)



    a.metric(

        "Normal Signal",

        f"{normal:.2f}s"

    )



    b.metric(

        "AI Signal",

        f"{ai:.2f}s"

    )



    c.metric(

        "Improvement",

        f"{improvement:.1f}%"

    )



    st.bar_chart(

        data,

        x="Mode",

        y="Average Waiting"

    )







# ===============================
# CCTV VIEW
# ===============================


st.divider()



st.subheader(
    "📷 Live CCTV Feed"
)



def show_camera(
        file,
        title
):


    if os.path.exists(file):


        # force reload image

        with open(
            file,
            "rb"
        ) as img:


            st.image(

                img.read(),

                caption=
                title,

                use_container_width=True

            )



        updated = (
            datetime
            .fromtimestamp(
                os.path.getmtime(file)
            )
            .strftime(
                "%H:%M:%S"
            )
        )



        st.caption(

            "Updated: "
            +
            updated

        )



    else:


        st.error(

            title
            +
            " Offline"

        )





c1,c2 = st.columns(2)



with c1:


    show_camera(

        "camera_feed/north.jpg",

        "North CCTV"

    )



with c2:


    show_camera(

        "camera_feed/south.jpg",

        "South CCTV"

    )





c3,c4 = st.columns(2)



with c3:


    show_camera(

        "camera_feed/east.jpg",

        "East CCTV"

    )



with c4:


    show_camera(

        "camera_feed/west.jpg",

        "West CCTV"

    )





# ===============================
# STATUS
# ===============================


st.divider()



st.subheader(
    "System Status"
)



x,y,z = st.columns(3)



x.success(
    "SUMO Online"
)


y.success(
    "Unity Connected"
)


z.success(
    "AI Ready"
)





# ===============================
# FINES
# ===============================


st.divider()



st.subheader(
    "🚨 AI Fine System"
)



st.table(

    {

    "Vehicle":

    [
        "KL07AB2026",
        "KL05XY7788"
    ],


    "Violation":

    [
        "Insurance Expired",
        "PUC Expired"
    ],


    "Fine":

    [
        "₹2000",
        "₹1000"
    ]

    }

)