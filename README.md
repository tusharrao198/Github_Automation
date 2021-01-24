# Github Repo creation Automation

- For Windows Users,

1. Place both the `chromedriver.exe` from (`https://chromedriver.chromium.org/`) in the same directory with `Github_Automation.exe` file.
2. Run Github_Automation.exe file.

- For Linux Users,

Now you can easily start a new project, Github repo creation automated using selenium-python.
Program will create a project repo on github with changes being updated to git locally.

- Prerequisites,

* VS Code or Atom must be installed. Also, Chromium/Chrome browser.

1. Install requirements.txt using `pip3 install -r requirements.txt`
2. Install Chromedriver in your sysytem/OS from `https://chromedriver.chromium.org/`
3. After installing driver, extract them and move the chromedriver file to local bin using `sudo mv chromedriver/usr/local/bin/`
4. Add PATH to environment variable using `nano .bashrc`
   and add this line, `export PATH="$PATH:/usr/local/bin/chromedriver"`
5. Create a .env file to store your credentials.
6. That's it run the py file using `python3 automate_git.py`
