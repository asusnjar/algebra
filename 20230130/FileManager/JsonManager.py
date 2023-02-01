import os
import json

def file_exists(file_path):
    '''
    Method that returns True/False based on whether "filePath" exists
    '''
    return os.path.exists(file_path)

def open_file_for_reading(file_path):
    '''
    Method to open a connection for reading to "filePath"
    '''

    if not file_exists(file_path):
        return f'File {file_path} does not exist!'
    try:
        with open(file_path) as file_reader:
            return json.load(file_reader)
    except Exception as ex:
        return f'Error occurred: {ex}' 

def open_file_for_writing(file_path):
    '''
    Method to open a connection for writing to "filePath"
    '''

    if not file_exists(file_path):
        return f'File {file_path} does not exist!'
    try:
        with open(file_path, 'w') as file_writer:
            return file_writer
    except Exception as ex:
        return f'Error occurred: {ex}' 

def open_file_for_appending(file_path):
    '''
    Method to open a connection for appending to "filePath"
    '''

    if not file_exists(file_path):
        return f'File {file_path} does not exist!'
    try:
        with open(file_path, 'a') as file_writer:
            return file_writer
    except Exception as ex:
        return f'Error occurred: {ex}' 

def write_to_file_and_close(file_path, content):
    '''
    Method to write the content of "content" variable to a file
    '''
    try:
        with open(file_path, 'w') as file_writer:
            json.dump(content, file_writer)
    except Exception as ex:
        return f'Error occurred: {ex}'

def read_from_file(file_path):
    '''
    Method to read a file
    '''
    if not file_exists(file_path):
        return f'File {file_path} does not exist!'
    try:
        with open(file_path) as file_reader:
            return json.load(file_reader)
    except Exception as ex:
        return f'Error occurred: {ex}'