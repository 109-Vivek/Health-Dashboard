import asyncio
import js
import re
import module1 as mdl
from js import document, FileReader
from pyodide import create_proxy

global final_text

def read_complete(event):

    content = document.getElementById("main_text");
    content.innerText = event.target.result
    global final_text
    final_text = event.target.result
    final_text = final_text.replace("**","")


def read_disease(event):
    content = document.getElementById("main_text");
    content.innerText = ""
    for i in re.split(r"\s+",final_text):
        i = i.strip()
        div = document.createElement('span')
        if(mdl.isDisease(i)):
            div.classList = "bg-gradient-to-r from-emerald-500 to-green-700 rounded-md m-1 p-1"
        else:
            div.classList = "p-1 mx-1 my-1"
        div.innerText = i
        content.appendChild(div)

def read_medicine(event):
    content = document.getElementById("main_text");
    content.innerText = ""
    for i in re.split(r"\s+",final_text):
        i = i.strip()
        div = document.createElement('span')
        if(mdl.isMedicine(i)):
            div.classList = "bg-gradient-to-r from-emerald-500 to-green-700 rounded-md p-1 mx-1 my-1"
        else:
            div.classList = "p-1 mx-1 my-1"
        div.innerText = i
        content.appendChild(div)


def read_symptoms(event):
    content = document.getElementById("main_text");
    content.innerText = ""
    for i in re.split(r"\s+",final_text):
        i = i.strip()
        div = document.createElement('span')
        if(mdl.isSymptom(i)):
            div.classList = "bg-gradient-to-r from-emerald-500 to-green-700 rounded-md p-1 mx-1 my-1"
        else:
            div.classList = "p-1 mx-1 my-1"
        div.innerText = i
        content.appendChild(div)

async def process_file(x):
    fileList = document.getElementById('fileInput').files

    for f in fileList:
        reader = FileReader.new()

        onload_event = create_proxy(read_complete)

        reader.onload = onload_event

        reader.readAsText(f)

    return

def main():
    file_event = create_proxy(process_file)
    file_disease = create_proxy(read_disease)
    file_medicine = create_proxy(read_medicine)
    file_symptoms = create_proxy(read_symptoms)
    e = document.getElementById("upload")
    e.addEventListener("click", file_event)

    dis = document.getElementById("disease_btn")
    dis.addEventListener("click", file_disease)

    med = document.getElementById("medicine_btn")
    med.addEventListener("click", file_medicine)

    sym = document.getElementById("symptoms_btn")
    sym.addEventListener("click", file_symptoms)

main()