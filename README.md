# Getting Started

## Setup your desired capabilities before running the tests

After download the project in the github https://github.com/priformaggio/poc_calculator_python, is necessary to setup the desired capabilities according to your emulator/device:

1. In the base_test.py file, update the informations about platformName, deviceName, app(PATH of your app), appPackage and appActivity.

    ```
    Example:

        url = 'http://0.0.0.0:4723/wd/hub'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'Nexus'
        desired_caps['app'] = '/home/priscila/poc_calculator/calculator.apk'
        desired_caps['appPackage'] = 'com.maroyakasoft.dentak'
        desired_caps['appActivity'] = 'com.umadigital.dentak.MainActivity'

        self.driver = webdriver.Remote(url, desired_caps)
      ```

2. In case you have doubts how to get de appPackage and appActivity of your app, you can try:

      - Thinking that you have already configured the android on your machine and the emulator/device is launched, go to your project folder and input this command in your terminal:

    ```
      $ adb install [apk name]
    ```

      Example: adb install calculator.apk

      - Then you have to launch the activity from the app that you want to describe the appPackage and appActivity

      - Then you have to input this command in the terminal:

    ```
    $ adb shell  
    ```

      - Then input this other command:

    ```
      $ dumpsys
    ```

      - A log should be shown, look for 'mCurrentFocus' in the final of the log. You can try using:

      ```
       $ dumpsys	window	windows	|	grep	-E 'mCurrentFocus'
      ```

      In this line, should be shown something like this example:com.maroyakasoft.dentak/ com.umadigital.dentak.MainActivity. Where the first part is the appPackage and the second part is the appActivity.



## Installing Python

1. Windows

- Download the latest version https://www.python.org/
- By default, it will be installed at C:\Python36\, so that you can have multiple versions of Python on the same system without conflicts. Then, add this to your PATH:

```
C:\Python36\;C:\Python36\Scripts\
```

- Close the terminal and open again
- Type ``` $python ``` on the terminal to see if this was installed with success. If the response is "command not found", the installation is not correct.


2. Linux

- Open your terminal and type this command to update the system:

```
$ sudo apt-get update
```

- Then type this command to install python:

```
$ sudo apt-get install python
```

3. MAC Os

- Before python, you have to install the homebrew:

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

- Insert the homebrew directory to your PATH, in your ~/.profile file:

```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

- Now, you can install Python:

```
$ brew install python
```

## Installing Appium

### Using the Appium GUI

1. Download and install the Appium GUI. [[Windows Download]](https://bitbucket.org/appium/appium.app/downloads/AppiumForWindows_1_4_16_1.zip). [[OS X Download]](https://bitbucket.org/appium/appium.app/downloads/appium-1.4.13.dmg).


2. Read the Appium GUI [documentation](http://appium.io/slate/en/v1.4.13/#appium-gui).

### Using the Appium CLI

1. In order to use 1.4.16, download Appium through NPM with this command:

    ```
    $ npm install -g appium@1.4.16
    ```

2. Verify that you have Appium installed with this command:

    ```
    $ appium -v
    ```

   You should get "1.4.16" as the output


## Set up the Appium Python environment

1. We recommend setting up [Python's virtualenv](https://pypi.python.org/pypi/virtualenv) for developing and packaging tests so that unnecessary dependencies are not including in the bundled zip file.
2. Create your workspace and install py.test in your virtual environment. For example:

    ```
    $ virtualenv workspace
    $ cd workspace
    $ source bin/activate
    $ pip install pytest
    $ pip install Appium-Python-Client
    ```

3. Put all Python test scripts under a **tests/** folder in your workspace.

    ```
    - workspace
        └─ tests/ (tests go here)
    ```

## Running Your Tests Locally on Real Devices

### **Important Note**
Certain desired capabilities must be set when running locally. Refer to [BaseTest.java](./tests/tests/base_tests/base_test.py#L26-L32)

### Appium GUI

1. Start the Appium server.
    1. Click on the Android button.
    2. Set the "App Path", "Package", and "Device Name" and make sure their checkboxes are checked.
    3. Press the "Launch" button to start the Appium server locally.

2. Navigate into your workspace project directory in the terminal and activate the virtualenv.

    ```
    $ source bin/activate
    ```

3. Verify that your test cases are discoverable by the following command, which should be run from your workspace folder.

    ```
    $ py.test --collect-only tests/
    ```

4. Run your tests.

    ```
    $ py.test tests/
    ```

### Appium CLI

1. Start the Appium server.
    1. Make sure that you have followed all the steps in the [Appium getting started guide]
    2. Edit the [start-appium-android.sh](./start-appium-android.sh) script to include your app's absolute path and your device's UDID.
    3. Run [start-appium-android.sh](./start-appium-android.sh) to start the Appium server locally.

2. Navigate into your workspace project directory in the terminal and activate the virtualenv.

    ```
    $ source bin/activate
    ```

3. Verify that your test cases are discoverable by the following command, which should be run from your workspace folder.

    ```
    $ py.test --collect-only tests/
    ```
4. Run your tests.

    ```
    $ py.test tests/
    ```
5. In case you want to run only a scenario, with a tag, type this command:

```
$ py.test -m lala
```
Where "lala" is the example of the tag name. But in the scenario/test must be written in this way:

```
@pytest.mark.lala
```

6. In case you want to run by a method:

```
pytest test_mod.py::TestClass::test_method
```

- Other examples could be possible to see in this link: https://docs.pytest.org/en/latest/usage.html

7. Create your report_html

- Install pytest html: ``` pip install pytest-html ```

- Run your test with: ``` pytest --html=report.html ```

- For xml: ``` py.test tests/tests/calculator_test.py --junitxml=/home/priscila/poc_calculator_python\out_report.xml ```

Examples here: https://pypi.python.org/pypi/pytest-html/


## Clean the _pycache_ and .pyc

- When you run a program in python, the interpreter compiles it to bytecode first (this is an oversimplification) and stores it in the __pycache__ folder. If you look in there you will find a bunch of files sharing the names of the .py files in your project's folder, only their extensions will be either .pyc or .pyo. These are bytecode-compiled and optimized bytecode-compiled versions of your program's files, respectively.

- As a programmer, you can largely just ignore it... All it does is make your program start a little faster. When your scripts change, they will be recompiled, and if you delete the files or the whole folder and run your program again, they will reappear (unless you specifically suppress that behavior)

- In case you want to delete before run the test or commit, type this command manually in your terminal:

```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```

Informations here: https://stackoverflow.com/questions/16869024/what-is-pycache

https://stackoverflow.com/questions/5551269/ignore-file-pyc-in-git-repository

- In your gitignore file, type these lines:
```
.Python
bin/
include/
lib/
local/
pip-selfcheck.json
requirements.txt
selenium/
wheelhouse/
*.pyc
*.cache
/__pycache__
/assets
/venv
```
