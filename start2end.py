import asyncio
import ollama
import speech_recognition as sr
import time

r = sr.Recognizer()
m = sr.Microphone()
print("noise check - start")
with m as source:
    a=r.adjust_for_ambient_noise(source, 2)  # we only need to calibrate once, before we start listening
print("noise check - end")
  r.energy_threshold *=2
  r.dynamic_energy_ratio = 2

async def speak(speaker, content):
  if speaker:
    p = await asyncio.create_subprocess_exec(speaker, content)
    await p.communicate()



async def main():
  speaker = '/usr/bin/say'

  client = ollama.AsyncClient()

  messages = []

  while True:
    print("listening...")
    with m as source:
      audio = r.listen(source)#, phrase_time_limit=5) # set timeout to 5 seconds

      text = r.recognize_google(audio, language='en-in') #it-IT #en-in

      if text:
          print(f"You said: {text}")
      if text =="exit" or text =="Exit":
          raise Exception('Stop this thing')
          exit(0)


      messages.append({'role': 'user', 'content': text})
      content_out = ''
      message = {'role': 'assistant', 'content': ''}
      async for response in await client.chat(model='mistral', messages=messages, stream=True):
        if response['done']:
          messages.append(message)

        content = response['message']['content']
        print(content, end='', flush=True)

        content_out += content
        if content in ['.', '!', '?', '\n']:
          await speak(speaker, content_out)
          content_out = ''

        message['content'] += content

      if content_out:
        await speak(speaker, content_out)
      print()


try:
  asyncio.run(main())
except (KeyboardInterrupt, EOFError):
  ...
