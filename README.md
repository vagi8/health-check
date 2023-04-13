# Fetch-Take-Home-Exercise-SRE
Author  -  Vageeshan Mankala
[LinkedIn](https://www.linkedin.com/in/vageeshan-mankala-4b8128126/)

# Monitor HTTP/S Endpoints
Problem Statement - [fetch-take-home-execercise-SRE](https://fetch-hiring.s3.us-east-1.amazonaws.com/site-reliability-engineer/health-check.pdf)
Organizer - [Fetch Rewards](https://fetch.com/)

# Installation
1. [Install python](https://www.python.org/downloads/). 
    Install for required operating sysmtem if not already installed. Verified versions for python are [3.10, 3.9, 3.8].
2. Create virtual environment using venv.
    - create a new virtual environment named `myenv`
    ```
    python -m venv path/to/myenv
    ```
    - To activate the virtual environment run the following command. make sure to use the use it from the appropriate path. (HINT- the goal is to run a `activate` script inside the newly created myenv/Scripts directory) 
    ### Windows
    ```
    path/to/myenv/Scripts/activate
    ```
    ### Linux / Mac
    ```
    source path/to/myenv/bin/activate
    ```
3. Clone the repository. ([Git Installation Instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))
```
git clone https://github.com/vagi8/Fetch-Take-Home-Exercise-SRE.git
```
3. Go into project directory.
```
cd Fetch-Take-Home-Exercise-SRE
```
3. Install dependencies. If you are using virtual environment, make sure you activate it before installing the dependencies. `pip` command is usually installed with python. If not installed please install it.
```
pip install -r requirements.txt
```

# Execution
Run the program. Again, this is to be run after activating virtual environment if you are using one. 
```
python main.py
```
