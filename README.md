# AI-Powered-Code-Review-System
## Project Summary
- Select language
- Select Framework
- Your code
- Issues Found
- Issues Fixed
- Correct Code
- Execution Time


---
## Running this project

Linux and macOS:

```bash
sudo git clone https://github.com/AbRehmansaif/AI-Powered-Code-Review-System.git
```

Windows:

```bash
git clone https://github.com/AbRehmansaif/AI-Powered-Code-Review-System.git
```

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with
Windows:
```
python -m venv venv
```
Linux:
```
python3 -m venv myenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```

That will create a new folder `env` in your project directory. Next activate it with this command on Win/linux:
Window:
```
venv\Scripts\activate
```
Linux
```
source env/bin/active
```
CMD to Deactivate `env`
```
deactivate
```
Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```
CMD to Run project on custom Port

```
python manage.py runserver 0.0.0.0:9000
```
