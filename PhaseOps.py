
import PhaseA.taskA1 as taskA1
import PhaseA.taskA2 as taskA2
import PhaseA.taskA3 as taskA3
import PhaseA.taskA4 as taskA4
import PhaseA.taskA5 as taskA5
import PhaseA.taskA6 as taskA6
import PhaseA.taskA7 as taskA7
import PhaseA.taskA8 as taskA8
import PhaseA.taskA9 as taskA9
import PhaseA.taskA10 as taskA10

import PhaseB.taskB1 as taskB1
import PhaseB.taskB3 as taskB3
import PhaseB.taskB4 as taskB4
import PhaseB.taskB5 as taskB5
import PhaseB.taskB6 as taskB6
import PhaseB.taskB7 as taskB7
import PhaseB.taskB8 as taskB8
import PhaseB.taskB9 as taskB9
import PhaseB.taskB10 as taskB10

import json, re
from AIProxy import get_completions


def execute_task(task_classification, task_query: str) -> str:
    """ Execute the task based on the task code. """
    
    #print(task_classification)
    #task_classification = json.loads(task_classification)
    #print(task_classification)
    
    task_code = task_classification["name"]
    arguments = json.loads(task_classification["arguments"])
    #print(arguments)
    if "filename" in arguments:
        arguments["filename"] = f".{arguments["filename"]}"
    if "targetfile" in arguments:
        arguments["targetfile"] = f".{arguments["targetfile"]}"
        
    print(f"Task code: {task_code} | Filename: {arguments.get("filename")} | Targetfile: {arguments.get("targetfile")}")
    
    if task_code == "A1":
        arguments = json.loads(task_classification["arguments"])
        return taskA1.execute_task(**arguments)
    elif task_code == "A2":
        return taskA2.execute_task(**arguments)
    elif task_code == "A3":
        return taskA3.execute_task(**arguments)
    elif task_code == "A4":
        return taskA4.execute_task(**arguments)
    elif task_code == "A5":
        return taskA5.execute_task(**arguments)
    elif task_code == "A6":
        return taskA6.execute_task(**arguments)
    elif task_code == "A7":
        return taskA7.execute_task(**arguments)
    elif task_code == "A8":
        return taskA8.execute_task(**arguments)
    elif task_code == "A9":
        return taskA9.execute_task(**arguments)
    elif task_code == "A10":
        return taskA10.execute_task(**arguments)
    elif task_code == "B3":
        return taskB3.fetch_and_save_data(json.loads(task_classification["arguments"])["filename"], arguments["targetfile"])
    elif task_code == "B4":
        arguments = json.loads(task_classification["arguments"])
        return taskB4.clone_and_commit(**arguments)
    elif task_code == "B5":
        return taskB5.run_sql_query(**arguments)
    elif task_code == "B6":
        return taskB6.scrape_website(**arguments)
    elif task_code == "B7":
        return taskB7.process_image(**arguments)
    elif task_code == "B8":
        return taskB8.transcribe_audio(**arguments)
    elif task_code == "B9":
        return taskB9.md_file_to_html(**arguments)
    elif task_code == "B10":
        return taskB10.filter_csv(**arguments)
    elif task_code == "FALLBACK":
        return fallback_task(task_query)
    else:
        raise ValueError("Unknown task code")


def fallback_task(task_query: str) -> str:
    """ Fallback to the original task query. """
    messages = [
        {"role": "assistant", "content": "give proper steps to complete the task"},
        {"role": "user", "content": task_query}
    ]
    response = get_completions(messages)
    return response