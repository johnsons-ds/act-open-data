# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to My Portfolio! 👋")

    st.sidebar.success("Select a project above.")

    st.markdown(
        """
        I've use Streamlit to create my data science portfolio. Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a project from the sidebar** to see some examples
        of what I can do!

        The DataFrame Demo, Animation Demo and Plotting Demo comes with Streamlit. I will replace these pages with time! Happy analysing 🤓
    """
    )


if __name__ == "__main__":
    run()
