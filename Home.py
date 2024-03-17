import streamlit, pandas, datetime, mysql.connector

page_title = "GameVerse"
main_style = "./styles/main.css"

def init():
	streamlit.set_page_config(page_title = page_title)
	with open(main_style) as style:
		streamlit.markdown(f"<style>{style.read()}</style>", unsafe_allow_html = True)

def run():
	init()

if __name__ == "__main__":
	run()