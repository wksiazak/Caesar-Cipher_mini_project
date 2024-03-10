# Caesar cipher script

Script which allows to encrypt and decyrypt data by using Caesar cipher method. Created in Python. 

### Table of content 
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [More details about technology](#more-details)

## General info <a name="general-info"></a>
<details>
<summary>Click here to see general information about <b>Caesar cipher script </b>!</summary>

Main purpose of this  script is to encrypt or decrypt text which is provided by user or provided in json file. All operations are collecting in connected database. 
This simple aplication is created on Facade pattern. 
</details>

## Technolgies <a name="technologies"></a>
<ul>
<li>Python</li>
<li>SQL</li>
<li>pytest</li>
</ul>

## Setup <a name="setup"></a>
<details>
<summary>Click here to see general information about <b>Setup</b>!</summary>
<li>Clone the repo</li>
<code>git clone [https://github.com/your_username_/Project-Name](https://github.com/wksiazak/Caesar-Cipher_mini_project).git</code>
<li>In the terminal go to directory with repository and run this command</li>
<code>pip install -r requirements.txt</code>
<li>In the terminal go to directory with repository and run this command</li>
<code> python main.py</code>
</details>

## More details about technology <a name="more-details"></a>
<details>
<summary>Click here to see more about <b>details</b>!</summary>
As mentioned in general info application is using facade design pattern. File fascade.py includes main menu which allows user for: 
    <li>encrypt</li>
    <li>decrypt</li>
    <li>encrypt from json file</li>
    <li>decrypt from json file</li>
    <li>export ciphers from memory to file</li>
As aplication is running all operations are saved in connected database. There is an option to export all records to file. 
</details>
