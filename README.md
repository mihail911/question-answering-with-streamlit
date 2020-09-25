# State-of-the-art Question Answering With Streamlit and HuggingFace

This is the code accompanying [this post](https://www.mihaileric.com/posts/state-of-the-art-question-answering-streamlit-huggingface/). You can try the app [here](https://wikipedia-transformers-qa.herokuapp.com/). Built using Streamlit and deployed on Heroku

**Note**: Heroku app is deployed using *tensorflow* framework, which doesn't play nicely with streamlit caching. For best experiences use *pytorch* framework. I have added a conditional decorator to avoid model reloading & effecient caching. However, the slug size for pytorch is above 850MB which far exceeds heroku's allowed slug size (500MB).

![qa_streamlit](resources/qa_streamlit.gif)

## Libraries Used
* Transformers
* Streamlit

## Running Locally
All the experiments are run on `python 3.8.0`.

1. Clone the repository
2. If you do not have python3.8 installed. Run the below steps for easy installation using [asdf](https://asdf-vm.com/). *asdf* allows us to manage multiple runtime versions such for different languages such as `nvm`, `rbenv`, `pyenv`, etc using a CLI tool
	* Install asdf using this [guide](https://asdf-vm.com/#/core-manage-asdf-vm?id=install)
	* Now install `python3.8.0`
	```bash
	asdf plugin add python
	asdf install python 3.8.0
	asdf local python 3.8.0	# sets python3.8 as interpreter for the project
	```
	* Check the set python version
	```bash
	asdf current python
	```
3. Install poetry. [Poetry](https://python-poetry.org/docs/) is a python dependency management & packaging tool. Allows us to declare project libraries dependency & manage them
	```bash
	asdf plugin add poetry
	asdf install poetry latest # current 1.0.10; might need sudo
	asdf local poetry 1.0.10
	```
4. Install all dependencies
	```bash
	poetry install
	```
5. (Optional) Explicitly instantiate the env
    ```bash
    source "$( poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate"
    ```
6. To run the application -
    ```bash
    streamlit run app.py
    ```
7. Change `config` dictionary values in `config.py` as required
```python
framework: tf/pt # choose tensorflow or pytorch framework
NUM_SENT: int # number of wiki sentences for context
```
