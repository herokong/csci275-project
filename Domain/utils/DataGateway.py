import json
import os
import jsonpickle
from flask import session

class DataGateway:
  """
  Acess to text file in order to save and update the data of user data
  """
  # ------------------------Acessor and Mutator method to the text file-----------------------------
  def get_data(type, file_name):
    """
    Get data from text file and return a json object
    Parameters
    ----------
    `type` : str
        the type of the object should be classroom or user
    `file_name` : str
        the file name (User -> email) (Classroom -> id).
    """
    try:
      if (not DataGateway.is_data_existed(type, file_name)):
        return False
      with open(f"./Data/{type}/{file_name}.json") as file:
        return jsonpickle.decode(json.load(file))
    except:
      return False
  
  def save_data(type, file_name, data):
    """
    Save data to text file as a json object
    Parameters
    ----------
    `type` : str
        the type of the object should be classroom or user
    `file_name` : str
        the file name (User -> email) (Classroom -> id).
    `data` : object
        the new object to save into the file can be new or updated
    """
    try:
      with open(f"./Data/{type}/{file_name}.json", "w") as file:
        json.dump(jsonpickle.encode(data), file)
    except:
      raise ValueError("Unsuccessfully save data!")
  
  def delete_data(type, file_name):
    """
    Remove data
    Parameters
    ----------
    `type` : str
        the type of the object should be classroom or user
    `file_name` : str
        the file name (User -> email) (Classroom -> id).
    """
    if(not DataGateway.is_data_existed( type, file_name )):
      return False
    try:
      os.remove(f"./Data/{type}/{file_name}.json")
      return True
    except:
      print("Unsuccessfully delete the data!")
      return False
  
  def is_data_existed(type, file_name):
    """
    Check if there is already existing data
    Parameters
    ----------
    `type` : str
        the type of the object should be classroom or user
    `file_name` : str
        the file name (User -> email) (Classroom -> id).
    """
    try:
      with open(f"./Data/{type}/{file_name}.json"):
        return True;
    except:
      return False


