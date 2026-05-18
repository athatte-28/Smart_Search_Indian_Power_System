import os
import streamlit as st
from mainEngine import search


st.set_page_config(
    page_title="Legal Search Engine",
    page_icon="⚖️",
    layout="wide"
)

st.title("Legal Search Engine")

st.markdown(
    "Search legal sections, punishments and provisions instantly."
)


query = st.text_input(
    "Search laws and sections"
)

if query:

    results = search(query)

    for r in results:

        with st.container(border=True):

        # =====================================
        # TOP ROW
        # =====================================

            col1, col2 = st.columns([1, 6])

        # SECTION NUMBER BOX
            with col1:

                st.markdown(
                f"""
                <div style="
                    background-color:#1f77b4;
                    color:white;
                    padding:18px;
                    border-radius:12px;
                    text-align:center;
                    font-size:24px;
                    font-weight:bold;
                ">
                    {r['section']}
                </div>
                """,
                unsafe_allow_html=True
            )

        # SUMMARY AREA
            with col2:

                st.markdown(
                f"""
                <div style="
                    font-size:24px;
                    font-weight:600;
                    margin-top:5px;
                ">
                    {r['one_line_summary']}
                </div>
                """,
                unsafe_allow_html=True
            )

                st.markdown(
                f"""
                <div style="
                    color:gray;
                    font-size:16px;
                    margin-top:5px;
                ">
                    {r['name']}
                </div>
                """,
                unsafe_allow_html=True
            )

        # =====================================
        # FULL SUMMARY DROPDOWN
        # =====================================

            with st.expander("View Full Summary"):

                st.write(r["description"])

        # =====================================
        # PDF BUTTON
        # =====================================

            pdf_name = os.path.basename(r["pdf_file"])

            with open(r["pdf_file"], "rb") as pdf_file:

                st.download_button(
                    label="📄 View Full PDF",
                    data=pdf_file,
                    file_name=pdf_name,
                    mime="application/pdf"
                )

          

        # =====================================
        # RELEVANCE SCORE
        # =====================================

            st.markdown(
            f"""
            <div style="
                text-align:right;
                color:gray;
                font-size:14px;
                margin-top:15px;
            ">
                Relevance Score: {round(r['score'], 4)}
            </div>
            """,
            unsafe_allow_html=True
        )

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("---")
