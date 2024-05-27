# neurocloud-eeg-analysis
This project is focused on developing an applicaiton capable of presenting and processing EEG data extracted from an EDF (European data format) file.

## Necessary dependencies and tools used to build the project
The application's interface is built on the framework **Dash**, specialized on building dashboards and graphs. It also uses external auxiliary libraries for the frontend, namely, **Dash bootstrap components**.
Moreover, the library **MNE-Python** is used for dealing with the EEG data analysis and EDF file.
**SQLAlchemy** and **MySQL** were choosen as the tools for developing the newly-implemented database. By 27/05/2024 the database is still under development.

## Logic separation of the files.

The files that compose this project are separated by role and its syntaxes follow the rules stated on Dash docs: https://dash.plotly.com/.

Generally, the names describe the content of the files, however their roles will be stated below.

The file "app.py" contains the instance of the dash application.

The file "index.py" launches the application.

The ordinary person may not understand what the file "callbacks.py" stands for. As a short description, it incorporates ways of communicating the frontend and the backend of the application. Callbacks are a feature from Dash.

The folder "assets" contains the images used on the application.

The file "layout.py" contains all the layouts for the frontend, including the pages, the modals and the graph layout.

The file "logic.py" contains functions that are not necessarilly bound to callbacks, besides being used inside some.

The file "styles.py" contains a collection of python dictionaries for styling the app.

