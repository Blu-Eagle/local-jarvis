This is a test to build a completely local interface to artificial intelligense using speech in input and getting back speech to output.
th idea is to:
- get audio from microphone
- convert it to text using speech2text
- feeding it ollama mistral (you need to install it froom its web site)
- push the answer to a text2speech

it tries to have everython locally.
as long as it is noow it works :)

if you improve it let me know :)

start making a virtual environment with
python -m venv venv

and then install all the dependencies from requirements.txt, probably there is more than it is needed, i forgot to remove the unsused ones.
