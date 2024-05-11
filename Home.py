import streamlit, pandas, datetime, mysql.connector

# General info
page_title = "GameVerse"
page_icon = ":joystick:"
main_style = "./styles/main.css"

# Main functions
def init():
	streamlit.set_page_config(page_title = page_title, page_icon = page_icon, layout = "wide")
	with open(main_style) as style:
		streamlit.markdown(f"<style>{style.read()}</style>", unsafe_allow_html = True)

def build_home_page():
	title_container = streamlit.container(border = False)
	with title_container:
		streamlit.markdown("<h1 style = 'color: #ffffff'>GameVerse</h1>", unsafe_allow_html = True)
		streamlit.markdown("<p style = 'color: #ffffff'>Open World Trade</p>", unsafe_allow_html = True)

	streamlit.markdown("#")
	streamlit.markdown("#")
	streamlit.header("Games")
	cols = streamlit.columns([0.1, 0.1, 0.4, 0.2, 0.2])
	with cols[2]:
		streamlit.text_input("Game Title", placeholder = "Input game title")
	with cols[3]:
		streamlit.multiselect("Genre", options = ["Action"], placeholder = "Pick genre")

# Run
def run():
	init()
	build_home_page()

if __name__ == "__main__":
	run()