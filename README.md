# exercise-1-modularity-sunithapriya
exercise-1-modularity-sunithapriya created by GitHub Classroom

The aim of this project is to provide integration for the modular deisgn of Patient Monitoring System. 
The main repo of Patient Monitoring System is at the location:
```https://github.com/alexlin0625/EC500_Spring19```

The task was divided into set of following modules and each module have multiple implementations:
* **Input Module**
* **Storage Module**
* **Alert Module**
* **Output Module**

 ***main.py*** has the integration of the modules. It uses the following implementations from the above mentioned modules:
1. Input module - Reads input from csv file. 
    * Author - Sunitha Priyadarshini Sampath
    * Github location: ```https://github.com/alexlin0625/EC500_Spring19/blob/input_module/input.py```
2. Storage module - Stores data in mongodb. 
    * Author - XiangkunYe
    * Github location: ```https://github.com/alexlin0625/EC500_Spring19/blob/storage_module/storage.py```
3. Alert module - Alerts if input is less than threshhold. 
    * Author - XiangkunYe
    * Github location: ```https://github.com/XiangkunYe/exercise-1-modularity-XiangkunYe/blob/master/alert_system.py```
4. Output module - Displays data to the terminal.
    * Author -  Zhizhou
    * Github location: ```https://github.com/alexlin0625/EC500_Spring19/blob/output_module/output.py```

The above integrations were made seamlessly with slight changes to output.py
