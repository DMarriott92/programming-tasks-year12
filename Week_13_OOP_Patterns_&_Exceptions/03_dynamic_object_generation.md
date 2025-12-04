# Dynamic Object Generation
Given a config file (JSON), dynamically create Python objects with attributes loaded at runtime.
Effectively what you are doing is importing data from a JSON file that holds all of the details to be added to an object.
Like the pokemon example of having the pokemon base stats stored in a database and importing them to the python file.
I have provided 3 config files, please attempt this task on all three separately.
Example below for simple config.
{
  "Player": {
    "name": "Hero",
    "health": 100,
    "mana": 50
  }
}